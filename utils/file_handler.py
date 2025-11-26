# utils/file_handler.py
import os
import shutil
from fastapi import UploadFile
from uuid import uuid4

TEMP_DIR = "assets/temp_uploads"
os.makedirs(TEMP_DIR, exist_ok=True)

def save_upload_temp(upload: UploadFile) -> str:
    """
    Save a FastAPI UploadFile to a temp path and return the path.
    """
    ext = os.path.splitext(upload.filename)[1] if hasattr(upload, "filename") else ""
    fname = f"{uuid4().hex}{ext}"
    path = os.path.join(TEMP_DIR, fname)
    with open(path, "wb") as f:
        shutil.copyfileobj(upload.file, f)
    return path

def cleanup_path(path: str):
    try:
        if os.path.exists(path):
            os.remove(path)
    except Exception:
        pass
