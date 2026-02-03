from fastapi import FastAPI, UploadFile, File, Form
from pypdf import PdfReader
import spacy
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import os

app = FastAPI()

# FIX: Add a Root route so you don't get "Not Found"
@app.get("/")
def home():
    return {"status": "API is Live", "message": "Backend is working! Use the UI to interact."}

def read_pdf(file):
    reader = PdfReader(file)
    return " ".join(page.extract_text() for page in reader.pages)

@app.post("/match")
async def match_resume(resume: UploadFile = File(...), job_desc: str = Form(...)):
    try:
        resume_text = read_pdf(resume.file)
        
        # Load existing model or create new one on the fly
        if os.path.exists("tfidf_model.pkl"):
            vectorizer = joblib.load("tfidf_model.pkl")
            # Fit-transform to ensure the vocabulary matches the new input
            tfidf = vectorizer.fit_transform([resume_text, job_desc])
        else:
            vectorizer = TfidfVectorizer()
            tfidf = vectorizer.fit_transform([resume_text, job_desc])
            joblib.dump(vectorizer, "tfidf_model.pkl")

        score = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
        return {"match_score": round(score * 100, 2)}
    except Exception as e:
        return {"error": str(e)}