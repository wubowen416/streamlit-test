import streamlit as st

st.title('Intro')

next_button = st.button(
    label="Next"
)

if next_button:
    st.switch_page('pages/exp.py')