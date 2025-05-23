"""
Project Recommender Module
Generates relevant project ideas based on missing skills or keywords.
"""

from typing import List
import logging

# Simple project template bank per skill
PROJECT_TEMPLATES = {
    "pandas": "Build a data cleaning and analysis pipeline using Pandas on a real-world dataset.",
    "sql": "Create a SQL-based reporting dashboard for analyzing e-commerce transactions.",
    "machine": "Train a machine learning model on a Kaggle dataset and evaluate performance.",
    "aws": "Deploy a Flask app on AWS using EC2 and S3.",
    "docker": "Dockerize a Python microservice and deploy it using Docker Compose.",
    "api": "Design and document a RESTful API using FastAPI and Swagger.",
    "spark": "Build a distributed data processing job using PySpark for log analytics.",
    "kubernetes": "Deploy a multi-container app to a Kubernetes cluster using Helm charts.",
    "llm": "Build an LLM-powered question-answering app using OpenAI APIs.",
    "react": "Create a React frontend that interacts with a backend ML inference API."
}


def recommend_projects(missing_skills: List[str]) -> List[str]:
    """
    Recommends relevant projects based on missing keywords/skills.

    Args:
        missing_skills: List of keywords or skills the resume lacks.

    Returns:
        List of project descriptions.
    """
    recommended = []
    for skill in missing_skills:
        for keyword, template in PROJECT_TEMPLATES.items():
            if keyword in skill:
                recommended.append(template)
                break

    if not recommended:
        recommended.append("Research and replicate an open-source project in your desired role's domain.")

    logging.info("Recommended projects: %s", recommended)
    return recommended
