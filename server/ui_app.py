# server/ui_app.py
import streamlit as st
import requests

st.title("Multi-Modal Assistant — Demo")

text_input = st.text_area("Text input", height=120)
audio_upload = st.file_uploader("Upload audio (wav/mp3)", type=["wav", "mp3"])
image_upload = st.file_uploader("Upload image", type=["png", "jpg", "jpeg"])

if st.button("Ask"):
    files = {}
    data = {}
    if text_input:
        data["text"] = text_input
    if audio_upload:
        files["audio"] = (audio_upload.name, audio_upload.getvalue())
    if image_upload:
        files["image"] = (image_upload.name, image_upload.getvalue())

    with st.spinner("Contacting assistant..."):
        try:
            res = requests.post("http://127.0.0.1:8000/ask", files=files, data=data, timeout=120)
            res.raise_for_status()
            st.subheader("Assistant reply")
            st.write(res.json().get("response", "No response"))
        except Exception as e:
            st.error(f"Request failed: {e}")
