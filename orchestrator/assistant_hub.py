# orchestrator/assistant_hub.py
from core.llm_engine import load_text_model
from core.audio_engine import transcribe_audio
from core.vision_engine import describe_image
from core.response_engine import generate_response
from utils.file_handler import save_upload_temp, cleanup_path

# load text model once
TOKENIZER, MODEL = load_text_model("gpt2")  # change to stronger model if available

def handle_multi_modal(text_input: str = None, audio_file=None, image_file=None, max_samples: int = 1) -> str:
    """
    Accepts optional text_input (str), audio_file (file-like path), image_file (file-like path).
    Returns assistant response string.
    """
    context_parts = []
    saved_paths = []

    # text
    if text_input:
        context_parts.append(f"User: {text_input}")

    # audio_file: if passed as UploadFile like object from FastAPI, first save and pass path
    if audio_file:
        audio_path = save_upload_temp(audio_file)
        saved_paths.append(audio_path)
        spoken = transcribe_audio(audio_path)
        context_parts.append(f"User (audio): {spoken}")

    # image_file
    if image_file:
        image_path = save_upload_temp(image_file)
        saved_paths.append(image_path)
        descr = describe_image(image_path)
        context_parts.append(f"User (image): {descr}")

    if not context_parts:
        # cleanup and return helpful message
        for p in saved_paths:
            cleanup_path(p)
        return "Please provide text, audio, or an image."

    prompt = "\n\n".join(context_parts) + "\n\nAssistant:"
    response = generate_response(MODEL, TOKENIZER, prompt, max_new_tokens=160)

    # cleanup temp files
    for p in saved_paths:
        cleanup_path(p)

    return response
