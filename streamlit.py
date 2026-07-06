import streamlit as st
import os
import tempfile
import json

# Backend Modules
from models.whisper_model import transcribe_audio
from models.semantic import semantic_similarity
from models.audio_analysis import analyze_audio
from models.scoring import calculate_score

# -------------------- PAGE CONFIG --------------------

st.set_page_config(
    page_title="Voice Based Concept Understanding Analyser",
    page_icon="🎤",
    layout="wide"
)

st.title("🎤 Voice Based Concept Understanding Analyser")
st.write("Evaluate conceptual understanding using AI-powered speech analysis.")

# -------------------- LOAD REFERENCE CONCEPTS --------------------

with open("reference/concepts.json", "r") as f:
    concepts = json.load(f)

topic = st.selectbox(
    "Select Concept",
    list(concepts.keys())
)

reference_text = concepts[topic]

# -------------------- AUDIO UPLOAD --------------------

uploaded_file = st.file_uploader(
    "Upload Audio",
    type=["wav", "mp3", "m4a"]
)

# -------------------- ANALYZE BUTTON --------------------

if uploaded_file is not None:

    st.audio(uploaded_file)

    if st.button("Analyze Audio"):

        with st.spinner("Processing Audio..."):

            # Save uploaded file temporarily
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
                tmp.write(uploaded_file.read())
                audio_path = tmp.name

            # -------------------- Speech to Text --------------------

            transcript = transcribe_audio(audio_path)

            # -------------------- Semantic Similarity --------------------

            semantic_score = semantic_similarity(
                reference_text,
                transcript
            )

            # -------------------- Audio Analysis --------------------

            audio_metrics = analyze_audio(
                audio_path,
                transcript
            )

            # -------------------- Final Score --------------------

            final_score = calculate_score(
                semantic_score,
                audio_metrics
            )

        # -------------------- DISPLAY RESULTS --------------------

        st.success("Analysis Completed")

        st.subheader("Transcript")

        st.write(transcript)

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Semantic Similarity",
                f"{semantic_score:.2f}"
            )

            st.metric(
                "Speech Duration",
                f"{audio_metrics['speech_duration']:.2f} sec"
            )

            st.metric(
                "Pause Ratio",
                f"{audio_metrics['pause_ratio']:.2f}"
            )

        with col2:

            st.metric(
                "Filler Words",
                audio_metrics["filler_count"]
            )

            st.metric(
                "Energy",
                f"{audio_metrics['energy']:.4f}"
            )

            st.metric(
                "Overall Score",
                f"{final_score:.1f}/100"
            )

        # -------------------- FEEDBACK --------------------

        st.subheader("Performance")

        if final_score >= 85:
            st.success("Excellent Concept Understanding")

        elif final_score >= 70:
            st.info("Good Understanding. Improve fluency.")

        elif final_score >= 50:
            st.warning("Average Understanding. More explanation required.")

        else:
            st.error("Poor Understanding. Please practice the topic.")

        # -------------------- REFERENCE ANSWER --------------------

        with st.expander("Reference Concept"):

            st.write(reference_text)

        # Remove temporary file
        os.remove(audio_path)

else:
    st.info("Please upload an audio file to begin analysis.")