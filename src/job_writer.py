import logging
import os
from datetime import datetime
import pytz
import gspread
from google.oauth2.service_account import Credentials
import config
from utils import clean_html
from logger import setup_logger


logger = setup_logger("job_writer")

def add_filtered_jobs_to_sheets(jobs, model_used="TF-IDF", batch_size=100, update_pool=False):
    """Upserts job listings to Google Sheets in batches."""
    logging.info("Connecting to Google Sheets...")

    try:
        creds = Credentials.from_service_account_file(config.SHEETS_CREDENTIALS_FILE, scopes=config.GOOGLE_SCOPES)
        client = gspread.authorize(creds)
        sheet = client.open(config.GOOGLE_SHEET_NAME)

        job_pool = sheet.worksheet(config.JOB_POOL_SHEET_NAME)
        recommended_jobs = sheet.worksheet(config.RECOMMENDED_JOBS_SHEET_NAME)

        # Get current timestamp
        current_time = datetime.now(pytz.timezone("UTC")).strftime("%Y-%m-%d %H:%M:%S")

        # Step 1: Update Job Pool (if applicable)
        if update_pool:
            existing_jobs = job_pool.get_all_records()
            existing_urls = {job["URL"]: idx + 2 for idx, job in enumerate(existing_jobs)}

            pool_rows_to_add = []
            pool_rows_to_update = []

            for job in jobs:
                row_number = existing_urls.get(job.get("url"))
                row_data = [
                    job.get("title", "N/A"),  # Job Title
                    job.get("company_name", "N/A"),  # Company
                    job.get("candidate_required_location", "N/A"),  # Location
                    clean_html(job.get("description", "N/A")),  # Cleaned Job Description
                    job.get("url", "N/A"),  # URL
                    current_time,  # Date Added
                    "Remotive",  # Job Portal
                    job.get("type", "N/A"),  # Job Type
                    job.get("category", "N/A"),  # Job Category
                    model_used
                ]

                if row_number:
                    # Update existing job (collect rows to update)
                    pool_rows_to_update.append((row_number, row_data))
                else:
                    # Add new job
                    pool_rows_to_add.append(row_data)

            # Batch Update Existing Rows in Job Pool
            for start in range(0, len(pool_rows_to_update), batch_size):
                batch = pool_rows_to_update[start:start + batch_size]
                cell_range = f"A{batch[0][0]}:I{batch[-1][0]}"
                batch_values = [row[1] for row in batch]
                job_pool.update(cell_range, batch_values)
                logging.info(f"Batch updated {len(batch)} existing jobs in 'Job Pool'.")

            # Batch Add New Rows to Job Pool
            for start in range(0, len(pool_rows_to_add), batch_size):
                batch = pool_rows_to_add[start:start + batch_size]
                job_pool.append_rows(batch, value_input_option="RAW")
                logging.info(f"Batch added {len(batch)} new jobs to 'Job Pool'.")

        # Step 2: Update Recommended Jobs
        sorted_jobs = sorted(jobs, key=lambda x: float(x.get("score", 0)), reverse=True)[:config.TOP_N_JOBS]

        # Fetch existing recommended jobs and their URLs
        existing_recommended = recommended_jobs.get_all_records()
        existing_recommended_urls = {job["URL"]: idx + 2 for idx, job in enumerate(existing_recommended)}

        recommended_rows_to_add = []
        recommended_rows_to_update = []

        for job in sorted_jobs:
            row_number = existing_recommended_urls.get(job.get("url"))
            row_data = [
                job.get("title", "N/A"),  # Job Title
                job.get("company_name", "N/A"),  # Company
                job.get("candidate_required_location", "N/A"),  # Location
                clean_html(job.get("description", "N/A")), 
                float(job.get("score", 0)),  # Relevance Score
                "",  # Placeholder for AI Insights
                "",  # Placeholder for Application Status
                "",  # Placeholder for Follow-up Date
                current_time,  # Last Updated
                job.get("url", "N/A"),  # URL
                "Remotive",  # Job Portal
                job.get("category", "N/A"),  # Job Category
                job.get("type", "N/A"), # Job Type
                model_used
            ]

            if row_number:
                # Update existing recommended job
                recommended_rows_to_update.append((row_number, row_data))
            else:
                # Add new recommended job
                recommended_rows_to_add.append(row_data)

        # Batch Update Existing Recommended Jobs
        for start in range(0, len(recommended_rows_to_update), batch_size):
            batch = recommended_rows_to_update[start:start + batch_size]
            cell_range = f"A{batch[0][0]}:N{batch[-1][0]}"
            batch_values = [row[1] for row in batch]
            recommended_jobs.update(cell_range, batch_values)
            logging.info(f"Batch updated {len(batch)} existing jobs in 'Recommended Jobs'.")

        # Batch Add New Recommended Jobs
        for start in range(0, len(recommended_rows_to_add), batch_size):
            batch = recommended_rows_to_add[start:start + batch_size]
            recommended_jobs.append_rows(batch, value_input_option="RAW")
            logging.info(f"Batch added {len(batch)} new recommended jobs to 'Recommended Jobs'.")

    except Exception as e:
        logging.error(f"Error accessing Google Sheets: {e}")

