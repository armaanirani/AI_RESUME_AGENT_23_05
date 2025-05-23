"""LLM Agent Controller

This module initializes the correct LLM based on .env settings,
and constructs the LangChain agents for the job analysis workflow.
"""

import os
from langchain.chat_models import ChatOpenAI
from langchain_community.chat_models import ChatGroq
from langchain_community.chat_models import ChatOllama
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from dotenv import load_dotenv

load_dotenv()

# --- Step 1: Load Config ---
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "openai").lower()

# --- Step 2: Instantiate LLM ---
def get_llm():
    if LLM_PROVIDER == "openai":
        return ChatOpenAI(
            temperature=0.3,
            model=os.getenv("OPENAI_MODEL", "gpt-4o"),
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )
    elif LLM_PROVIDER == "groq":
        return ChatGroq(
            temperature=0.3,
            model=os.getenv("GROQ_MODEL", "mixtral-8x7b"),
            groq_api_key=os.getenv("GROQ_API_KEY")
        )
    elif LLM_PROVIDER == "ollama":
        return ChatOllama(
            temperature=0.3,
            model=os.getenv("OLLAMA_MODEL", "llama3")
        )
    else:
        raise ValueError(f"Unsupported LLM provider: {LLM_PROVIDER}")

# --- Step 3: Define Tools (wrap existing functions/modules) ---
def checklist_tool(job_text):
    return "TODO: checklist output from job_text"

def project_tool(gaps):
    return "TODO: project ideas based on gaps"

def resume_suggest_tool(resume, job):
    return "TODO: resume suggestions"

TOOLS = [
    Tool(name="Checklist Generator", func=checklist_tool, description="Extracts requirements from job description."),
    Tool(name="Project Recommender", func=project_tool, description="Recommends projects based on skill gaps."),
    Tool(name="Resume Suggestor", func=resume_suggest_tool, description="Improves resume to match job requirements.")
]

# --- Step 4: Initialize Agent ---
def create_jobfit_agent():
    llm = get_llm()
    return initialize_agent(
        TOOLS,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
