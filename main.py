"""
Main Streamlit App
Provides UI to analyze resume vs job description and get suggestions.
"""

import streamlit as st
from app.session_state import init_session_state
from app.resume_parser import extract_text as extract_resume_text
from app.job_parser import extract_text as extract_jd_text
from app.gap_analyzer import analyze_gaps
from app.project_recommender import recommend_projects
from app.resume_optimizer import suggest_resume_improvements

from pathlib import Path

st.set_page_config(page_title="JobFit AI Agent", layout="wide")

# Initialize state
init_session_state()

st.title("🔍 JobFit AI Agent")
st.markdown("Upload a job description and your resume to analyze skill gaps and receive project and resume suggestions.")

col1, col2 = st.columns(2)

with col1:
    jd_file = st.file_uploader("📄 Upload Job Description (PDF/DOCX/TXT)", type=["pdf", "docx", "txt"], key="jd")
with col2:
    resume_file = st.file_uploader("📄 Upload Your Resume (PDF/DOCX/TXT)", type=["pdf", "docx", "txt"], key="resume")

if jd_file and resume_file:
    with st.spinner("Extracting and analyzing text..."):
        try:
            st.session_state.jd_text = extract_jd_text(jd_file)
            st.session_state.resume_text = extract_resume_text(resume_file)
        except Exception as e:
            st.error(f"❌ Error processing files: {str(e)}")

        if st.session_state.jd_text and st.session_state.resume_text:
            matched, missing = analyze_gaps(st.session_state.jd_text, st.session_state.resume_text)
            st.session_state.checklist = matched
            st.session_state.missing_skills = missing
            st.session_state.projects = recommend_projects(missing)
            st.session_state.resume_suggestions = suggest_resume_improvements(missing)

            # Save history
            st.session_state.history.append({
                "matched": matched,
                "missing": missing,
                "projects": st.session_state.projects,
                "suggestions": st.session_state.resume_suggestions
            })

            st.success("✅ Analysis complete!")

st.divider()

if st.session_state.checklist:
    st.subheader("✅ Skills You Already Have")
    st.markdown("\n".join(f"- {skill}" for skill in st.session_state.checklist))

if st.session_state.missing_skills:
    st.subheader("🚧 Missing Skills / Gaps")
    st.markdown("\n".join(f"- {skill}" for skill in st.session_state.missing_skills))

if st.session_state.projects:
    st.subheader("💡 Suggested Projects to Build")
    for proj in st.session_state.projects:
        st.markdown(f"- {proj}")

if st.session_state.resume_suggestions:
    st.subheader("✍️ Resume Improvement Suggestions")
    for s in st.session_state.resume_suggestions:
        st.markdown(f"- {s}")

st.divider()

if st.session_state.history:
    if st.checkbox("📚 Show Session History"):
        st.write(st.session_state.history)