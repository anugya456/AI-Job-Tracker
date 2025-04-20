
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

### Tried and Dropped:
- **Sentence Transformers (BERT/MiniLM)**
- **Doc2Vec**
- **GEMMA**
- **OpenAI Embeddings**

Reasons: Too slow, inconsistent, or overkill for our problem space.

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

## Visualization Setup

1. Link your **Recommended Jobs** Google Sheet to **Google Data Studio**.
2. Create the following charts:
   - **Application Status** (Pie Chart)
   - **Relevance Score Distribution** (Histogram or Bar)
   - **Top 10 Jobs Table**
   - **Job Portal Breakdown** (Bar Chart)

---

## How to Run

1. Set your configs in `config.py`
2. Run the tracker:
   ```bash
   python job_processor.py
   ```
3. View updates in Google Sheets and Google Data Studio.

---

## Lessons Learned
- Embedding models weren’t always better — TF-IDF gave better, faster results.
- Modularity made testing and debugging easier.
- Email automation should always be tested in a sandbox phase.

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
├─ docs
├─ logs
├─ requirements.txt
├─ run_job_tracker.bat
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
