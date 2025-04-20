import os
import os
from dotenv import load_dotenv

# Project root is the parent directory of src/
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Subdirectories
SRC_DIR = os.path.join(BASE_DIR, "src")
CONFIG_DIR = os.path.join(BASE_DIR, "config")
LOGS_DIR = os.path.join(BASE_DIR, "logs")
DATA_DIR = os.path.join(BASE_DIR, "data")

# Log files
SEND_GMAIL_LOG = os.path.join(LOGS_DIR, "send_gmail.log")
JOB_TRACKER_LOG = os.path.join(LOGS_DIR, "job_tracker.log")
JOB_WRITER_LOG = os.path.join(LOGS_DIR, "job_writer.log")

# Cached data
# File to store cached jobs (prevents duplicate fetches)
CACHED_JOBS_FILE = os.path.join(DATA_DIR, "cached_jobs.json")

# Google API credentials
TOKEN_JSON = os.path.join(DATA_DIR, "token.json")
TOKEN_PICKLE = os.path.join(DATA_DIR, "token.pickle")

# === Google Sheets Setup === #
GOOGLE_SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

# Google Sheets Credentials
SHEETS_CREDENTIALS_FILE = os.path.join(CONFIG_DIR, "job_tracker_key.json")

# Name of the Google Sheets document
GOOGLE_SHEET_NAME = "Job Tracker"

# Name of sheet 1
JOB_POOL_SHEET_NAME = "Job Pool"

# Name of sheet 2
RECOMMENDED_JOBS_SHEET_NAME = "Recommended Jobs"

SPREADSHEET_ID = "1yd5RR_RiDx2yEpuGzsHxG5EwdDyREHBhxrmnsZ09HjM"  # Replace with actual ID

# Number of top jobs to display in the "Recommended Jobs" sheet
TOP_N_JOBS = 20  # We can update this number as needed

CREDENTIALS_FILE = os.path.join(CONFIG_DIR, "client_secret.json")

REMOTIVE_URL = "https://remotive.io/api/remote-jobs"

# Ensure all directories exist
for dir_path in [LOGS_DIR, DATA_DIR, CONFIG_DIR]:
    os.makedirs(dir_path, exist_ok=True)


REQUIRED_SKILLS = [
    "Project Management", "Scrum", "Agile", "Product Management", 
    "Stakeholder Management", "Software Development", "Cloud Computing",
    "AWS", "Python", "SQL", "Communication", "Leadership"
]


# Define keyword priorities
TARGET_KEYWORDS = {
    "high_priority": [
        "Product Manager", "Project Manager", "Technical Program Manager", 
        "Scrum", "Agile", "Jira", "Stakeholder Management"
    ],
    "medium_priority": [
        "Program Manager", "Process Improvement", "Business Strategy", 
        "Cloud", "Kanban", "Leadership", "Collaboration"
    ],
    "low_priority": [
        "QA", "Testing", "Automation Engineer", "DevOps", "Full Stack Engineer", "Software Engineer"
    ]
}


# Adjust keyword weights
WEIGHTS = {
    "high_priority": 10,  # Lowered from 12
    "medium_priority": 5,  # Lowered from 6
    "low_priority": 1  # Keep as is
}


# Define excluded keywords that should be **immediately filtered out**
EXCLUDED_KEYWORDS = [
    "Intern", "Entry-Level", "Sales", "Marketing", "Support", "Assistant", 
    "Accounting", "Investment", "Finance", "FinOps", "Banking", "Trading"
]

# Predefined skill keywords (expandable)
TECHNICAL_SKILLS = [
    "Python", "Java", "C++", "SQL", "AWS", "Azure", "Jira", "Agile", "Scrum", "Kanban",
    "Project Management", "Stakeholder Management", "Sprint Planning", "Backlog Grooming",
    "Risk Mitigation", "Process Optimization", "Cloud Computing", "Data Validation",
    "Software Development", "Technical Product Management"
]

# Constants for filtering
MIN_SCORE_THRESHOLD = 20  # Only keep highly relevant jobs
MAX_JOBS_TO_SAVE = 500  # Save a maximum of 500 jobs to Google Sheets


RESUME_FILE = os.path.join(DATA_DIR, "resume.docx")  # Change to your actual resume file path

# RESUME_FILE = os.path.join(DATA_DIR, "resume.pdf")

# Ideal job description (modify based on target job profile)
IDEAL_JOB_DESC = """
Project Manager with experience in Agile, Scrum, and Jira. 
Strong expertise in cloud platforms like AWS and software development.
Proficient in backlog grooming, sprint planning, and stakeholder management.
Looking for remote or hybrid opportunities in product or program management.
"""

# Target job titles for prioritization
TARGET_TITLES = ["product manager", "project manager", "scrum master", "program manager", "technical program manager", "agile coach"]

# Load credentials from .env file
LINKEDIN_EMAIL = os.getenv("LINKEDIN_EMAIL")
LINKEDIN_PASSWORD = os.getenv("LINKEDIN_PASSWORD")
INDEED_LOGIN_METHOD = os.getenv("INDEED_LOGIN_METHOD")

LINKEDIN_URL = "https://www.linkedin.com/"
LINKEDIN_LOGIN_URL = "https://www.linkedin.com/login"
LINKEDIN_JOB_URL = "https://www.linkedin.com/jobs/"
INDEED_LOGIN_URL = "https://secure.indeed.com/"
REMOTIVE_HOME_URL = "https://remotive.io/"

EDGE_WEBDRIVER = "C:/WebDriver/msedgedriver.exe"

# Define cookie storage filenames
COOKIE_PATH = "cookies.pkl"  # File to store session cookies
LINKEDIN_COOKIE_PATH = "linkedin_cookies.pkl"
INDEED_COOKIE_PATH = "indeed_cookies.pkl"


