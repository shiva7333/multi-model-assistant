

```
multi-modal-assistant/README.md
```

---

# ✅ **README.md **

---

# 🌟 **ShivaGPT — Your Personal Voice–Vision–Text AI Assistant**

ShivaGPT is an advanced **multi-modal AI assistant** that can understand **text**, analyze **images**, and transcribe **audio**, all inside a clean Streamlit UI.
Built using OpenAI’s latest models, ShivaGPT serves as a personal productivity tool capable of summarization, reasoning, content creation, and more.

---

## 🚀 **Features**

### 🔤 Text Intelligence

* Smart text-based chat
* Summaries, rewriting, Q&A, explanations
* Generates professional posts, ideas, answers

### 🖼️ Image Intelligence

* Understands uploaded images
* Generates captions, summaries, descriptions
* Extracts insight from posters, documents, screenshots

### 🎤 Audio Intelligence

* Transcribes audio (mp3/wav) using Whisper
* Converts speech to text
* Supports long-form audio transcription

### 🧠 Multi-Modal Fusion

* Takes **text + image + audio** together
* Produces context-aware intelligent responses

### 🎨 Clean Streamlit UI

* Simple interface
* File upload for audio & images
* Real-time response display

---

## 📁 **Project Structure**

```
shivaGPT/
│── server/
│     ├── core_engine.py        # Main model logic
│     ├── audio_processor.py    # Whisper audio handler
│     ├── image_processor.py    # Image captioning/extraction
│     ├── settings.py           # API keys & config
│     ├── ui_app.py             # Streamlit frontend
│
│── output/                     # Screenshots, demo outputs
│── .gitignore
│── README.md
│── requirements.txt
│── venv/ (ignored in git)
```

---

## 🔧 **Tech Stack**

| Component           | Technology        |
| ------------------- | ----------------- |
| Frontend UI         | Streamlit         |
| LLM                 | OpenAI GPT Models |
| Image Processing    | OpenAI Vision     |
| Audio Transcription | Whisper API       |
| Backend             | Python 3.11       |
| Environment         | Virtualenv        |

---

## 🛠️ **Installation Guide (Local Setup)**

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/YOUR_USERNAME/shivaGPT.git
cd shivaGPT
```

---

### **2️⃣ Create Virtual Environment**

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
.\venv\Scripts\activate
```

---

### **3️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

---

### **4️⃣ Add Your OpenAI API Key**

Create file:

```
server/settings.py
```

Add:

```python
OPENAI_API_KEY = "your-key-here"
```

---

### **5️⃣ Run the Application**

```bash
streamlit run server/ui_app.py
```

The interface will open in your browser.

---

## 🖼️ **Demo Output Screenshots**

Store your screenshots inside:

```
output/
```

Example preview (add real screenshots after running):

```
output/
│── ui_home.png
│── image_summary_result.png
│── audio_to_text_result.png
```

---

## 🧩 **How It Works (Architecture)**

```
User Input
   │
   ├── Text → LLM
   ├── Image → Vision Model
   ├── Audio → Whisper Transcription
   │
   ▼
Core Engine Combines All Inputs
   │
   ▼
OpenAI Multi-Modal Model Generates Response
   │
   ▼
Streamlit UI Displays Final Answer
```

---

## 🤝 **Contributing**

Contributions are welcome!

1. Fork the repo
2. Create a new branch
3. Commit your changes
4. Open a Pull Request

---

## 📜 **License**

This project is licensed under the **MIT License** — free for personal & commercial use.

---
