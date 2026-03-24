import pdfplumber
import string
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize


def extract_text_from_pdf(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        text = ""
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text: 
                text += page_text + "\n"


    return text.strip()

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess(text):
    
    text = text.lower()
    text = text.replace('-', '')
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    

    # text = text.translate(str.maketrans('', '', string.punctuation))
    words = word_tokenize(text)

    words = [word for word in words if word not in stop_words]

    words = [lemmatizer.lemmatize(word) for word in words]

    return " ".join(words)



def analyze_resume(resume_text, job_description_text):
    resume_clean = preprocess(resume_text)
    job_clean = preprocess(job_description_text)

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_clean, job_clean])

    resume_vector = vectors[0]
    job_vector = vectors[1]

    
    similarity_score = cosine_similarity(vectors[0], vectors[1])[0][0]
   
    resume_words = set(resume_clean.split())
    job_words = set(job_clean.split())

    missing_keywords = list(job_words - resume_words)

 
    missing_keywords.sort()

   
    return {
        "score": round(similarity_score * 100, 2),  # percentage
        "missing_keywords": missing_keywords
    }
