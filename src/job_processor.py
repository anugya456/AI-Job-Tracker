import time
import logging
import os
from datetime import datetime
import config
from job_scraper import get_new_jobs, load_cached_jobs
from job_filter import score_job_relevance
from job_writer import add_filtered_jobs_to_sheets
from skill_extractor import get_resume_skills
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from logger import setup_logger

logger = setup_logger("job_processor")

logger.info("Starting job processing...")


def process_jobs():
    """Fetches, processes, and filters jobs using NLP-based relevance scoring with TF-IDF."""
    logger.info("Starting job processing...")

    # Step 1: Extract skills from resume
    print("Extracting skills from resume...")
    resume_skills = get_resume_skills()
    print(f"Extracted Skills: {', '.join(resume_skills)}")
    logger.info(f"Extracted Skills: {resume_skills}")

    print("Fetching new jobs from Remotive.io...")
    new_jobs = get_new_jobs()

    # Step 2: Check if new jobs exist
    if new_jobs:
        print(f"{len(new_jobs)} new jobs found. Adding to Job Pool...")
        logger.info(f"{len(new_jobs)} new jobs found. Adding to Job Pool...")
        add_filtered_jobs_to_sheets(new_jobs, update_pool=True)

    else:
        print("No new jobs found. Using cached jobs...")
        logger.warning("No new jobs fetched. Using cached jobs.")
        new_jobs = load_cached_jobs()

    print(f"{len(new_jobs)} jobs fetched. Computing TF-IDF and filtering relevant ones...")
    logger.info(f"Fetched {len(new_jobs)} jobs. Computing TF-IDF...")

    # **Step 3: Compute TF-IDF for all job descriptions**
    job_texts = [job["description"] for job in new_jobs] + [config.IDEAL_JOB_DESC]  # Add ideal job description
    vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
    tfidf_matrix = vectorizer.fit_transform(job_texts)  # Compute TF-IDF matrix
    feature_names = vectorizer.get_feature_names_out()

    # **Extract Ideal Job Vector**
    ideal_job_vector = tfidf_matrix[-1]  # Last entry is the ideal job description
    job_tfidf_vectors = tfidf_matrix[:-1]  # Exclude ideal job vector from job postings

    logger.info("TF-IDF computation complete. Starting job relevance scoring.")

    # **Step 4: Process and score Jobs in Batches**
    filtered_jobs = []
    batch_size = 100
    total_jobs = len(new_jobs)
    start_time = time.time()

    for idx, (job, job_vector) in enumerate(zip(new_jobs, job_tfidf_vectors)):
        score = score_job_relevance(job["title"], job["description"], job_vector, vectorizer, feature_names, resume_skills, ideal_job_vector)

        logger.debug(f"Job {idx+1}/{total_jobs}: {job['title']} | Score: {score}")

        if score > 3.5:
            filtered_jobs.append({
                "title": job["title"],
                "company": job["company_name"],
                "location": job["candidate_required_location"],
                "url": job["url"],
                "score": float(score)
            })

        # **Log progress every batch_size jobs**
        if (idx + 1) % batch_size == 0:
            elapsed_time = time.time() - start_time
            print(f"Processed {idx+1}/{total_jobs} jobs... Time elapsed: {elapsed_time:.2f} sec")
            logger.info(f"Processed {idx+1}/{total_jobs} jobs... Time elapsed: {elapsed_time:.2f} sec")

    total_time = time.time() - start_time
    print(f"Job filtering completed in {total_time:.2f} sec")
    logger.info(f"Job filtering completed in {total_time:.2f} sec")

    # **Step 5: Save to Recommended Jobs if any filtered jobs exist**
    if filtered_jobs:
        print(f"{len(filtered_jobs)} relevant jobs found. Saving to Recommended Jobs sheet...")
        logger.info(f"{len(filtered_jobs)} relevant jobs found. Saving to Recommended Jobs sheet...")
        add_filtered_jobs_to_sheets(filtered_jobs)
    else:
        print("No relevant jobs found.")
        logger.warning("No jobs passed the filtering criteria.")

    # **Sort jobs by score**
    sorted_jobs = sorted(filtered_jobs, key=lambda x: x["score"], reverse=True)

    # **Log top 10 jobs**
    logger.info("Top 10 highest-scoring jobs:")
    for job in sorted_jobs[:10]:
        logger.info(f"{job['title']} | {job['company']} | Score: {job['score']}")

    logger.info("Job processing completed.\n")


# Close the handlers explicitly at the end
def close_logger():
    for handler in logger.handlers:
        handler.close()
        logger.removeHandler(handler)

if __name__ == "__main__":
    try:
        process_jobs()
    finally:
        close_logger()