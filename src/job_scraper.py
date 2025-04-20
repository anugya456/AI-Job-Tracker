import requests
import json
import os
import config


def fetch_jobs_from_remotive():
    """Fetches remote jobs from Remotive.io API and returns a list of jobs."""
    response = requests.get(config.REMOTIVE_URL)

    if response.status_code == 200:
        jobs = response.json().get("jobs", [])
        return jobs
    else:
        print(f"Error fetching jobs from Remotive.io: {response.status_code}")
        return []

def load_cached_jobs():
    """Loads cached job listings from JSON file."""
    if os.path.exists(config.CACHED_JOBS_FILE):
        with open(config.CACHED_JOBS_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []  # Return empty if the cache file is corrupted
    return []

def save_jobs_to_cache(jobs):
    """Saves the latest job listings to cache."""
    with open(config.CACHED_JOBS_FILE, "w", encoding="utf-8") as f:
        json.dump(jobs, f, indent=4)

def get_new_jobs():
    """Fetches new jobs from API and compares with cache to find fresh listings."""
    fetched_jobs = fetch_jobs_from_remotive()
    cached_jobs = load_cached_jobs()

    # Convert cached jobs to a set of job URLs for easy comparison
    cached_urls = {job["url"] for job in cached_jobs}
    
    # Filter out already cached jobs
    new_jobs = [job for job in fetched_jobs if job["url"] not in cached_urls]

    if new_jobs:
        print(f"Found {len(new_jobs)} new jobs. Adding to Google Sheets...")
        save_jobs_to_cache(fetched_jobs)  # Update cache with latest jobs
    else:
        print("No new jobs found.")

    return new_jobs
