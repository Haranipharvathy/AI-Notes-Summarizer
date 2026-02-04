import streamlit as st
from transformers import pipeline

# Page config
st.set_page_config(page_title="AI Notes Summarizer", page_icon="📝")

st.title("📝 AI Notes Summarizer")
st.write("Get a short and clear summary of your notes.")

# Load model (cached)
@st.cache_resource
def load_model():
    return pipeline(
        "text2text-generation",
        model="facebook/bart-large-cnn"
    )

summarizer = load_model()

# Input
text = st.text_area(
    "Enter your notes",
    height=200,
    placeholder="Paste your long notes here..."
)

# Button
if st.button("Summarize"):
    if text.strip() == "":
        st.warning("Please enter some text to summarize.")
    else:
        with st.spinner("Summarizing..."):
            summary = summarizer(
                text,
                max_length=130,
                min_length=30,
                do_sample=False
            )

        st.success("Summary generated!")
        st.subheader("📌 Summary")
        st.write(summary[0]["generated_text"])
