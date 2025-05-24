import streamlit as st

st.title("App")

with st.form("user_info"):
    st.session_state['user'] = st.text_input(label="ID", help="Your User ID.")
    submit_button = st.form_submit_button()
    if submit_button:
        st.switch_page("pages/intro.py")