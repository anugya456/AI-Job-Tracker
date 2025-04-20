import spacy
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import config

# Load NLP Model
print("Loading NLP Model...")
nlp = spacy.load("en_core_web_md")  # Medium model for balanced speed & accuracy

# Convert ideal job description into vector representation
ideal_vector = nlp(config.IDEAL_JOB_DESC).vector.reshape(1, -1)

def extract_job_entities(text, resume_skills):
    """
    Extracts key entities from a job description using Named Entity Recognition (NER).
    - Identifies company names, job roles, and relevant skills dynamically.
    - Uses dependency parsing to extract job titles instead of unreliable entity labels.
    """
    doc = nlp(text)
    job_role, skills = [], []
    company_name = "Unknown"

    # Extract company names from the text
    for ent in doc.ents:
        if ent.label_ == "ORG":  # Organization (Company Name)
            company_name = ent.text

    # Extract job titles using dependency parsing (Scrum Master, Project Manager, etc.)
    for token in doc:
        if any(keyword in token.text.lower() for keyword in ["manager", "master", "engineer", "coordinator", "consultant"]):
            if token.pos_ in ["NOUN", "PROPN"] and token.dep_ in ["nsubj", "attr", "compound"]:
                job_role.append(token.text)

    # Construct job title from extracted words
    job_role = " ".join(job_role) if job_role else "Unknown"

    # Ensure resume_skills is a list of actual words
    if isinstance(resume_skills, list):
        resume_skills = set(map(str.lower, resume_skills))  # Convert list of words to lowercase set
    else:
        raise TypeError(f"Expected list for resume_skills, got {type(resume_skills)}")
    
    # Extract technical terms and keywords from text
    for token in doc:
        if token.pos_ in ["NOUN", "PROPN"] and token.text.lower() in resume_skills:
            skills.append(token.text)

    return {
        "company": company_name,
        "job_role": job_role,
        "skills": list(set(skills))
    }

def compute_tfidf_weights(jobs):
    """
    Computes TF-IDF scores for all job descriptions to weigh skill importance.
    - Skills that appear frequently across multiple job postings are given lower importance.
    - Rare but relevant skills get higher importance.
    """
    job_descriptions = [job["description"] for job in jobs]
    
    # TF-IDF Vectorizer
    vectorizer = TfidfVectorizer(stop_words="english", max_features=1000)
    tfidf_matrix = vectorizer.fit_transform(job_descriptions)
    feature_names = vectorizer.get_feature_names_out()

    return vectorizer, tfidf_matrix, feature_names

def score_job_relevance(job_title, job_description, job_vector, vectorizer, feature_names, resume_skills, ideal_job_vector):
    """Calculates job relevance using TF-IDF cosine similarity, skill matching, and title weighting."""

    # Convert sparse vector to array
    job_tfidf_vector = job_vector.toarray()

    # Compute similarity with ideal job profile
    similarity_score = cosine_similarity(job_tfidf_vector, ideal_job_vector.toarray())[0][0]

    # Extract job details
    job_info = extract_job_entities(job_description, resume_skills)

    # Skill match count
    skill_match_count = sum(1 for skill in job_info["skills"] if skill.lower() in resume_skills)

    # Title match weight
    job_title_lower = job_title.lower()
    title_match_weight = 5 if any(title in job_title_lower for title in config.TARGET_TITLES) else 0

    # Compute final score with scaling
    final_score = (similarity_score * 100) + (skill_match_count * 5) + title_match_weight

    return float(final_score)  # Convert to standard float