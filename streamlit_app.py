import streamlit as st

st.title("Hello World")

left, right = st.columns(2, border=True)
with left:
    st.header("Left")
    st.video("https://cospeech-smplx-gesture-videos.s3.ap-northeast-3.amazonaws.com/videos/generated/10_kieks_0_10_10_27.mp4")

with right:
    st.header("Right")
    st.video("https://cospeech-smplx-gesture-videos.s3.ap-northeast-3.amazonaws.com/videos/generated/10_kieks_0_10_10_27.mp4")

st.radio(
    label="Select a video", 
    options=["Left", "Equal", "Right"]
)