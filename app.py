import streamlit as st
import os
from speech_to_text import transcribe

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="VBCUA",
    page_icon="🎤",
    layout="wide"
)

# ----------------------------
# Title
# ----------------------------
st.title("🎤 Voice-Based Concept Understanding Analyser")

st.markdown("""
Welcome to the **Voice-Based Concept Understanding Analyser (VBCUA)**.

This AI-powered application evaluates:

- 📖 Concept Understanding
- 🎙️ Speech Fluency
- 🧠 Semantic Similarity
- 📊 Performance Score
""")

st.divider()

# ----------------------------
# Audio Upload
# ----------------------------
uploaded_file = st.file_uploader(
    "Upload your audio explanation",
    type=["wav", "mp3", "m4a"]
)

# ----------------------------
# Save Uploaded File
# ----------------------------
if uploaded_file is not None:

    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join("uploads", uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("✅ Audio uploaded successfully!")

    st.write("**File Name:**", uploaded_file.name)

    st.audio(file_path)

    # ----------------------------
    # Speech to Text
    # ----------------------------
    with st.spinner("Transcribing audio..."):

        text = transcribe(file_path)

    st.subheader("📝 Transcribed Text")

    st.write(text)  