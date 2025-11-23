from flask import Flask, render_template, request 
import pandas as pd
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Added
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import Normalizer
from sklearn.pipeline import make_pipeline
import numpy as np

app = Flask(__name__)

# --------------------------------------------------------
# 1. Load the FAQ dataset and clean the text
# --------------------------------------------------------
faq_df = pd.read_csv("data/faq_data.csv")

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9? ]', ' ', text)
    return text

faq_df["clean_question"] = faq_df["question"].apply(clean_text)

# --------------------------------------------------------
# TF-IDF + single best match
# --------------------------------------------------------
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(faq_df["clean_question"])

def get_answer(user_query):
    clean_q = clean_text(user_query)
    user_vec = tfidf.transform([clean_q])
    sims = cosine_similarity(user_vec, tfidf_matrix)[0]

    best_index = sims.argmax()
    best_question = faq_df.iloc[best_index]["question"]
    best_answer = faq_df.iloc[best_index]["answer"]

    return best_question, best_answer

# --------------------------------------------------------
# ADDED: LSA MODEL (TF-IDF → SVD → Normalizer)
# --------------------------------------------------------
lsa_model = make_pipeline(
    TfidfVectorizer(stop_words='english'),
    TruncatedSVD(n_components=100, random_state=42),
    Normalizer(copy=False)
)

faq_df["combined"] = (faq_df["question"] + " " + faq_df["answer"]).apply(clean_text)
lsa_matrix = lsa_model.fit_transform(faq_df["combined"])

# --------------------------------------------------------
# ADDED: MULTIPLE MATCHES + CONFIDENCE SCORES
# --------------------------------------------------------
def get_similar_answers(user_query, top_k=3, min_conf=0.30):
    """
    Returns multiple similar FAQs with confidence scores.
    Does NOT replace the original function.
    """
    clean_q = clean_text(user_query)
    user_vec = lsa_model.transform([clean_q])

    sims = cosine_similarity(user_vec, lsa_matrix)[0]
    ranked = np.argsort(sims)[::-1]

    results = []
    for idx in ranked[:top_k]:
        conf = float(sims[idx])
        if conf < min_conf:
            continue
        
        results.append({
            "question": faq_df.iloc[idx]["question"],
            "answer": faq_df.iloc[idx]["answer"],
            "confidence": round(conf * 100, 2)
        })
    
    return results

# --------------------------------------------------------
# UPDATED ROUTE: Supports both single & multi matches
# --------------------------------------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    user_q = ""
    match_q = ""
    match_a = ""
    multi_matches = []

    if request.method == "POST":
        user_q = request.form.get("question")

        if user_q:
            # Keep original teammate functionality
            match_q, match_a = get_answer(user_q)

            # Add enhanced multi-match feature
            multi_matches = get_similar_answers(user_q, top_k=3)

    return render_template("index.html",
                           user_q=user_q,
                           match_q=match_q,
                           match_a=match_a,
                           multi_matches=multi_matches)

if __name__ == "__main__":
    app.run(debug=True)
