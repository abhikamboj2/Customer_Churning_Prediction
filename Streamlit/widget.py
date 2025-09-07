import streamlit as st
st.title("Input Text")
name=st.text_input("Enter your name")
if name:
    st.write(f"Hello,{name}")