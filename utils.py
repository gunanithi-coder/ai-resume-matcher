import streamlit as st

def set_bg():
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #1e3c72, #2a5298);
        color: white;
    }
    .stTextArea textarea { color: black; }
    </style>
    """, unsafe_allow_html=True)