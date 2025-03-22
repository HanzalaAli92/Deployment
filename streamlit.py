import streamlit as st

st.title("🚀 Simple Streamlit App")

user_input = st.text_input("💬 Enter some text:")

if st.button("✨ Show Text"):
    st.success(f"✅ You entered: {user_input}")