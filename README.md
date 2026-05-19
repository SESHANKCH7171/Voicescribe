# 🎙️ VoiceScribe — Open Source Wispr Flow Clone

> **Speak anything. Get text instantly. No word limits. Completely free.**

A local Wispr Flow alternative built with Python + Streamlit + Groq API (Whisper Large V3). Record your voice, transcribe it in seconds, copy it anywhere — VS Code, browser, terminal, Claude Code.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35%2B-red?style=flat-square&logo=streamlit)
![Groq](https://img.shields.io/badge/Groq-Whisper%20V3-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

---

## ✨ Features

- 🔴 **One-click voice recording** from your microphone
- ⚡ **Instant transcription** via Groq's free cloud API (Whisper Large V3)
- 🌍 **Multilingual** — English, Hindi, or auto-detect
- 📋 **One-click copy** of transcribed text
- 🗂️ **Session history** — all your transcriptions in one place
- ⬇️ **Download all transcriptions** as a .txt file
- 🆓 **Free** — Groq free tier = 7,200 sec/day (~2 hrs), no credit card needed
- 🔒 **Private** — your API key never leaves your machine

---

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/voicescribe.git
cd voicescribe
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your Groq API Key
```bash
# Copy the example file
cp .env.example .env

# Open .env and paste your key
# Get a free key at: https://console.groq.com
GROQ_API_KEY=your_key_here
```

### 4. Run the app
```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501` — done! 🎉

---

## 🎙️ How It Works

```
Your Voice (Mic)
      ↓
sounddevice records audio locally
      ↓
Saved as temp .wav file (16kHz)
      ↓
Sent to Groq API (Whisper Large V3)
      ↓
Text returned instantly
      ↓
Copy anywhere — VS Code, browser, terminal
```

No heavy models run on your machine. Groq handles all AI compute on their cloud — your PC uses near-zero RAM.

---

## 📦 Stack

| Tool | Role |
|------|------|
| **Streamlit** | UI framework (pure Python) |
| **Groq API** | Cloud STT — Whisper Large V3 |
| **sounddevice** | Mic recording |
| **scipy / numpy** | Audio processing |
| **python-dotenv** | API key management |

---

## 💰 Cost

| Usage | Cost |
|-------|------|
| Up to 7,200 sec/day (~2 hrs) | **$0 — Free forever** |
| Beyond free tier | $0.001/min (≈ $0.60 per 10 hrs) |

No credit card needed to start.

---

## 🌐 Deploy Online (Optional)

You can deploy this to **Streamlit Cloud** for free so it works from any browser:

1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. Add `GROQ_API_KEY` in the Secrets section
5. Deploy — get a public URL instantly

> ⚠️ Note: Browser-based mic recording has limitations on some cloud deployments. Local usage (`streamlit run app.py`) is most reliable.

---

## 🙋 Why I Built This

[Wispr Flow](https://wisprflow.ai) is an amazing tool but limits free users to **2,000 words/week**. This project replicates its core functionality — speak → get text — with **zero limits** using open-source models and free APIs.

---

## 📄 License

MIT — use it, modify it, ship it.

---

*Built by an AI developer from Nashik, India 🇮🇳 — because voice-to-text should be free.*
