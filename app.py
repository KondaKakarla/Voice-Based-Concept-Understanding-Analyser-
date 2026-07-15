from modules.file_handler import save_uploaded_file
from modules.transcription import transcribe_audio
from modules.semantic_similarity import calculate_similarity
from modules.speech_analysis import analyze_speech
from modules.waveform import plot_waveform
from modules.feedback import generate_feedback
from modules.pdf_report import generate_pdf
import streamlit as st

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
### AI Powered Concept Evaluation System

Evaluate spoken explanations using Artificial Intelligence.

### Features

- 🧠 Concept Understanding
- 🎙 Speech Fluency
- 📊 Semantic Similarity
- 📈 Waveform Analysis
- 🤖 AI Feedback
- 📄 PDF Report
""")

st.divider()

# ----------------------------
# Topic Selection
# ----------------------------
topic = st.selectbox(
    "Select Concept",
    [
        "Machine Learning",
        "Cloud Computing",
        "Artificial Intelligence",
        "Data Science",
        "Cyber Security"
    ]
)

st.write("### Selected Topic")
st.info(topic)

# ----------------------------
# Audio Upload
# ----------------------------
uploaded_audio = st.file_uploader(
    "Upload Audio File",
    type=["wav", "mp3", "m4a"]
)

# ----------------------------
# Process Audio
# ----------------------------
if uploaded_audio is not None:

    saved_path = save_uploaded_file(uploaded_audio)

    st.success("✅ Audio Uploaded Successfully!")

    st.audio(uploaded_audio)

    st.subheader("📈 Audio Waveform")
    fig = plot_waveform(saved_path)
    st.pyplot(fig)

    st.subheader("📁 Saved Location")
    st.code(saved_path)

    if st.button("🚀 Evaluate"):

        # ----------------------------
        # Transcription
        # ----------------------------
        with st.spinner("🎙 Transcribing Audio..."):
            transcript = transcribe_audio(saved_path)

        st.success("✅ Transcription Completed!")

        st.subheader("📝 Transcript")
        st.write(transcript)

        # ----------------------------
        # Speech Analysis
        # ----------------------------
        speech = analyze_speech(transcript)

        st.subheader("🎙 Speech Analysis")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Words", speech["word_count"])

        with col2:
            st.metric("Fillers", speech["fillers"])

        with col3:
            st.metric("WPM", speech["wpm"])

        # ----------------------------
        # Semantic Similarity
        # ----------------------------
        with st.spinner("🧠 Calculating Semantic Similarity..."):
            score = calculate_similarity(topic, transcript)

        st.subheader("🧠 Concept Understanding")

        st.metric(
            label="Similarity Score",
            value=f"{score:.2f}%"
        )

        if score >= 80:
            st.success("🌟 Excellent Understanding")

        elif score >= 60:
            st.warning("🙂 Moderate Understanding")

        else:
            st.error("❌ Poor Understanding")

        # ----------------------------
        # Overall AI Score
        # ----------------------------
        overall = score

        if speech["fillers"] <= 2:
            overall += 5

        if speech["wpm"] >= 100:
            overall += 5

        overall = min(100, overall)

        st.subheader("⭐ Overall AI Score")

        st.metric(
            label="Overall Score",
            value=f"{overall:.2f}/100"
        )

        if overall >= 90:
            st.success("🏆 Outstanding Performance")

        elif overall >= 75:
            st.success("✅ Good Performance")

        elif overall >= 60:
            st.warning("⚠️ Average Performance")

        else:
            st.error("❌ Needs Improvement")

        # ----------------------------
        # AI Feedback
        # ----------------------------
        st.subheader("🤖 AI Feedback")

        feedback = generate_feedback(score, speech)

        for item in feedback:
            st.write(item)
        

        # ----------------------------
        # PDF Report
        # ----------------------------
                # ----------------------------
        # PDF Report
        # ----------------------------
        pdf_file = generate_pdf(
            topic,
            transcript,
            score,
            overall,
            speech
        )

        st.subheader("📄 Download Report")

        with open(pdf_file, "rb") as file:
            st.download_button(
                label="⬇ Download AI Evaluation Report",
                data=file,
                file_name="AI_Evaluation_Report.pdf",
                mime="application/pdf"
            )