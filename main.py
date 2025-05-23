import streamlit as st
import os
import logging
from pathlib import Path
from app import session_state, resume_parser, job_parser

# Setup logs directory and file
Path("logs").mkdir(exist_ok=True)
logging.basicConfig(
    filename="logs/agent.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

st.set_page_config(page_title="AI Resume Agent", layout="wide")
st.title("🤖 AI Resume Agent")
st.write("Upload a job description, job requirements, and your resume to get started.")

# Session state initialization
if 'parsed_resume' not in st.session_state:
    session_state.init_session_state()

# Layout
col1, col2 = st.columns(2)

with col1:
    jd_file = st.file_uploader("Upload Job Description (TXT/PDF/DOCX)", type=["txt", "pdf", "docx"])
    jr_file = st.file_uploader("Upload Job Requirements (TXT/PDF/DOCX)", type=["txt", "pdf", "docx"])

with col2:
    resume_file = st.file_uploader("Upload Your Resume (TXT/PDF/DOCX)", type=["txt", "pdf", "docx"])

if jd_file and jr_file and resume_file:
    try:
        jd_text = job_parser.extract_text(jd_file)
        jr_text = job_parser.extract_text(jr_file)
        resume_text = resume_parser.extract_text(resume_file)

        # Store in session state
        st.session_state["jd_text"] = jd_text
        st.session_state["jr_text"] = jr_text
        st.session_state["resume_text"] = resume_text

        st.success("Files successfully parsed. Proceed to analysis and recommendations.")
        logging.info("Uploaded files successfully parsed and stored in session state.")

        with st.expander("📄 Parsed Job Description"):
            st.text(jd_text[:1000])
        with st.expander("📄 Parsed Job Requirements"):
            st.text(jr_text[:1000])
        with st.expander("📄 Parsed Resume"):
            st.text(resume_text[:1000])

    except Exception as e:
        st.error(f"❌ Failed to parse files: {str(e)}")
        logging.error("Error during file parsing: %s", str(e))
else:
    st.info("⬆️ Upload all three documents to begin analysis.")