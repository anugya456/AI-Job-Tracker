import spacy
import re
from resume_parser import extract_resume_text
import config

# Load SpaCy NLP model
nlp = spacy.load("en_core_web_sm")


def extract_skills_from_text(resume_text):
    """Extracts skills from resume text using NLP and keyword matching."""
    extracted_skills = set()
    doc = nlp(resume_text)

    # Extracting noun phrases (potential skills)
    for chunk in doc.noun_chunks:
        skill = chunk.text.strip()
        if skill in config.TECHNICAL_SKILLS:
            extracted_skills.add(skill)

    # Matching predefined skills in resume text (case-insensitive)
    for skill in config.TECHNICAL_SKILLS:
        if re.search(rf"\b{re.escape(skill)}\b", resume_text, re.IGNORECASE):
            extracted_skills.add(skill)

    return sorted(list(extracted_skills))

def get_resume_skills():
    """Wrapper function to extract skills from the resume file."""
    resume_text = extract_resume_text()
    if not resume_text:
        return []

    skills = extract_skills_from_text(resume_text)
    return skills

if __name__ == "__main__":
    extracted_skills = get_resume_skills()
    print("\nExtracted Skills:")
    print(", ".join(extracted_skills) if extracted_skills else "No skills detected.")
