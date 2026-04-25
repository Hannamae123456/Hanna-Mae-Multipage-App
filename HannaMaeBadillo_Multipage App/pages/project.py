import streamlit as st

st.title("📂 Projects")

projects = {"Mini streamlit App":"🍎interactive form app.",
        "liquor system": "🍾Sell any kind of alcholic drinks."}

for name, desc in projects.items():
    with st.expander(name):
        st.write(desc)