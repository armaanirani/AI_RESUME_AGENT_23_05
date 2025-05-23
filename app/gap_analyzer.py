"""
Gap Analyzer Module
Compares job requirements with resume text to identify skill matches and gaps.
"""

import logging
import re
from typing import List, Tuple
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def clean_text(text: str) -> str:
    """
    Basic text cleaning: lowercasing, removing non-alphanumerics.
    """
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    return text


def extract_keywords(text: str, max_features: int = 30) -> List[str]:
    """
    Extracts keywords from text using bag-of-words frequency.

    Args:
        text: The input text string to extract keywords from.
        max_features: Number of top keywords to extract.

    Returns:
        List of extracted keyword strings.
    """
    try:
        cleaned = clean_text(text)
        vectorizer = CountVectorizer(max_features=max_features, stop_words="english")
        X = vectorizer.fit_transform([cleaned])
        return vectorizer.get_feature_names_out().tolist()
    except Exception as e:
        logging.error("Keyword extraction failed: %s", str(e))
        return []


def analyze_gaps(jd_text: str, resume_text: str) -> Tuple[List[str], List[str]]:
    """
    Compares job description keywords with resume to determine matches and gaps.

    Args:
        jd_text: Job description and requirements text.
        resume_text: Candidate's resume text.

    Returns:
        A tuple of (met_keywords, missing_keywords).
    """
    try:
        jd_keywords = extract_keywords(jd_text)
        resume_keywords = extract_keywords(resume_text)

        matched = [kw for kw in jd_keywords if kw in resume_keywords]
        missing = [kw for kw in jd_keywords if kw not in resume_keywords]

        logging.info("Matched: %s", matched)
        logging.info("Missing: %s", missing)

        return matched, missing

    except Exception as e:
        logging.error("Gap analysis failed: %s", str(e))
        return [], []
