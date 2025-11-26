# core/vision_engine.py
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# lazy-load models to avoid heavy startup unless used
_processor = None
_model = None

def _ensure_loaded():
    global _processor, _model
    if _processor is None or _model is None:
        _processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        _model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return _processor, _model

def describe_image(image_path: str, max_new_tokens: int = 50) -> str:
    processor, model = _ensure_loaded()
    image = Image.open(image_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")
    out = model.generate(**inputs, max_new_tokens=max_new_tokens)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption
