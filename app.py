import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="AI Notes Summarizer", layout="centered")

st.title("📄 AI Notes Summarizer")
st.write("Get a short and clear summary of your notes.")

@st.cache_resource
def load_model():
    return pipeline(
        task="summarization",
        model="facebook/bart-large-cnn"
    )

summarizer = load_model()

text = st.text_area("Enter your notes", height=200)

if st.button("Summarize"):
    if text.strip():
        with st.spinner("Summarizing..."):
            summary = summarizer(
                text,
                max_length=130,
                min_length=30,
                do_sample=False
            )
            st.success("Summary")
            st.write(summary[0]["summary_text"])
    else:
        st.warning("Please enter some text.")
