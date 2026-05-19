import streamlit as st
from groq import Groq
import os
import io
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# ── Page Config ────────────────────────────────────────────
st.set_page_config(
    page_title="VoiceScribe — Wispr Flow Clone",
    page_icon="🎙️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ── Custom CSS ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.stApp { background: #0f0f0f; color: #e0e0e0; }
.hero-title {
    font-size: 2.2rem; font-weight: 700; color: #ffffff;
    letter-spacing: -0.03em; margin-bottom: 0.2rem; line-height: 1.2;
}
.hero-sub { font-size: 1rem; color: #888; margin-bottom: 1.5rem; }
.hero-badge {
    display: inline-block; background: #1a2e1a; color: #4caf50;
    border: 1px solid #2e4d2e; border-radius: 999px; padding: 4px 14px;
    font-size: 0.75rem; font-weight: 600; margin-bottom: 1rem; letter-spacing: 0.05em;
}
.result-box {
    background: #141414; border: 1px solid #2a2a2a; border-radius: 14px;
    padding: 20px 24px; margin: 1rem 0; font-size: 1rem; line-height: 1.8;
    color: #e8e8e8; white-space: pre-wrap; word-wrap: break-word;
}
.history-item {
    background: #141414; border: 1px solid #222;
    border-radius: 10px; padding: 14px 18px; margin-bottom: 10px;
}
.history-time {
    font-size: 0.72rem; color: #555; margin-bottom: 6px;
    font-weight: 600; letter-spacing: 0.04em; text-transform: uppercase;
}
.history-text { font-size: 0.9rem; color: #ccc; line-height: 1.6; }
.stat-card {
    background: #141414; border: 1px solid #222;
    border-radius: 12px; padding: 16px 20px; text-align: center;
}
.stat-num { font-size: 1.8rem; font-weight: 700; color: #4fc3f7; }
.stat-label {
    font-size: 0.75rem; color: #666;
    text-transform: uppercase; letter-spacing: 0.05em; margin-top: 2px;
}
.info-tip {
    background: #1a1a2e; color: #7c9fff; border: 1px solid #2e3a6e;
    border-radius: 8px; padding: 10px 14px; font-size: 0.82rem;
    margin-bottom: 1rem; line-height: 1.6;
}
div[data-testid="stSidebar"] { background: #0a0a0a; border-right: 1px solid #1a1a1a; }
</style>
""", unsafe_allow_html=True)

# ── Session State ──────────────────────────────────────────
for k, v in {"history": [], "last_text": "", "total_words": 0}.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ── Transcribe Function ────────────────────────────────────
def transcribe_audio(audio_bytes, filename, api_key, language, model):
    try:
        client = Groq(api_key=api_key)
        audio_file = (filename, io.BytesIO(audio_bytes), "audio/wav")
        kwargs = {"model": model, "file": audio_file}
        if language != "auto":
            kwargs["language"] = language
        result = client.audio.transcriptions.create(**kwargs)
        return result.text.strip()
    except Exception as e:
        return f"❌ Groq Error: {str(e)}"

def save_to_history(text, language, source):
    word_count = len(text.split())
    st.session_state.total_words += word_count
    st.session_state.last_text = text
    st.session_state.history.insert(0, {
        "text": text,
        "time": datetime.now().strftime("%I:%M %p"),
        "words": word_count,
        "lang": language,
        "source": source
    })

# ── Sidebar ────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### ⚙️ Settings")
    st.markdown("---")

    api_key = st.text_input(
        "Groq API Key",
        value=os.getenv("GROQ_API_KEY", ""),
        type="password",
        help="Free key at console.groq.com — no credit card needed"
    )

    language = st.selectbox(
        "Language",
        options=["en", "hi", "auto"],
        format_func=lambda x: {
            "en": "🇺🇸 English",
            "hi": "🇮🇳 Hindi",
            "auto": "🌍 Auto Detect"
        }[x],
        index=0
    )

    model = st.selectbox(
        "Whisper Model",
        options=["whisper-large-v3", "whisper-large-v3-turbo", "distil-whisper-large-v3-en"],
        index=0,
        help="Large V3 = best accuracy. Turbo = faster. Distil = English only, fastest."
    )

    st.markdown("---")
    st.markdown("### 📊 Session Stats")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-num">{len(st.session_state.history)}</div>
            <div class="stat-label">Clips</div>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-num">{st.session_state.total_words}</div>
            <div class="stat-label">Words</div>
        </div>""", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("🤖 Groq · Whisper Large V3")
    st.markdown("🐍 Python · Streamlit")
    st.markdown("[⭐ GitHub](https://github.com) · [🔑 Get Free API Key](https://console.groq.com)")

# ── Hero ───────────────────────────────────────────────────
st.markdown('<div class="hero-badge">🟢 FREE · NO WORD LIMITS · OPEN SOURCE</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-title">🎙️ VoiceScribe</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-sub">Your personal Wispr Flow — speak anything, get text instantly.</div>', unsafe_allow_html=True)

if not api_key:
    st.warning("👈 Add your **Groq API Key** in the sidebar. Free at [console.groq.com](https://console.groq.com)")
    st.stop()

st.markdown("---")

# ── TABS ──────────────────────────────────────────────────
tab1, tab2 = st.tabs(["🎙️ Record Voice", "📂 Upload / Drag & Drop"])

# ── TAB 1: MIC RECORDING ──────────────────────────────────
with tab1:
    st.markdown("""
    <div class="info-tip">
        🔵 <b>How to use:</b> Click the mic icon below → speak → click stop →
        hit <b>Transcribe</b>. Browser will ask mic permission the first time — click <b>Allow</b>.
    </div>
    """, unsafe_allow_html=True)

    audio_value = st.audio_input(
        "🎙️ Click mic to record",
        help="Click mic to start. Click again to stop. Then press Transcribe."
    )

    if audio_value is not None:
        st.audio(audio_value, format="audio/wav")
        st.success("✅ Audio captured! Click Transcribe below.")

        if st.button("⚡ Transcribe Recording", type="primary", use_container_width=True):
            with st.spinner("⚡ Sending to Groq Whisper..."):
                text = transcribe_audio(
                    audio_value.getvalue(), "recording.wav", api_key, language, model
                )
            if text.startswith("❌"):
                st.error(text)
            else:
                save_to_history(text, language, "🎙️ Mic")
                st.success("✅ Done!")
                st.rerun()
    else:
        st.info("👆 Click the mic icon above to start recording.")

# ── TAB 2: DRAG & DROP FILE UPLOAD ────────────────────────
with tab2:
    st.markdown("""
    <div class="info-tip">
        📂 <b>Drag & Drop</b> any audio file here, or click Browse.
        Supports: MP3, WAV, M4A, MP4, WEBM, MPEG. Max 25MB.
    </div>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Drop your audio file here",
        type=["mp3", "wav", "m4a", "mp4", "webm", "mpeg", "mpga"],
        label_visibility="collapsed"
    )

    if uploaded_file is not None:
        file_size_mb = uploaded_file.size / (1024 * 1024)

        c1, c2, c3 = st.columns(3)
        c1.metric("📄 File", uploaded_file.name[:18])
        c2.metric("📦 Size", f"{file_size_mb:.1f} MB")
        c3.metric("🎵 Format", uploaded_file.type.split("/")[-1].upper())

        st.audio(uploaded_file, format=uploaded_file.type)

        if file_size_mb > 25:
            st.error("❌ File too large. Groq accepts max 25MB.")
        else:
            if st.button("⚡ Transcribe File", type="primary", use_container_width=True):
                with st.spinner(f"⚡ Transcribing {uploaded_file.name}..."):
                    text = transcribe_audio(
                        uploaded_file.getvalue(), uploaded_file.name,
                        api_key, language, model
                    )
                if text.startswith("❌"):
                    st.error(text)
                else:
                    save_to_history(text, language, f"📂 {uploaded_file.name[:18]}")
                    st.success("✅ Done!")
                    st.rerun()

# ── Latest Result ──────────────────────────────────────────
if st.session_state.last_text:
    st.markdown("---")
    st.markdown("#### 📝 Latest Transcription")
    st.markdown(f'<div class="result-box">{st.session_state.last_text}</div>', unsafe_allow_html=True)
    col_copy, col_clear = st.columns([3, 1])
    with col_copy:
        st.code(st.session_state.last_text, language=None)
    with col_clear:
        if st.button("🗑️ Clear", use_container_width=True):
            st.session_state.last_text = ""
            st.rerun()

# ── History ───────────────────────────────────────────────
if st.session_state.history:
    st.markdown("---")
    st.markdown("#### 🗂️ Transcription History")

    col_dl, col_clr = st.columns([3, 1])
    with col_clr:
        if st.button("🗑️ Clear All", use_container_width=True):
            st.session_state.history = []
            st.session_state.total_words = 0
            st.session_state.last_text = ""
            st.rerun()
    with col_dl:
        full_text = "\n\n".join(
            [f"[{h['time']}] [{h['source']}]\n{h['text']}" for h in st.session_state.history]
        )
        st.download_button(
            "⬇️ Download All as .txt",
            data=full_text,
            file_name=f"voicescribe_{datetime.now().strftime('%Y%m%d_%H%M')}.txt",
            mime="text/plain",
            use_container_width=True
        )

    for item in st.session_state.history:
        st.markdown(f"""
        <div class="history-item">
            <div class="history-time">
                🕐 {item['time']} &nbsp;·&nbsp; {item['words']} words
                &nbsp;·&nbsp; {item['lang'].upper()} &nbsp;·&nbsp; {item['source']}
            </div>
            <div class="history-text">{item['text']}</div>
        </div>
        """, unsafe_allow_html=True)