# 🎙️ VoiceScribe — Open Source Wispr Flow Clone

> **Speak anything. Get text instantly. No word limits. Completely free.**

A local voice-to-text app built with Python + Streamlit + Groq API (Whisper Large V3). Record your voice in the browser, transcribe it in seconds, or drag and drop audio files for instant speech-to-text. The current app uses Streamlit’s built-in `st.audio_input` for microphone capture and Groq’s speech-to-text API for transcription. [web:48][web:53]

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.34%2B-red?style=flat-square&logo=streamlit)
![Groq](https://img.shields.io/badge/Groq-Whisper%20V3-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

---

## ✨ Features

- 🎙️ **Browser microphone recording** using Streamlit’s native audio input widget. [web:48]
- ⚡ **Instant transcription** via Groq’s speech-to-text API. [web:53][web:55]
- 📂 **Drag and drop audio upload** for existing files.
- 🌍 **Multilingual** — English, Hindi, or auto-detect.
- 📋 **Copy-ready output** for VS Code, browser prompts, terminals, or Claude Code workflows.
- 🗂️ **Session history** with timestamps, source labels, and word counts.
- ⬇️ **Download all transcriptions** as a `.txt` file.
- 🆓 **Free to start** — Groq offers a free tier for speech-to-text usage. [web:53]

---

## 🚀 Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/Voicescribe.git
cd Voicescribe
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your Groq API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Get a free API key from [console.groq.com](https://console.groq.com). [web:55]

### 4. Run the app

```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`.

---

## 📦 Requirements

The updated app only needs these packages:

```txt
streamlit>=1.34.0
groq>=0.9.0
python-dotenv>=1.0.0
```

`st.audio_input` is available in newer Streamlit versions, so Streamlit must be at least version 1.34.0. [web:48]

---

## 🎙️ How It Works

### Microphone flow

```text
Your Voice (Mic)
      ↓
Streamlit st.audio_input captures audio in the browser
      ↓
Audio is passed to the Python app
      ↓
Groq Whisper Large V3 transcribes it
      ↓
Text appears instantly in the UI
```

### File upload flow

```text
Drag & Drop Audio File
      ↓
Streamlit file_uploader accepts the file
      ↓
Audio bytes are sent to Groq
      ↓
Whisper Large V3 transcribes it
      ↓
Text appears instantly in the UI
```

This version does **not** use `sounddevice`, local WAV writing, or thread-based recording anymore. It relies on browser-side audio capture and Groq’s cloud transcription endpoint instead. [file:58][web:48][web:53]

---

## 🧱 Stack

| Tool | Role |
|------|------|
| **Streamlit** | UI framework and native microphone input via `st.audio_input` [web:48] |
| **Groq API** | Speech-to-text transcription with Whisper models [web:53][web:55] |
| **python-dotenv** | Loads `GROQ_API_KEY` from `.env` |

---

## 📂 Supported Input Modes

| Mode | Purpose |
|------|---------|
| **Record Voice** | Speak directly into the browser mic |
| **Upload / Drag & Drop** | Transcribe an existing audio file |

Supported upload formats in the app include: `mp3`, `wav`, `m4a`, `mp4`, `webm`, `mpeg`, and `mpga`. Groq’s speech-to-text API supports common audio file inputs for transcription workflows. [web:53]

---

## 💰 Cost

| Usage | Cost |
|-------|------|
| Free-tier usage | **$0 to start** [web:53] |
| Higher usage | Depends on Groq pricing and limits [web:55] |

Groq provides a free starting tier, so the app can be used without paying upfront. [web:53]

---

## 🛠️ Troubleshooting

### `AttributeError: module 'streamlit' has no attribute 'audio_input'`

Your Streamlit version is too old. Upgrade it:

```bash
pip install --upgrade streamlit
```

Then verify:

```bash
streamlit --version
```

You need Streamlit 1.34.0 or higher for `st.audio_input`. [web:48]

### Browser does not ask for microphone permission

Use a supported modern browser and ensure microphone access is allowed for `localhost`. Since this version uses browser-based microphone capture, permission is handled by the browser, not by Windows audio libraries. [web:48]

### Uploaded file fails

Check the format and file size. The app is designed for common audio formats and should work best with standard speech recordings.

---

## 🌐 Deploy Online

You can deploy this to Streamlit Community Cloud:

1. Push the repo to GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io).
3. Connect your repository.
4. Add `GROQ_API_KEY` in app secrets.
5. Deploy.

For the most reliable microphone behavior, local usage with `streamlit run app.py` is usually the easiest setup.

---

## Why This Exists

Wispr Flow is useful, but many users want a simpler personal alternative they can run themselves. This project recreates the core workflow — **speak → transcribe → copy text** — using Python, Streamlit, and Groq’s speech-to-text stack. [file:58][web:53]

---

## 📄 License

MIT — use it, modify it, ship it.

---

*Built by an AI developer from Nashik, India 🇮🇳 — because voice-to-text should be free.*

***

## 👤 Author

**Seshank** — AI Systems Architect | Agentic AI & LLM Interoperability  
🔗 [LinkedIn](https://www.linkedin.com/in/seshankch/) | 🐙 [GitHub](https://github.com/SESHANKCH7171)

***

## ⭐ If this helped you

Star the repo and share it with a developer who's tired of single-provider lock-in.
