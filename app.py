import streamlit as st

st.title("AI Notes Summarizer")

st.write("get summary of your notes.")

text = st.text_area("Enter your notes")

if st.button("Summarize"):
    st.success("Button clicked!")
    st.write(text)
