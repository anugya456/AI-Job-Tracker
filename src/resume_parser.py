import fitz  # PyMuPDF for PDFs
import docx  # python-docx for DOCX
import os
import config

def extract_text_from_pdf(pdf_path):
    """Extracts raw text from a PDF file."""
    try:
        doc = fitz.open(pdf_path)
        text = "\n".join([page.get_text("text") for page in doc])
        return text.strip()
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return ""

def extract_text_from_docx(docx_path):
    """Extracts raw text from a DOCX file."""
    try:
        doc = docx.Document(docx_path)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text.strip()
    except Exception as e:
        print(f"Error extracting text from DOCX: {e}")
        return ""

def extract_resume_text():
    """Detects file format and extracts text accordingly."""
    resume_path = config.RESUME_FILE
    if resume_path.lower().endswith(".pdf"):
        return extract_text_from_pdf(resume_path)
    elif resume_path.lower().endswith(".docx"):
        return extract_text_from_docx(resume_path)
    else:
        print("Unsupported file format. Please use PDF or DOCX.")
        return ""

if __name__ == "__main__":
    extracted_text = extract_resume_text()
    print("\nExtracted Resume Text Preview:")
    print(extracted_text[:1000])  # Show first 1000 characters
