import streamlit as st

st.title("📝 AI Notes Summarizer")

st.write("If you can see this text, Streamlit is working.")

text = st.text_area("Enter your notes")

if st.button("Summarize"):
    st.success("Button clicked!")
    st.write(text)
