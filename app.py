import streamlit as st

st.set_page_config(page_title="AI Notes Summarizer")

st.title("AI Notes Summarizer")
st.write("Paste your notes below and click Summarize")

text = st.text_area("Enter your notes here")

if st.button("Summarize"):
    if text.strip() == "":
        st.warning("Please enter some text")
    else:
        st.success("App is working!")
        st.write("You entered:")
        st.write(text)

