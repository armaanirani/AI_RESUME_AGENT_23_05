"""
Session State Initialization Module
Maintains Streamlit session state across components.
"""

def init_session_state() -> None:
    """
    Initializes default session state keys to track inputs and outputs.
    Should be called once at the start of the app.
    """
    import streamlit as st

    st.session_state.setdefault("jd_text", None)
    st.session_state.setdefault("jr_text", None)
    st.session_state.setdefault("resume_text", None)
    st.session_state.setdefault("checklist", [])
    st.session_state.setdefault("missing_skills", [])
    st.session_state.setdefault("projects", [])
    st.session_state.setdefault("resume_suggestions", [])
    st.session_state.setdefault("history", [])
