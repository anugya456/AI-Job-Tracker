
# AI Job Tracker

Automates job filtering, tracking, and follow-up through a modular AI-powered pipeline using TF-IDF and Google Sheets integration.

---

## Features

- Intelligent job matching using TF-IDF scoring
- Auto-populates Google Sheets with Job Pool & Recommended Jobs
- Visual insights using Google Looker Studio dashboards
- (Optional) Gmail follow-up automation for recruiters
- Resume-to-job matching capability
- Scheduled execution via Windows Task Scheduler
---

## ML Models

### In Use:
- **TF-IDF + Cosine Similarity** (via `tfidf_ranker.py`)
  - Fast, interpretable, ideal for this domain.

### Evaluated Alternatives:
- **Sentence Transformers (BERT/MiniLM)**
- **Doc2Vec**
- **GEMMA**
- **OpenAI Embeddings**

**Rationale:** These models were excluded due to higher computational cost, inconsistent relevance scoring, and limited advantage over TF-IDF in this focused job-matching use case.

---

## Workflow Overview

```bash
job_processor.py
    ├── Checks if new jobs exist
    ├── If yes, updates Job Pool
    └── Calls filters + tfidf_ranker
        └── Ranks jobs
            └── Calls job_writer.py
                └── Updates Recommended Jobs sheet
```

---

## Key Components

- **Main Entry Script**: `job_processor.py`
- **Google Sheets Writer**: `job_writer.py`
- **Job Scraper**: `job_scraper.py`
- **Resume Parser**: `resume_parser.py`
- **Skill Extractor**: `skill_extractor.py`
- **Job Filter**: `job_filter.py`
- **Follow-Up Email Sender**: `send_gmail.py` (currently commented out)

Configurable settings like `IDEAL_JOB_DESC`, `TOP_N`, and `TARGET_TITLES` live in `config.py`.

---

## 🔧 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/anugya456/AI-Job-Tracker.git
cd AI-Job-Tracker
```

### 2. Create Your `.env`

```bash
cp .env.example .env
```

Then fill in your credentials:

```env
SPREADSHEET_ID=your-google-sheet-id
GOOGLE_CLIENT_ID=your-client-id
GOOGLE_CLIENT_SECRET=your-client-secret
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Run the Tracker

```bash
python src/job_processor.py
```

Or let it run automatically every 8 hours via:

```bash
run_job_tracker.bat
```

---

## Visualization Setup

1. Link your **Recommended Jobs** Google Sheet to **Google Data Studio**.
2. Create the following charts:
   - **Application Status** (Pie Chart)
   - **Relevance Score Distribution** (Histogram or Bar)
   - **Top 10 Jobs Table**
   - **Job Portal Breakdown** (Bar Chart)

---

## Project Structure
```
JobApplicationTrackerAI
├─ config
│  ├─ client_secret.json
│  └─ job_tracker_key.json
├─ data
│  ├─ cached_jobs.json
│  └─ resume.docx
├── docs/
│   ├── AI_Job_Tracker_Report_Complete.docx (local use only)
│   ├── job_tracker_architecture.drawio (local use only)
│   └── dashboard_screenshots/ (local use only)
├─ logs
├─ requirements.txt
├─ run_job_tracker.bat
├── .env
├── .env.example
├─ src
│  ├─ config.py
│  ├─ job_apply.py
│  ├─ job_filter.py
│  ├─ job_portal_logins.py
│  ├─ job_processor.py
│  ├─ job_scraper.py
│  ├─ job_writer.py
│  ├─ resume_parser.py
│  ├─ send_gmail.py
│  ├─ skill_extractor.py
│  └─ utils.py
├─ tests
└─ venv
   ├─ Include
   ├─ Lib
   │  └─ site-packages
   │     ├─ annotated_types
   │     │  ├─ py.typed
   │     │  ├─ test_cases.py
   │     │  └─ __init__.py
   │     ├─ annotated_types-0.7.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses


```
---

## Technical + Business Report

A complete, portfolio-ready project report is available in `/docs/` as:

- `AI_Job_Tracker_Report.docx`

*(Not pushed to GitHub — kept local due to size/security. Contact the author if you’d like to review it.)*

---

## Security Best Practices

- `.env`, secrets, and credentials removed from Git history
- `.env.example` provided as template
- `.gitignore` enforces safety for all secret-related files
- Gmail follow-up automation is disabled by default

---

## Tech Stack

- Python 3.10+
- Google Sheets API
- TF-IDF + Cosine Similarity
- Google Looker Studio
- dotenv, requests, schedule, pandas

---

## Lessons Learned
- Embedding models weren’t always better — TF-IDF gave better, faster results.
- Modularity made testing and debugging easier.
- Email automation should always be tested in a sandbox phase.

---

## Author

**Anugya**  
[GitHub](https://github.com/anugya456)
