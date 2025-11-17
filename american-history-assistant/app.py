from flask import Flask, render_template, request 
import pandas as pd
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# --------------------------------------------------------
# 1. Load the FAQ dataset and clean the text
# --------------------------------------------------------
faq_df = pd.read_csv("data/faq_data.csv")

# Basic cleaning so TF-IDF can process the text correctly
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9? ]', ' ', text)
    return text

faq_df["clean_question"] = faq_df["question"].apply(clean_text)

# --------------------------------------------------------
# 2. Build the TF-IDF "AI" model
#    (converts questions into numerical vectors)
# --------------------------------------------------------
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(faq_df["clean_question"])

# Use cosine similarity to find the closest FAQ match
def get_answer(user_query):
    clean_q = clean_text(user_query)
    user_vec = tfidf.transform([clean_q])
    sims = cosine_similarity(user_vec, tfidf_matrix)[0]

    best_index = sims.argmax()
    best_question = faq_df.iloc[best_index]["question"]
    best_answer = faq_df.iloc[best_index]["answer"]

    return best_question, best_answer

# --------------------------------------------------------
# 3. Flask route for the homepage / chatbot interface
# --------------------------------------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    user_q = ""
    match_q = ""
    match_a = ""

    # When the user submits a question
    if request.method == "POST":
        user_q = request.form.get("question")
        if user_q:
            match_q, match_a = get_answer(user_q)

    # Display results in the HTML template
    return render_template("index.html",
                           user_q=user_q,
                           match_q=match_q,
                           match_a=match_a)

# --------------------------------------------------------
# Run the Flask web app
# --------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
