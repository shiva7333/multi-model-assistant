# core/response_engine.py
import torch

def generate_response(model, tokenizer, prompt: str, max_new_tokens: int = 120) -> str:
    """
    Generate a text response using the loaded tokenizer & model.
    Removes prompt echo if present.
    """
    inputs = tokenizer(prompt, return_tensors="pt")
    if torch.cuda.is_available():
        inputs = {k: v.to("cuda") for k, v in inputs.items()}
        model.to("cuda")
    with torch.no_grad():
        out = model.generate(**inputs, max_new_tokens=max_new_tokens, do_sample=True, top_p=0.95, temperature=0.7)
    text = tokenizer.decode(out[0], skip_special_tokens=True)
    # remove prompt (if model echoes)
    if text.startswith(prompt):
        text = text[len(prompt):].strip()
    return text.strip()
