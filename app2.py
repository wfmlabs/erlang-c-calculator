import streamlit as st

st.title("Hello Streamlit!")
st.write("This is a simple Streamlit app.")
name = st.text_input("Enter your name:", "World")
st.write(f"Hello, {name}!")
