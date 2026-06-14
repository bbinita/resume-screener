# Resume Screener

An AI powered web application that compares a resume against a job description using Natural Language Processing. It returns a match score and highlights missing keywords helping job seekers tailor their resumes more effectively.



## 🛠️ Built With

- **Python** — core language
- **Django** — web framework
- **pdfplumber** — PDF text extraction
- **NLTK** — text preprocessing (tokenization, stopwords, lemmatization)
- **scikit-learn** — TF-IDF vectorization and cosine similarity

---

## ✨ Features

- Upload resume as PDF
- Paste any job description
- Get a match score as a percentage
- See missing keywords from the job description
- Error handling for invalid files and empty inputs

---

## ⚙️ How It Works

1. Extract text from uploaded PDF using pdfplumber
2. Preprocess both texts - lowercase, remove punctuation, remove stopwords, lemmatize
3. Vectorize both texts using TF-IDF
4. Calculate cosine similarity between the two vectors
5. Extract keywords present in job description but missing from resume
6. Display match score and missing keywords

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- pip

### Installation

```bash
# Clone the repo
git clone https://github.com/bbinita/resume-screener.git
cd resume-screener

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install django pdfplumber nltk scikit-learn

# Download NLTK data
python -c "import nltk; nltk.download('stopwords'); nltk.download('wordnet'); nltk.download('punkt_tab')"

# Run the server
python manage.py runserver
```

Then open `http://127.0.0.1:8000` in your browser.

---
