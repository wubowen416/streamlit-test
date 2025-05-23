import streamlit as st

st.title("Hello World")

col1, col2 = st.columns(2)
with col1:
    st.header("Left Video")
    st.video("https://cospeech-smplx-gesture-videos.s3.ap-northeast-3.amazonaws.com/videos/generated/10_kieks_0_10_10_27.mp4")

with col2:
    st.header("Right Video")
    st.video("https://cospeech-smplx-gesture-videos.s3.ap-northeast-3.amazonaws.com/videos/generated/10_kieks_0_10_10_27.mp4")
