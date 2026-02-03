📄 AI Resume Matcher (NLP & ML Pipeline)
A professional-grade NLP tool that uses Machine Learning to calculate semantic similarity. This project features a FastAPI backend and a Streamlit frontend with a custom Dark-Glassmorphism UI.

🛠️ Project Deep Dive (Click to Expand)
<details> <summary><b>🚀 Key Features</b></summary>

NLP Matching: Uses Scikit-Learn for TF-IDF Vectorization and Cosine Similarity.

Production API: Built with FastAPI for asynchronous PDF processing.

Modern UI: High-end Dark Mode with Glassmorphism built using Streamlit.

Scalable Architecture: Decoupled frontend and backend.

</details>

<details> <summary><b>🏗️ System Architecture & Logic</b></summary>

Input: User uploads a PDF and pastes a Job Description.

Extraction: pypdf extracts raw text from the document.

Vectorization: Text is converted into numerical vectors using TfidfVectorizer.

Similarity: Calculation of Cosine Similarity between the Resume and JD vectors.

Output: Percentage score returned with visual feedback.

</details>

<details> <summary><b>🚦 Installation & Setup</b></summary>

1. Install Dependencies
Bash

pip install -r requirements.txt
2. Run Backend
Bash

uvicorn main:app --host 0.0.0.0 --port 8000
(Ensure Port 8000 is set to Public in Codespaces)

3. Run Frontend
Bash

streamlit run ui.py
</details>

<details> <summary><b>📈 Technical Stack</b></summary>

Backend: Python, FastAPI, Uvicorn

ML/NLP: Scikit-Learn, PyPDF, Spacy

Frontend: Streamlit, Custom CSS

Environment: GitHub Codespaces

</details>
