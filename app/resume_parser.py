import io
import logging
from typing import Union
from pdfminer.high_level import extract_text as extract_pdf_text
from docx import Document

def extract_text(file: Union[io.BytesIO, io.StringIO]) -> str:
    """
    Extracts plain text from uploaded resume file.

    Args:
        file: Uploaded file object (Streamlit uploader).

    Returns:
        Extracted plain text from resume.

    Raises:
        ValueError: If the file type is unsupported or unreadable.
    """
    filename = file.name.lower()
    logging.info("Extracting text from resume: %s", filename)

    if filename.endswith(".txt"):
        return file.read().decode("utf-8")

    elif filename.endswith(".pdf"):
        try:
            return extract_pdf_text(file)
        except Exception as e:
            logging.error("Failed to extract PDF: %s", str(e))
            raise ValueError("Failed to read PDF file.")

    elif filename.endswith(".docx"):
        try:
            doc = Document(file)
            return "\n".join([para.text for para in doc.paragraphs])
        except Exception as e:
            logging.error("Failed to extract DOCX: %s", str(e))
            raise ValueError("Failed to read DOCX file.")

    else:
        logging.warning("Unsupported file type: %s", filename)
        raise ValueError("Unsupported file type. Only TXT, PDF, and DOCX are supported.")
