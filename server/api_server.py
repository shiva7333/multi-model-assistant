# server/api_server.py
from fastapi import FastAPI, UploadFile, Form
from orchestrator.assistant_hub import handle_multi_modal

app = FastAPI()

@app.post("/ask")
async def ask_endpoint(text: str = Form(None), audio: UploadFile = None, image: UploadFile = None):
    """
    Accept text (form) and optional files (audio, image).
    Returns JSON with assistant response.
    """
    resp = handle_multi_modal(text_input=text, audio_file=audio, image_file=image)
    return {"response": resp}
