import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="AI Notes Summarizer", layout="centered")

st.title("📝 AI Notes Summarizer")
st.write("Get a short and clear summary of your notes.")

@st.cache_resource
def load_model():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_model()

text = st.text_area("Enter your notes", height=200)

if st.button("Summarize"):
    if len(text.strip()) < 50:
        st.warning("Please enter more text (at least 50 characters).")
    else:
        with st.spinner("Summarizing..."):
            summary = summarizer(
                text,
                max_length=120,
                min_length=40,
                do_sample=False
            )

        st.subheader("📌 Summary")
        st.success(summary[0]["summary_text"])
