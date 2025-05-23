"""
Resume Optimizer Module
Suggests improvements to resume content based on job requirements.
"""

from typing import List
import logging


def suggest_resume_improvements(missing_skills: List[str]) -> List[str]:
    """
    Generates suggested resume enhancements for missing skills.

    Args:
        missing_skills: List of skills not found in resume but required in job.

    Returns:
        List of bullet-point suggestions for resume additions.
    """
    suggestions = []

    for skill in missing_skills:
        if "sql" in skill:
            suggestions.append("Add examples of using SQL for querying databases and generating reports.")
        elif "api" in skill:
            suggestions.append("Include experience with REST API design, development, or consumption.")
        elif "aws" in skill:
            suggestions.append("Mention usage of AWS services like EC2, Lambda, or S3 in prior work or projects.")
        elif "ml" in skill or "machine" in skill:
            suggestions.append("Highlight ML model training, evaluation, or deployment experience.")
        elif "docker" in skill:
            suggestions.append("Include containerization experience using Docker and Docker Compose.")
        elif "spark" in skill:
            suggestions.append("Demonstrate data engineering work using Apache Spark or PySpark.")
        elif "kubernetes" in skill:
            suggestions.append("Mention orchestration/deployment using Kubernetes or Helm.")
        elif "react" in skill:
            suggestions.append("Include frontend development work with React or similar libraries.")
        elif "pandas" in skill:
            suggestions.append("Emphasize data manipulation or analysis using Pandas.")
        elif "llm" in skill or "openai" in skill:
            suggestions.append("List experience building apps powered by OpenAI or similar LLM APIs.")

    if not suggestions:
        suggestions.append("Add concrete examples of applying job-related skills in real-world contexts.")

    logging.info("Resume suggestions: %s", suggestions)
    return suggestions
