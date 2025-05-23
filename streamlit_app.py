import streamlit as st

st.title("Hello World")

left, right = st.columns(2)
with left:
    st.header("Left Video")
    st.video("https://cospeech-smplx-gesture-videos.s3.ap-northeast-3.amazonaws.com/videos/generated/10_kieks_0_10_10_27.mp4")

with right:
    st.header("Right Video")
    st.video("https://cospeech-smplx-gesture-videos.s3.ap-northeast-3.amazonaws.com/videos/generated/10_kieks_0_10_10_27.mp4")

st.radio("Select a video", ["Left Video", "Right Video"])