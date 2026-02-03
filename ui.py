import streamlit as st
import requests

st.set_page_config(page_title="AI Resume Matcher PRO", layout="wide")

# Dark Glassmorphism CSS
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
        color: #ffffff;
    }
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 40px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.8);
    }
    .stMetricValue { color: #00ffcc !important; }
    h1, h2, h3, p, label { color: #e0e0e0 !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌑 AI Resume Matcher: Dark Edition")

st.markdown('<div class="glass-card">', unsafe_allow_html=True)

# Connection Input
backend_url = st.text_input("🔗 Paste your Backend URL (Port 8000 link)", 
                            value="https://opulent-robot-7vp7rg4w5q9rcxr4w-8000.app.github.dev")

col1, col2 = st.columns(2)
with col1:
    resume = st.file_uploader("📂 Upload Candidate Resume (PDF)", type="pdf")
with col2:
    jd = st.text_area("📝 Target Job Description", height=200)

if st.button("RUN AI ANALYSIS"):
    if resume and jd:
        with st.spinner('Calculating NLP Vectors...'):
            try:
                # API Call - ensure we hit the /match endpoint
                api_endpoint = f"{backend_url.rstrip('/')}/match"
                payload = {"job_desc": jd}
                files = {"resume": (resume.name, resume.getvalue(), "application/pdf")}
                
                response = requests.post(api_endpoint, files=files, data=payload)
                result = response.json()
                
                if "match_score" in result:
                    score = result['match_score']
                    st.balloons()
                    st.metric("NLP Match Score", f"{score}%")
                else:
                    st.error(f"API Error: {result.get('error')}")
            except Exception as e:
                st.error("Connection failed. Did you set Port 8000 to PUBLIC?")
    else:
        st.warning("Please upload a resume and JD.")

st.markdown('</div>', unsafe_allow_html=True)