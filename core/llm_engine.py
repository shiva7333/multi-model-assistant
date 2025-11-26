# core/llm_engine.py
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

def load_text_model(model_name: str = "gpt2"):
    """
    Load tokenizer and causal LM. Move to CUDA if available.
    """
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    model.eval()
    if torch.cuda.is_available():
        model.to("cuda")
    return tokenizer, model
