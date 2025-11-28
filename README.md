# AI-Powered FAQ Helpdesk - (American History Example)

An intelligent FAQ helpdesk system that uses Natural Language Processing (NLP) to automatically match user questions with the most relevant answers from a predefined FAQ dataset.

Presentation Recording link: https://drive.google.com/file/d/1sJem246q0j43wxepjEVvWyfILpqKVxIf/view?usp=sharing 

## Project Overview

This AI-Powered FAQ Helpdesk system:
- Analyzes user questions using NLP techniques (TF-IDF vectorization)
- Matches queries to the most relevant FAQ entries using cosine similarity
- Provides instant, accurate responses with confidence scores
- Offers a modern, user-friendly web interface

## Prerequisites
Visual Studio Code

## Prerequisites

Before running this project, ensure you have the following installed:

- **Python 3.7 or higher** 
- **pip** (Python package installer) 

To check if Python is installed:
```bash
python3 --version
```

## Installation Instructions

### Step 1: Navigate to the Project Directory

```bash
cd american-history-assistant
```

### Step 2: Install Required Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

This will install:
- `flask` - Web framework for the application
- `pandas` - Data manipulation and CSV handling
- `scikit-learn` - Machine learning library for NLP (TF-IDF, cosine similarity)
- `numpy` - Numerical computing library

## Running the Application

### Step 1: Start the Flask Server

In Visual Studio Code, 1st select, the app.py file in the "american-history-assistant" folder, and navigate to the menu bar and select "Run" -> then select "Run Without Debugging"


You should see output similar to:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### Step 2: Access the Application

Open your web browser and enter this address on an url search bar :

```
http://127.0.0.1:5000
```

Or use:

```
http://localhost:5000
```

**Note:** If you encounter "Access to localhost was denied", try using `http://127.0.0.1:5000` instead.

### Step 3: Using the FAQ Helpdesk

1. Enter your question in the text field
2. Click "Ask Question" or press Enter
3. The system will:
   - Analyze your question using NLP
   - Find the most relevant FAQ match
   - Display the answer with a confidence score
