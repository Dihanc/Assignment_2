pip install streamlit
import streamlit as st

name = st.text_input('Enter your name:')

if name:
    st.write(f'Hello, {name}!')

streamlit run streamlit_app.py
