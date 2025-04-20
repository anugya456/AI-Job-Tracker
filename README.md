
# AI Job Tracker

Automates job filtering, tracking, and follow-up through a modular AI-powered pipeline using TF-IDF and Google Sheets integration.

---

## Features

- **Job Filtering & Ranking:**
  - Uses TF-IDF and cosine similarity to filter jobs based on your `IDEAL_JOB_DESC`.
  - Keyword-based filtering via `TARGET_TITLES` and other hard filters.

- **Job Tracking:**
  - Maintains two Google Sheets:
    - **Job Pool**: All jobs from various sources.
    - **Recommended Jobs**: Top-ranked jobs with scores and metadata.

- **Email Follow-Up (Optional):**
  - Uses Gmail API to send follow-up emails to recruiters (commented out for safety).

- **Resume Parsing & Skill Extraction:**
  - Extracts skills from your resume and compares with job descriptions (via `resume_parser.py` and `skill_extractor.py`).

- **Data Visualization:**
  - Google Data Studio dashboard to visualize application status, top jobs, source distribution, etc.

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
   │     │  │  └─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  └─ WHEEL
   │     ├─ apiclient
   │     │  └─ __init__.py
   │     ├─ attr
   │     │  ├─ converters.py
   │     │  ├─ converters.pyi
   │     │  ├─ exceptions.py
   │     │  ├─ exceptions.pyi
   │     │  ├─ filters.py
   │     │  ├─ filters.pyi
   │     │  ├─ py.typed
   │     │  ├─ setters.py
   │     │  ├─ setters.pyi
   │     │  ├─ validators.py
   │     │  ├─ validators.pyi
   │     │  ├─ _cmp.py
   │     │  ├─ _cmp.pyi
   │     │  ├─ _compat.py
   │     │  ├─ _config.py
   │     │  ├─ _funcs.py
   │     │  ├─ _make.py
   │     │  ├─ _next_gen.py
   │     │  ├─ _typing_compat.pyi
   │     │  ├─ _version_info.py
   │     │  ├─ _version_info.pyi
   │     │  ├─ __init__.py
   │     │  └─ __init__.pyi
   │     ├─ attrs
   │     │  ├─ converters.py
   │     │  ├─ exceptions.py
   │     │  ├─ filters.py
   │     │  ├─ py.typed
   │     │  ├─ setters.py
   │     │  ├─ validators.py
   │     │  ├─ __init__.py
   │     │  └─ __init__.pyi
   │     ├─ attrs-25.3.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  └─ WHEEL
   │     ├─ beautifulsoup4-4.13.3.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  ├─ AUTHORS
   │     │  │  └─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  └─ WHEEL
   │     ├─ blis
   │     │  ├─ about.py
   │     │  ├─ benchmark.py
   │     │  ├─ cy.cp311-win_amd64.exp
   │     │  ├─ cy.cp311-win_amd64.lib
   │     │  ├─ cy.cp311-win_amd64.pyd
   │     │  ├─ cy.pxd
   │     │  ├─ cy.pyx
   │     │  ├─ py.cp311-win_amd64.exp
   │     │  ├─ py.cp311-win_amd64.lib
   │     │  ├─ py.cp311-win_amd64.pyd
   │     │  ├─ py.pyx
   │     │  ├─ tests
   │     │  │  ├─ common.py
   │     │  │  ├─ test_dotv.py
   │     │  │  ├─ test_gemm.py
   │     │  │  └─ __init__.py
   │     │  ├─ __init__.pxd
   │     │  └─ __init__.py
   │     ├─ blis-1.2.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ bs4
   │     │  ├─ builder
   │     │  │  ├─ _html5lib.py
   │     │  │  ├─ _htmlparser.py
   │     │  │  ├─ _lxml.py
   │     │  │  └─ __init__.py
   │     │  ├─ css.py
   │     │  ├─ dammit.py
   │     │  ├─ diagnose.py
   │     │  ├─ element.py
   │     │  ├─ exceptions.py
   │     │  ├─ filter.py
   │     │  ├─ formatter.py
   │     │  ├─ py.typed
   │     │  ├─ tests
   │     │  │  ├─ fuzz
   │     │  │  │  ├─ clusterfuzz-testcase-minimized-bs4_fuzzer-4670634698080256.testcase
   │     │  │  │  ├─ clusterfuzz-testcase-minimized-bs4_fuzzer-4818336571064320.testcase
   │     │  │  │  ├─ clusterfuzz-testcase-minimized-bs4_fuzzer-4999465949331456.testcase
   │     │  │  │  ├─ clusterfuzz-testcase-minimized-bs4_fuzzer-5000587759190016.testcase
   │     │  │  │  ├─ clusterfuzz-testcase-minimized-bs4_fuzzer-5167584867909632.testcase
   │     │  │  │  ├─ clusterfuzz-testcase-minimized-bs4_fuzzer-5270998950477824.testcase
   │     │  │  │  ├─ clusterfuzz-testcase-minimized-bs4_fuzzer-5375146639360000.testcase
   │     │  │  │  ├─ clusterfuzz-testcase-minimized-bs4_fuzzer-5492400320282624.testcase
   │     │  │  │  ├─ clusterfuzz-testcase-minimized-bs4_fuzzer-5703933063462912.testcase
   │     │  │  │  ├─ clusterfuzz-testcase-minimized-bs4_fuzzer-5843991618256896.testcase
   │     │  │  │  ├─ clusterfuzz-testcase-minimized-bs4_fuzzer-5984173902397440.testcase
   │     │  │  │  ├─ clusterfuzz-testcase-minimized-bs4_fuzzer-6124268085182464.testcase
   │     │  │  │  ├─ clusterfuzz-testcase-minimized-bs4_fuzzer-6241471367348224.testcase
   │     │  │  │  ├─ clusterfuzz-testcase-minimized-bs4_fuzzer-6306874195312640.testcase
   │     │  │  │  ├─ clusterfuzz-testcase-minimized-bs4_fuzzer-6450958476902400.testcase
   │     │  │  │  ├─ clusterfuzz-testcase-minimized-bs4_fuzzer-6600557255327744.testcase
   │     │  │  │  ├─ crash-0d306a50c8ed8bcd0785b67000fcd5dea1d33f08.testcase
   │     │  │  │  └─ crash-ffbdfa8a2b26f13537b68d3794b0478a4090ee4a.testcase
   │     │  │  ├─ test_builder.py
   │     │  │  ├─ test_builder_registry.py
   │     │  │  ├─ test_css.py
   │     │  │  ├─ test_dammit.py
   │     │  │  ├─ test_element.py
   │     │  │  ├─ test_filter.py
   │     │  │  ├─ test_formatter.py
   │     │  │  ├─ test_fuzz.py
   │     │  │  ├─ test_html5lib.py
   │     │  │  ├─ test_htmlparser.py
   │     │  │  ├─ test_lxml.py
   │     │  │  ├─ test_navigablestring.py
   │     │  │  ├─ test_pageelement.py
   │     │  │  ├─ test_soup.py
   │     │  │  ├─ test_tag.py
   │     │  │  ├─ test_tree.py
   │     │  │  └─ __init__.py
   │     │  ├─ _deprecation.py
   │     │  ├─ _typing.py
   │     │  ├─ _warnings.py
   │     │  └─ __init__.py
   │     ├─ cachetools
   │     │  ├─ func.py
   │     │  ├─ keys.py
   │     │  ├─ _decorators.py
   │     │  └─ __init__.py
   │     ├─ cachetools-5.5.2.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ catalogue
   │     │  ├─ tests
   │     │  │  ├─ test_catalogue.py
   │     │  │  └─ __init__.py
   │     │  ├─ _importlib_metadata
   │     │  │  ├─ _compat.py
   │     │  │  └─ __init__.py
   │     │  └─ __init__.py
   │     ├─ catalogue-2.0.10.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  ├─ WHEEL
   │     │  └─ zip-safe
   │     ├─ certifi
   │     │  ├─ cacert.pem
   │     │  ├─ core.py
   │     │  ├─ py.typed
   │     │  ├─ __init__.py
   │     │  └─ __main__.py
   │     ├─ certifi-2025.1.31.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ cffi
   │     │  ├─ api.py
   │     │  ├─ backend_ctypes.py
   │     │  ├─ cffi_opcode.py
   │     │  ├─ commontypes.py
   │     │  ├─ cparser.py
   │     │  ├─ error.py
   │     │  ├─ ffiplatform.py
   │     │  ├─ lock.py
   │     │  ├─ model.py
   │     │  ├─ parse_c_type.h
   │     │  ├─ pkgconfig.py
   │     │  ├─ recompiler.py
   │     │  ├─ setuptools_ext.py
   │     │  ├─ vengine_cpy.py
   │     │  ├─ vengine_gen.py
   │     │  ├─ verifier.py
   │     │  ├─ _cffi_errors.h
   │     │  ├─ _cffi_include.h
   │     │  ├─ _embedding.h
   │     │  ├─ _imp_emulation.py
   │     │  ├─ _shimmed_dist_utils.py
   │     │  └─ __init__.py
   │     ├─ cffi-1.17.1.dist-info
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ charset_normalizer
   │     │  ├─ api.py
   │     │  ├─ cd.py
   │     │  ├─ cli
   │     │  │  ├─ __init__.py
   │     │  │  └─ __main__.py
   │     │  ├─ constant.py
   │     │  ├─ legacy.py
   │     │  ├─ md.cp311-win_amd64.pyd
   │     │  ├─ md.py
   │     │  ├─ md__mypyc.cp311-win_amd64.pyd
   │     │  ├─ models.py
   │     │  ├─ py.typed
   │     │  ├─ utils.py
   │     │  ├─ version.py
   │     │  ├─ __init__.py
   │     │  └─ __main__.py
   │     ├─ charset_normalizer-3.4.1.dist-info
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ click
   │     │  ├─ core.py
   │     │  ├─ decorators.py
   │     │  ├─ exceptions.py
   │     │  ├─ formatting.py
   │     │  ├─ globals.py
   │     │  ├─ parser.py
   │     │  ├─ py.typed
   │     │  ├─ shell_completion.py
   │     │  ├─ termui.py
   │     │  ├─ testing.py
   │     │  ├─ types.py
   │     │  ├─ utils.py
   │     │  ├─ _compat.py
   │     │  ├─ _termui_impl.py
   │     │  ├─ _textwrap.py
   │     │  ├─ _winconsole.py
   │     │  └─ __init__.py
   │     ├─ click-8.1.8.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE.txt
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  └─ WHEEL
   │     ├─ cloudpathlib
   │     │  ├─ anypath.py
   │     │  ├─ azure
   │     │  │  ├─ azblobclient.py
   │     │  │  ├─ azblobpath.py
   │     │  │  └─ __init__.py
   │     │  ├─ client.py
   │     │  ├─ cloudpath.py
   │     │  ├─ enums.py
   │     │  ├─ exceptions.py
   │     │  ├─ gs
   │     │  │  ├─ gsclient.py
   │     │  │  ├─ gspath.py
   │     │  │  └─ __init__.py
   │     │  ├─ legacy
   │     │  │  └─ glob.py
   │     │  ├─ local
   │     │  │  ├─ implementations
   │     │  │  │  ├─ azure.py
   │     │  │  │  ├─ gs.py
   │     │  │  │  ├─ s3.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ localclient.py
   │     │  │  ├─ localpath.py
   │     │  │  └─ __init__.py
   │     │  ├─ py.typed
   │     │  ├─ s3
   │     │  │  ├─ s3client.py
   │     │  │  ├─ s3path.py
   │     │  │  └─ __init__.py
   │     │  ├─ url_utils.py
   │     │  └─ __init__.py
   │     ├─ cloudpathlib-0.21.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  └─ WHEEL
   │     ├─ colorama
   │     │  ├─ ansi.py
   │     │  ├─ ansitowin32.py
   │     │  ├─ initialise.py
   │     │  ├─ tests
   │     │  │  ├─ ansitowin32_test.py
   │     │  │  ├─ ansi_test.py
   │     │  │  ├─ initialise_test.py
   │     │  │  ├─ isatty_test.py
   │     │  │  ├─ utils.py
   │     │  │  ├─ winterm_test.py
   │     │  │  └─ __init__.py
   │     │  ├─ win32.py
   │     │  ├─ winterm.py
   │     │  └─ __init__.py
   │     ├─ colorama-0.4.6.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE.txt
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  └─ WHEEL
   │     ├─ confection
   │     │  ├─ py.typed
   │     │  ├─ tests
   │     │  │  ├─ conftest.py
   │     │  │  ├─ test_config.py
   │     │  │  ├─ test_frozen_structures.py
   │     │  │  ├─ util.py
   │     │  │  └─ __init__.py
   │     │  ├─ util.py
   │     │  └─ __init__.py
   │     ├─ confection-0.1.5.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  ├─ WHEEL
   │     │  └─ zip-safe
   │     ├─ cymem
   │     │  ├─ about.py
   │     │  ├─ cymem.cp311-win_amd64.pyd
   │     │  ├─ cymem.pxd
   │     │  ├─ cymem.pyx
   │     │  ├─ tests
   │     │  │  ├─ test_import.py
   │     │  │  └─ __init__.py
   │     │  ├─ __init__.pxd
   │     │  └─ __init__.py
   │     ├─ cymem-2.0.11.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ dateutil
   │     │  ├─ easter.py
   │     │  ├─ parser
   │     │  │  ├─ isoparser.py
   │     │  │  ├─ _parser.py
   │     │  │  └─ __init__.py
   │     │  ├─ relativedelta.py
   │     │  ├─ rrule.py
   │     │  ├─ tz
   │     │  │  ├─ tz.py
   │     │  │  ├─ win.py
   │     │  │  ├─ _common.py
   │     │  │  ├─ _factories.py
   │     │  │  └─ __init__.py
   │     │  ├─ tzwin.py
   │     │  ├─ utils.py
   │     │  ├─ zoneinfo
   │     │  │  ├─ dateutil-zoneinfo.tar.gz
   │     │  │  ├─ rebuild.py
   │     │  │  └─ __init__.py
   │     │  ├─ _common.py
   │     │  ├─ _version.py
   │     │  └─ __init__.py
   │     ├─ distutils-precedence.pth
   │     ├─ docs
   │     │  └─ conf.py
   │     ├─ docx
   │     │  ├─ api.py
   │     │  ├─ blkcntnr.py
   │     │  ├─ dml
   │     │  │  ├─ color.py
   │     │  │  └─ __init__.py
   │     │  ├─ document.py
   │     │  ├─ drawing
   │     │  │  └─ __init__.py
   │     │  ├─ enum
   │     │  │  ├─ base.py
   │     │  │  ├─ dml.py
   │     │  │  ├─ section.py
   │     │  │  ├─ shape.py
   │     │  │  ├─ style.py
   │     │  │  ├─ table.py
   │     │  │  ├─ text.py
   │     │  │  └─ __init__.py
   │     │  ├─ exceptions.py
   │     │  ├─ image
   │     │  │  ├─ bmp.py
   │     │  │  ├─ constants.py
   │     │  │  ├─ exceptions.py
   │     │  │  ├─ gif.py
   │     │  │  ├─ helpers.py
   │     │  │  ├─ image.py
   │     │  │  ├─ jpeg.py
   │     │  │  ├─ png.py
   │     │  │  ├─ tiff.py
   │     │  │  └─ __init__.py
   │     │  ├─ opc
   │     │  │  ├─ constants.py
   │     │  │  ├─ coreprops.py
   │     │  │  ├─ exceptions.py
   │     │  │  ├─ oxml.py
   │     │  │  ├─ package.py
   │     │  │  ├─ packuri.py
   │     │  │  ├─ part.py
   │     │  │  ├─ parts
   │     │  │  │  ├─ coreprops.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ phys_pkg.py
   │     │  │  ├─ pkgreader.py
   │     │  │  ├─ pkgwriter.py
   │     │  │  ├─ rel.py
   │     │  │  ├─ shared.py
   │     │  │  ├─ spec.py
   │     │  │  └─ __init__.py
   │     │  ├─ oxml
   │     │  │  ├─ coreprops.py
   │     │  │  ├─ document.py
   │     │  │  ├─ drawing.py
   │     │  │  ├─ exceptions.py
   │     │  │  ├─ ns.py
   │     │  │  ├─ numbering.py
   │     │  │  ├─ parser.py
   │     │  │  ├─ section.py
   │     │  │  ├─ settings.py
   │     │  │  ├─ shape.py
   │     │  │  ├─ shared.py
   │     │  │  ├─ simpletypes.py
   │     │  │  ├─ styles.py
   │     │  │  ├─ table.py
   │     │  │  ├─ text
   │     │  │  │  ├─ font.py
   │     │  │  │  ├─ hyperlink.py
   │     │  │  │  ├─ pagebreak.py
   │     │  │  │  ├─ paragraph.py
   │     │  │  │  ├─ parfmt.py
   │     │  │  │  ├─ run.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ xmlchemy.py
   │     │  │  └─ __init__.py
   │     │  ├─ package.py
   │     │  ├─ parts
   │     │  │  ├─ document.py
   │     │  │  ├─ hdrftr.py
   │     │  │  ├─ image.py
   │     │  │  ├─ numbering.py
   │     │  │  ├─ settings.py
   │     │  │  ├─ story.py
   │     │  │  ├─ styles.py
   │     │  │  └─ __init__.py
   │     │  ├─ py.typed
   │     │  ├─ section.py
   │     │  ├─ settings.py
   │     │  ├─ shape.py
   │     │  ├─ shared.py
   │     │  ├─ styles
   │     │  │  ├─ latent.py
   │     │  │  ├─ style.py
   │     │  │  ├─ styles.py
   │     │  │  └─ __init__.py
   │     │  ├─ table.py
   │     │  ├─ templates
   │     │  │  ├─ default-docx-template
   │     │  │  │  ├─ customXml
   │     │  │  │  │  ├─ item1.xml
   │     │  │  │  │  ├─ itemProps1.xml
   │     │  │  │  │  └─ _rels
   │     │  │  │  │     └─ item1.xml.rels
   │     │  │  │  ├─ docProps
   │     │  │  │  │  ├─ app.xml
   │     │  │  │  │  ├─ core.xml
   │     │  │  │  │  └─ thumbnail.jpeg
   │     │  │  │  ├─ word
   │     │  │  │  │  ├─ document.xml
   │     │  │  │  │  ├─ fontTable.xml
   │     │  │  │  │  ├─ numbering.xml
   │     │  │  │  │  ├─ settings.xml
   │     │  │  │  │  ├─ styles.xml
   │     │  │  │  │  ├─ stylesWithEffects.xml
   │     │  │  │  │  ├─ theme
   │     │  │  │  │  │  └─ theme1.xml
   │     │  │  │  │  ├─ webSettings.xml
   │     │  │  │  │  └─ _rels
   │     │  │  │  │     └─ document.xml.rels
   │     │  │  │  ├─ [Content_Types].xml
   │     │  │  │  └─ _rels
   │     │  │  │     └─ .rels
   │     │  │  ├─ default-footer.xml
   │     │  │  ├─ default-header.xml
   │     │  │  ├─ default-settings.xml
   │     │  │  ├─ default-styles.xml
   │     │  │  └─ default.docx
   │     │  ├─ text
   │     │  │  ├─ font.py
   │     │  │  ├─ hyperlink.py
   │     │  │  ├─ pagebreak.py
   │     │  │  ├─ paragraph.py
   │     │  │  ├─ parfmt.py
   │     │  │  ├─ run.py
   │     │  │  ├─ tabstops.py
   │     │  │  └─ __init__.py
   │     │  ├─ types.py
   │     │  └─ __init__.py
   │     ├─ dotenv
   │     │  ├─ cli.py
   │     │  ├─ ipython.py
   │     │  ├─ main.py
   │     │  ├─ parser.py
   │     │  ├─ py.typed
   │     │  ├─ variables.py
   │     │  ├─ version.py
   │     │  ├─ __init__.py
   │     │  └─ __main__.py
   │     ├─ en_core_web_md
   │     │  ├─ en_core_web_md-3.8.0
   │     │  │  ├─ accuracy.json
   │     │  │  ├─ attribute_ruler
   │     │  │  │  └─ patterns
   │     │  │  ├─ config.cfg
   │     │  │  ├─ lemmatizer
   │     │  │  │  └─ lookups
   │     │  │  │     └─ lookups.bin
   │     │  │  ├─ LICENSE
   │     │  │  ├─ LICENSES_SOURCES
   │     │  │  ├─ meta.json
   │     │  │  ├─ ner
   │     │  │  │  ├─ cfg
   │     │  │  │  ├─ model
   │     │  │  │  └─ moves
   │     │  │  ├─ parser
   │     │  │  │  ├─ cfg
   │     │  │  │  ├─ model
   │     │  │  │  └─ moves
   │     │  │  ├─ README.md
   │     │  │  ├─ senter
   │     │  │  │  ├─ cfg
   │     │  │  │  └─ model
   │     │  │  ├─ tagger
   │     │  │  │  ├─ cfg
   │     │  │  │  └─ model
   │     │  │  ├─ tok2vec
   │     │  │  │  ├─ cfg
   │     │  │  │  └─ model
   │     │  │  ├─ tokenizer
   │     │  │  └─ vocab
   │     │  │     ├─ key2row
   │     │  │     ├─ lookups.bin
   │     │  │     ├─ strings.json
   │     │  │     ├─ vectors
   │     │  │     └─ vectors.cfg
   │     │  ├─ meta.json
   │     │  └─ __init__.py
   │     ├─ en_core_web_md-3.8.0.dist-info
   │     │  ├─ direct_url.json
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ LICENSES_SOURCES
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ en_core_web_sm
   │     │  ├─ en_core_web_sm-3.8.0
   │     │  │  ├─ accuracy.json
   │     │  │  ├─ attribute_ruler
   │     │  │  │  └─ patterns
   │     │  │  ├─ config.cfg
   │     │  │  ├─ lemmatizer
   │     │  │  │  └─ lookups
   │     │  │  │     └─ lookups.bin
   │     │  │  ├─ LICENSE
   │     │  │  ├─ LICENSES_SOURCES
   │     │  │  ├─ meta.json
   │     │  │  ├─ ner
   │     │  │  │  ├─ cfg
   │     │  │  │  ├─ model
   │     │  │  │  └─ moves
   │     │  │  ├─ parser
   │     │  │  │  ├─ cfg
   │     │  │  │  ├─ model
   │     │  │  │  └─ moves
   │     │  │  ├─ README.md
   │     │  │  ├─ senter
   │     │  │  │  ├─ cfg
   │     │  │  │  └─ model
   │     │  │  ├─ tagger
   │     │  │  │  ├─ cfg
   │     │  │  │  └─ model
   │     │  │  ├─ tok2vec
   │     │  │  │  ├─ cfg
   │     │  │  │  └─ model
   │     │  │  ├─ tokenizer
   │     │  │  └─ vocab
   │     │  │     ├─ key2row
   │     │  │     ├─ lookups.bin
   │     │  │     ├─ strings.json
   │     │  │     ├─ vectors
   │     │  │     └─ vectors.cfg
   │     │  ├─ meta.json
   │     │  └─ __init__.py
   │     ├─ en_core_web_sm-3.8.0.dist-info
   │     │  ├─ direct_url.json
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ LICENSES_SOURCES
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ fitz
   │     │  ├─ table.py
   │     │  ├─ utils.py
   │     │  └─ __init__.py
   │     ├─ google
   │     │  ├─ api
   │     │  │  ├─ annotations.proto
   │     │  │  ├─ annotations_pb2.py
   │     │  │  ├─ annotations_pb2.pyi
   │     │  │  ├─ auth.proto
   │     │  │  ├─ auth_pb2.py
   │     │  │  ├─ auth_pb2.pyi
   │     │  │  ├─ backend.proto
   │     │  │  ├─ backend_pb2.py
   │     │  │  ├─ backend_pb2.pyi
   │     │  │  ├─ billing.proto
   │     │  │  ├─ billing_pb2.py
   │     │  │  ├─ billing_pb2.pyi
   │     │  │  ├─ client.proto
   │     │  │  ├─ client_pb2.py
   │     │  │  ├─ client_pb2.pyi
   │     │  │  ├─ config_change.proto
   │     │  │  ├─ config_change_pb2.py
   │     │  │  ├─ config_change_pb2.pyi
   │     │  │  ├─ consumer.proto
   │     │  │  ├─ consumer_pb2.py
   │     │  │  ├─ consumer_pb2.pyi
   │     │  │  ├─ context.proto
   │     │  │  ├─ context_pb2.py
   │     │  │  ├─ context_pb2.pyi
   │     │  │  ├─ control.proto
   │     │  │  ├─ control_pb2.py
   │     │  │  ├─ control_pb2.pyi
   │     │  │  ├─ distribution.proto
   │     │  │  ├─ distribution_pb2.py
   │     │  │  ├─ distribution_pb2.pyi
   │     │  │  ├─ documentation.proto
   │     │  │  ├─ documentation_pb2.py
   │     │  │  ├─ documentation_pb2.pyi
   │     │  │  ├─ endpoint.proto
   │     │  │  ├─ endpoint_pb2.py
   │     │  │  ├─ endpoint_pb2.pyi
   │     │  │  ├─ error_reason.proto
   │     │  │  ├─ error_reason_pb2.py
   │     │  │  ├─ error_reason_pb2.pyi
   │     │  │  ├─ field_behavior.proto
   │     │  │  ├─ field_behavior_pb2.py
   │     │  │  ├─ field_behavior_pb2.pyi
   │     │  │  ├─ field_info.proto
   │     │  │  ├─ field_info_pb2.py
   │     │  │  ├─ field_info_pb2.pyi
   │     │  │  ├─ http.proto
   │     │  │  ├─ httpbody.proto
   │     │  │  ├─ httpbody_pb2.py
   │     │  │  ├─ httpbody_pb2.pyi
   │     │  │  ├─ http_pb2.py
   │     │  │  ├─ http_pb2.pyi
   │     │  │  ├─ label.proto
   │     │  │  ├─ label_pb2.py
   │     │  │  ├─ label_pb2.pyi
   │     │  │  ├─ launch_stage.proto
   │     │  │  ├─ launch_stage_pb2.py
   │     │  │  ├─ launch_stage_pb2.pyi
   │     │  │  ├─ log.proto
   │     │  │  ├─ logging.proto
   │     │  │  ├─ logging_pb2.py
   │     │  │  ├─ logging_pb2.pyi
   │     │  │  ├─ log_pb2.py
   │     │  │  ├─ log_pb2.pyi
   │     │  │  ├─ metric.proto
   │     │  │  ├─ metric_pb2.py
   │     │  │  ├─ metric_pb2.pyi
   │     │  │  ├─ monitored_resource.proto
   │     │  │  ├─ monitored_resource_pb2.py
   │     │  │  ├─ monitored_resource_pb2.pyi
   │     │  │  ├─ monitoring.proto
   │     │  │  ├─ monitoring_pb2.py
   │     │  │  ├─ monitoring_pb2.pyi
   │     │  │  ├─ policy.proto
   │     │  │  ├─ policy_pb2.py
   │     │  │  ├─ policy_pb2.pyi
   │     │  │  ├─ quota.proto
   │     │  │  ├─ quota_pb2.py
   │     │  │  ├─ quota_pb2.pyi
   │     │  │  ├─ resource.proto
   │     │  │  ├─ resource_pb2.py
   │     │  │  ├─ resource_pb2.pyi
   │     │  │  ├─ routing.proto
   │     │  │  ├─ routing_pb2.py
   │     │  │  ├─ routing_pb2.pyi
   │     │  │  ├─ service.proto
   │     │  │  ├─ service_pb2.py
   │     │  │  ├─ service_pb2.pyi
   │     │  │  ├─ source_info.proto
   │     │  │  ├─ source_info_pb2.py
   │     │  │  ├─ source_info_pb2.pyi
   │     │  │  ├─ system_parameter.proto
   │     │  │  ├─ system_parameter_pb2.py
   │     │  │  ├─ system_parameter_pb2.pyi
   │     │  │  ├─ usage.proto
   │     │  │  ├─ usage_pb2.py
   │     │  │  ├─ usage_pb2.pyi
   │     │  │  ├─ visibility.proto
   │     │  │  ├─ visibility_pb2.py
   │     │  │  └─ visibility_pb2.pyi
   │     │  ├─ api_core
   │     │  │  ├─ bidi.py
   │     │  │  ├─ client_info.py
   │     │  │  ├─ client_logging.py
   │     │  │  ├─ client_options.py
   │     │  │  ├─ datetime_helpers.py
   │     │  │  ├─ exceptions.py
   │     │  │  ├─ extended_operation.py
   │     │  │  ├─ future
   │     │  │  │  ├─ async_future.py
   │     │  │  │  ├─ base.py
   │     │  │  │  ├─ polling.py
   │     │  │  │  ├─ _helpers.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ gapic_v1
   │     │  │  │  ├─ client_info.py
   │     │  │  │  ├─ config.py
   │     │  │  │  ├─ config_async.py
   │     │  │  │  ├─ method.py
   │     │  │  │  ├─ method_async.py
   │     │  │  │  ├─ routing_header.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ general_helpers.py
   │     │  │  ├─ grpc_helpers.py
   │     │  │  ├─ grpc_helpers_async.py
   │     │  │  ├─ iam.py
   │     │  │  ├─ operation.py
   │     │  │  ├─ operations_v1
   │     │  │  │  ├─ abstract_operations_base_client.py
   │     │  │  │  ├─ abstract_operations_client.py
   │     │  │  │  ├─ operations_async_client.py
   │     │  │  │  ├─ operations_client.py
   │     │  │  │  ├─ operations_client_config.py
   │     │  │  │  ├─ operations_rest_client_async.py
   │     │  │  │  ├─ pagers.py
   │     │  │  │  ├─ pagers_async.py
   │     │  │  │  ├─ pagers_base.py
   │     │  │  │  ├─ transports
   │     │  │  │  │  ├─ base.py
   │     │  │  │  │  ├─ rest.py
   │     │  │  │  │  ├─ rest_asyncio.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ operation_async.py
   │     │  │  ├─ page_iterator.py
   │     │  │  ├─ page_iterator_async.py
   │     │  │  ├─ path_template.py
   │     │  │  ├─ protobuf_helpers.py
   │     │  │  ├─ py.typed
   │     │  │  ├─ rest_helpers.py
   │     │  │  ├─ rest_streaming.py
   │     │  │  ├─ rest_streaming_async.py
   │     │  │  ├─ retry
   │     │  │  │  ├─ retry_base.py
   │     │  │  │  ├─ retry_streaming.py
   │     │  │  │  ├─ retry_streaming_async.py
   │     │  │  │  ├─ retry_unary.py
   │     │  │  │  ├─ retry_unary_async.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ retry_async.py
   │     │  │  ├─ timeout.py
   │     │  │  ├─ universe.py
   │     │  │  ├─ version.py
   │     │  │  ├─ version_header.py
   │     │  │  ├─ _rest_streaming_base.py
   │     │  │  └─ __init__.py
   │     │  ├─ auth
   │     │  │  ├─ aio
   │     │  │  │  ├─ credentials.py
   │     │  │  │  ├─ transport
   │     │  │  │  │  ├─ aiohttp.py
   │     │  │  │  │  ├─ sessions.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ api_key.py
   │     │  │  ├─ app_engine.py
   │     │  │  ├─ aws.py
   │     │  │  ├─ compute_engine
   │     │  │  │  ├─ credentials.py
   │     │  │  │  ├─ _metadata.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ credentials.py
   │     │  │  ├─ crypt
   │     │  │  │  ├─ base.py
   │     │  │  │  ├─ es256.py
   │     │  │  │  ├─ rsa.py
   │     │  │  │  ├─ _cryptography_rsa.py
   │     │  │  │  ├─ _helpers.py
   │     │  │  │  ├─ _python_rsa.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ downscoped.py
   │     │  │  ├─ environment_vars.py
   │     │  │  ├─ exceptions.py
   │     │  │  ├─ external_account.py
   │     │  │  ├─ external_account_authorized_user.py
   │     │  │  ├─ iam.py
   │     │  │  ├─ identity_pool.py
   │     │  │  ├─ impersonated_credentials.py
   │     │  │  ├─ jwt.py
   │     │  │  ├─ metrics.py
   │     │  │  ├─ pluggable.py
   │     │  │  ├─ py.typed
   │     │  │  ├─ transport
   │     │  │  │  ├─ grpc.py
   │     │  │  │  ├─ mtls.py
   │     │  │  │  ├─ requests.py
   │     │  │  │  ├─ urllib3.py
   │     │  │  │  ├─ _aiohttp_requests.py
   │     │  │  │  ├─ _custom_tls_signer.py
   │     │  │  │  ├─ _http_client.py
   │     │  │  │  ├─ _mtls_helper.py
   │     │  │  │  ├─ _requests_base.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ version.py
   │     │  │  ├─ _cloud_sdk.py
   │     │  │  ├─ _credentials_async.py
   │     │  │  ├─ _credentials_base.py
   │     │  │  ├─ _default.py
   │     │  │  ├─ _default_async.py
   │     │  │  ├─ _exponential_backoff.py
   │     │  │  ├─ _helpers.py
   │     │  │  ├─ _jwt_async.py
   │     │  │  ├─ _oauth2client.py
   │     │  │  ├─ _refresh_worker.py
   │     │  │  ├─ _service_account_info.py
   │     │  │  └─ __init__.py
   │     │  ├─ cloud
   │     │  │  ├─ extended_operations.proto
   │     │  │  ├─ extended_operations_pb2.py
   │     │  │  ├─ extended_operations_pb2.pyi
   │     │  │  └─ location
   │     │  │     ├─ locations.proto
   │     │  │     ├─ locations_pb2.py
   │     │  │     └─ locations_pb2.pyi
   │     │  ├─ gapic
   │     │  │  └─ metadata
   │     │  │     ├─ gapic_metadata.proto
   │     │  │     ├─ gapic_metadata_pb2.py
   │     │  │     └─ gapic_metadata_pb2.pyi
   │     │  ├─ logging
   │     │  │  └─ type
   │     │  │     ├─ http_request.proto
   │     │  │     ├─ http_request_pb2.py
   │     │  │     ├─ http_request_pb2.pyi
   │     │  │     ├─ log_severity.proto
   │     │  │     ├─ log_severity_pb2.py
   │     │  │     └─ log_severity_pb2.pyi
   │     │  ├─ longrunning
   │     │  │  ├─ operations_grpc.py
   │     │  │  ├─ operations_grpc_pb2.py
   │     │  │  ├─ operations_pb2.py
   │     │  │  ├─ operations_pb2_grpc.py
   │     │  │  ├─ operations_proto.proto
   │     │  │  ├─ operations_proto.py
   │     │  │  ├─ operations_proto_pb2.py
   │     │  │  └─ operations_proto_pb2.pyi
   │     │  ├─ oauth2
   │     │  │  ├─ challenges.py
   │     │  │  ├─ credentials.py
   │     │  │  ├─ gdch_credentials.py
   │     │  │  ├─ id_token.py
   │     │  │  ├─ py.typed
   │     │  │  ├─ reauth.py
   │     │  │  ├─ service_account.py
   │     │  │  ├─ sts.py
   │     │  │  ├─ utils.py
   │     │  │  ├─ webauthn_handler.py
   │     │  │  ├─ webauthn_handler_factory.py
   │     │  │  ├─ webauthn_types.py
   │     │  │  ├─ _client.py
   │     │  │  ├─ _client_async.py
   │     │  │  ├─ _credentials_async.py
   │     │  │  ├─ _id_token_async.py
   │     │  │  ├─ _reauth_async.py
   │     │  │  ├─ _service_account_async.py
   │     │  │  └─ __init__.py
   │     │  ├─ protobuf
   │     │  │  ├─ any.py
   │     │  │  ├─ any_pb2.py
   │     │  │  ├─ api_pb2.py
   │     │  │  ├─ compiler
   │     │  │  │  ├─ plugin_pb2.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ descriptor.py
   │     │  │  ├─ descriptor_database.py
   │     │  │  ├─ descriptor_pb2.py
   │     │  │  ├─ descriptor_pool.py
   │     │  │  ├─ duration.py
   │     │  │  ├─ duration_pb2.py
   │     │  │  ├─ empty_pb2.py
   │     │  │  ├─ field_mask_pb2.py
   │     │  │  ├─ internal
   │     │  │  │  ├─ api_implementation.py
   │     │  │  │  ├─ builder.py
   │     │  │  │  ├─ containers.py
   │     │  │  │  ├─ decoder.py
   │     │  │  │  ├─ encoder.py
   │     │  │  │  ├─ enum_type_wrapper.py
   │     │  │  │  ├─ extension_dict.py
   │     │  │  │  ├─ field_mask.py
   │     │  │  │  ├─ message_listener.py
   │     │  │  │  ├─ python_edition_defaults.py
   │     │  │  │  ├─ python_message.py
   │     │  │  │  ├─ testing_refleaks.py
   │     │  │  │  ├─ type_checkers.py
   │     │  │  │  ├─ well_known_types.py
   │     │  │  │  ├─ wire_format.py
   │     │  │  │  ├─ _parameterized.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ json_format.py
   │     │  │  ├─ message.py
   │     │  │  ├─ message_factory.py
   │     │  │  ├─ proto.py
   │     │  │  ├─ proto_builder.py
   │     │  │  ├─ proto_json.py
   │     │  │  ├─ pyext
   │     │  │  │  ├─ cpp_message.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ reflection.py
   │     │  │  ├─ runtime_version.py
   │     │  │  ├─ service.py
   │     │  │  ├─ service_reflection.py
   │     │  │  ├─ source_context_pb2.py
   │     │  │  ├─ struct_pb2.py
   │     │  │  ├─ symbol_database.py
   │     │  │  ├─ testdata
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ text_encoding.py
   │     │  │  ├─ text_format.py
   │     │  │  ├─ timestamp.py
   │     │  │  ├─ timestamp_pb2.py
   │     │  │  ├─ type_pb2.py
   │     │  │  ├─ unknown_fields.py
   │     │  │  ├─ util
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ wrappers_pb2.py
   │     │  │  └─ __init__.py
   │     │  ├─ rpc
   │     │  │  ├─ code.proto
   │     │  │  ├─ code_pb2.py
   │     │  │  ├─ code_pb2.pyi
   │     │  │  ├─ context
   │     │  │  │  ├─ attribute_context.proto
   │     │  │  │  ├─ attribute_context_pb2.py
   │     │  │  │  ├─ attribute_context_pb2.pyi
   │     │  │  │  ├─ audit_context.proto
   │     │  │  │  ├─ audit_context_pb2.py
   │     │  │  │  └─ audit_context_pb2.pyi
   │     │  │  ├─ error_details.proto
   │     │  │  ├─ error_details_pb2.py
   │     │  │  ├─ error_details_pb2.pyi
   │     │  │  ├─ http.proto
   │     │  │  ├─ http_pb2.py
   │     │  │  ├─ http_pb2.pyi
   │     │  │  ├─ status.proto
   │     │  │  ├─ status_pb2.py
   │     │  │  └─ status_pb2.pyi
   │     │  ├─ type
   │     │  │  ├─ calendar_period.proto
   │     │  │  ├─ calendar_period_pb2.py
   │     │  │  ├─ calendar_period_pb2.pyi
   │     │  │  ├─ color.proto
   │     │  │  ├─ color_pb2.py
   │     │  │  ├─ color_pb2.pyi
   │     │  │  ├─ date.proto
   │     │  │  ├─ datetime.proto
   │     │  │  ├─ datetime_pb2.py
   │     │  │  ├─ datetime_pb2.pyi
   │     │  │  ├─ date_pb2.py
   │     │  │  ├─ date_pb2.pyi
   │     │  │  ├─ dayofweek.proto
   │     │  │  ├─ dayofweek_pb2.py
   │     │  │  ├─ dayofweek_pb2.pyi
   │     │  │  ├─ decimal.proto
   │     │  │  ├─ decimal_pb2.py
   │     │  │  ├─ decimal_pb2.pyi
   │     │  │  ├─ expr.proto
   │     │  │  ├─ expr_pb2.py
   │     │  │  ├─ expr_pb2.pyi
   │     │  │  ├─ fraction.proto
   │     │  │  ├─ fraction_pb2.py
   │     │  │  ├─ fraction_pb2.pyi
   │     │  │  ├─ interval.proto
   │     │  │  ├─ interval_pb2.py
   │     │  │  ├─ interval_pb2.pyi
   │     │  │  ├─ latlng.proto
   │     │  │  ├─ latlng_pb2.py
   │     │  │  ├─ latlng_pb2.pyi
   │     │  │  ├─ localized_text.proto
   │     │  │  ├─ localized_text_pb2.py
   │     │  │  ├─ localized_text_pb2.pyi
   │     │  │  ├─ money.proto
   │     │  │  ├─ money_pb2.py
   │     │  │  ├─ money_pb2.pyi
   │     │  │  ├─ month.proto
   │     │  │  ├─ month_pb2.py
   │     │  │  ├─ month_pb2.pyi
   │     │  │  ├─ phone_number.proto
   │     │  │  ├─ phone_number_pb2.py
   │     │  │  ├─ phone_number_pb2.pyi
   │     │  │  ├─ postal_address.proto
   │     │  │  ├─ postal_address_pb2.py
   │     │  │  ├─ postal_address_pb2.pyi
   │     │  │  ├─ quaternion.proto
   │     │  │  ├─ quaternion_pb2.py
   │     │  │  ├─ quaternion_pb2.pyi
   │     │  │  ├─ timeofday.proto
   │     │  │  ├─ timeofday_pb2.py
   │     │  │  └─ timeofday_pb2.pyi
   │     │  └─ _upb
   │     │     └─ _message.pyd
   │     ├─ googleapiclient
   │     │  ├─ channel.py
   │     │  ├─ discovery.py
   │     │  ├─ discovery_cache
   │     │  │  ├─ appengine_memcache.py
   │     │  │  ├─ base.py
   │     │  │  ├─ documents
   │     │  │  │  ├─ abusiveexperiencereport.v1.json
   │     │  │  │  ├─ acceleratedmobilepageurl.v1.json
   │     │  │  │  ├─ accessapproval.v1.json
   │     │  │  │  ├─ accesscontextmanager.v1.json
   │     │  │  │  ├─ accesscontextmanager.v1beta.json
   │     │  │  │  ├─ acmedns.v1.json
   │     │  │  │  ├─ addressvalidation.v1.json
   │     │  │  │  ├─ adexchangebuyer.v1.2.json
   │     │  │  │  ├─ adexchangebuyer.v1.3.json
   │     │  │  │  ├─ adexchangebuyer.v1.4.json
   │     │  │  │  ├─ adexchangebuyer2.v2beta1.json
   │     │  │  │  ├─ adexperiencereport.v1.json
   │     │  │  │  ├─ admin.datatransferv1.json
   │     │  │  │  ├─ admin.datatransfer_v1.json
   │     │  │  │  ├─ admin.directoryv1.json
   │     │  │  │  ├─ admin.directory_v1.json
   │     │  │  │  ├─ admin.reportsv1.json
   │     │  │  │  ├─ admin.reports_v1.json
   │     │  │  │  ├─ admob.v1.json
   │     │  │  │  ├─ admob.v1beta.json
   │     │  │  │  ├─ adsense.v2.json
   │     │  │  │  ├─ adsensehost.v4.1.json
   │     │  │  │  ├─ adsenseplatform.v1.json
   │     │  │  │  ├─ adsenseplatform.v1alpha.json
   │     │  │  │  ├─ advisorynotifications.v1.json
   │     │  │  │  ├─ aiplatform.v1.json
   │     │  │  │  ├─ aiplatform.v1beta1.json
   │     │  │  │  ├─ airquality.v1.json
   │     │  │  │  ├─ alertcenter.v1beta1.json
   │     │  │  │  ├─ alloydb.v1.json
   │     │  │  │  ├─ alloydb.v1alpha.json
   │     │  │  │  ├─ alloydb.v1beta.json
   │     │  │  │  ├─ analytics.v3.json
   │     │  │  │  ├─ analyticsadmin.v1alpha.json
   │     │  │  │  ├─ analyticsadmin.v1beta.json
   │     │  │  │  ├─ analyticsdata.v1alpha.json
   │     │  │  │  ├─ analyticsdata.v1beta.json
   │     │  │  │  ├─ analyticshub.v1.json
   │     │  │  │  ├─ analyticshub.v1beta1.json
   │     │  │  │  ├─ analyticsreporting.v4.json
   │     │  │  │  ├─ androiddeviceprovisioning.v1.json
   │     │  │  │  ├─ androidenterprise.v1.json
   │     │  │  │  ├─ androidmanagement.v1.json
   │     │  │  │  ├─ androidpublisher.v3.json
   │     │  │  │  ├─ apigateway.v1.json
   │     │  │  │  ├─ apigateway.v1beta.json
   │     │  │  │  ├─ apigee.v1.json
   │     │  │  │  ├─ apigeeregistry.v1.json
   │     │  │  │  ├─ apikeys.v2.json
   │     │  │  │  ├─ apim.v1alpha.json
   │     │  │  │  ├─ appengine.v1.json
   │     │  │  │  ├─ appengine.v1alpha.json
   │     │  │  │  ├─ appengine.v1beta.json
   │     │  │  │  ├─ appengine.v1beta4.json
   │     │  │  │  ├─ appengine.v1beta5.json
   │     │  │  │  ├─ apphub.v1.json
   │     │  │  │  ├─ apphub.v1alpha.json
   │     │  │  │  ├─ area120tables.v1alpha1.json
   │     │  │  │  ├─ areainsights.v1.json
   │     │  │  │  ├─ artifactregistry.v1.json
   │     │  │  │  ├─ artifactregistry.v1beta1.json
   │     │  │  │  ├─ artifactregistry.v1beta2.json
   │     │  │  │  ├─ assuredworkloads.v1.json
   │     │  │  │  ├─ assuredworkloads.v1beta1.json
   │     │  │  │  ├─ authorizedbuyersmarketplace.v1.json
   │     │  │  │  ├─ authorizedbuyersmarketplace.v1alpha.json
   │     │  │  │  ├─ backupdr.v1.json
   │     │  │  │  ├─ baremetalsolution.v1.json
   │     │  │  │  ├─ baremetalsolution.v1alpha1.json
   │     │  │  │  ├─ baremetalsolution.v2.json
   │     │  │  │  ├─ batch.v1.json
   │     │  │  │  ├─ beyondcorp.v1.json
   │     │  │  │  ├─ beyondcorp.v1alpha.json
   │     │  │  │  ├─ biglake.v1.json
   │     │  │  │  ├─ bigquery.v2.json
   │     │  │  │  ├─ bigqueryconnection.v1.json
   │     │  │  │  ├─ bigqueryconnection.v1beta1.json
   │     │  │  │  ├─ bigquerydatapolicy.v1.json
   │     │  │  │  ├─ bigquerydatatransfer.v1.json
   │     │  │  │  ├─ bigqueryreservation.v1.json
   │     │  │  │  ├─ bigqueryreservation.v1alpha2.json
   │     │  │  │  ├─ bigqueryreservation.v1beta1.json
   │     │  │  │  ├─ bigtableadmin.v1.json
   │     │  │  │  ├─ bigtableadmin.v2.json
   │     │  │  │  ├─ billingbudgets.v1.json
   │     │  │  │  ├─ billingbudgets.v1beta1.json
   │     │  │  │  ├─ binaryauthorization.v1.json
   │     │  │  │  ├─ binaryauthorization.v1beta1.json
   │     │  │  │  ├─ blockchainnodeengine.v1.json
   │     │  │  │  ├─ blogger.v2.json
   │     │  │  │  ├─ blogger.v3.json
   │     │  │  │  ├─ books.v1.json
   │     │  │  │  ├─ businessprofileperformance.v1.json
   │     │  │  │  ├─ calendar.v3.json
   │     │  │  │  ├─ certificatemanager.v1.json
   │     │  │  │  ├─ chat.v1.json
   │     │  │  │  ├─ checks.v1alpha.json
   │     │  │  │  ├─ chromemanagement.v1.json
   │     │  │  │  ├─ chromepolicy.v1.json
   │     │  │  │  ├─ chromeuxreport.v1.json
   │     │  │  │  ├─ civicinfo.v2.json
   │     │  │  │  ├─ classroom.v1.json
   │     │  │  │  ├─ cloudasset.v1.json
   │     │  │  │  ├─ cloudasset.v1beta1.json
   │     │  │  │  ├─ cloudasset.v1p1beta1.json
   │     │  │  │  ├─ cloudasset.v1p4beta1.json
   │     │  │  │  ├─ cloudasset.v1p5beta1.json
   │     │  │  │  ├─ cloudasset.v1p7beta1.json
   │     │  │  │  ├─ cloudbilling.v1.json
   │     │  │  │  ├─ cloudbilling.v1beta.json
   │     │  │  │  ├─ cloudbuild.v1.json
   │     │  │  │  ├─ cloudbuild.v1alpha1.json
   │     │  │  │  ├─ cloudbuild.v1alpha2.json
   │     │  │  │  ├─ cloudbuild.v1beta1.json
   │     │  │  │  ├─ cloudbuild.v2.json
   │     │  │  │  ├─ cloudchannel.v1.json
   │     │  │  │  ├─ cloudcommerceprocurement.v1.json
   │     │  │  │  ├─ cloudcontrolspartner.v1.json
   │     │  │  │  ├─ cloudcontrolspartner.v1beta.json
   │     │  │  │  ├─ clouddebugger.v2.json
   │     │  │  │  ├─ clouddeploy.v1.json
   │     │  │  │  ├─ clouderrorreporting.v1beta1.json
   │     │  │  │  ├─ cloudfunctions.v1.json
   │     │  │  │  ├─ cloudfunctions.v2.json
   │     │  │  │  ├─ cloudfunctions.v2alpha.json
   │     │  │  │  ├─ cloudfunctions.v2beta.json
   │     │  │  │  ├─ cloudidentity.v1.json
   │     │  │  │  ├─ cloudidentity.v1beta1.json
   │     │  │  │  ├─ cloudiot.v1.json
   │     │  │  │  ├─ cloudkms.v1.json
   │     │  │  │  ├─ cloudprofiler.v2.json
   │     │  │  │  ├─ cloudresourcemanager.v1.json
   │     │  │  │  ├─ cloudresourcemanager.v1beta1.json
   │     │  │  │  ├─ cloudresourcemanager.v2.json
   │     │  │  │  ├─ cloudresourcemanager.v2beta1.json
   │     │  │  │  ├─ cloudresourcemanager.v3.json
   │     │  │  │  ├─ cloudscheduler.v1.json
   │     │  │  │  ├─ cloudscheduler.v1beta1.json
   │     │  │  │  ├─ cloudsearch.v1.json
   │     │  │  │  ├─ cloudshell.v1.json
   │     │  │  │  ├─ cloudshell.v1alpha1.json
   │     │  │  │  ├─ cloudsupport.v2.json
   │     │  │  │  ├─ cloudsupport.v2beta.json
   │     │  │  │  ├─ cloudtasks.v2.json
   │     │  │  │  ├─ cloudtasks.v2beta2.json
   │     │  │  │  ├─ cloudtasks.v2beta3.json
   │     │  │  │  ├─ cloudtrace.v1.json
   │     │  │  │  ├─ cloudtrace.v2.json
   │     │  │  │  ├─ cloudtrace.v2beta1.json
   │     │  │  │  ├─ composer.v1.json
   │     │  │  │  ├─ composer.v1beta1.json
   │     │  │  │  ├─ compute.alpha.json
   │     │  │  │  ├─ compute.beta.json
   │     │  │  │  ├─ compute.v1.json
   │     │  │  │  ├─ config.v1.json
   │     │  │  │  ├─ connectors.v1.json
   │     │  │  │  ├─ connectors.v2.json
   │     │  │  │  ├─ contactcenteraiplatform.v1alpha1.json
   │     │  │  │  ├─ contactcenterinsights.v1.json
   │     │  │  │  ├─ container.v1.json
   │     │  │  │  ├─ container.v1beta1.json
   │     │  │  │  ├─ containeranalysis.v1.json
   │     │  │  │  ├─ containeranalysis.v1alpha1.json
   │     │  │  │  ├─ containeranalysis.v1beta1.json
   │     │  │  │  ├─ content.v2.1.json
   │     │  │  │  ├─ content.v2.json
   │     │  │  │  ├─ contentwarehouse.v1.json
   │     │  │  │  ├─ css.v1.json
   │     │  │  │  ├─ customsearch.v1.json
   │     │  │  │  ├─ datacatalog.v1.json
   │     │  │  │  ├─ datacatalog.v1beta1.json
   │     │  │  │  ├─ dataflow.v1b3.json
   │     │  │  │  ├─ dataform.v1beta1.json
   │     │  │  │  ├─ datafusion.v1.json
   │     │  │  │  ├─ datafusion.v1beta1.json
   │     │  │  │  ├─ datalabeling.v1beta1.json
   │     │  │  │  ├─ datalineage.v1.json
   │     │  │  │  ├─ datamigration.v1.json
   │     │  │  │  ├─ datamigration.v1beta1.json
   │     │  │  │  ├─ datapipelines.v1.json
   │     │  │  │  ├─ dataplex.v1.json
   │     │  │  │  ├─ dataportability.v1.json
   │     │  │  │  ├─ dataportability.v1beta.json
   │     │  │  │  ├─ dataproc.v1.json
   │     │  │  │  ├─ dataproc.v1beta2.json
   │     │  │  │  ├─ datastore.v1.json
   │     │  │  │  ├─ datastore.v1beta1.json
   │     │  │  │  ├─ datastore.v1beta3.json
   │     │  │  │  ├─ datastream.v1.json
   │     │  │  │  ├─ datastream.v1alpha1.json
   │     │  │  │  ├─ deploymentmanager.alpha.json
   │     │  │  │  ├─ deploymentmanager.v2.json
   │     │  │  │  ├─ deploymentmanager.v2beta.json
   │     │  │  │  ├─ developerconnect.v1.json
   │     │  │  │  ├─ dfareporting.v3.3.json
   │     │  │  │  ├─ dfareporting.v3.4.json
   │     │  │  │  ├─ dfareporting.v3.5.json
   │     │  │  │  ├─ dfareporting.v4.json
   │     │  │  │  ├─ dialogflow.v2.json
   │     │  │  │  ├─ dialogflow.v2beta1.json
   │     │  │  │  ├─ dialogflow.v3.json
   │     │  │  │  ├─ dialogflow.v3beta1.json
   │     │  │  │  ├─ digitalassetlinks.v1.json
   │     │  │  │  ├─ discovery.v1.json
   │     │  │  │  ├─ discoveryengine.v1.json
   │     │  │  │  ├─ discoveryengine.v1alpha.json
   │     │  │  │  ├─ discoveryengine.v1beta.json
   │     │  │  │  ├─ displayvideo.v1.json
   │     │  │  │  ├─ displayvideo.v2.json
   │     │  │  │  ├─ displayvideo.v3.json
   │     │  │  │  ├─ displayvideo.v4.json
   │     │  │  │  ├─ dlp.v2.json
   │     │  │  │  ├─ dns.v1.json
   │     │  │  │  ├─ dns.v1beta2.json
   │     │  │  │  ├─ dns.v2.json
   │     │  │  │  ├─ docs.v1.json
   │     │  │  │  ├─ documentai.v1.json
   │     │  │  │  ├─ documentai.v1beta2.json
   │     │  │  │  ├─ documentai.v1beta3.json
   │     │  │  │  ├─ domains.v1.json
   │     │  │  │  ├─ domains.v1alpha2.json
   │     │  │  │  ├─ domains.v1beta1.json
   │     │  │  │  ├─ domainsrdap.v1.json
   │     │  │  │  ├─ doubleclickbidmanager.v1.1.json
   │     │  │  │  ├─ doubleclickbidmanager.v1.json
   │     │  │  │  ├─ doubleclickbidmanager.v2.json
   │     │  │  │  ├─ doubleclicksearch.v2.json
   │     │  │  │  ├─ drive.v2.json
   │     │  │  │  ├─ drive.v3.json
   │     │  │  │  ├─ driveactivity.v2.json
   │     │  │  │  ├─ drivelabels.v2.json
   │     │  │  │  ├─ drivelabels.v2beta.json
   │     │  │  │  ├─ essentialcontacts.v1.json
   │     │  │  │  ├─ eventarc.v1.json
   │     │  │  │  ├─ eventarc.v1beta1.json
   │     │  │  │  ├─ factchecktools.v1alpha1.json
   │     │  │  │  ├─ fcm.v1.json
   │     │  │  │  ├─ fcmdata.v1beta1.json
   │     │  │  │  ├─ file.v1.json
   │     │  │  │  ├─ file.v1beta1.json
   │     │  │  │  ├─ firebase.v1beta1.json
   │     │  │  │  ├─ firebaseappcheck.v1.json
   │     │  │  │  ├─ firebaseappcheck.v1beta.json
   │     │  │  │  ├─ firebaseappdistribution.v1.json
   │     │  │  │  ├─ firebaseappdistribution.v1alpha.json
   │     │  │  │  ├─ firebasedatabase.v1beta.json
   │     │  │  │  ├─ firebasedataconnect.v1beta.json
   │     │  │  │  ├─ firebasedynamiclinks.v1.json
   │     │  │  │  ├─ firebasehosting.v1.json
   │     │  │  │  ├─ firebasehosting.v1beta1.json
   │     │  │  │  ├─ firebaseml.v1.json
   │     │  │  │  ├─ firebaseml.v1beta2.json
   │     │  │  │  ├─ firebaseml.v2beta.json
   │     │  │  │  ├─ firebaserules.v1.json
   │     │  │  │  ├─ firebasestorage.v1beta.json
   │     │  │  │  ├─ firestore.v1.json
   │     │  │  │  ├─ firestore.v1beta1.json
   │     │  │  │  ├─ firestore.v1beta2.json
   │     │  │  │  ├─ fitness.v1.json
   │     │  │  │  ├─ forms.v1.json
   │     │  │  │  ├─ games.v1.json
   │     │  │  │  ├─ gamesConfiguration.v1configuration.json
   │     │  │  │  ├─ gameservices.v1.json
   │     │  │  │  ├─ gameservices.v1beta.json
   │     │  │  │  ├─ gamesManagement.v1management.json
   │     │  │  │  ├─ genomics.v1.json
   │     │  │  │  ├─ genomics.v1alpha2.json
   │     │  │  │  ├─ genomics.v2alpha1.json
   │     │  │  │  ├─ gkebackup.v1.json
   │     │  │  │  ├─ gkehub.v1.json
   │     │  │  │  ├─ gkehub.v1alpha.json
   │     │  │  │  ├─ gkehub.v1alpha2.json
   │     │  │  │  ├─ gkehub.v1beta.json
   │     │  │  │  ├─ gkehub.v1beta1.json
   │     │  │  │  ├─ gkehub.v2.json
   │     │  │  │  ├─ gkehub.v2alpha.json
   │     │  │  │  ├─ gkehub.v2beta.json
   │     │  │  │  ├─ gkeonprem.v1.json
   │     │  │  │  ├─ gmail.v1.json
   │     │  │  │  ├─ gmailpostmastertools.v1.json
   │     │  │  │  ├─ gmailpostmastertools.v1beta1.json
   │     │  │  │  ├─ groupsmigration.v1.json
   │     │  │  │  ├─ groupssettings.v1.json
   │     │  │  │  ├─ healthcare.v1.json
   │     │  │  │  ├─ healthcare.v1beta1.json
   │     │  │  │  ├─ homegraph.v1.json
   │     │  │  │  ├─ iam.v1.json
   │     │  │  │  ├─ iam.v2.json
   │     │  │  │  ├─ iam.v2beta.json
   │     │  │  │  ├─ iamcredentials.v1.json
   │     │  │  │  ├─ iap.v1.json
   │     │  │  │  ├─ iap.v1beta1.json
   │     │  │  │  ├─ ideahub.v1alpha.json
   │     │  │  │  ├─ ideahub.v1beta.json
   │     │  │  │  ├─ identitytoolkit.v1.json
   │     │  │  │  ├─ identitytoolkit.v2.json
   │     │  │  │  ├─ identitytoolkit.v3.json
   │     │  │  │  ├─ ids.v1.json
   │     │  │  │  ├─ index.json
   │     │  │  │  ├─ indexing.v3.json
   │     │  │  │  ├─ integrations.v1.json
   │     │  │  │  ├─ integrations.v1alpha.json
   │     │  │  │  ├─ jobs.v2.json
   │     │  │  │  ├─ jobs.v3.json
   │     │  │  │  ├─ jobs.v3p1beta1.json
   │     │  │  │  ├─ jobs.v4.json
   │     │  │  │  ├─ keep.v1.json
   │     │  │  │  ├─ kgsearch.v1.json
   │     │  │  │  ├─ kmsinventory.v1.json
   │     │  │  │  ├─ language.v1.json
   │     │  │  │  ├─ language.v1beta1.json
   │     │  │  │  ├─ language.v1beta2.json
   │     │  │  │  ├─ language.v2.json
   │     │  │  │  ├─ libraryagent.v1.json
   │     │  │  │  ├─ licensing.v1.json
   │     │  │  │  ├─ lifesciences.v2beta.json
   │     │  │  │  ├─ localservices.v1.json
   │     │  │  │  ├─ logging.v2.json
   │     │  │  │  ├─ looker.v1.json
   │     │  │  │  ├─ managedidentities.v1.json
   │     │  │  │  ├─ managedidentities.v1alpha1.json
   │     │  │  │  ├─ managedidentities.v1beta1.json
   │     │  │  │  ├─ manufacturers.v1.json
   │     │  │  │  ├─ marketingplatformadmin.v1alpha.json
   │     │  │  │  ├─ meet.v2.json
   │     │  │  │  ├─ memcache.v1.json
   │     │  │  │  ├─ memcache.v1beta2.json
   │     │  │  │  ├─ merchantapi.accounts_v1beta.json
   │     │  │  │  ├─ merchantapi.conversions_v1beta.json
   │     │  │  │  ├─ merchantapi.datasources_v1beta.json
   │     │  │  │  ├─ merchantapi.inventories_v1beta.json
   │     │  │  │  ├─ merchantapi.lfp_v1beta.json
   │     │  │  │  ├─ merchantapi.notifications_v1beta.json
   │     │  │  │  ├─ merchantapi.products_v1beta.json
   │     │  │  │  ├─ merchantapi.promotions_v1beta.json
   │     │  │  │  ├─ merchantapi.quota_v1beta.json
   │     │  │  │  ├─ merchantapi.reports_v1beta.json
   │     │  │  │  ├─ merchantapi.reviews_v1beta.json
   │     │  │  │  ├─ metastore.v1.json
   │     │  │  │  ├─ metastore.v1alpha.json
   │     │  │  │  ├─ metastore.v1beta.json
   │     │  │  │  ├─ metastore.v2.json
   │     │  │  │  ├─ metastore.v2alpha.json
   │     │  │  │  ├─ metastore.v2beta.json
   │     │  │  │  ├─ migrationcenter.v1.json
   │     │  │  │  ├─ migrationcenter.v1alpha1.json
   │     │  │  │  ├─ ml.v1.json
   │     │  │  │  ├─ monitoring.v1.json
   │     │  │  │  ├─ monitoring.v3.json
   │     │  │  │  ├─ mybusinessaccountmanagement.v1.json
   │     │  │  │  ├─ mybusinessbusinesscalls.v1.json
   │     │  │  │  ├─ mybusinessbusinessinformation.v1.json
   │     │  │  │  ├─ mybusinesslodging.v1.json
   │     │  │  │  ├─ mybusinessnotifications.v1.json
   │     │  │  │  ├─ mybusinessplaceactions.v1.json
   │     │  │  │  ├─ mybusinessqanda.v1.json
   │     │  │  │  ├─ mybusinessverifications.v1.json
   │     │  │  │  ├─ netapp.v1.json
   │     │  │  │  ├─ netapp.v1beta1.json
   │     │  │  │  ├─ networkconnectivity.v1.json
   │     │  │  │  ├─ networkconnectivity.v1alpha1.json
   │     │  │  │  ├─ networkmanagement.v1.json
   │     │  │  │  ├─ networkmanagement.v1beta1.json
   │     │  │  │  ├─ networksecurity.v1.json
   │     │  │  │  ├─ networksecurity.v1beta1.json
   │     │  │  │  ├─ networkservices.v1.json
   │     │  │  │  ├─ networkservices.v1beta1.json
   │     │  │  │  ├─ notebooks.v1.json
   │     │  │  │  ├─ notebooks.v2.json
   │     │  │  │  ├─ oauth2.v2.json
   │     │  │  │  ├─ ondemandscanning.v1.json
   │     │  │  │  ├─ ondemandscanning.v1beta1.json
   │     │  │  │  ├─ oracledatabase.v1.json
   │     │  │  │  ├─ orgpolicy.v2.json
   │     │  │  │  ├─ osconfig.v1.json
   │     │  │  │  ├─ osconfig.v1alpha.json
   │     │  │  │  ├─ osconfig.v1beta.json
   │     │  │  │  ├─ osconfig.v2beta.json
   │     │  │  │  ├─ oslogin.v1.json
   │     │  │  │  ├─ oslogin.v1alpha.json
   │     │  │  │  ├─ oslogin.v1beta.json
   │     │  │  │  ├─ pagespeedonline.v5.json
   │     │  │  │  ├─ parallelstore.v1.json
   │     │  │  │  ├─ parallelstore.v1beta.json
   │     │  │  │  ├─ paymentsresellersubscription.v1.json
   │     │  │  │  ├─ people.v1.json
   │     │  │  │  ├─ places.v1.json
   │     │  │  │  ├─ playablelocations.v3.json
   │     │  │  │  ├─ playcustomapp.v1.json
   │     │  │  │  ├─ playdeveloperreporting.v1alpha1.json
   │     │  │  │  ├─ playdeveloperreporting.v1beta1.json
   │     │  │  │  ├─ playgrouping.v1alpha1.json
   │     │  │  │  ├─ playintegrity.v1.json
   │     │  │  │  ├─ policyanalyzer.v1.json
   │     │  │  │  ├─ policyanalyzer.v1beta1.json
   │     │  │  │  ├─ policysimulator.v1.json
   │     │  │  │  ├─ policysimulator.v1alpha.json
   │     │  │  │  ├─ policysimulator.v1beta.json
   │     │  │  │  ├─ policysimulator.v1beta1.json
   │     │  │  │  ├─ policytroubleshooter.v1.json
   │     │  │  │  ├─ policytroubleshooter.v1beta.json
   │     │  │  │  ├─ pollen.v1.json
   │     │  │  │  ├─ poly.v1.json
   │     │  │  │  ├─ privateca.v1.json
   │     │  │  │  ├─ privateca.v1beta1.json
   │     │  │  │  ├─ prod_tt_sasportal.v1alpha1.json
   │     │  │  │  ├─ publicca.v1.json
   │     │  │  │  ├─ publicca.v1alpha1.json
   │     │  │  │  ├─ publicca.v1beta1.json
   │     │  │  │  ├─ pubsub.v1.json
   │     │  │  │  ├─ pubsub.v1beta1a.json
   │     │  │  │  ├─ pubsub.v1beta2.json
   │     │  │  │  ├─ pubsublite.v1.json
   │     │  │  │  ├─ rapidmigrationassessment.v1.json
   │     │  │  │  ├─ readerrevenuesubscriptionlinking.v1.json
   │     │  │  │  ├─ realtimebidding.v1.json
   │     │  │  │  ├─ realtimebidding.v1alpha.json
   │     │  │  │  ├─ recaptchaenterprise.v1.json
   │     │  │  │  ├─ recommendationengine.v1beta1.json
   │     │  │  │  ├─ recommender.v1.json
   │     │  │  │  ├─ recommender.v1beta1.json
   │     │  │  │  ├─ redis.v1.json
   │     │  │  │  ├─ redis.v1beta1.json
   │     │  │  │  ├─ remotebuildexecution.v1.json
   │     │  │  │  ├─ remotebuildexecution.v1alpha.json
   │     │  │  │  ├─ remotebuildexecution.v2.json
   │     │  │  │  ├─ reseller.v1.json
   │     │  │  │  ├─ resourcesettings.v1.json
   │     │  │  │  ├─ retail.v2.json
   │     │  │  │  ├─ retail.v2alpha.json
   │     │  │  │  ├─ retail.v2beta.json
   │     │  │  │  ├─ run.v1.json
   │     │  │  │  ├─ run.v1alpha1.json
   │     │  │  │  ├─ run.v1beta1.json
   │     │  │  │  ├─ run.v2.json
   │     │  │  │  ├─ runtimeconfig.v1.json
   │     │  │  │  ├─ runtimeconfig.v1beta1.json
   │     │  │  │  ├─ safebrowsing.v4.json
   │     │  │  │  ├─ safebrowsing.v5.json
   │     │  │  │  ├─ sasportal.v1alpha1.json
   │     │  │  │  ├─ script.v1.json
   │     │  │  │  ├─ searchads360.v0.json
   │     │  │  │  ├─ searchconsole.v1.json
   │     │  │  │  ├─ secretmanager.v1.json
   │     │  │  │  ├─ secretmanager.v1beta1.json
   │     │  │  │  ├─ secretmanager.v1beta2.json
   │     │  │  │  ├─ securitycenter.v1.json
   │     │  │  │  ├─ securitycenter.v1beta1.json
   │     │  │  │  ├─ securitycenter.v1beta2.json
   │     │  │  │  ├─ securityposture.v1.json
   │     │  │  │  ├─ serviceconsumermanagement.v1.json
   │     │  │  │  ├─ serviceconsumermanagement.v1beta1.json
   │     │  │  │  ├─ servicecontrol.v1.json
   │     │  │  │  ├─ servicecontrol.v2.json
   │     │  │  │  ├─ servicedirectory.v1.json
   │     │  │  │  ├─ servicedirectory.v1beta1.json
   │     │  │  │  ├─ servicemanagement.v1.json
   │     │  │  │  ├─ servicenetworking.v1.json
   │     │  │  │  ├─ servicenetworking.v1beta.json
   │     │  │  │  ├─ serviceusage.v1.json
   │     │  │  │  ├─ serviceusage.v1beta1.json
   │     │  │  │  ├─ sheets.v4.json
   │     │  │  │  ├─ siteVerification.v1.json
   │     │  │  │  ├─ slides.v1.json
   │     │  │  │  ├─ smartdevicemanagement.v1.json
   │     │  │  │  ├─ solar.v1.json
   │     │  │  │  ├─ sourcerepo.v1.json
   │     │  │  │  ├─ spanner.v1.json
   │     │  │  │  ├─ speech.v1.json
   │     │  │  │  ├─ speech.v1p1beta1.json
   │     │  │  │  ├─ speech.v2beta1.json
   │     │  │  │  ├─ sqladmin.v1.json
   │     │  │  │  ├─ sqladmin.v1beta4.json
   │     │  │  │  ├─ storage.v1.json
   │     │  │  │  ├─ storagetransfer.v1.json
   │     │  │  │  ├─ streetviewpublish.v1.json
   │     │  │  │  ├─ sts.v1.json
   │     │  │  │  ├─ sts.v1beta.json
   │     │  │  │  ├─ tagmanager.v1.json
   │     │  │  │  ├─ tagmanager.v2.json
   │     │  │  │  ├─ tasks.v1.json
   │     │  │  │  ├─ testing.v1.json
   │     │  │  │  ├─ texttospeech.v1.json
   │     │  │  │  ├─ texttospeech.v1beta1.json
   │     │  │  │  ├─ toolresults.v1beta3.json
   │     │  │  │  ├─ tpu.v1.json
   │     │  │  │  ├─ tpu.v1alpha1.json
   │     │  │  │  ├─ tpu.v2.json
   │     │  │  │  ├─ tpu.v2alpha1.json
   │     │  │  │  ├─ trafficdirector.v2.json
   │     │  │  │  ├─ trafficdirector.v3.json
   │     │  │  │  ├─ transcoder.v1.json
   │     │  │  │  ├─ transcoder.v1beta1.json
   │     │  │  │  ├─ translate.v2.json
   │     │  │  │  ├─ translate.v3.json
   │     │  │  │  ├─ translate.v3beta1.json
   │     │  │  │  ├─ travelimpactmodel.v1.json
   │     │  │  │  ├─ vault.v1.json
   │     │  │  │  ├─ vectortile.v1.json
   │     │  │  │  ├─ verifiedaccess.v1.json
   │     │  │  │  ├─ verifiedaccess.v2.json
   │     │  │  │  ├─ versionhistory.v1.json
   │     │  │  │  ├─ videointelligence.v1.json
   │     │  │  │  ├─ videointelligence.v1beta2.json
   │     │  │  │  ├─ videointelligence.v1p1beta1.json
   │     │  │  │  ├─ videointelligence.v1p2beta1.json
   │     │  │  │  ├─ videointelligence.v1p3beta1.json
   │     │  │  │  ├─ vision.v1.json
   │     │  │  │  ├─ vision.v1p1beta1.json
   │     │  │  │  ├─ vision.v1p2beta1.json
   │     │  │  │  ├─ vmmigration.v1.json
   │     │  │  │  ├─ vmmigration.v1alpha1.json
   │     │  │  │  ├─ vmwareengine.v1.json
   │     │  │  │  ├─ vpcaccess.v1.json
   │     │  │  │  ├─ vpcaccess.v1beta1.json
   │     │  │  │  ├─ walletobjects.v1.json
   │     │  │  │  ├─ webfonts.v1.json
   │     │  │  │  ├─ webmasters.v3.json
   │     │  │  │  ├─ webrisk.v1.json
   │     │  │  │  ├─ websecurityscanner.v1.json
   │     │  │  │  ├─ websecurityscanner.v1alpha.json
   │     │  │  │  ├─ websecurityscanner.v1beta.json
   │     │  │  │  ├─ workflowexecutions.v1.json
   │     │  │  │  ├─ workflowexecutions.v1beta.json
   │     │  │  │  ├─ workflows.v1.json
   │     │  │  │  ├─ workflows.v1beta.json
   │     │  │  │  ├─ workloadmanager.v1.json
   │     │  │  │  ├─ workspaceevents.v1.json
   │     │  │  │  ├─ workstations.v1.json
   │     │  │  │  ├─ workstations.v1beta.json
   │     │  │  │  ├─ youtube.v3.json
   │     │  │  │  ├─ youtubeAnalytics.v1.json
   │     │  │  │  ├─ youtubeAnalytics.v2.json
   │     │  │  │  └─ youtubereporting.v1.json
   │     │  │  ├─ file_cache.py
   │     │  │  └─ __init__.py
   │     │  ├─ errors.py
   │     │  ├─ http.py
   │     │  ├─ mimeparse.py
   │     │  ├─ model.py
   │     │  ├─ sample_tools.py
   │     │  ├─ schema.py
   │     │  ├─ version.py
   │     │  ├─ _auth.py
   │     │  ├─ _helpers.py
   │     │  └─ __init__.py
   │     ├─ googleapis_common_protos-1.69.1.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ google_api_core-2.24.2.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ google_api_python_client-2.164.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ google_auth-2.38.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ google_auth_httplib2-0.2.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ google_auth_httplib2.py
   │     ├─ google_auth_oauthlib
   │     │  ├─ flow.py
   │     │  ├─ helpers.py
   │     │  ├─ interactive.py
   │     │  ├─ tool
   │     │  │  ├─ __init__.py
   │     │  │  └─ __main__.py
   │     │  └─ __init__.py
   │     ├─ google_auth_oauthlib-1.2.1.dist-info
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ gspread
   │     │  ├─ auth.py
   │     │  ├─ cell.py
   │     │  ├─ client.py
   │     │  ├─ exceptions.py
   │     │  ├─ http_client.py
   │     │  ├─ py.typed
   │     │  ├─ spreadsheet.py
   │     │  ├─ urls.py
   │     │  ├─ utils.py
   │     │  ├─ worksheet.py
   │     │  └─ __init__.py
   │     ├─ gspread-6.2.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE.txt
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  └─ WHEEL
   │     ├─ h11
   │     │  ├─ py.typed
   │     │  ├─ tests
   │     │  │  ├─ data
   │     │  │  │  └─ test-file
   │     │  │  ├─ helpers.py
   │     │  │  ├─ test_against_stdlib_http.py
   │     │  │  ├─ test_connection.py
   │     │  │  ├─ test_events.py
   │     │  │  ├─ test_headers.py
   │     │  │  ├─ test_helpers.py
   │     │  │  ├─ test_io.py
   │     │  │  ├─ test_receivebuffer.py
   │     │  │  ├─ test_state.py
   │     │  │  ├─ test_util.py
   │     │  │  └─ __init__.py
   │     │  ├─ _abnf.py
   │     │  ├─ _connection.py
   │     │  ├─ _events.py
   │     │  ├─ _headers.py
   │     │  ├─ _readers.py
   │     │  ├─ _receivebuffer.py
   │     │  ├─ _state.py
   │     │  ├─ _util.py
   │     │  ├─ _version.py
   │     │  ├─ _writers.py
   │     │  └─ __init__.py
   │     ├─ h11-0.14.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE.txt
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ httplib2
   │     │  ├─ auth.py
   │     │  ├─ cacerts.txt
   │     │  ├─ certs.py
   │     │  ├─ error.py
   │     │  ├─ iri2uri.py
   │     │  ├─ socks.py
   │     │  └─ __init__.py
   │     ├─ httplib2-0.22.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ idna
   │     │  ├─ codec.py
   │     │  ├─ compat.py
   │     │  ├─ core.py
   │     │  ├─ idnadata.py
   │     │  ├─ intranges.py
   │     │  ├─ package_data.py
   │     │  ├─ py.typed
   │     │  ├─ uts46data.py
   │     │  └─ __init__.py
   │     ├─ idna-3.10.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE.md
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  └─ WHEEL
   │     ├─ jinja2
   │     │  ├─ async_utils.py
   │     │  ├─ bccache.py
   │     │  ├─ compiler.py
   │     │  ├─ constants.py
   │     │  ├─ debug.py
   │     │  ├─ defaults.py
   │     │  ├─ environment.py
   │     │  ├─ exceptions.py
   │     │  ├─ ext.py
   │     │  ├─ filters.py
   │     │  ├─ idtracking.py
   │     │  ├─ lexer.py
   │     │  ├─ loaders.py
   │     │  ├─ meta.py
   │     │  ├─ nativetypes.py
   │     │  ├─ nodes.py
   │     │  ├─ optimizer.py
   │     │  ├─ parser.py
   │     │  ├─ py.typed
   │     │  ├─ runtime.py
   │     │  ├─ sandbox.py
   │     │  ├─ tests.py
   │     │  ├─ utils.py
   │     │  ├─ visitor.py
   │     │  ├─ _identifier.py
   │     │  └─ __init__.py
   │     ├─ jinja2-3.1.6.dist-info
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE.txt
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  └─ WHEEL
   │     ├─ joblib
   │     │  ├─ backports.py
   │     │  ├─ compressor.py
   │     │  ├─ disk.py
   │     │  ├─ executor.py
   │     │  ├─ externals
   │     │  │  ├─ cloudpickle
   │     │  │  │  ├─ cloudpickle.py
   │     │  │  │  ├─ cloudpickle_fast.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ loky
   │     │  │  │  ├─ backend
   │     │  │  │  │  ├─ context.py
   │     │  │  │  │  ├─ fork_exec.py
   │     │  │  │  │  ├─ popen_loky_posix.py
   │     │  │  │  │  ├─ popen_loky_win32.py
   │     │  │  │  │  ├─ process.py
   │     │  │  │  │  ├─ queues.py
   │     │  │  │  │  ├─ reduction.py
   │     │  │  │  │  ├─ resource_tracker.py
   │     │  │  │  │  ├─ spawn.py
   │     │  │  │  │  ├─ synchronize.py
   │     │  │  │  │  ├─ utils.py
   │     │  │  │  │  ├─ _posix_reduction.py
   │     │  │  │  │  ├─ _win_reduction.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ cloudpickle_wrapper.py
   │     │  │  │  ├─ initializers.py
   │     │  │  │  ├─ process_executor.py
   │     │  │  │  ├─ reusable_executor.py
   │     │  │  │  ├─ _base.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ func_inspect.py
   │     │  ├─ hashing.py
   │     │  ├─ logger.py
   │     │  ├─ memory.py
   │     │  ├─ numpy_pickle.py
   │     │  ├─ numpy_pickle_compat.py
   │     │  ├─ numpy_pickle_utils.py
   │     │  ├─ parallel.py
   │     │  ├─ pool.py
   │     │  ├─ test
   │     │  │  ├─ common.py
   │     │  │  ├─ data
   │     │  │  │  ├─ create_numpy_pickle.py
   │     │  │  │  ├─ joblib_0.10.0_compressed_pickle_py27_np16.gz
   │     │  │  │  ├─ joblib_0.10.0_compressed_pickle_py27_np17.gz
   │     │  │  │  ├─ joblib_0.10.0_compressed_pickle_py33_np18.gz
   │     │  │  │  ├─ joblib_0.10.0_compressed_pickle_py34_np19.gz
   │     │  │  │  ├─ joblib_0.10.0_compressed_pickle_py35_np19.gz
   │     │  │  │  ├─ joblib_0.10.0_pickle_py27_np17.pkl
   │     │  │  │  ├─ joblib_0.10.0_pickle_py27_np17.pkl.bz2
   │     │  │  │  ├─ joblib_0.10.0_pickle_py27_np17.pkl.gzip
   │     │  │  │  ├─ joblib_0.10.0_pickle_py27_np17.pkl.lzma
   │     │  │  │  ├─ joblib_0.10.0_pickle_py27_np17.pkl.xz
   │     │  │  │  ├─ joblib_0.10.0_pickle_py33_np18.pkl
   │     │  │  │  ├─ joblib_0.10.0_pickle_py33_np18.pkl.bz2
   │     │  │  │  ├─ joblib_0.10.0_pickle_py33_np18.pkl.gzip
   │     │  │  │  ├─ joblib_0.10.0_pickle_py33_np18.pkl.lzma
   │     │  │  │  ├─ joblib_0.10.0_pickle_py33_np18.pkl.xz
   │     │  │  │  ├─ joblib_0.10.0_pickle_py34_np19.pkl
   │     │  │  │  ├─ joblib_0.10.0_pickle_py34_np19.pkl.bz2
   │     │  │  │  ├─ joblib_0.10.0_pickle_py34_np19.pkl.gzip
   │     │  │  │  ├─ joblib_0.10.0_pickle_py34_np19.pkl.lzma
   │     │  │  │  ├─ joblib_0.10.0_pickle_py34_np19.pkl.xz
   │     │  │  │  ├─ joblib_0.10.0_pickle_py35_np19.pkl
   │     │  │  │  ├─ joblib_0.10.0_pickle_py35_np19.pkl.bz2
   │     │  │  │  ├─ joblib_0.10.0_pickle_py35_np19.pkl.gzip
   │     │  │  │  ├─ joblib_0.10.0_pickle_py35_np19.pkl.lzma
   │     │  │  │  ├─ joblib_0.10.0_pickle_py35_np19.pkl.xz
   │     │  │  │  ├─ joblib_0.11.0_compressed_pickle_py36_np111.gz
   │     │  │  │  ├─ joblib_0.11.0_pickle_py36_np111.pkl
   │     │  │  │  ├─ joblib_0.11.0_pickle_py36_np111.pkl.bz2
   │     │  │  │  ├─ joblib_0.11.0_pickle_py36_np111.pkl.gzip
   │     │  │  │  ├─ joblib_0.11.0_pickle_py36_np111.pkl.lzma
   │     │  │  │  ├─ joblib_0.11.0_pickle_py36_np111.pkl.xz
   │     │  │  │  ├─ joblib_0.8.4_compressed_pickle_py27_np17.gz
   │     │  │  │  ├─ joblib_0.9.2_compressed_pickle_py27_np16.gz
   │     │  │  │  ├─ joblib_0.9.2_compressed_pickle_py27_np17.gz
   │     │  │  │  ├─ joblib_0.9.2_compressed_pickle_py34_np19.gz
   │     │  │  │  ├─ joblib_0.9.2_compressed_pickle_py35_np19.gz
   │     │  │  │  ├─ joblib_0.9.2_pickle_py27_np16.pkl
   │     │  │  │  ├─ joblib_0.9.2_pickle_py27_np16.pkl_01.npy
   │     │  │  │  ├─ joblib_0.9.2_pickle_py27_np16.pkl_02.npy
   │     │  │  │  ├─ joblib_0.9.2_pickle_py27_np16.pkl_03.npy
   │     │  │  │  ├─ joblib_0.9.2_pickle_py27_np16.pkl_04.npy
   │     │  │  │  ├─ joblib_0.9.2_pickle_py27_np17.pkl
   │     │  │  │  ├─ joblib_0.9.2_pickle_py27_np17.pkl_01.npy
   │     │  │  │  ├─ joblib_0.9.2_pickle_py27_np17.pkl_02.npy
   │     │  │  │  ├─ joblib_0.9.2_pickle_py27_np17.pkl_03.npy
   │     │  │  │  ├─ joblib_0.9.2_pickle_py27_np17.pkl_04.npy
   │     │  │  │  ├─ joblib_0.9.2_pickle_py33_np18.pkl
   │     │  │  │  ├─ joblib_0.9.2_pickle_py33_np18.pkl_01.npy
   │     │  │  │  ├─ joblib_0.9.2_pickle_py33_np18.pkl_02.npy
   │     │  │  │  ├─ joblib_0.9.2_pickle_py33_np18.pkl_03.npy
   │     │  │  │  ├─ joblib_0.9.2_pickle_py33_np18.pkl_04.npy
   │     │  │  │  ├─ joblib_0.9.2_pickle_py34_np19.pkl
   │     │  │  │  ├─ joblib_0.9.2_pickle_py34_np19.pkl_01.npy
   │     │  │  │  ├─ joblib_0.9.2_pickle_py34_np19.pkl_02.npy
   │     │  │  │  ├─ joblib_0.9.2_pickle_py34_np19.pkl_03.npy
   │     │  │  │  ├─ joblib_0.9.2_pickle_py34_np19.pkl_04.npy
   │     │  │  │  ├─ joblib_0.9.2_pickle_py35_np19.pkl
   │     │  │  │  ├─ joblib_0.9.2_pickle_py35_np19.pkl_01.npy
   │     │  │  │  ├─ joblib_0.9.2_pickle_py35_np19.pkl_02.npy
   │     │  │  │  ├─ joblib_0.9.2_pickle_py35_np19.pkl_03.npy
   │     │  │  │  ├─ joblib_0.9.2_pickle_py35_np19.pkl_04.npy
   │     │  │  │  ├─ joblib_0.9.4.dev0_compressed_cache_size_pickle_py35_np19.gz
   │     │  │  │  ├─ joblib_0.9.4.dev0_compressed_cache_size_pickle_py35_np19.gz_01.npy.z
   │     │  │  │  ├─ joblib_0.9.4.dev0_compressed_cache_size_pickle_py35_np19.gz_02.npy.z
   │     │  │  │  ├─ joblib_0.9.4.dev0_compressed_cache_size_pickle_py35_np19.gz_03.npy.z
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ testutils.py
   │     │  │  ├─ test_backports.py
   │     │  │  ├─ test_cloudpickle_wrapper.py
   │     │  │  ├─ test_config.py
   │     │  │  ├─ test_dask.py
   │     │  │  ├─ test_disk.py
   │     │  │  ├─ test_func_inspect.py
   │     │  │  ├─ test_func_inspect_special_encoding.py
   │     │  │  ├─ test_hashing.py
   │     │  │  ├─ test_init.py
   │     │  │  ├─ test_logger.py
   │     │  │  ├─ test_memmapping.py
   │     │  │  ├─ test_memory.py
   │     │  │  ├─ test_memory_async.py
   │     │  │  ├─ test_missing_multiprocessing.py
   │     │  │  ├─ test_module.py
   │     │  │  ├─ test_numpy_pickle.py
   │     │  │  ├─ test_numpy_pickle_compat.py
   │     │  │  ├─ test_numpy_pickle_utils.py
   │     │  │  ├─ test_parallel.py
   │     │  │  ├─ test_store_backends.py
   │     │  │  ├─ test_testing.py
   │     │  │  ├─ test_utils.py
   │     │  │  └─ __init__.py
   │     │  ├─ testing.py
   │     │  ├─ _cloudpickle_wrapper.py
   │     │  ├─ _dask.py
   │     │  ├─ _memmapping_reducer.py
   │     │  ├─ _multiprocessing_helpers.py
   │     │  ├─ _parallel_backends.py
   │     │  ├─ _store_backends.py
   │     │  ├─ _utils.py
   │     │  └─ __init__.py
   │     ├─ joblib-1.4.2.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE.txt
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ langcodes
   │     │  ├─ build_data.py
   │     │  ├─ data
   │     │  │  └─ language-subtag-registry.txt
   │     │  ├─ data_dicts.py
   │     │  ├─ language_distance.py
   │     │  ├─ language_lists.py
   │     │  ├─ py.typed
   │     │  ├─ registry_parser.py
   │     │  ├─ tag_parser.py
   │     │  ├─ tests
   │     │  │  ├─ README.md
   │     │  │  ├─ test_alpha3.py
   │     │  │  ├─ test_issue_59.py
   │     │  │  ├─ test_language.py
   │     │  │  ├─ test_language_data.py
   │     │  │  └─ test_wikt_languages.py
   │     │  ├─ util.py
   │     │  └─ __init__.py
   │     ├─ langcodes-3.5.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE.txt
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ language_data
   │     │  ├─ build_data.py
   │     │  ├─ data
   │     │  │  ├─ extra_language_names.csv
   │     │  │  ├─ language-subtag-registry.txt
   │     │  │  ├─ languageInfo.xml
   │     │  │  ├─ override_language_names.csv
   │     │  │  ├─ supplementalData.xml
   │     │  │  ├─ trie
   │     │  │  │  ├─ ab
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ af
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ agq
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ak
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ am
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ an
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ ang
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ ann
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ apc
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ ar
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ arn
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ as
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ asa
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ast
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ az
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ba
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ bal
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ bas
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ be
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ bem
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ bez
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ bg
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ bgc
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ bgn
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ bho
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ blo
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ blt
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ bm
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ bn
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ bo
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ br
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ brx
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ bs
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ bss
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ byn
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ ca
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ cch
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ ccp
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ce
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ceb
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ cgg
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ cho
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ chr
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ cic
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ckb
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ co
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ cs
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ csw
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ cu
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ cv
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ cy
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ da
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ dav
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ de
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ dje
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ doi
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ dsb
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ dua
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ dyo
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ dz
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ebu
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ee
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ el
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ en
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ eo
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ es
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ et
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ eu
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ewo
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ fa
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ff
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ fi
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ fil
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ fo
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ fr
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ frr
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ fur
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ fy
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ga
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ gaa
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ gd
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ gl
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ gn
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ gsw
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ gu
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ guz
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ gv
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ha
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ haw
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ he
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ hi
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ hil
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ hnj
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ hr
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ hsb
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ hu
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ hy
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ia
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ id
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ie
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ig
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ii
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ilo
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ io
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ is
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ it
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ja
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ jbo
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ jgo
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ jmc
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ jv
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ka
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ kab
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ kaj
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ kam
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ kcg
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ kcm
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ kde
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ kea
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ken
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ kgp
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ khq
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ki
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ kk
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ kkj
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ kl
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ kln
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ km
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ kn
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ko
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ kok
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ kpe
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ ks
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ksb
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ksf
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ksh
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ku
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ kw
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ kxv
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ky
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ la
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ lag
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ lah
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ lb
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ lg
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ lij
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ lkt
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ lmo
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ln
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ lo
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ lrc
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ lt
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ lu
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ luo
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ luy
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ lv
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ mai
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ mas
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ mdf
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ mer
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ mfe
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ mg
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ mgh
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ mgo
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ mi
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ mic
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ mk
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ml
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ mn
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ mni
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ moh
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ mr
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ms
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ mt
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ mua
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ mus
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ my
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ myv
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ mzn
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ nah
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ nan
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ naq
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ nb
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ nd
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ nds
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ne
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ nl
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ nmg
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ nn
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ nnh
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ no
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ nqo
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ nus
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ nv
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ ny
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ nyn
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ oc
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ om
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ or
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ os
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ osa
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ pa
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ pap
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ pcm
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ pis
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ pl
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ prg
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ps
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ pt
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ qu
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ quc
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ raj
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ rhg
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ rif
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ rm
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ rn
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ro
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ rof
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ru
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ rup
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ rw
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ rwk
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ sa
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ sah
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ saq
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ sat
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ sbp
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ sc
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ scn
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ sd
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ sdh
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ se
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ seh
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ses
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ sg
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ sh
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ shi
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ shn
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ si
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ sk
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ skr
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ sl
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ sma
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ smj
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ smn
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ sms
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ sn
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ so
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ sq
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ sr
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ss
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ssy
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ st
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ su
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ sv
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ sw
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ syr
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ szl
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ta
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ te
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ teo
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ tg
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ th
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ti
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ tig
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ tk
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ to
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ tok
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ tpi
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ tr
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ trv
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ trw
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ tt
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ twq
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ tzm
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ug
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ uk
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ und
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ur
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ uz
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ vai
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ ve
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ vec
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ vi
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ vmw
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ vo
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ vun
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ wa
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ wae
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ wbp
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  ├─ wo
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ xh
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ xnr
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ xog
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ yav
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ yi
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ yo
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ yrl
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ yue
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ za
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ zgh
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ zh
   │     │  │  │  │  ├─ name_to_language.marisa
   │     │  │  │  │  ├─ name_to_script.marisa
   │     │  │  │  │  └─ name_to_territory.marisa
   │     │  │  │  ├─ zsm
   │     │  │  │  │  └─ name_to_language.marisa
   │     │  │  │  └─ zu
   │     │  │  │     ├─ name_to_language.marisa
   │     │  │  │     ├─ name_to_script.marisa
   │     │  │  │     └─ name_to_territory.marisa
   │     │  │  └─ wiktionary
   │     │  │     └─ codes-en.csv
   │     │  ├─ language_lists.py
   │     │  ├─ names.py
   │     │  ├─ name_data.py
   │     │  ├─ population_data.py
   │     │  ├─ registry_parser.py
   │     │  ├─ util.py
   │     │  └─ __init__.py
   │     ├─ language_data-1.3.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ lxml
   │     │  ├─ apihelpers.pxi
   │     │  ├─ builder.cp311-win_amd64.pyd
   │     │  ├─ builder.py
   │     │  ├─ classlookup.pxi
   │     │  ├─ cleanup.pxi
   │     │  ├─ cssselect.py
   │     │  ├─ debug.pxi
   │     │  ├─ docloader.pxi
   │     │  ├─ doctestcompare.py
   │     │  ├─ dtd.pxi
   │     │  ├─ ElementInclude.py
   │     │  ├─ etree.cp311-win_amd64.pyd
   │     │  ├─ etree.h
   │     │  ├─ etree.pyx
   │     │  ├─ etree_api.h
   │     │  ├─ extensions.pxi
   │     │  ├─ html
   │     │  │  ├─ builder.py
   │     │  │  ├─ clean.py
   │     │  │  ├─ defs.py
   │     │  │  ├─ diff.cp311-win_amd64.pyd
   │     │  │  ├─ diff.py
   │     │  │  ├─ ElementSoup.py
   │     │  │  ├─ formfill.py
   │     │  │  ├─ html5parser.py
   │     │  │  ├─ soupparser.py
   │     │  │  ├─ usedoctest.py
   │     │  │  ├─ _diffcommand.py
   │     │  │  ├─ _html5builder.py
   │     │  │  ├─ _setmixin.py
   │     │  │  └─ __init__.py
   │     │  ├─ includes
   │     │  │  ├─ c14n.pxd
   │     │  │  ├─ config.pxd
   │     │  │  ├─ dtdvalid.pxd
   │     │  │  ├─ etreepublic.pxd
   │     │  │  ├─ etree_defs.h
   │     │  │  ├─ extlibs
   │     │  │  │  ├─ zconf.h
   │     │  │  │  ├─ zlib.h
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ htmlparser.pxd
   │     │  │  ├─ libexslt
   │     │  │  │  ├─ exslt.h
   │     │  │  │  ├─ exsltconfig.h
   │     │  │  │  ├─ exsltexports.h
   │     │  │  │  ├─ libexslt.h
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ libxml
   │     │  │  │  ├─ c14n.h
   │     │  │  │  ├─ catalog.h
   │     │  │  │  ├─ chvalid.h
   │     │  │  │  ├─ debugXML.h
   │     │  │  │  ├─ dict.h
   │     │  │  │  ├─ encoding.h
   │     │  │  │  ├─ entities.h
   │     │  │  │  ├─ globals.h
   │     │  │  │  ├─ hash.h
   │     │  │  │  ├─ HTMLparser.h
   │     │  │  │  ├─ HTMLtree.h
   │     │  │  │  ├─ list.h
   │     │  │  │  ├─ nanoftp.h
   │     │  │  │  ├─ nanohttp.h
   │     │  │  │  ├─ parser.h
   │     │  │  │  ├─ parserInternals.h
   │     │  │  │  ├─ pattern.h
   │     │  │  │  ├─ relaxng.h
   │     │  │  │  ├─ SAX.h
   │     │  │  │  ├─ SAX2.h
   │     │  │  │  ├─ schemasInternals.h
   │     │  │  │  ├─ schematron.h
   │     │  │  │  ├─ threads.h
   │     │  │  │  ├─ tree.h
   │     │  │  │  ├─ uri.h
   │     │  │  │  ├─ valid.h
   │     │  │  │  ├─ xinclude.h
   │     │  │  │  ├─ xlink.h
   │     │  │  │  ├─ xmlautomata.h
   │     │  │  │  ├─ xmlerror.h
   │     │  │  │  ├─ xmlexports.h
   │     │  │  │  ├─ xmlIO.h
   │     │  │  │  ├─ xmlmemory.h
   │     │  │  │  ├─ xmlmodule.h
   │     │  │  │  ├─ xmlreader.h
   │     │  │  │  ├─ xmlregexp.h
   │     │  │  │  ├─ xmlsave.h
   │     │  │  │  ├─ xmlschemas.h
   │     │  │  │  ├─ xmlschemastypes.h
   │     │  │  │  ├─ xmlstring.h
   │     │  │  │  ├─ xmlunicode.h
   │     │  │  │  ├─ xmlversion.h
   │     │  │  │  ├─ xmlwriter.h
   │     │  │  │  ├─ xpath.h
   │     │  │  │  ├─ xpathInternals.h
   │     │  │  │  ├─ xpointer.h
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ libxslt
   │     │  │  │  ├─ attributes.h
   │     │  │  │  ├─ documents.h
   │     │  │  │  ├─ extensions.h
   │     │  │  │  ├─ extra.h
   │     │  │  │  ├─ functions.h
   │     │  │  │  ├─ imports.h
   │     │  │  │  ├─ keys.h
   │     │  │  │  ├─ libxslt.h
   │     │  │  │  ├─ namespaces.h
   │     │  │  │  ├─ numbersInternals.h
   │     │  │  │  ├─ preproc.h
   │     │  │  │  ├─ security.h
   │     │  │  │  ├─ templates.h
   │     │  │  │  ├─ transform.h
   │     │  │  │  ├─ trio.h
   │     │  │  │  ├─ triodef.h
   │     │  │  │  ├─ variables.h
   │     │  │  │  ├─ win32config.h
   │     │  │  │  ├─ xslt.h
   │     │  │  │  ├─ xsltconfig.h
   │     │  │  │  ├─ xsltexports.h
   │     │  │  │  ├─ xsltInternals.h
   │     │  │  │  ├─ xsltlocale.h
   │     │  │  │  ├─ xsltutils.h
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ lxml-version.h
   │     │  │  ├─ relaxng.pxd
   │     │  │  ├─ schematron.pxd
   │     │  │  ├─ tree.pxd
   │     │  │  ├─ uri.pxd
   │     │  │  ├─ xinclude.pxd
   │     │  │  ├─ xmlerror.pxd
   │     │  │  ├─ xmlparser.pxd
   │     │  │  ├─ xmlschema.pxd
   │     │  │  ├─ xpath.pxd
   │     │  │  ├─ xslt.pxd
   │     │  │  ├─ __init__.pxd
   │     │  │  └─ __init__.py
   │     │  ├─ isoschematron
   │     │  │  ├─ resources
   │     │  │  │  ├─ rng
   │     │  │  │  │  └─ iso-schematron.rng
   │     │  │  │  └─ xsl
   │     │  │  │     ├─ iso-schematron-xslt1
   │     │  │  │     │  ├─ iso_abstract_expand.xsl
   │     │  │  │     │  ├─ iso_dsdl_include.xsl
   │     │  │  │     │  ├─ iso_schematron_message.xsl
   │     │  │  │     │  ├─ iso_schematron_skeleton_for_xslt1.xsl
   │     │  │  │     │  ├─ iso_svrl_for_xslt1.xsl
   │     │  │  │     │  └─ readme.txt
   │     │  │  │     ├─ RNG2Schtrn.xsl
   │     │  │  │     └─ XSD2Schtrn.xsl
   │     │  │  └─ __init__.py
   │     │  ├─ iterparse.pxi
   │     │  ├─ lxml.etree.h
   │     │  ├─ lxml.etree_api.h
   │     │  ├─ nsclasses.pxi
   │     │  ├─ objectify.cp311-win_amd64.pyd
   │     │  ├─ objectify.pyx
   │     │  ├─ objectpath.pxi
   │     │  ├─ parser.pxi
   │     │  ├─ parsertarget.pxi
   │     │  ├─ proxy.pxi
   │     │  ├─ public-api.pxi
   │     │  ├─ pyclasslookup.py
   │     │  ├─ readonlytree.pxi
   │     │  ├─ relaxng.pxi
   │     │  ├─ sax.cp311-win_amd64.pyd
   │     │  ├─ sax.py
   │     │  ├─ saxparser.pxi
   │     │  ├─ schematron.pxi
   │     │  ├─ serializer.pxi
   │     │  ├─ usedoctest.py
   │     │  ├─ xinclude.pxi
   │     │  ├─ xmlerror.pxi
   │     │  ├─ xmlid.pxi
   │     │  ├─ xmlschema.pxi
   │     │  ├─ xpath.pxi
   │     │  ├─ xslt.pxi
   │     │  ├─ xsltext.pxi
   │     │  ├─ _elementpath.cp311-win_amd64.pyd
   │     │  ├─ _elementpath.py
   │     │  └─ __init__.py
   │     ├─ lxml-5.3.1.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE.txt
   │     │  ├─ LICENSES.txt
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ marisa_trie-1.2.1.dist-info
   │     │  ├─ AUTHORS.rst
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ marisa_trie.cp311-win_amd64.pyd
   │     ├─ markdown_it
   │     │  ├─ cli
   │     │  │  ├─ parse.py
   │     │  │  └─ __init__.py
   │     │  ├─ common
   │     │  │  ├─ entities.py
   │     │  │  ├─ html_blocks.py
   │     │  │  ├─ html_re.py
   │     │  │  ├─ normalize_url.py
   │     │  │  ├─ utils.py
   │     │  │  └─ __init__.py
   │     │  ├─ helpers
   │     │  │  ├─ parse_link_destination.py
   │     │  │  ├─ parse_link_label.py
   │     │  │  ├─ parse_link_title.py
   │     │  │  └─ __init__.py
   │     │  ├─ main.py
   │     │  ├─ parser_block.py
   │     │  ├─ parser_core.py
   │     │  ├─ parser_inline.py
   │     │  ├─ port.yaml
   │     │  ├─ presets
   │     │  │  ├─ commonmark.py
   │     │  │  ├─ default.py
   │     │  │  ├─ zero.py
   │     │  │  └─ __init__.py
   │     │  ├─ py.typed
   │     │  ├─ renderer.py
   │     │  ├─ ruler.py
   │     │  ├─ rules_block
   │     │  │  ├─ blockquote.py
   │     │  │  ├─ code.py
   │     │  │  ├─ fence.py
   │     │  │  ├─ heading.py
   │     │  │  ├─ hr.py
   │     │  │  ├─ html_block.py
   │     │  │  ├─ lheading.py
   │     │  │  ├─ list.py
   │     │  │  ├─ paragraph.py
   │     │  │  ├─ reference.py
   │     │  │  ├─ state_block.py
   │     │  │  ├─ table.py
   │     │  │  └─ __init__.py
   │     │  ├─ rules_core
   │     │  │  ├─ block.py
   │     │  │  ├─ inline.py
   │     │  │  ├─ linkify.py
   │     │  │  ├─ normalize.py
   │     │  │  ├─ replacements.py
   │     │  │  ├─ smartquotes.py
   │     │  │  ├─ state_core.py
   │     │  │  ├─ text_join.py
   │     │  │  └─ __init__.py
   │     │  ├─ rules_inline
   │     │  │  ├─ autolink.py
   │     │  │  ├─ backticks.py
   │     │  │  ├─ balance_pairs.py
   │     │  │  ├─ emphasis.py
   │     │  │  ├─ entity.py
   │     │  │  ├─ escape.py
   │     │  │  ├─ fragments_join.py
   │     │  │  ├─ html_inline.py
   │     │  │  ├─ image.py
   │     │  │  ├─ link.py
   │     │  │  ├─ linkify.py
   │     │  │  ├─ newline.py
   │     │  │  ├─ state_inline.py
   │     │  │  ├─ strikethrough.py
   │     │  │  ├─ text.py
   │     │  │  └─ __init__.py
   │     │  ├─ token.py
   │     │  ├─ tree.py
   │     │  ├─ utils.py
   │     │  ├─ _compat.py
   │     │  ├─ _punycode.py
   │     │  └─ __init__.py
   │     ├─ markdown_it_py-3.0.0.dist-info
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ LICENSE.markdown-it
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  └─ WHEEL
   │     ├─ markupsafe
   │     │  ├─ py.typed
   │     │  ├─ _native.py
   │     │  ├─ _speedups.c
   │     │  ├─ _speedups.cp311-win_amd64.pyd
   │     │  ├─ _speedups.pyi
   │     │  └─ __init__.py
   │     ├─ MarkupSafe-3.0.2.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE.txt
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ mdurl
   │     │  ├─ py.typed
   │     │  ├─ _decode.py
   │     │  ├─ _encode.py
   │     │  ├─ _format.py
   │     │  ├─ _parse.py
   │     │  ├─ _url.py
   │     │  └─ __init__.py
   │     ├─ mdurl-0.1.2.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  └─ WHEEL
   │     ├─ murmurhash
   │     │  ├─ about.py
   │     │  ├─ include
   │     │  │  └─ murmurhash
   │     │  │     ├─ MurmurHash2.h
   │     │  │     └─ MurmurHash3.h
   │     │  ├─ mrmr.cp311-win_amd64.pyd
   │     │  ├─ mrmr.pxd
   │     │  ├─ mrmr.pyx
   │     │  ├─ tests
   │     │  │  ├─ test_hash.py
   │     │  │  ├─ test_import.py
   │     │  │  └─ __init__.py
   │     │  ├─ __init__.pxd
   │     │  └─ __init__.py
   │     ├─ murmurhash-1.0.12.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ nltk
   │     │  ├─ app
   │     │  │  ├─ chartparser_app.py
   │     │  │  ├─ chunkparser_app.py
   │     │  │  ├─ collocations_app.py
   │     │  │  ├─ concordance_app.py
   │     │  │  ├─ nemo_app.py
   │     │  │  ├─ rdparser_app.py
   │     │  │  ├─ srparser_app.py
   │     │  │  ├─ wordfreq_app.py
   │     │  │  ├─ wordnet_app.py
   │     │  │  └─ __init__.py
   │     │  ├─ book.py
   │     │  ├─ ccg
   │     │  │  ├─ api.py
   │     │  │  ├─ chart.py
   │     │  │  ├─ combinator.py
   │     │  │  ├─ lexicon.py
   │     │  │  ├─ logic.py
   │     │  │  └─ __init__.py
   │     │  ├─ chat
   │     │  │  ├─ eliza.py
   │     │  │  ├─ iesha.py
   │     │  │  ├─ rude.py
   │     │  │  ├─ suntsu.py
   │     │  │  ├─ util.py
   │     │  │  ├─ zen.py
   │     │  │  └─ __init__.py
   │     │  ├─ chunk
   │     │  │  ├─ api.py
   │     │  │  ├─ named_entity.py
   │     │  │  ├─ regexp.py
   │     │  │  ├─ util.py
   │     │  │  └─ __init__.py
   │     │  ├─ classify
   │     │  │  ├─ api.py
   │     │  │  ├─ decisiontree.py
   │     │  │  ├─ maxent.py
   │     │  │  ├─ megam.py
   │     │  │  ├─ naivebayes.py
   │     │  │  ├─ positivenaivebayes.py
   │     │  │  ├─ rte_classify.py
   │     │  │  ├─ scikitlearn.py
   │     │  │  ├─ senna.py
   │     │  │  ├─ svm.py
   │     │  │  ├─ tadm.py
   │     │  │  ├─ textcat.py
   │     │  │  ├─ util.py
   │     │  │  ├─ weka.py
   │     │  │  └─ __init__.py
   │     │  ├─ cli.py
   │     │  ├─ cluster
   │     │  │  ├─ api.py
   │     │  │  ├─ em.py
   │     │  │  ├─ gaac.py
   │     │  │  ├─ kmeans.py
   │     │  │  ├─ util.py
   │     │  │  └─ __init__.py
   │     │  ├─ collections.py
   │     │  ├─ collocations.py
   │     │  ├─ compat.py
   │     │  ├─ corpus
   │     │  │  ├─ europarl_raw.py
   │     │  │  ├─ reader
   │     │  │  │  ├─ aligned.py
   │     │  │  │  ├─ api.py
   │     │  │  │  ├─ bcp47.py
   │     │  │  │  ├─ bnc.py
   │     │  │  │  ├─ bracket_parse.py
   │     │  │  │  ├─ categorized_sents.py
   │     │  │  │  ├─ chasen.py
   │     │  │  │  ├─ childes.py
   │     │  │  │  ├─ chunked.py
   │     │  │  │  ├─ cmudict.py
   │     │  │  │  ├─ comparative_sents.py
   │     │  │  │  ├─ conll.py
   │     │  │  │  ├─ crubadan.py
   │     │  │  │  ├─ dependency.py
   │     │  │  │  ├─ framenet.py
   │     │  │  │  ├─ ieer.py
   │     │  │  │  ├─ indian.py
   │     │  │  │  ├─ ipipan.py
   │     │  │  │  ├─ knbc.py
   │     │  │  │  ├─ lin.py
   │     │  │  │  ├─ markdown.py
   │     │  │  │  ├─ mte.py
   │     │  │  │  ├─ nkjp.py
   │     │  │  │  ├─ nombank.py
   │     │  │  │  ├─ nps_chat.py
   │     │  │  │  ├─ opinion_lexicon.py
   │     │  │  │  ├─ panlex_lite.py
   │     │  │  │  ├─ panlex_swadesh.py
   │     │  │  │  ├─ pl196x.py
   │     │  │  │  ├─ plaintext.py
   │     │  │  │  ├─ ppattach.py
   │     │  │  │  ├─ propbank.py
   │     │  │  │  ├─ pros_cons.py
   │     │  │  │  ├─ reviews.py
   │     │  │  │  ├─ rte.py
   │     │  │  │  ├─ semcor.py
   │     │  │  │  ├─ senseval.py
   │     │  │  │  ├─ sentiwordnet.py
   │     │  │  │  ├─ sinica_treebank.py
   │     │  │  │  ├─ string_category.py
   │     │  │  │  ├─ switchboard.py
   │     │  │  │  ├─ tagged.py
   │     │  │  │  ├─ timit.py
   │     │  │  │  ├─ toolbox.py
   │     │  │  │  ├─ twitter.py
   │     │  │  │  ├─ udhr.py
   │     │  │  │  ├─ util.py
   │     │  │  │  ├─ verbnet.py
   │     │  │  │  ├─ wordlist.py
   │     │  │  │  ├─ wordnet.py
   │     │  │  │  ├─ xmldocs.py
   │     │  │  │  ├─ ycoe.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ util.py
   │     │  │  └─ __init__.py
   │     │  ├─ data.py
   │     │  ├─ decorators.py
   │     │  ├─ downloader.py
   │     │  ├─ draw
   │     │  │  ├─ cfg.py
   │     │  │  ├─ dispersion.py
   │     │  │  ├─ table.py
   │     │  │  ├─ tree.py
   │     │  │  ├─ util.py
   │     │  │  └─ __init__.py
   │     │  ├─ featstruct.py
   │     │  ├─ grammar.py
   │     │  ├─ help.py
   │     │  ├─ inference
   │     │  │  ├─ api.py
   │     │  │  ├─ discourse.py
   │     │  │  ├─ mace.py
   │     │  │  ├─ nonmonotonic.py
   │     │  │  ├─ prover9.py
   │     │  │  ├─ resolution.py
   │     │  │  ├─ tableau.py
   │     │  │  └─ __init__.py
   │     │  ├─ internals.py
   │     │  ├─ jsontags.py
   │     │  ├─ langnames.py
   │     │  ├─ lazyimport.py
   │     │  ├─ lm
   │     │  │  ├─ api.py
   │     │  │  ├─ counter.py
   │     │  │  ├─ models.py
   │     │  │  ├─ preprocessing.py
   │     │  │  ├─ smoothing.py
   │     │  │  ├─ util.py
   │     │  │  ├─ vocabulary.py
   │     │  │  └─ __init__.py
   │     │  ├─ metrics
   │     │  │  ├─ agreement.py
   │     │  │  ├─ aline.py
   │     │  │  ├─ association.py
   │     │  │  ├─ confusionmatrix.py
   │     │  │  ├─ distance.py
   │     │  │  ├─ paice.py
   │     │  │  ├─ scores.py
   │     │  │  ├─ segmentation.py
   │     │  │  ├─ spearman.py
   │     │  │  └─ __init__.py
   │     │  ├─ misc
   │     │  │  ├─ babelfish.py
   │     │  │  ├─ chomsky.py
   │     │  │  ├─ minimalset.py
   │     │  │  ├─ sort.py
   │     │  │  ├─ wordfinder.py
   │     │  │  └─ __init__.py
   │     │  ├─ parse
   │     │  │  ├─ api.py
   │     │  │  ├─ bllip.py
   │     │  │  ├─ chart.py
   │     │  │  ├─ corenlp.py
   │     │  │  ├─ dependencygraph.py
   │     │  │  ├─ earleychart.py
   │     │  │  ├─ evaluate.py
   │     │  │  ├─ featurechart.py
   │     │  │  ├─ generate.py
   │     │  │  ├─ malt.py
   │     │  │  ├─ nonprojectivedependencyparser.py
   │     │  │  ├─ pchart.py
   │     │  │  ├─ projectivedependencyparser.py
   │     │  │  ├─ recursivedescent.py
   │     │  │  ├─ shiftreduce.py
   │     │  │  ├─ stanford.py
   │     │  │  ├─ transitionparser.py
   │     │  │  ├─ util.py
   │     │  │  ├─ viterbi.py
   │     │  │  └─ __init__.py
   │     │  ├─ probability.py
   │     │  ├─ sem
   │     │  │  ├─ boxer.py
   │     │  │  ├─ chat80.py
   │     │  │  ├─ cooper_storage.py
   │     │  │  ├─ drt.py
   │     │  │  ├─ drt_glue_demo.py
   │     │  │  ├─ evaluate.py
   │     │  │  ├─ glue.py
   │     │  │  ├─ hole.py
   │     │  │  ├─ lfg.py
   │     │  │  ├─ linearlogic.py
   │     │  │  ├─ logic.py
   │     │  │  ├─ relextract.py
   │     │  │  ├─ skolemize.py
   │     │  │  ├─ util.py
   │     │  │  └─ __init__.py
   │     │  ├─ sentiment
   │     │  │  ├─ sentiment_analyzer.py
   │     │  │  ├─ util.py
   │     │  │  ├─ vader.py
   │     │  │  └─ __init__.py
   │     │  ├─ stem
   │     │  │  ├─ api.py
   │     │  │  ├─ arlstem.py
   │     │  │  ├─ arlstem2.py
   │     │  │  ├─ cistem.py
   │     │  │  ├─ isri.py
   │     │  │  ├─ lancaster.py
   │     │  │  ├─ porter.py
   │     │  │  ├─ regexp.py
   │     │  │  ├─ rslp.py
   │     │  │  ├─ snowball.py
   │     │  │  ├─ util.py
   │     │  │  ├─ wordnet.py
   │     │  │  └─ __init__.py
   │     │  ├─ tabdata.py
   │     │  ├─ tag
   │     │  │  ├─ api.py
   │     │  │  ├─ brill.py
   │     │  │  ├─ brill_trainer.py
   │     │  │  ├─ crf.py
   │     │  │  ├─ hmm.py
   │     │  │  ├─ hunpos.py
   │     │  │  ├─ mapping.py
   │     │  │  ├─ perceptron.py
   │     │  │  ├─ senna.py
   │     │  │  ├─ sequential.py
   │     │  │  ├─ stanford.py
   │     │  │  ├─ tnt.py
   │     │  │  ├─ util.py
   │     │  │  └─ __init__.py
   │     │  ├─ tbl
   │     │  │  ├─ api.py
   │     │  │  ├─ demo.py
   │     │  │  ├─ erroranalysis.py
   │     │  │  ├─ feature.py
   │     │  │  ├─ rule.py
   │     │  │  ├─ template.py
   │     │  │  └─ __init__.py
   │     │  ├─ test
   │     │  │  ├─ all.py
   │     │  │  ├─ bleu.doctest
   │     │  │  ├─ bnc.doctest
   │     │  │  ├─ ccg.doctest
   │     │  │  ├─ ccg_semantics.doctest
   │     │  │  ├─ chat80.doctest
   │     │  │  ├─ childes.doctest
   │     │  │  ├─ childes_fixt.py
   │     │  │  ├─ chunk.doctest
   │     │  │  ├─ classify.doctest
   │     │  │  ├─ classify_fixt.py
   │     │  │  ├─ collections.doctest
   │     │  │  ├─ collocations.doctest
   │     │  │  ├─ concordance.doctest
   │     │  │  ├─ conftest.py
   │     │  │  ├─ corpus.doctest
   │     │  │  ├─ crubadan.doctest
   │     │  │  ├─ data.doctest
   │     │  │  ├─ dependency.doctest
   │     │  │  ├─ discourse.doctest
   │     │  │  ├─ drt.doctest
   │     │  │  ├─ featgram.doctest
   │     │  │  ├─ featstruct.doctest
   │     │  │  ├─ framenet.doctest
   │     │  │  ├─ generate.doctest
   │     │  │  ├─ gensim.doctest
   │     │  │  ├─ gensim_fixt.py
   │     │  │  ├─ gluesemantics.doctest
   │     │  │  ├─ gluesemantics_malt.doctest
   │     │  │  ├─ gluesemantics_malt_fixt.py
   │     │  │  ├─ grammar.doctest
   │     │  │  ├─ grammartestsuites.doctest
   │     │  │  ├─ index.doctest
   │     │  │  ├─ inference.doctest
   │     │  │  ├─ internals.doctest
   │     │  │  ├─ japanese.doctest
   │     │  │  ├─ lm.doctest
   │     │  │  ├─ logic.doctest
   │     │  │  ├─ meteor.doctest
   │     │  │  ├─ metrics.doctest
   │     │  │  ├─ misc.doctest
   │     │  │  ├─ nonmonotonic.doctest
   │     │  │  ├─ paice.doctest
   │     │  │  ├─ parse.doctest
   │     │  │  ├─ portuguese_en.doctest
   │     │  │  ├─ portuguese_en_fixt.py
   │     │  │  ├─ probability.doctest
   │     │  │  ├─ probability_fixt.py
   │     │  │  ├─ propbank.doctest
   │     │  │  ├─ relextract.doctest
   │     │  │  ├─ resolution.doctest
   │     │  │  ├─ semantics.doctest
   │     │  │  ├─ sentiment.doctest
   │     │  │  ├─ sentiwordnet.doctest
   │     │  │  ├─ setup_fixt.py
   │     │  │  ├─ simple.doctest
   │     │  │  ├─ stem.doctest
   │     │  │  ├─ tag.doctest
   │     │  │  ├─ tokenize.doctest
   │     │  │  ├─ toolbox.doctest
   │     │  │  ├─ translate.doctest
   │     │  │  ├─ tree.doctest
   │     │  │  ├─ treeprettyprinter.doctest
   │     │  │  ├─ treetransforms.doctest
   │     │  │  ├─ unit
   │     │  │  │  ├─ lm
   │     │  │  │  │  ├─ test_counter.py
   │     │  │  │  │  ├─ test_models.py
   │     │  │  │  │  ├─ test_preprocessing.py
   │     │  │  │  │  ├─ test_vocabulary.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_aline.py
   │     │  │  │  ├─ test_bllip.py
   │     │  │  │  ├─ test_brill.py
   │     │  │  │  ├─ test_cfd_mutation.py
   │     │  │  │  ├─ test_cfg2chomsky.py
   │     │  │  │  ├─ test_chunk.py
   │     │  │  │  ├─ test_classify.py
   │     │  │  │  ├─ test_collocations.py
   │     │  │  │  ├─ test_concordance.py
   │     │  │  │  ├─ test_corenlp.py
   │     │  │  │  ├─ test_corpora.py
   │     │  │  │  ├─ test_corpus_views.py
   │     │  │  │  ├─ test_data.py
   │     │  │  │  ├─ test_disagreement.py
   │     │  │  │  ├─ test_distance.py
   │     │  │  │  ├─ test_downloader.py
   │     │  │  │  ├─ test_freqdist.py
   │     │  │  │  ├─ test_hmm.py
   │     │  │  │  ├─ test_json2csv_corpus.py
   │     │  │  │  ├─ test_json_serialization.py
   │     │  │  │  ├─ test_metrics.py
   │     │  │  │  ├─ test_naivebayes.py
   │     │  │  │  ├─ test_nombank.py
   │     │  │  │  ├─ test_pl196x.py
   │     │  │  │  ├─ test_pos_tag.py
   │     │  │  │  ├─ test_ribes.py
   │     │  │  │  ├─ test_rte_classify.py
   │     │  │  │  ├─ test_seekable_unicode_stream_reader.py
   │     │  │  │  ├─ test_senna.py
   │     │  │  │  ├─ test_stem.py
   │     │  │  │  ├─ test_tag.py
   │     │  │  │  ├─ test_tgrep.py
   │     │  │  │  ├─ test_tokenize.py
   │     │  │  │  ├─ test_twitter_auth.py
   │     │  │  │  ├─ test_util.py
   │     │  │  │  ├─ test_wordnet.py
   │     │  │  │  ├─ translate
   │     │  │  │  │  ├─ test_bleu.py
   │     │  │  │  │  ├─ test_gdfa.py
   │     │  │  │  │  ├─ test_ibm1.py
   │     │  │  │  │  ├─ test_ibm2.py
   │     │  │  │  │  ├─ test_ibm3.py
   │     │  │  │  │  ├─ test_ibm4.py
   │     │  │  │  │  ├─ test_ibm5.py
   │     │  │  │  │  ├─ test_ibm_model.py
   │     │  │  │  │  ├─ test_meteor.py
   │     │  │  │  │  ├─ test_nist.py
   │     │  │  │  │  ├─ test_stack_decoder.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ util.doctest
   │     │  │  ├─ wordnet.doctest
   │     │  │  ├─ wordnet_lch.doctest
   │     │  │  ├─ wsd.doctest
   │     │  │  └─ __init__.py
   │     │  ├─ text.py
   │     │  ├─ tgrep.py
   │     │  ├─ tokenize
   │     │  │  ├─ api.py
   │     │  │  ├─ casual.py
   │     │  │  ├─ destructive.py
   │     │  │  ├─ legality_principle.py
   │     │  │  ├─ mwe.py
   │     │  │  ├─ nist.py
   │     │  │  ├─ punkt.py
   │     │  │  ├─ regexp.py
   │     │  │  ├─ repp.py
   │     │  │  ├─ sexpr.py
   │     │  │  ├─ simple.py
   │     │  │  ├─ sonority_sequencing.py
   │     │  │  ├─ stanford.py
   │     │  │  ├─ stanford_segmenter.py
   │     │  │  ├─ texttiling.py
   │     │  │  ├─ toktok.py
   │     │  │  ├─ treebank.py
   │     │  │  ├─ util.py
   │     │  │  └─ __init__.py
   │     │  ├─ toolbox.py
   │     │  ├─ translate
   │     │  │  ├─ api.py
   │     │  │  ├─ bleu_score.py
   │     │  │  ├─ chrf_score.py
   │     │  │  ├─ gale_church.py
   │     │  │  ├─ gdfa.py
   │     │  │  ├─ gleu_score.py
   │     │  │  ├─ ibm1.py
   │     │  │  ├─ ibm2.py
   │     │  │  ├─ ibm3.py
   │     │  │  ├─ ibm4.py
   │     │  │  ├─ ibm5.py
   │     │  │  ├─ ibm_model.py
   │     │  │  ├─ meteor_score.py
   │     │  │  ├─ metrics.py
   │     │  │  ├─ nist_score.py
   │     │  │  ├─ phrase_based.py
   │     │  │  ├─ ribes_score.py
   │     │  │  ├─ stack_decoder.py
   │     │  │  └─ __init__.py
   │     │  ├─ tree
   │     │  │  ├─ immutable.py
   │     │  │  ├─ parented.py
   │     │  │  ├─ parsing.py
   │     │  │  ├─ prettyprinter.py
   │     │  │  ├─ probabilistic.py
   │     │  │  ├─ transforms.py
   │     │  │  ├─ tree.py
   │     │  │  └─ __init__.py
   │     │  ├─ treeprettyprinter.py
   │     │  ├─ treetransforms.py
   │     │  ├─ twitter
   │     │  │  ├─ api.py
   │     │  │  ├─ common.py
   │     │  │  ├─ twitterclient.py
   │     │  │  ├─ twitter_demo.py
   │     │  │  ├─ util.py
   │     │  │  └─ __init__.py
   │     │  ├─ util.py
   │     │  ├─ VERSION
   │     │  ├─ wsd.py
   │     │  └─ __init__.py
   │     ├─ nltk-3.9.1.dist-info
   │     │  ├─ AUTHORS.md
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE.txt
   │     │  ├─ METADATA
   │     │  ├─ README.md
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ numpy
   │     │  ├─ char
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ compat
   │     │  │  ├─ py3k.py
   │     │  │  ├─ tests
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ conftest.py
   │     │  ├─ core
   │     │  │  ├─ arrayprint.py
   │     │  │  ├─ defchararray.py
   │     │  │  ├─ einsumfunc.py
   │     │  │  ├─ fromnumeric.py
   │     │  │  ├─ function_base.py
   │     │  │  ├─ getlimits.py
   │     │  │  ├─ multiarray.py
   │     │  │  ├─ numeric.py
   │     │  │  ├─ numerictypes.py
   │     │  │  ├─ overrides.py
   │     │  │  ├─ records.py
   │     │  │  ├─ shape_base.py
   │     │  │  ├─ umath.py
   │     │  │  ├─ _dtype.py
   │     │  │  ├─ _dtype_ctypes.py
   │     │  │  ├─ _internal.py
   │     │  │  ├─ _multiarray_umath.py
   │     │  │  ├─ _utils.py
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ ctypeslib.py
   │     │  ├─ ctypeslib.pyi
   │     │  ├─ distutils
   │     │  │  ├─ armccompiler.py
   │     │  │  ├─ ccompiler.py
   │     │  │  ├─ ccompiler_opt.py
   │     │  │  ├─ checks
   │     │  │  │  ├─ cpu_asimd.c
   │     │  │  │  ├─ cpu_asimddp.c
   │     │  │  │  ├─ cpu_asimdfhm.c
   │     │  │  │  ├─ cpu_asimdhp.c
   │     │  │  │  ├─ cpu_avx.c
   │     │  │  │  ├─ cpu_avx2.c
   │     │  │  │  ├─ cpu_avx512cd.c
   │     │  │  │  ├─ cpu_avx512f.c
   │     │  │  │  ├─ cpu_avx512_clx.c
   │     │  │  │  ├─ cpu_avx512_cnl.c
   │     │  │  │  ├─ cpu_avx512_icl.c
   │     │  │  │  ├─ cpu_avx512_knl.c
   │     │  │  │  ├─ cpu_avx512_knm.c
   │     │  │  │  ├─ cpu_avx512_skx.c
   │     │  │  │  ├─ cpu_avx512_spr.c
   │     │  │  │  ├─ cpu_f16c.c
   │     │  │  │  ├─ cpu_fma3.c
   │     │  │  │  ├─ cpu_fma4.c
   │     │  │  │  ├─ cpu_neon.c
   │     │  │  │  ├─ cpu_neon_fp16.c
   │     │  │  │  ├─ cpu_neon_vfpv4.c
   │     │  │  │  ├─ cpu_popcnt.c
   │     │  │  │  ├─ cpu_rvv.c
   │     │  │  │  ├─ cpu_sse.c
   │     │  │  │  ├─ cpu_sse2.c
   │     │  │  │  ├─ cpu_sse3.c
   │     │  │  │  ├─ cpu_sse41.c
   │     │  │  │  ├─ cpu_sse42.c
   │     │  │  │  ├─ cpu_ssse3.c
   │     │  │  │  ├─ cpu_sve.c
   │     │  │  │  ├─ cpu_vsx.c
   │     │  │  │  ├─ cpu_vsx2.c
   │     │  │  │  ├─ cpu_vsx3.c
   │     │  │  │  ├─ cpu_vsx4.c
   │     │  │  │  ├─ cpu_vx.c
   │     │  │  │  ├─ cpu_vxe.c
   │     │  │  │  ├─ cpu_vxe2.c
   │     │  │  │  ├─ cpu_xop.c
   │     │  │  │  ├─ extra_avx512bw_mask.c
   │     │  │  │  ├─ extra_avx512dq_mask.c
   │     │  │  │  ├─ extra_avx512f_reduce.c
   │     │  │  │  ├─ extra_vsx3_half_double.c
   │     │  │  │  ├─ extra_vsx4_mma.c
   │     │  │  │  ├─ extra_vsx_asm.c
   │     │  │  │  └─ test_flags.c
   │     │  │  ├─ command
   │     │  │  │  ├─ autodist.py
   │     │  │  │  ├─ bdist_rpm.py
   │     │  │  │  ├─ build.py
   │     │  │  │  ├─ build_clib.py
   │     │  │  │  ├─ build_ext.py
   │     │  │  │  ├─ build_py.py
   │     │  │  │  ├─ build_scripts.py
   │     │  │  │  ├─ build_src.py
   │     │  │  │  ├─ config.py
   │     │  │  │  ├─ config_compiler.py
   │     │  │  │  ├─ develop.py
   │     │  │  │  ├─ egg_info.py
   │     │  │  │  ├─ install.py
   │     │  │  │  ├─ install_clib.py
   │     │  │  │  ├─ install_data.py
   │     │  │  │  ├─ install_headers.py
   │     │  │  │  ├─ sdist.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ conv_template.py
   │     │  │  ├─ core.py
   │     │  │  ├─ cpuinfo.py
   │     │  │  ├─ exec_command.py
   │     │  │  ├─ extension.py
   │     │  │  ├─ fcompiler
   │     │  │  │  ├─ absoft.py
   │     │  │  │  ├─ arm.py
   │     │  │  │  ├─ compaq.py
   │     │  │  │  ├─ environment.py
   │     │  │  │  ├─ fujitsu.py
   │     │  │  │  ├─ g95.py
   │     │  │  │  ├─ gnu.py
   │     │  │  │  ├─ hpux.py
   │     │  │  │  ├─ ibm.py
   │     │  │  │  ├─ intel.py
   │     │  │  │  ├─ lahey.py
   │     │  │  │  ├─ mips.py
   │     │  │  │  ├─ nag.py
   │     │  │  │  ├─ none.py
   │     │  │  │  ├─ nv.py
   │     │  │  │  ├─ pathf95.py
   │     │  │  │  ├─ pg.py
   │     │  │  │  ├─ sun.py
   │     │  │  │  ├─ vast.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ from_template.py
   │     │  │  ├─ fujitsuccompiler.py
   │     │  │  ├─ intelccompiler.py
   │     │  │  ├─ lib2def.py
   │     │  │  ├─ line_endings.py
   │     │  │  ├─ log.py
   │     │  │  ├─ mingw
   │     │  │  │  └─ gfortran_vs2003_hack.c
   │     │  │  ├─ mingw32ccompiler.py
   │     │  │  ├─ misc_util.py
   │     │  │  ├─ msvc9compiler.py
   │     │  │  ├─ msvccompiler.py
   │     │  │  ├─ npy_pkg_config.py
   │     │  │  ├─ numpy_distribution.py
   │     │  │  ├─ pathccompiler.py
   │     │  │  ├─ system_info.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_build_ext.py
   │     │  │  │  ├─ test_ccompiler_opt.py
   │     │  │  │  ├─ test_ccompiler_opt_conf.py
   │     │  │  │  ├─ test_exec_command.py
   │     │  │  │  ├─ test_fcompiler.py
   │     │  │  │  ├─ test_fcompiler_gnu.py
   │     │  │  │  ├─ test_fcompiler_intel.py
   │     │  │  │  ├─ test_fcompiler_nagfor.py
   │     │  │  │  ├─ test_from_template.py
   │     │  │  │  ├─ test_log.py
   │     │  │  │  ├─ test_mingw32ccompiler.py
   │     │  │  │  ├─ test_misc_util.py
   │     │  │  │  ├─ test_npy_pkg_config.py
   │     │  │  │  ├─ test_shell_utils.py
   │     │  │  │  ├─ test_system_info.py
   │     │  │  │  ├─ utilities.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ unixccompiler.py
   │     │  │  ├─ _shell_utils.py
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ doc
   │     │  │  └─ ufuncs.py
   │     │  ├─ dtypes.py
   │     │  ├─ dtypes.pyi
   │     │  ├─ exceptions.py
   │     │  ├─ exceptions.pyi
   │     │  ├─ f2py
   │     │  │  ├─ auxfuncs.py
   │     │  │  ├─ capi_maps.py
   │     │  │  ├─ cb_rules.py
   │     │  │  ├─ cfuncs.py
   │     │  │  ├─ common_rules.py
   │     │  │  ├─ crackfortran.py
   │     │  │  ├─ diagnose.py
   │     │  │  ├─ f2py2e.py
   │     │  │  ├─ f90mod_rules.py
   │     │  │  ├─ func2subr.py
   │     │  │  ├─ rules.py
   │     │  │  ├─ setup.cfg
   │     │  │  ├─ src
   │     │  │  │  ├─ fortranobject.c
   │     │  │  │  └─ fortranobject.h
   │     │  │  ├─ symbolic.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ src
   │     │  │  │  │  ├─ abstract_interface
   │     │  │  │  │  │  ├─ foo.f90
   │     │  │  │  │  │  └─ gh18403_mod.f90
   │     │  │  │  │  ├─ array_from_pyobj
   │     │  │  │  │  │  └─ wrapmodule.c
   │     │  │  │  │  ├─ assumed_shape
   │     │  │  │  │  │  ├─ .f2py_f2cmap
   │     │  │  │  │  │  ├─ foo_free.f90
   │     │  │  │  │  │  ├─ foo_mod.f90
   │     │  │  │  │  │  ├─ foo_use.f90
   │     │  │  │  │  │  └─ precision.f90
   │     │  │  │  │  ├─ block_docstring
   │     │  │  │  │  │  └─ foo.f
   │     │  │  │  │  ├─ callback
   │     │  │  │  │  │  ├─ foo.f
   │     │  │  │  │  │  ├─ gh17797.f90
   │     │  │  │  │  │  ├─ gh18335.f90
   │     │  │  │  │  │  ├─ gh25211.f
   │     │  │  │  │  │  ├─ gh25211.pyf
   │     │  │  │  │  │  └─ gh26681.f90
   │     │  │  │  │  ├─ cli
   │     │  │  │  │  │  ├─ gh_22819.pyf
   │     │  │  │  │  │  ├─ hi77.f
   │     │  │  │  │  │  └─ hiworld.f90
   │     │  │  │  │  ├─ common
   │     │  │  │  │  │  ├─ block.f
   │     │  │  │  │  │  └─ gh19161.f90
   │     │  │  │  │  ├─ crackfortran
   │     │  │  │  │  │  ├─ accesstype.f90
   │     │  │  │  │  │  ├─ data_common.f
   │     │  │  │  │  │  ├─ data_multiplier.f
   │     │  │  │  │  │  ├─ data_stmts.f90
   │     │  │  │  │  │  ├─ data_with_comments.f
   │     │  │  │  │  │  ├─ foo_deps.f90
   │     │  │  │  │  │  ├─ gh15035.f
   │     │  │  │  │  │  ├─ gh17859.f
   │     │  │  │  │  │  ├─ gh22648.pyf
   │     │  │  │  │  │  ├─ gh23533.f
   │     │  │  │  │  │  ├─ gh23598.f90
   │     │  │  │  │  │  ├─ gh23598Warn.f90
   │     │  │  │  │  │  ├─ gh23879.f90
   │     │  │  │  │  │  ├─ gh27697.f90
   │     │  │  │  │  │  ├─ gh2848.f90
   │     │  │  │  │  │  ├─ operators.f90
   │     │  │  │  │  │  ├─ privatemod.f90
   │     │  │  │  │  │  ├─ publicmod.f90
   │     │  │  │  │  │  ├─ pubprivmod.f90
   │     │  │  │  │  │  └─ unicode_comment.f90
   │     │  │  │  │  ├─ f2cmap
   │     │  │  │  │  │  ├─ .f2py_f2cmap
   │     │  │  │  │  │  └─ isoFortranEnvMap.f90
   │     │  │  │  │  ├─ isocintrin
   │     │  │  │  │  │  └─ isoCtests.f90
   │     │  │  │  │  ├─ kind
   │     │  │  │  │  │  └─ foo.f90
   │     │  │  │  │  ├─ mixed
   │     │  │  │  │  │  ├─ foo.f
   │     │  │  │  │  │  ├─ foo_fixed.f90
   │     │  │  │  │  │  └─ foo_free.f90
   │     │  │  │  │  ├─ modules
   │     │  │  │  │  │  ├─ gh25337
   │     │  │  │  │  │  │  ├─ data.f90
   │     │  │  │  │  │  │  └─ use_data.f90
   │     │  │  │  │  │  ├─ gh26920
   │     │  │  │  │  │  │  ├─ two_mods_with_no_public_entities.f90
   │     │  │  │  │  │  │  └─ two_mods_with_one_public_routine.f90
   │     │  │  │  │  │  ├─ module_data_docstring.f90
   │     │  │  │  │  │  └─ use_modules.f90
   │     │  │  │  │  ├─ negative_bounds
   │     │  │  │  │  │  └─ issue_20853.f90
   │     │  │  │  │  ├─ parameter
   │     │  │  │  │  │  ├─ constant_array.f90
   │     │  │  │  │  │  ├─ constant_both.f90
   │     │  │  │  │  │  ├─ constant_compound.f90
   │     │  │  │  │  │  ├─ constant_integer.f90
   │     │  │  │  │  │  ├─ constant_non_compound.f90
   │     │  │  │  │  │  └─ constant_real.f90
   │     │  │  │  │  ├─ quoted_character
   │     │  │  │  │  │  └─ foo.f
   │     │  │  │  │  ├─ regression
   │     │  │  │  │  │  ├─ AB.inc
   │     │  │  │  │  │  ├─ assignOnlyModule.f90
   │     │  │  │  │  │  ├─ datonly.f90
   │     │  │  │  │  │  ├─ f77comments.f
   │     │  │  │  │  │  ├─ f77fixedform.f95
   │     │  │  │  │  │  ├─ f90continuation.f90
   │     │  │  │  │  │  ├─ incfile.f90
   │     │  │  │  │  │  ├─ inout.f90
   │     │  │  │  │  │  └─ lower_f2py_fortran.f90
   │     │  │  │  │  ├─ return_character
   │     │  │  │  │  │  ├─ foo77.f
   │     │  │  │  │  │  └─ foo90.f90
   │     │  │  │  │  ├─ return_complex
   │     │  │  │  │  │  ├─ foo77.f
   │     │  │  │  │  │  └─ foo90.f90
   │     │  │  │  │  ├─ return_integer
   │     │  │  │  │  │  ├─ foo77.f
   │     │  │  │  │  │  └─ foo90.f90
   │     │  │  │  │  ├─ return_logical
   │     │  │  │  │  │  ├─ foo77.f
   │     │  │  │  │  │  └─ foo90.f90
   │     │  │  │  │  ├─ return_real
   │     │  │  │  │  │  ├─ foo77.f
   │     │  │  │  │  │  └─ foo90.f90
   │     │  │  │  │  ├─ routines
   │     │  │  │  │  │  ├─ funcfortranname.f
   │     │  │  │  │  │  ├─ funcfortranname.pyf
   │     │  │  │  │  │  ├─ subrout.f
   │     │  │  │  │  │  └─ subrout.pyf
   │     │  │  │  │  ├─ size
   │     │  │  │  │  │  └─ foo.f90
   │     │  │  │  │  ├─ string
   │     │  │  │  │  │  ├─ char.f90
   │     │  │  │  │  │  ├─ fixed_string.f90
   │     │  │  │  │  │  ├─ gh24008.f
   │     │  │  │  │  │  ├─ gh24662.f90
   │     │  │  │  │  │  ├─ gh25286.f90
   │     │  │  │  │  │  ├─ gh25286.pyf
   │     │  │  │  │  │  ├─ gh25286_bc.pyf
   │     │  │  │  │  │  ├─ scalar_string.f90
   │     │  │  │  │  │  └─ string.f
   │     │  │  │  │  └─ value_attrspec
   │     │  │  │  │     └─ gh21665.f90
   │     │  │  │  ├─ test_abstract_interface.py
   │     │  │  │  ├─ test_array_from_pyobj.py
   │     │  │  │  ├─ test_assumed_shape.py
   │     │  │  │  ├─ test_block_docstring.py
   │     │  │  │  ├─ test_callback.py
   │     │  │  │  ├─ test_character.py
   │     │  │  │  ├─ test_common.py
   │     │  │  │  ├─ test_crackfortran.py
   │     │  │  │  ├─ test_data.py
   │     │  │  │  ├─ test_docs.py
   │     │  │  │  ├─ test_f2cmap.py
   │     │  │  │  ├─ test_f2py2e.py
   │     │  │  │  ├─ test_isoc.py
   │     │  │  │  ├─ test_kind.py
   │     │  │  │  ├─ test_mixed.py
   │     │  │  │  ├─ test_modules.py
   │     │  │  │  ├─ test_parameter.py
   │     │  │  │  ├─ test_pyf_src.py
   │     │  │  │  ├─ test_quoted_character.py
   │     │  │  │  ├─ test_regression.py
   │     │  │  │  ├─ test_return_character.py
   │     │  │  │  ├─ test_return_complex.py
   │     │  │  │  ├─ test_return_integer.py
   │     │  │  │  ├─ test_return_logical.py
   │     │  │  │  ├─ test_return_real.py
   │     │  │  │  ├─ test_routines.py
   │     │  │  │  ├─ test_semicolon_split.py
   │     │  │  │  ├─ test_size.py
   │     │  │  │  ├─ test_string.py
   │     │  │  │  ├─ test_symbolic.py
   │     │  │  │  ├─ test_value_attrspec.py
   │     │  │  │  ├─ util.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ use_rules.py
   │     │  │  ├─ _backends
   │     │  │  │  ├─ meson.build.template
   │     │  │  │  ├─ _backend.py
   │     │  │  │  ├─ _distutils.py
   │     │  │  │  ├─ _meson.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _isocbind.py
   │     │  │  ├─ _src_pyf.py
   │     │  │  ├─ __init__.py
   │     │  │  ├─ __init__.pyi
   │     │  │  ├─ __main__.py
   │     │  │  └─ __version__.py
   │     │  ├─ fft
   │     │  │  ├─ helper.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_helper.py
   │     │  │  │  ├─ test_pocketfft.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _helper.py
   │     │  │  ├─ _helper.pyi
   │     │  │  ├─ _pocketfft.py
   │     │  │  ├─ _pocketfft.pyi
   │     │  │  ├─ _pocketfft_umath.cp311-win_amd64.lib
   │     │  │  ├─ _pocketfft_umath.cp311-win_amd64.pyd
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ lib
   │     │  │  ├─ array_utils.py
   │     │  │  ├─ array_utils.pyi
   │     │  │  ├─ format.py
   │     │  │  ├─ format.pyi
   │     │  │  ├─ introspect.py
   │     │  │  ├─ introspect.pyi
   │     │  │  ├─ mixins.py
   │     │  │  ├─ mixins.pyi
   │     │  │  ├─ npyio.py
   │     │  │  ├─ npyio.pyi
   │     │  │  ├─ recfunctions.py
   │     │  │  ├─ recfunctions.pyi
   │     │  │  ├─ scimath.py
   │     │  │  ├─ scimath.pyi
   │     │  │  ├─ stride_tricks.py
   │     │  │  ├─ stride_tricks.pyi
   │     │  │  ├─ tests
   │     │  │  │  ├─ data
   │     │  │  │  │  ├─ py2-np0-objarr.npy
   │     │  │  │  │  ├─ py2-objarr.npy
   │     │  │  │  │  ├─ py2-objarr.npz
   │     │  │  │  │  ├─ py3-objarr.npy
   │     │  │  │  │  ├─ py3-objarr.npz
   │     │  │  │  │  ├─ python3.npy
   │     │  │  │  │  └─ win64python2.npy
   │     │  │  │  ├─ test_arraypad.py
   │     │  │  │  ├─ test_arraysetops.py
   │     │  │  │  ├─ test_arrayterator.py
   │     │  │  │  ├─ test_array_utils.py
   │     │  │  │  ├─ test_format.py
   │     │  │  │  ├─ test_function_base.py
   │     │  │  │  ├─ test_histograms.py
   │     │  │  │  ├─ test_index_tricks.py
   │     │  │  │  ├─ test_io.py
   │     │  │  │  ├─ test_loadtxt.py
   │     │  │  │  ├─ test_mixins.py
   │     │  │  │  ├─ test_nanfunctions.py
   │     │  │  │  ├─ test_packbits.py
   │     │  │  │  ├─ test_polynomial.py
   │     │  │  │  ├─ test_recfunctions.py
   │     │  │  │  ├─ test_regression.py
   │     │  │  │  ├─ test_shape_base.py
   │     │  │  │  ├─ test_stride_tricks.py
   │     │  │  │  ├─ test_twodim_base.py
   │     │  │  │  ├─ test_type_check.py
   │     │  │  │  ├─ test_ufunclike.py
   │     │  │  │  ├─ test_utils.py
   │     │  │  │  ├─ test__datasource.py
   │     │  │  │  ├─ test__iotools.py
   │     │  │  │  ├─ test__version.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ user_array.py
   │     │  │  ├─ user_array.pyi
   │     │  │  ├─ _arraypad_impl.py
   │     │  │  ├─ _arraypad_impl.pyi
   │     │  │  ├─ _arraysetops_impl.py
   │     │  │  ├─ _arraysetops_impl.pyi
   │     │  │  ├─ _arrayterator_impl.py
   │     │  │  ├─ _arrayterator_impl.pyi
   │     │  │  ├─ _array_utils_impl.py
   │     │  │  ├─ _array_utils_impl.pyi
   │     │  │  ├─ _datasource.py
   │     │  │  ├─ _datasource.pyi
   │     │  │  ├─ _function_base_impl.py
   │     │  │  ├─ _function_base_impl.pyi
   │     │  │  ├─ _histograms_impl.py
   │     │  │  ├─ _histograms_impl.pyi
   │     │  │  ├─ _index_tricks_impl.py
   │     │  │  ├─ _index_tricks_impl.pyi
   │     │  │  ├─ _iotools.py
   │     │  │  ├─ _iotools.pyi
   │     │  │  ├─ _nanfunctions_impl.py
   │     │  │  ├─ _nanfunctions_impl.pyi
   │     │  │  ├─ _npyio_impl.py
   │     │  │  ├─ _npyio_impl.pyi
   │     │  │  ├─ _polynomial_impl.py
   │     │  │  ├─ _polynomial_impl.pyi
   │     │  │  ├─ _scimath_impl.py
   │     │  │  ├─ _scimath_impl.pyi
   │     │  │  ├─ _shape_base_impl.py
   │     │  │  ├─ _shape_base_impl.pyi
   │     │  │  ├─ _stride_tricks_impl.py
   │     │  │  ├─ _stride_tricks_impl.pyi
   │     │  │  ├─ _twodim_base_impl.py
   │     │  │  ├─ _twodim_base_impl.pyi
   │     │  │  ├─ _type_check_impl.py
   │     │  │  ├─ _type_check_impl.pyi
   │     │  │  ├─ _ufunclike_impl.py
   │     │  │  ├─ _ufunclike_impl.pyi
   │     │  │  ├─ _user_array_impl.py
   │     │  │  ├─ _user_array_impl.pyi
   │     │  │  ├─ _utils_impl.py
   │     │  │  ├─ _utils_impl.pyi
   │     │  │  ├─ _version.py
   │     │  │  ├─ _version.pyi
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ linalg
   │     │  │  ├─ lapack_lite.cp311-win_amd64.lib
   │     │  │  ├─ lapack_lite.cp311-win_amd64.pyd
   │     │  │  ├─ linalg.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_deprecations.py
   │     │  │  │  ├─ test_linalg.py
   │     │  │  │  ├─ test_regression.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _linalg.py
   │     │  │  ├─ _linalg.pyi
   │     │  │  ├─ _umath_linalg.cp311-win_amd64.lib
   │     │  │  ├─ _umath_linalg.cp311-win_amd64.pyd
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ ma
   │     │  │  ├─ API_CHANGES.txt
   │     │  │  ├─ core.py
   │     │  │  ├─ core.pyi
   │     │  │  ├─ extras.py
   │     │  │  ├─ extras.pyi
   │     │  │  ├─ LICENSE
   │     │  │  ├─ mrecords.py
   │     │  │  ├─ mrecords.pyi
   │     │  │  ├─ README.rst
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_arrayobject.py
   │     │  │  │  ├─ test_core.py
   │     │  │  │  ├─ test_deprecations.py
   │     │  │  │  ├─ test_extras.py
   │     │  │  │  ├─ test_mrecords.py
   │     │  │  │  ├─ test_old_ma.py
   │     │  │  │  ├─ test_regression.py
   │     │  │  │  ├─ test_subclassing.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ testutils.py
   │     │  │  ├─ timer_comparison.py
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ matlib.py
   │     │  ├─ matlib.pyi
   │     │  ├─ matrixlib
   │     │  │  ├─ defmatrix.py
   │     │  │  ├─ defmatrix.pyi
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_defmatrix.py
   │     │  │  │  ├─ test_interaction.py
   │     │  │  │  ├─ test_masked_matrix.py
   │     │  │  │  ├─ test_matrix_linalg.py
   │     │  │  │  ├─ test_multiarray.py
   │     │  │  │  ├─ test_numeric.py
   │     │  │  │  ├─ test_regression.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ polynomial
   │     │  │  ├─ chebyshev.py
   │     │  │  ├─ chebyshev.pyi
   │     │  │  ├─ hermite.py
   │     │  │  ├─ hermite.pyi
   │     │  │  ├─ hermite_e.py
   │     │  │  ├─ hermite_e.pyi
   │     │  │  ├─ laguerre.py
   │     │  │  ├─ laguerre.pyi
   │     │  │  ├─ legendre.py
   │     │  │  ├─ legendre.pyi
   │     │  │  ├─ polynomial.py
   │     │  │  ├─ polynomial.pyi
   │     │  │  ├─ polyutils.py
   │     │  │  ├─ polyutils.pyi
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_chebyshev.py
   │     │  │  │  ├─ test_classes.py
   │     │  │  │  ├─ test_hermite.py
   │     │  │  │  ├─ test_hermite_e.py
   │     │  │  │  ├─ test_laguerre.py
   │     │  │  │  ├─ test_legendre.py
   │     │  │  │  ├─ test_polynomial.py
   │     │  │  │  ├─ test_polyutils.py
   │     │  │  │  ├─ test_printing.py
   │     │  │  │  ├─ test_symbol.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _polybase.py
   │     │  │  ├─ _polybase.pyi
   │     │  │  ├─ _polytypes.pyi
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ py.typed
   │     │  ├─ random
   │     │  │  ├─ bit_generator.cp311-win_amd64.lib
   │     │  │  ├─ bit_generator.cp311-win_amd64.pyd
   │     │  │  ├─ bit_generator.pxd
   │     │  │  ├─ bit_generator.pyi
   │     │  │  ├─ c_distributions.pxd
   │     │  │  ├─ lib
   │     │  │  │  └─ npyrandom.lib
   │     │  │  ├─ LICENSE.md
   │     │  │  ├─ mtrand.cp311-win_amd64.lib
   │     │  │  ├─ mtrand.cp311-win_amd64.pyd
   │     │  │  ├─ mtrand.pyi
   │     │  │  ├─ tests
   │     │  │  │  ├─ data
   │     │  │  │  │  ├─ generator_pcg64_np121.pkl.gz
   │     │  │  │  │  ├─ generator_pcg64_np126.pkl.gz
   │     │  │  │  │  ├─ mt19937-testset-1.csv
   │     │  │  │  │  ├─ mt19937-testset-2.csv
   │     │  │  │  │  ├─ pcg64-testset-1.csv
   │     │  │  │  │  ├─ pcg64-testset-2.csv
   │     │  │  │  │  ├─ pcg64dxsm-testset-1.csv
   │     │  │  │  │  ├─ pcg64dxsm-testset-2.csv
   │     │  │  │  │  ├─ philox-testset-1.csv
   │     │  │  │  │  ├─ philox-testset-2.csv
   │     │  │  │  │  ├─ sfc64-testset-1.csv
   │     │  │  │  │  ├─ sfc64-testset-2.csv
   │     │  │  │  │  ├─ sfc64_np126.pkl.gz
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_direct.py
   │     │  │  │  ├─ test_extending.py
   │     │  │  │  ├─ test_generator_mt19937.py
   │     │  │  │  ├─ test_generator_mt19937_regressions.py
   │     │  │  │  ├─ test_random.py
   │     │  │  │  ├─ test_randomstate.py
   │     │  │  │  ├─ test_randomstate_regression.py
   │     │  │  │  ├─ test_regression.py
   │     │  │  │  ├─ test_seed_sequence.py
   │     │  │  │  ├─ test_smoke.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _bounded_integers.cp311-win_amd64.lib
   │     │  │  ├─ _bounded_integers.cp311-win_amd64.pyd
   │     │  │  ├─ _bounded_integers.pxd
   │     │  │  ├─ _common.cp311-win_amd64.lib
   │     │  │  ├─ _common.cp311-win_amd64.pyd
   │     │  │  ├─ _common.pxd
   │     │  │  ├─ _examples
   │     │  │  │  ├─ cffi
   │     │  │  │  │  ├─ extending.py
   │     │  │  │  │  └─ parse.py
   │     │  │  │  ├─ cython
   │     │  │  │  │  ├─ extending.pyx
   │     │  │  │  │  ├─ extending_distributions.pyx
   │     │  │  │  │  └─ meson.build
   │     │  │  │  └─ numba
   │     │  │  │     ├─ extending.py
   │     │  │  │     └─ extending_distributions.py
   │     │  │  ├─ _generator.cp311-win_amd64.lib
   │     │  │  ├─ _generator.cp311-win_amd64.pyd
   │     │  │  ├─ _generator.pyi
   │     │  │  ├─ _mt19937.cp311-win_amd64.lib
   │     │  │  ├─ _mt19937.cp311-win_amd64.pyd
   │     │  │  ├─ _mt19937.pyi
   │     │  │  ├─ _pcg64.cp311-win_amd64.lib
   │     │  │  ├─ _pcg64.cp311-win_amd64.pyd
   │     │  │  ├─ _pcg64.pyi
   │     │  │  ├─ _philox.cp311-win_amd64.lib
   │     │  │  ├─ _philox.cp311-win_amd64.pyd
   │     │  │  ├─ _philox.pyi
   │     │  │  ├─ _pickle.py
   │     │  │  ├─ _sfc64.cp311-win_amd64.lib
   │     │  │  ├─ _sfc64.cp311-win_amd64.pyd
   │     │  │  ├─ _sfc64.pyi
   │     │  │  ├─ __init__.pxd
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ rec
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ strings
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ testing
   │     │  │  ├─ overrides.py
   │     │  │  ├─ overrides.pyi
   │     │  │  ├─ print_coercion_tables.py
   │     │  │  ├─ print_coercion_tables.pyi
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_utils.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _private
   │     │  │  │  ├─ extbuild.py
   │     │  │  │  ├─ extbuild.pyi
   │     │  │  │  ├─ utils.py
   │     │  │  │  ├─ utils.pyi
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __init__.pyi
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ tests
   │     │  │  ├─ test_configtool.py
   │     │  │  ├─ test_ctypeslib.py
   │     │  │  ├─ test_lazyloading.py
   │     │  │  ├─ test_matlib.py
   │     │  │  ├─ test_numpy_config.py
   │     │  │  ├─ test_numpy_version.py
   │     │  │  ├─ test_public_api.py
   │     │  │  ├─ test_reloading.py
   │     │  │  ├─ test_scripts.py
   │     │  │  ├─ test_warnings.py
   │     │  │  ├─ test__all__.py
   │     │  │  └─ __init__.py
   │     │  ├─ typing
   │     │  │  ├─ mypy_plugin.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ data
   │     │  │  │  │  ├─ fail
   │     │  │  │  │  │  ├─ arithmetic.pyi
   │     │  │  │  │  │  ├─ arrayprint.pyi
   │     │  │  │  │  │  ├─ arrayterator.pyi
   │     │  │  │  │  │  ├─ array_constructors.pyi
   │     │  │  │  │  │  ├─ array_like.pyi
   │     │  │  │  │  │  ├─ array_pad.pyi
   │     │  │  │  │  │  ├─ bitwise_ops.pyi
   │     │  │  │  │  │  ├─ char.pyi
   │     │  │  │  │  │  ├─ chararray.pyi
   │     │  │  │  │  │  ├─ comparisons.pyi
   │     │  │  │  │  │  ├─ constants.pyi
   │     │  │  │  │  │  ├─ datasource.pyi
   │     │  │  │  │  │  ├─ dtype.pyi
   │     │  │  │  │  │  ├─ einsumfunc.pyi
   │     │  │  │  │  │  ├─ flatiter.pyi
   │     │  │  │  │  │  ├─ fromnumeric.pyi
   │     │  │  │  │  │  ├─ histograms.pyi
   │     │  │  │  │  │  ├─ index_tricks.pyi
   │     │  │  │  │  │  ├─ lib_function_base.pyi
   │     │  │  │  │  │  ├─ lib_polynomial.pyi
   │     │  │  │  │  │  ├─ lib_utils.pyi
   │     │  │  │  │  │  ├─ lib_version.pyi
   │     │  │  │  │  │  ├─ linalg.pyi
   │     │  │  │  │  │  ├─ memmap.pyi
   │     │  │  │  │  │  ├─ modules.pyi
   │     │  │  │  │  │  ├─ multiarray.pyi
   │     │  │  │  │  │  ├─ ndarray.pyi
   │     │  │  │  │  │  ├─ ndarray_misc.pyi
   │     │  │  │  │  │  ├─ nditer.pyi
   │     │  │  │  │  │  ├─ nested_sequence.pyi
   │     │  │  │  │  │  ├─ npyio.pyi
   │     │  │  │  │  │  ├─ numerictypes.pyi
   │     │  │  │  │  │  ├─ random.pyi
   │     │  │  │  │  │  ├─ rec.pyi
   │     │  │  │  │  │  ├─ scalars.pyi
   │     │  │  │  │  │  ├─ shape.pyi
   │     │  │  │  │  │  ├─ shape_base.pyi
   │     │  │  │  │  │  ├─ stride_tricks.pyi
   │     │  │  │  │  │  ├─ strings.pyi
   │     │  │  │  │  │  ├─ testing.pyi
   │     │  │  │  │  │  ├─ twodim_base.pyi
   │     │  │  │  │  │  ├─ type_check.pyi
   │     │  │  │  │  │  ├─ ufunclike.pyi
   │     │  │  │  │  │  ├─ ufuncs.pyi
   │     │  │  │  │  │  ├─ ufunc_config.pyi
   │     │  │  │  │  │  └─ warnings_and_errors.pyi
   │     │  │  │  │  ├─ misc
   │     │  │  │  │  │  └─ extended_precision.pyi
   │     │  │  │  │  ├─ mypy.ini
   │     │  │  │  │  ├─ pass
   │     │  │  │  │  │  ├─ arithmetic.py
   │     │  │  │  │  │  ├─ arrayprint.py
   │     │  │  │  │  │  ├─ arrayterator.py
   │     │  │  │  │  │  ├─ array_constructors.py
   │     │  │  │  │  │  ├─ array_like.py
   │     │  │  │  │  │  ├─ bitwise_ops.py
   │     │  │  │  │  │  ├─ comparisons.py
   │     │  │  │  │  │  ├─ dtype.py
   │     │  │  │  │  │  ├─ einsumfunc.py
   │     │  │  │  │  │  ├─ flatiter.py
   │     │  │  │  │  │  ├─ fromnumeric.py
   │     │  │  │  │  │  ├─ index_tricks.py
   │     │  │  │  │  │  ├─ lib_user_array.py
   │     │  │  │  │  │  ├─ lib_utils.py
   │     │  │  │  │  │  ├─ lib_version.py
   │     │  │  │  │  │  ├─ literal.py
   │     │  │  │  │  │  ├─ ma.py
   │     │  │  │  │  │  ├─ mod.py
   │     │  │  │  │  │  ├─ modules.py
   │     │  │  │  │  │  ├─ multiarray.py
   │     │  │  │  │  │  ├─ ndarray_conversion.py
   │     │  │  │  │  │  ├─ ndarray_misc.py
   │     │  │  │  │  │  ├─ ndarray_shape_manipulation.py
   │     │  │  │  │  │  ├─ nditer.py
   │     │  │  │  │  │  ├─ numeric.py
   │     │  │  │  │  │  ├─ numerictypes.py
   │     │  │  │  │  │  ├─ random.py
   │     │  │  │  │  │  ├─ recfunctions.py
   │     │  │  │  │  │  ├─ scalars.py
   │     │  │  │  │  │  ├─ shape.py
   │     │  │  │  │  │  ├─ simple.py
   │     │  │  │  │  │  ├─ simple_py3.py
   │     │  │  │  │  │  ├─ ufunclike.py
   │     │  │  │  │  │  ├─ ufuncs.py
   │     │  │  │  │  │  ├─ ufunc_config.py
   │     │  │  │  │  │  └─ warnings_and_errors.py
   │     │  │  │  │  └─ reveal
   │     │  │  │  │     ├─ arithmetic.pyi
   │     │  │  │  │     ├─ arraypad.pyi
   │     │  │  │  │     ├─ arrayprint.pyi
   │     │  │  │  │     ├─ arraysetops.pyi
   │     │  │  │  │     ├─ arrayterator.pyi
   │     │  │  │  │     ├─ array_api_info.pyi
   │     │  │  │  │     ├─ array_constructors.pyi
   │     │  │  │  │     ├─ bitwise_ops.pyi
   │     │  │  │  │     ├─ char.pyi
   │     │  │  │  │     ├─ chararray.pyi
   │     │  │  │  │     ├─ comparisons.pyi
   │     │  │  │  │     ├─ constants.pyi
   │     │  │  │  │     ├─ ctypeslib.pyi
   │     │  │  │  │     ├─ datasource.pyi
   │     │  │  │  │     ├─ dtype.pyi
   │     │  │  │  │     ├─ einsumfunc.pyi
   │     │  │  │  │     ├─ emath.pyi
   │     │  │  │  │     ├─ fft.pyi
   │     │  │  │  │     ├─ flatiter.pyi
   │     │  │  │  │     ├─ fromnumeric.pyi
   │     │  │  │  │     ├─ getlimits.pyi
   │     │  │  │  │     ├─ histograms.pyi
   │     │  │  │  │     ├─ index_tricks.pyi
   │     │  │  │  │     ├─ lib_function_base.pyi
   │     │  │  │  │     ├─ lib_polynomial.pyi
   │     │  │  │  │     ├─ lib_utils.pyi
   │     │  │  │  │     ├─ lib_version.pyi
   │     │  │  │  │     ├─ linalg.pyi
   │     │  │  │  │     ├─ matrix.pyi
   │     │  │  │  │     ├─ memmap.pyi
   │     │  │  │  │     ├─ mod.pyi
   │     │  │  │  │     ├─ modules.pyi
   │     │  │  │  │     ├─ multiarray.pyi
   │     │  │  │  │     ├─ nbit_base_example.pyi
   │     │  │  │  │     ├─ ndarray_assignability.pyi
   │     │  │  │  │     ├─ ndarray_conversion.pyi
   │     │  │  │  │     ├─ ndarray_misc.pyi
   │     │  │  │  │     ├─ ndarray_shape_manipulation.pyi
   │     │  │  │  │     ├─ nditer.pyi
   │     │  │  │  │     ├─ nested_sequence.pyi
   │     │  │  │  │     ├─ npyio.pyi
   │     │  │  │  │     ├─ numeric.pyi
   │     │  │  │  │     ├─ numerictypes.pyi
   │     │  │  │  │     ├─ polynomial_polybase.pyi
   │     │  │  │  │     ├─ polynomial_polyutils.pyi
   │     │  │  │  │     ├─ polynomial_series.pyi
   │     │  │  │  │     ├─ random.pyi
   │     │  │  │  │     ├─ rec.pyi
   │     │  │  │  │     ├─ scalars.pyi
   │     │  │  │  │     ├─ shape.pyi
   │     │  │  │  │     ├─ shape_base.pyi
   │     │  │  │  │     ├─ stride_tricks.pyi
   │     │  │  │  │     ├─ strings.pyi
   │     │  │  │  │     ├─ testing.pyi
   │     │  │  │  │     ├─ twodim_base.pyi
   │     │  │  │  │     ├─ type_check.pyi
   │     │  │  │  │     ├─ ufunclike.pyi
   │     │  │  │  │     ├─ ufuncs.pyi
   │     │  │  │  │     ├─ ufunc_config.pyi
   │     │  │  │  │     └─ warnings_and_errors.pyi
   │     │  │  │  ├─ test_isfile.py
   │     │  │  │  ├─ test_runtime.py
   │     │  │  │  ├─ test_typing.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ version.py
   │     │  ├─ version.pyi
   │     │  ├─ _array_api_info.py
   │     │  ├─ _array_api_info.pyi
   │     │  ├─ _configtool.py
   │     │  ├─ _configtool.pyi
   │     │  ├─ _core
   │     │  │  ├─ arrayprint.py
   │     │  │  ├─ arrayprint.pyi
   │     │  │  ├─ cversions.py
   │     │  │  ├─ defchararray.py
   │     │  │  ├─ defchararray.pyi
   │     │  │  ├─ einsumfunc.py
   │     │  │  ├─ einsumfunc.pyi
   │     │  │  ├─ fromnumeric.py
   │     │  │  ├─ fromnumeric.pyi
   │     │  │  ├─ function_base.py
   │     │  │  ├─ function_base.pyi
   │     │  │  ├─ getlimits.py
   │     │  │  ├─ getlimits.pyi
   │     │  │  ├─ include
   │     │  │  │  └─ numpy
   │     │  │  │     ├─ arrayobject.h
   │     │  │  │     ├─ arrayscalars.h
   │     │  │  │     ├─ dtype_api.h
   │     │  │  │     ├─ halffloat.h
   │     │  │  │     ├─ ndarrayobject.h
   │     │  │  │     ├─ ndarraytypes.h
   │     │  │  │     ├─ npy_1_7_deprecated_api.h
   │     │  │  │     ├─ npy_2_compat.h
   │     │  │  │     ├─ npy_2_complexcompat.h
   │     │  │  │     ├─ npy_3kcompat.h
   │     │  │  │     ├─ npy_common.h
   │     │  │  │     ├─ npy_cpu.h
   │     │  │  │     ├─ npy_endian.h
   │     │  │  │     ├─ npy_math.h
   │     │  │  │     ├─ npy_no_deprecated_api.h
   │     │  │  │     ├─ npy_os.h
   │     │  │  │     ├─ numpyconfig.h
   │     │  │  │     ├─ random
   │     │  │  │     │  ├─ bitgen.h
   │     │  │  │     │  ├─ distributions.h
   │     │  │  │     │  ├─ libdivide.h
   │     │  │  │     │  └─ LICENSE.txt
   │     │  │  │     ├─ ufuncobject.h
   │     │  │  │     ├─ utils.h
   │     │  │  │     ├─ _neighborhood_iterator_imp.h
   │     │  │  │     ├─ _numpyconfig.h
   │     │  │  │     ├─ _public_dtype_api_table.h
   │     │  │  │     ├─ __multiarray_api.c
   │     │  │  │     ├─ __multiarray_api.h
   │     │  │  │     ├─ __ufunc_api.c
   │     │  │  │     └─ __ufunc_api.h
   │     │  │  ├─ lib
   │     │  │  │  ├─ npy-pkg-config
   │     │  │  │  │  ├─ mlib.ini
   │     │  │  │  │  └─ npymath.ini
   │     │  │  │  ├─ npymath.lib
   │     │  │  │  └─ pkgconfig
   │     │  │  │     └─ numpy.pc
   │     │  │  ├─ memmap.py
   │     │  │  ├─ memmap.pyi
   │     │  │  ├─ multiarray.py
   │     │  │  ├─ multiarray.pyi
   │     │  │  ├─ numeric.py
   │     │  │  ├─ numeric.pyi
   │     │  │  ├─ numerictypes.py
   │     │  │  ├─ numerictypes.pyi
   │     │  │  ├─ overrides.py
   │     │  │  ├─ printoptions.py
   │     │  │  ├─ records.py
   │     │  │  ├─ records.pyi
   │     │  │  ├─ shape_base.py
   │     │  │  ├─ shape_base.pyi
   │     │  │  ├─ strings.py
   │     │  │  ├─ strings.pyi
   │     │  │  ├─ tests
   │     │  │  │  ├─ data
   │     │  │  │  │  ├─ astype_copy.pkl
   │     │  │  │  │  ├─ generate_umath_validation_data.cpp
   │     │  │  │  │  ├─ recarray_from_file.fits
   │     │  │  │  │  ├─ umath-validation-set-arccos.csv
   │     │  │  │  │  ├─ umath-validation-set-arccosh.csv
   │     │  │  │  │  ├─ umath-validation-set-arcsin.csv
   │     │  │  │  │  ├─ umath-validation-set-arcsinh.csv
   │     │  │  │  │  ├─ umath-validation-set-arctan.csv
   │     │  │  │  │  ├─ umath-validation-set-arctanh.csv
   │     │  │  │  │  ├─ umath-validation-set-cbrt.csv
   │     │  │  │  │  ├─ umath-validation-set-cos.csv
   │     │  │  │  │  ├─ umath-validation-set-cosh.csv
   │     │  │  │  │  ├─ umath-validation-set-exp.csv
   │     │  │  │  │  ├─ umath-validation-set-exp2.csv
   │     │  │  │  │  ├─ umath-validation-set-expm1.csv
   │     │  │  │  │  ├─ umath-validation-set-log.csv
   │     │  │  │  │  ├─ umath-validation-set-log10.csv
   │     │  │  │  │  ├─ umath-validation-set-log1p.csv
   │     │  │  │  │  ├─ umath-validation-set-log2.csv
   │     │  │  │  │  ├─ umath-validation-set-README.txt
   │     │  │  │  │  ├─ umath-validation-set-sin.csv
   │     │  │  │  │  ├─ umath-validation-set-sinh.csv
   │     │  │  │  │  ├─ umath-validation-set-tan.csv
   │     │  │  │  │  └─ umath-validation-set-tanh.csv
   │     │  │  │  ├─ examples
   │     │  │  │  │  ├─ cython
   │     │  │  │  │  │  ├─ checks.pyx
   │     │  │  │  │  │  ├─ meson.build
   │     │  │  │  │  │  └─ setup.py
   │     │  │  │  │  └─ limited_api
   │     │  │  │  │     ├─ limited_api1.c
   │     │  │  │  │     ├─ limited_api2.pyx
   │     │  │  │  │     ├─ limited_api_latest.c
   │     │  │  │  │     ├─ meson.build
   │     │  │  │  │     └─ setup.py
   │     │  │  │  ├─ test_abc.py
   │     │  │  │  ├─ test_api.py
   │     │  │  │  ├─ test_argparse.py
   │     │  │  │  ├─ test_arraymethod.py
   │     │  │  │  ├─ test_arrayobject.py
   │     │  │  │  ├─ test_arrayprint.py
   │     │  │  │  ├─ test_array_api_info.py
   │     │  │  │  ├─ test_array_coercion.py
   │     │  │  │  ├─ test_array_interface.py
   │     │  │  │  ├─ test_casting_floatingpoint_errors.py
   │     │  │  │  ├─ test_casting_unittests.py
   │     │  │  │  ├─ test_conversion_utils.py
   │     │  │  │  ├─ test_cpu_dispatcher.py
   │     │  │  │  ├─ test_cpu_features.py
   │     │  │  │  ├─ test_custom_dtypes.py
   │     │  │  │  ├─ test_cython.py
   │     │  │  │  ├─ test_datetime.py
   │     │  │  │  ├─ test_defchararray.py
   │     │  │  │  ├─ test_deprecations.py
   │     │  │  │  ├─ test_dlpack.py
   │     │  │  │  ├─ test_dtype.py
   │     │  │  │  ├─ test_einsum.py
   │     │  │  │  ├─ test_errstate.py
   │     │  │  │  ├─ test_extint128.py
   │     │  │  │  ├─ test_function_base.py
   │     │  │  │  ├─ test_getlimits.py
   │     │  │  │  ├─ test_half.py
   │     │  │  │  ├─ test_hashtable.py
   │     │  │  │  ├─ test_indexerrors.py
   │     │  │  │  ├─ test_indexing.py
   │     │  │  │  ├─ test_item_selection.py
   │     │  │  │  ├─ test_limited_api.py
   │     │  │  │  ├─ test_longdouble.py
   │     │  │  │  ├─ test_machar.py
   │     │  │  │  ├─ test_memmap.py
   │     │  │  │  ├─ test_mem_overlap.py
   │     │  │  │  ├─ test_mem_policy.py
   │     │  │  │  ├─ test_multiarray.py
   │     │  │  │  ├─ test_multithreading.py
   │     │  │  │  ├─ test_nditer.py
   │     │  │  │  ├─ test_nep50_promotions.py
   │     │  │  │  ├─ test_numeric.py
   │     │  │  │  ├─ test_numerictypes.py
   │     │  │  │  ├─ test_overrides.py
   │     │  │  │  ├─ test_print.py
   │     │  │  │  ├─ test_protocols.py
   │     │  │  │  ├─ test_records.py
   │     │  │  │  ├─ test_regression.py
   │     │  │  │  ├─ test_scalarbuffer.py
   │     │  │  │  ├─ test_scalarinherit.py
   │     │  │  │  ├─ test_scalarmath.py
   │     │  │  │  ├─ test_scalarprint.py
   │     │  │  │  ├─ test_scalar_ctors.py
   │     │  │  │  ├─ test_scalar_methods.py
   │     │  │  │  ├─ test_shape_base.py
   │     │  │  │  ├─ test_simd.py
   │     │  │  │  ├─ test_simd_module.py
   │     │  │  │  ├─ test_stringdtype.py
   │     │  │  │  ├─ test_strings.py
   │     │  │  │  ├─ test_ufunc.py
   │     │  │  │  ├─ test_umath.py
   │     │  │  │  ├─ test_umath_accuracy.py
   │     │  │  │  ├─ test_umath_complex.py
   │     │  │  │  ├─ test_unicode.py
   │     │  │  │  ├─ test__exceptions.py
   │     │  │  │  ├─ _locales.py
   │     │  │  │  └─ _natype.py
   │     │  │  ├─ umath.py
   │     │  │  ├─ _add_newdocs.py
   │     │  │  ├─ _add_newdocs_scalars.py
   │     │  │  ├─ _asarray.py
   │     │  │  ├─ _asarray.pyi
   │     │  │  ├─ _dtype.py
   │     │  │  ├─ _dtype_ctypes.py
   │     │  │  ├─ _exceptions.py
   │     │  │  ├─ _internal.py
   │     │  │  ├─ _internal.pyi
   │     │  │  ├─ _machar.py
   │     │  │  ├─ _methods.py
   │     │  │  ├─ _multiarray_tests.cp311-win_amd64.lib
   │     │  │  ├─ _multiarray_tests.cp311-win_amd64.pyd
   │     │  │  ├─ _multiarray_umath.cp311-win_amd64.lib
   │     │  │  ├─ _multiarray_umath.cp311-win_amd64.pyd
   │     │  │  ├─ _operand_flag_tests.cp311-win_amd64.lib
   │     │  │  ├─ _operand_flag_tests.cp311-win_amd64.pyd
   │     │  │  ├─ _rational_tests.cp311-win_amd64.lib
   │     │  │  ├─ _rational_tests.cp311-win_amd64.pyd
   │     │  │  ├─ _simd.cp311-win_amd64.lib
   │     │  │  ├─ _simd.cp311-win_amd64.pyd
   │     │  │  ├─ _string_helpers.py
   │     │  │  ├─ _struct_ufunc_tests.cp311-win_amd64.lib
   │     │  │  ├─ _struct_ufunc_tests.cp311-win_amd64.pyd
   │     │  │  ├─ _type_aliases.py
   │     │  │  ├─ _type_aliases.pyi
   │     │  │  ├─ _ufunc_config.py
   │     │  │  ├─ _ufunc_config.pyi
   │     │  │  ├─ _umath_tests.cp311-win_amd64.lib
   │     │  │  ├─ _umath_tests.cp311-win_amd64.pyd
   │     │  │  ├─ __init__.py
   │     │  │  └─ __init__.pyi
   │     │  ├─ _distributor_init.py
   │     │  ├─ _distributor_init.pyi
   │     │  ├─ _expired_attrs_2_0.py
   │     │  ├─ _expired_attrs_2_0.pyi
   │     │  ├─ _globals.py
   │     │  ├─ _globals.pyi
   │     │  ├─ _pyinstaller
   │     │  │  ├─ hook-numpy.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ pyinstaller-smoke.py
   │     │  │  │  ├─ test_pyinstaller.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ _pytesttester.py
   │     │  ├─ _pytesttester.pyi
   │     │  ├─ _typing
   │     │  │  ├─ _add_docstring.py
   │     │  │  ├─ _array_like.py
   │     │  │  ├─ _callable.pyi
   │     │  │  ├─ _char_codes.py
   │     │  │  ├─ _dtype_like.py
   │     │  │  ├─ _extended_precision.py
   │     │  │  ├─ _nbit.py
   │     │  │  ├─ _nbit_base.py
   │     │  │  ├─ _nested_sequence.py
   │     │  │  ├─ _scalars.py
   │     │  │  ├─ _shape.py
   │     │  │  ├─ _ufunc.py
   │     │  │  ├─ _ufunc.pyi
   │     │  │  └─ __init__.py
   │     │  ├─ _utils
   │     │  │  ├─ _convertions.py
   │     │  │  ├─ _inspect.py
   │     │  │  ├─ _pep440.py
   │     │  │  └─ __init__.py
   │     │  ├─ __config__.py
   │     │  ├─ __config__.pyi
   │     │  ├─ __init__.cython-30.pxd
   │     │  ├─ __init__.pxd
   │     │  ├─ __init__.py
   │     │  └─ __init__.pyi
   │     ├─ numpy-2.2.3-cp311-cp311-win_amd64.whl
   │     ├─ numpy-2.2.3.dist-info
   │     │  ├─ DELVEWHEEL
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE.txt
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  └─ WHEEL
   │     ├─ numpy.libs
   │     │  ├─ libscipy_openblas64_-43e11ff0749b8cbe0a615c9cf6737e0e.dll
   │     │  └─ msvcp140-263139962577ecda4cd9469ca360a746.dll
   │     ├─ oauthlib
   │     │  ├─ common.py
   │     │  ├─ oauth1
   │     │  │  ├─ rfc5849
   │     │  │  │  ├─ endpoints
   │     │  │  │  │  ├─ access_token.py
   │     │  │  │  │  ├─ authorization.py
   │     │  │  │  │  ├─ base.py
   │     │  │  │  │  ├─ pre_configured.py
   │     │  │  │  │  ├─ request_token.py
   │     │  │  │  │  ├─ resource.py
   │     │  │  │  │  ├─ signature_only.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ errors.py
   │     │  │  │  ├─ parameters.py
   │     │  │  │  ├─ request_validator.py
   │     │  │  │  ├─ signature.py
   │     │  │  │  ├─ utils.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ oauth2
   │     │  │  ├─ rfc6749
   │     │  │  │  ├─ clients
   │     │  │  │  │  ├─ backend_application.py
   │     │  │  │  │  ├─ base.py
   │     │  │  │  │  ├─ legacy_application.py
   │     │  │  │  │  ├─ mobile_application.py
   │     │  │  │  │  ├─ service_application.py
   │     │  │  │  │  ├─ web_application.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ endpoints
   │     │  │  │  │  ├─ authorization.py
   │     │  │  │  │  ├─ base.py
   │     │  │  │  │  ├─ introspect.py
   │     │  │  │  │  ├─ metadata.py
   │     │  │  │  │  ├─ pre_configured.py
   │     │  │  │  │  ├─ resource.py
   │     │  │  │  │  ├─ revocation.py
   │     │  │  │  │  ├─ token.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ errors.py
   │     │  │  │  ├─ grant_types
   │     │  │  │  │  ├─ authorization_code.py
   │     │  │  │  │  ├─ base.py
   │     │  │  │  │  ├─ client_credentials.py
   │     │  │  │  │  ├─ implicit.py
   │     │  │  │  │  ├─ refresh_token.py
   │     │  │  │  │  ├─ resource_owner_password_credentials.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ parameters.py
   │     │  │  │  ├─ request_validator.py
   │     │  │  │  ├─ tokens.py
   │     │  │  │  ├─ utils.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ rfc8628
   │     │  │  │  ├─ clients
   │     │  │  │  │  ├─ device.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ openid
   │     │  │  ├─ connect
   │     │  │  │  ├─ core
   │     │  │  │  │  ├─ endpoints
   │     │  │  │  │  │  ├─ pre_configured.py
   │     │  │  │  │  │  ├─ userinfo.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ exceptions.py
   │     │  │  │  │  ├─ grant_types
   │     │  │  │  │  │  ├─ authorization_code.py
   │     │  │  │  │  │  ├─ base.py
   │     │  │  │  │  │  ├─ dispatchers.py
   │     │  │  │  │  │  ├─ hybrid.py
   │     │  │  │  │  │  ├─ implicit.py
   │     │  │  │  │  │  ├─ refresh_token.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ request_validator.py
   │     │  │  │  │  ├─ tokens.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ signals.py
   │     │  ├─ uri_validate.py
   │     │  └─ __init__.py
   │     ├─ oauthlib-3.2.2.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ outcome
   │     │  ├─ py.typed
   │     │  ├─ _impl.py
   │     │  ├─ _util.py
   │     │  ├─ _version.py
   │     │  └─ __init__.py
   │     ├─ outcome-1.3.0.post0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ LICENSE.APACHE2
   │     │  ├─ LICENSE.MIT
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ packaging
   │     │  ├─ licenses
   │     │  │  ├─ _spdx.py
   │     │  │  └─ __init__.py
   │     │  ├─ markers.py
   │     │  ├─ metadata.py
   │     │  ├─ py.typed
   │     │  ├─ requirements.py
   │     │  ├─ specifiers.py
   │     │  ├─ tags.py
   │     │  ├─ utils.py
   │     │  ├─ version.py
   │     │  ├─ _elffile.py
   │     │  ├─ _manylinux.py
   │     │  ├─ _musllinux.py
   │     │  ├─ _parser.py
   │     │  ├─ _structures.py
   │     │  ├─ _tokenizer.py
   │     │  └─ __init__.py
   │     ├─ packaging-24.2.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ LICENSE.APACHE
   │     │  ├─ LICENSE.BSD
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  └─ WHEEL
   │     ├─ pandas
   │     │  ├─ api
   │     │  │  ├─ extensions
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ indexers
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ interchange
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ types
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ typing
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ arrays
   │     │  │  └─ __init__.py
   │     │  ├─ compat
   │     │  │  ├─ compressors.py
   │     │  │  ├─ numpy
   │     │  │  │  ├─ function.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ pickle_compat.py
   │     │  │  ├─ pyarrow.py
   │     │  │  ├─ _constants.py
   │     │  │  ├─ _optional.py
   │     │  │  └─ __init__.py
   │     │  ├─ conftest.py
   │     │  ├─ core
   │     │  │  ├─ accessor.py
   │     │  │  ├─ algorithms.py
   │     │  │  ├─ api.py
   │     │  │  ├─ apply.py
   │     │  │  ├─ arraylike.py
   │     │  │  ├─ arrays
   │     │  │  │  ├─ arrow
   │     │  │  │  │  ├─ accessors.py
   │     │  │  │  │  ├─ array.py
   │     │  │  │  │  ├─ extension_types.py
   │     │  │  │  │  ├─ _arrow_utils.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ base.py
   │     │  │  │  ├─ boolean.py
   │     │  │  │  ├─ categorical.py
   │     │  │  │  ├─ datetimelike.py
   │     │  │  │  ├─ datetimes.py
   │     │  │  │  ├─ floating.py
   │     │  │  │  ├─ integer.py
   │     │  │  │  ├─ interval.py
   │     │  │  │  ├─ masked.py
   │     │  │  │  ├─ numeric.py
   │     │  │  │  ├─ numpy_.py
   │     │  │  │  ├─ period.py
   │     │  │  │  ├─ sparse
   │     │  │  │  │  ├─ accessor.py
   │     │  │  │  │  ├─ array.py
   │     │  │  │  │  ├─ scipy_sparse.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ string_.py
   │     │  │  │  ├─ string_arrow.py
   │     │  │  │  ├─ timedeltas.py
   │     │  │  │  ├─ _arrow_string_mixins.py
   │     │  │  │  ├─ _mixins.py
   │     │  │  │  ├─ _ranges.py
   │     │  │  │  ├─ _utils.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ array_algos
   │     │  │  │  ├─ datetimelike_accumulations.py
   │     │  │  │  ├─ masked_accumulations.py
   │     │  │  │  ├─ masked_reductions.py
   │     │  │  │  ├─ putmask.py
   │     │  │  │  ├─ quantile.py
   │     │  │  │  ├─ replace.py
   │     │  │  │  ├─ take.py
   │     │  │  │  ├─ transforms.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ base.py
   │     │  │  ├─ common.py
   │     │  │  ├─ computation
   │     │  │  │  ├─ align.py
   │     │  │  │  ├─ api.py
   │     │  │  │  ├─ check.py
   │     │  │  │  ├─ common.py
   │     │  │  │  ├─ engines.py
   │     │  │  │  ├─ eval.py
   │     │  │  │  ├─ expr.py
   │     │  │  │  ├─ expressions.py
   │     │  │  │  ├─ ops.py
   │     │  │  │  ├─ parsing.py
   │     │  │  │  ├─ pytables.py
   │     │  │  │  ├─ scope.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ config_init.py
   │     │  │  ├─ construction.py
   │     │  │  ├─ dtypes
   │     │  │  │  ├─ api.py
   │     │  │  │  ├─ astype.py
   │     │  │  │  ├─ base.py
   │     │  │  │  ├─ cast.py
   │     │  │  │  ├─ common.py
   │     │  │  │  ├─ concat.py
   │     │  │  │  ├─ dtypes.py
   │     │  │  │  ├─ generic.py
   │     │  │  │  ├─ inference.py
   │     │  │  │  ├─ missing.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ flags.py
   │     │  │  ├─ frame.py
   │     │  │  ├─ generic.py
   │     │  │  ├─ groupby
   │     │  │  │  ├─ base.py
   │     │  │  │  ├─ categorical.py
   │     │  │  │  ├─ generic.py
   │     │  │  │  ├─ groupby.py
   │     │  │  │  ├─ grouper.py
   │     │  │  │  ├─ indexing.py
   │     │  │  │  ├─ numba_.py
   │     │  │  │  ├─ ops.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ indexers
   │     │  │  │  ├─ objects.py
   │     │  │  │  ├─ utils.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ indexes
   │     │  │  │  ├─ accessors.py
   │     │  │  │  ├─ api.py
   │     │  │  │  ├─ base.py
   │     │  │  │  ├─ category.py
   │     │  │  │  ├─ datetimelike.py
   │     │  │  │  ├─ datetimes.py
   │     │  │  │  ├─ extension.py
   │     │  │  │  ├─ frozen.py
   │     │  │  │  ├─ interval.py
   │     │  │  │  ├─ multi.py
   │     │  │  │  ├─ period.py
   │     │  │  │  ├─ range.py
   │     │  │  │  ├─ timedeltas.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ indexing.py
   │     │  │  ├─ interchange
   │     │  │  │  ├─ buffer.py
   │     │  │  │  ├─ column.py
   │     │  │  │  ├─ dataframe.py
   │     │  │  │  ├─ dataframe_protocol.py
   │     │  │  │  ├─ from_dataframe.py
   │     │  │  │  ├─ utils.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ internals
   │     │  │  │  ├─ api.py
   │     │  │  │  ├─ array_manager.py
   │     │  │  │  ├─ base.py
   │     │  │  │  ├─ blocks.py
   │     │  │  │  ├─ concat.py
   │     │  │  │  ├─ construction.py
   │     │  │  │  ├─ managers.py
   │     │  │  │  ├─ ops.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ methods
   │     │  │  │  ├─ describe.py
   │     │  │  │  ├─ selectn.py
   │     │  │  │  ├─ to_dict.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ missing.py
   │     │  │  ├─ nanops.py
   │     │  │  ├─ ops
   │     │  │  │  ├─ array_ops.py
   │     │  │  │  ├─ common.py
   │     │  │  │  ├─ dispatch.py
   │     │  │  │  ├─ docstrings.py
   │     │  │  │  ├─ invalid.py
   │     │  │  │  ├─ mask_ops.py
   │     │  │  │  ├─ missing.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ resample.py
   │     │  │  ├─ reshape
   │     │  │  │  ├─ api.py
   │     │  │  │  ├─ concat.py
   │     │  │  │  ├─ encoding.py
   │     │  │  │  ├─ melt.py
   │     │  │  │  ├─ merge.py
   │     │  │  │  ├─ pivot.py
   │     │  │  │  ├─ reshape.py
   │     │  │  │  ├─ tile.py
   │     │  │  │  ├─ util.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ roperator.py
   │     │  │  ├─ sample.py
   │     │  │  ├─ series.py
   │     │  │  ├─ shared_docs.py
   │     │  │  ├─ sorting.py
   │     │  │  ├─ sparse
   │     │  │  │  ├─ api.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ strings
   │     │  │  │  ├─ accessor.py
   │     │  │  │  ├─ base.py
   │     │  │  │  ├─ object_array.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ tools
   │     │  │  │  ├─ datetimes.py
   │     │  │  │  ├─ numeric.py
   │     │  │  │  ├─ timedeltas.py
   │     │  │  │  ├─ times.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ util
   │     │  │  │  ├─ hashing.py
   │     │  │  │  ├─ numba_.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ window
   │     │  │  │  ├─ common.py
   │     │  │  │  ├─ doc.py
   │     │  │  │  ├─ ewm.py
   │     │  │  │  ├─ expanding.py
   │     │  │  │  ├─ numba_.py
   │     │  │  │  ├─ online.py
   │     │  │  │  ├─ rolling.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _numba
   │     │  │  │  ├─ executor.py
   │     │  │  │  ├─ extensions.py
   │     │  │  │  ├─ kernels
   │     │  │  │  │  ├─ mean_.py
   │     │  │  │  │  ├─ min_max_.py
   │     │  │  │  │  ├─ shared.py
   │     │  │  │  │  ├─ sum_.py
   │     │  │  │  │  ├─ var_.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ errors
   │     │  │  └─ __init__.py
   │     │  ├─ io
   │     │  │  ├─ api.py
   │     │  │  ├─ clipboard
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ clipboards.py
   │     │  │  ├─ common.py
   │     │  │  ├─ excel
   │     │  │  │  ├─ _base.py
   │     │  │  │  ├─ _calamine.py
   │     │  │  │  ├─ _odfreader.py
   │     │  │  │  ├─ _odswriter.py
   │     │  │  │  ├─ _openpyxl.py
   │     │  │  │  ├─ _pyxlsb.py
   │     │  │  │  ├─ _util.py
   │     │  │  │  ├─ _xlrd.py
   │     │  │  │  ├─ _xlsxwriter.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ feather_format.py
   │     │  │  ├─ formats
   │     │  │  │  ├─ console.py
   │     │  │  │  ├─ css.py
   │     │  │  │  ├─ csvs.py
   │     │  │  │  ├─ excel.py
   │     │  │  │  ├─ format.py
   │     │  │  │  ├─ html.py
   │     │  │  │  ├─ info.py
   │     │  │  │  ├─ printing.py
   │     │  │  │  ├─ string.py
   │     │  │  │  ├─ style.py
   │     │  │  │  ├─ style_render.py
   │     │  │  │  ├─ templates
   │     │  │  │  │  ├─ html.tpl
   │     │  │  │  │  ├─ html_style.tpl
   │     │  │  │  │  ├─ html_table.tpl
   │     │  │  │  │  ├─ latex.tpl
   │     │  │  │  │  ├─ latex_longtable.tpl
   │     │  │  │  │  ├─ latex_table.tpl
   │     │  │  │  │  └─ string.tpl
   │     │  │  │  ├─ xml.py
   │     │  │  │  ├─ _color_data.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ gbq.py
   │     │  │  ├─ html.py
   │     │  │  ├─ json
   │     │  │  │  ├─ _json.py
   │     │  │  │  ├─ _normalize.py
   │     │  │  │  ├─ _table_schema.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ orc.py
   │     │  │  ├─ parquet.py
   │     │  │  ├─ parsers
   │     │  │  │  ├─ arrow_parser_wrapper.py
   │     │  │  │  ├─ base_parser.py
   │     │  │  │  ├─ c_parser_wrapper.py
   │     │  │  │  ├─ python_parser.py
   │     │  │  │  ├─ readers.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ pickle.py
   │     │  │  ├─ pytables.py
   │     │  │  ├─ sas
   │     │  │  │  ├─ sas7bdat.py
   │     │  │  │  ├─ sasreader.py
   │     │  │  │  ├─ sas_constants.py
   │     │  │  │  ├─ sas_xport.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ spss.py
   │     │  │  ├─ sql.py
   │     │  │  ├─ stata.py
   │     │  │  ├─ xml.py
   │     │  │  ├─ _util.py
   │     │  │  └─ __init__.py
   │     │  ├─ plotting
   │     │  │  ├─ _core.py
   │     │  │  ├─ _matplotlib
   │     │  │  │  ├─ boxplot.py
   │     │  │  │  ├─ converter.py
   │     │  │  │  ├─ core.py
   │     │  │  │  ├─ groupby.py
   │     │  │  │  ├─ hist.py
   │     │  │  │  ├─ misc.py
   │     │  │  │  ├─ style.py
   │     │  │  │  ├─ timeseries.py
   │     │  │  │  ├─ tools.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _misc.py
   │     │  │  └─ __init__.py
   │     │  ├─ pyproject.toml
   │     │  ├─ testing.py
   │     │  ├─ tests
   │     │  │  ├─ api
   │     │  │  │  ├─ test_api.py
   │     │  │  │  ├─ test_types.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ apply
   │     │  │  │  ├─ common.py
   │     │  │  │  ├─ test_frame_apply.py
   │     │  │  │  ├─ test_frame_apply_relabeling.py
   │     │  │  │  ├─ test_frame_transform.py
   │     │  │  │  ├─ test_invalid_arg.py
   │     │  │  │  ├─ test_numba.py
   │     │  │  │  ├─ test_series_apply.py
   │     │  │  │  ├─ test_series_apply_relabeling.py
   │     │  │  │  ├─ test_series_transform.py
   │     │  │  │  ├─ test_str.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ arithmetic
   │     │  │  │  ├─ common.py
   │     │  │  │  ├─ conftest.py
   │     │  │  │  ├─ test_array_ops.py
   │     │  │  │  ├─ test_categorical.py
   │     │  │  │  ├─ test_datetime64.py
   │     │  │  │  ├─ test_interval.py
   │     │  │  │  ├─ test_numeric.py
   │     │  │  │  ├─ test_object.py
   │     │  │  │  ├─ test_period.py
   │     │  │  │  ├─ test_timedelta64.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ arrays
   │     │  │  │  ├─ boolean
   │     │  │  │  │  ├─ test_arithmetic.py
   │     │  │  │  │  ├─ test_astype.py
   │     │  │  │  │  ├─ test_comparison.py
   │     │  │  │  │  ├─ test_construction.py
   │     │  │  │  │  ├─ test_function.py
   │     │  │  │  │  ├─ test_indexing.py
   │     │  │  │  │  ├─ test_logical.py
   │     │  │  │  │  ├─ test_ops.py
   │     │  │  │  │  ├─ test_reduction.py
   │     │  │  │  │  ├─ test_repr.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ categorical
   │     │  │  │  │  ├─ test_algos.py
   │     │  │  │  │  ├─ test_analytics.py
   │     │  │  │  │  ├─ test_api.py
   │     │  │  │  │  ├─ test_astype.py
   │     │  │  │  │  ├─ test_constructors.py
   │     │  │  │  │  ├─ test_dtypes.py
   │     │  │  │  │  ├─ test_indexing.py
   │     │  │  │  │  ├─ test_map.py
   │     │  │  │  │  ├─ test_missing.py
   │     │  │  │  │  ├─ test_operators.py
   │     │  │  │  │  ├─ test_replace.py
   │     │  │  │  │  ├─ test_repr.py
   │     │  │  │  │  ├─ test_sorting.py
   │     │  │  │  │  ├─ test_subclass.py
   │     │  │  │  │  ├─ test_take.py
   │     │  │  │  │  ├─ test_warnings.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ datetimes
   │     │  │  │  │  ├─ test_constructors.py
   │     │  │  │  │  ├─ test_cumulative.py
   │     │  │  │  │  ├─ test_reductions.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ floating
   │     │  │  │  │  ├─ conftest.py
   │     │  │  │  │  ├─ test_arithmetic.py
   │     │  │  │  │  ├─ test_astype.py
   │     │  │  │  │  ├─ test_comparison.py
   │     │  │  │  │  ├─ test_concat.py
   │     │  │  │  │  ├─ test_construction.py
   │     │  │  │  │  ├─ test_contains.py
   │     │  │  │  │  ├─ test_function.py
   │     │  │  │  │  ├─ test_repr.py
   │     │  │  │  │  ├─ test_to_numpy.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ integer
   │     │  │  │  │  ├─ conftest.py
   │     │  │  │  │  ├─ test_arithmetic.py
   │     │  │  │  │  ├─ test_comparison.py
   │     │  │  │  │  ├─ test_concat.py
   │     │  │  │  │  ├─ test_construction.py
   │     │  │  │  │  ├─ test_dtypes.py
   │     │  │  │  │  ├─ test_function.py
   │     │  │  │  │  ├─ test_indexing.py
   │     │  │  │  │  ├─ test_reduction.py
   │     │  │  │  │  ├─ test_repr.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ interval
   │     │  │  │  │  ├─ test_astype.py
   │     │  │  │  │  ├─ test_formats.py
   │     │  │  │  │  ├─ test_interval.py
   │     │  │  │  │  ├─ test_interval_pyarrow.py
   │     │  │  │  │  ├─ test_overlaps.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ masked
   │     │  │  │  │  ├─ test_arithmetic.py
   │     │  │  │  │  ├─ test_arrow_compat.py
   │     │  │  │  │  ├─ test_function.py
   │     │  │  │  │  ├─ test_indexing.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ masked_shared.py
   │     │  │  │  ├─ numpy_
   │     │  │  │  │  ├─ test_indexing.py
   │     │  │  │  │  ├─ test_numpy.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ period
   │     │  │  │  │  ├─ test_arrow_compat.py
   │     │  │  │  │  ├─ test_astype.py
   │     │  │  │  │  ├─ test_constructors.py
   │     │  │  │  │  ├─ test_reductions.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ sparse
   │     │  │  │  │  ├─ test_accessor.py
   │     │  │  │  │  ├─ test_arithmetics.py
   │     │  │  │  │  ├─ test_array.py
   │     │  │  │  │  ├─ test_astype.py
   │     │  │  │  │  ├─ test_combine_concat.py
   │     │  │  │  │  ├─ test_constructors.py
   │     │  │  │  │  ├─ test_dtype.py
   │     │  │  │  │  ├─ test_indexing.py
   │     │  │  │  │  ├─ test_libsparse.py
   │     │  │  │  │  ├─ test_reductions.py
   │     │  │  │  │  ├─ test_unary.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ string_
   │     │  │  │  │  ├─ test_string.py
   │     │  │  │  │  ├─ test_string_arrow.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_array.py
   │     │  │  │  ├─ test_datetimelike.py
   │     │  │  │  ├─ test_datetimes.py
   │     │  │  │  ├─ test_ndarray_backed.py
   │     │  │  │  ├─ test_period.py
   │     │  │  │  ├─ test_timedeltas.py
   │     │  │  │  ├─ timedeltas
   │     │  │  │  │  ├─ test_constructors.py
   │     │  │  │  │  ├─ test_cumulative.py
   │     │  │  │  │  ├─ test_reductions.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ base
   │     │  │  │  ├─ common.py
   │     │  │  │  ├─ test_constructors.py
   │     │  │  │  ├─ test_conversion.py
   │     │  │  │  ├─ test_fillna.py
   │     │  │  │  ├─ test_misc.py
   │     │  │  │  ├─ test_transpose.py
   │     │  │  │  ├─ test_unique.py
   │     │  │  │  ├─ test_value_counts.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ computation
   │     │  │  │  ├─ test_compat.py
   │     │  │  │  ├─ test_eval.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ config
   │     │  │  │  ├─ test_config.py
   │     │  │  │  ├─ test_localization.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ construction
   │     │  │  │  ├─ test_extract_array.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ copy_view
   │     │  │  │  ├─ index
   │     │  │  │  │  ├─ test_datetimeindex.py
   │     │  │  │  │  ├─ test_index.py
   │     │  │  │  │  ├─ test_periodindex.py
   │     │  │  │  │  ├─ test_timedeltaindex.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_array.py
   │     │  │  │  ├─ test_astype.py
   │     │  │  │  ├─ test_chained_assignment_deprecation.py
   │     │  │  │  ├─ test_clip.py
   │     │  │  │  ├─ test_constructors.py
   │     │  │  │  ├─ test_core_functionalities.py
   │     │  │  │  ├─ test_functions.py
   │     │  │  │  ├─ test_indexing.py
   │     │  │  │  ├─ test_internals.py
   │     │  │  │  ├─ test_interp_fillna.py
   │     │  │  │  ├─ test_methods.py
   │     │  │  │  ├─ test_replace.py
   │     │  │  │  ├─ test_setitem.py
   │     │  │  │  ├─ test_util.py
   │     │  │  │  ├─ util.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ dtypes
   │     │  │  │  ├─ cast
   │     │  │  │  │  ├─ test_can_hold_element.py
   │     │  │  │  │  ├─ test_construct_from_scalar.py
   │     │  │  │  │  ├─ test_construct_ndarray.py
   │     │  │  │  │  ├─ test_construct_object_arr.py
   │     │  │  │  │  ├─ test_dict_compat.py
   │     │  │  │  │  ├─ test_downcast.py
   │     │  │  │  │  ├─ test_find_common_type.py
   │     │  │  │  │  ├─ test_infer_datetimelike.py
   │     │  │  │  │  ├─ test_infer_dtype.py
   │     │  │  │  │  ├─ test_maybe_box_native.py
   │     │  │  │  │  ├─ test_promote.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_common.py
   │     │  │  │  ├─ test_concat.py
   │     │  │  │  ├─ test_dtypes.py
   │     │  │  │  ├─ test_generic.py
   │     │  │  │  ├─ test_inference.py
   │     │  │  │  ├─ test_missing.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ extension
   │     │  │  │  ├─ array_with_attr
   │     │  │  │  │  ├─ array.py
   │     │  │  │  │  ├─ test_array_with_attr.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ base
   │     │  │  │  │  ├─ accumulate.py
   │     │  │  │  │  ├─ base.py
   │     │  │  │  │  ├─ casting.py
   │     │  │  │  │  ├─ constructors.py
   │     │  │  │  │  ├─ dim2.py
   │     │  │  │  │  ├─ dtype.py
   │     │  │  │  │  ├─ getitem.py
   │     │  │  │  │  ├─ groupby.py
   │     │  │  │  │  ├─ index.py
   │     │  │  │  │  ├─ interface.py
   │     │  │  │  │  ├─ io.py
   │     │  │  │  │  ├─ methods.py
   │     │  │  │  │  ├─ missing.py
   │     │  │  │  │  ├─ ops.py
   │     │  │  │  │  ├─ printing.py
   │     │  │  │  │  ├─ reduce.py
   │     │  │  │  │  ├─ reshaping.py
   │     │  │  │  │  ├─ setitem.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ conftest.py
   │     │  │  │  ├─ date
   │     │  │  │  │  ├─ array.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ decimal
   │     │  │  │  │  ├─ array.py
   │     │  │  │  │  ├─ test_decimal.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ json
   │     │  │  │  │  ├─ array.py
   │     │  │  │  │  ├─ test_json.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ list
   │     │  │  │  │  ├─ array.py
   │     │  │  │  │  ├─ test_list.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_arrow.py
   │     │  │  │  ├─ test_categorical.py
   │     │  │  │  ├─ test_common.py
   │     │  │  │  ├─ test_datetime.py
   │     │  │  │  ├─ test_extension.py
   │     │  │  │  ├─ test_interval.py
   │     │  │  │  ├─ test_masked.py
   │     │  │  │  ├─ test_numpy.py
   │     │  │  │  ├─ test_period.py
   │     │  │  │  ├─ test_sparse.py
   │     │  │  │  ├─ test_string.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ frame
   │     │  │  │  ├─ common.py
   │     │  │  │  ├─ conftest.py
   │     │  │  │  ├─ constructors
   │     │  │  │  │  ├─ test_from_dict.py
   │     │  │  │  │  ├─ test_from_records.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ indexing
   │     │  │  │  │  ├─ test_coercion.py
   │     │  │  │  │  ├─ test_delitem.py
   │     │  │  │  │  ├─ test_get.py
   │     │  │  │  │  ├─ test_getitem.py
   │     │  │  │  │  ├─ test_get_value.py
   │     │  │  │  │  ├─ test_indexing.py
   │     │  │  │  │  ├─ test_insert.py
   │     │  │  │  │  ├─ test_mask.py
   │     │  │  │  │  ├─ test_setitem.py
   │     │  │  │  │  ├─ test_set_value.py
   │     │  │  │  │  ├─ test_take.py
   │     │  │  │  │  ├─ test_where.py
   │     │  │  │  │  ├─ test_xs.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ methods
   │     │  │  │  │  ├─ test_add_prefix_suffix.py
   │     │  │  │  │  ├─ test_align.py
   │     │  │  │  │  ├─ test_asfreq.py
   │     │  │  │  │  ├─ test_asof.py
   │     │  │  │  │  ├─ test_assign.py
   │     │  │  │  │  ├─ test_astype.py
   │     │  │  │  │  ├─ test_at_time.py
   │     │  │  │  │  ├─ test_between_time.py
   │     │  │  │  │  ├─ test_clip.py
   │     │  │  │  │  ├─ test_combine.py
   │     │  │  │  │  ├─ test_combine_first.py
   │     │  │  │  │  ├─ test_compare.py
   │     │  │  │  │  ├─ test_convert_dtypes.py
   │     │  │  │  │  ├─ test_copy.py
   │     │  │  │  │  ├─ test_count.py
   │     │  │  │  │  ├─ test_cov_corr.py
   │     │  │  │  │  ├─ test_describe.py
   │     │  │  │  │  ├─ test_diff.py
   │     │  │  │  │  ├─ test_dot.py
   │     │  │  │  │  ├─ test_drop.py
   │     │  │  │  │  ├─ test_droplevel.py
   │     │  │  │  │  ├─ test_dropna.py
   │     │  │  │  │  ├─ test_drop_duplicates.py
   │     │  │  │  │  ├─ test_dtypes.py
   │     │  │  │  │  ├─ test_duplicated.py
   │     │  │  │  │  ├─ test_equals.py
   │     │  │  │  │  ├─ test_explode.py
   │     │  │  │  │  ├─ test_fillna.py
   │     │  │  │  │  ├─ test_filter.py
   │     │  │  │  │  ├─ test_first_and_last.py
   │     │  │  │  │  ├─ test_first_valid_index.py
   │     │  │  │  │  ├─ test_get_numeric_data.py
   │     │  │  │  │  ├─ test_head_tail.py
   │     │  │  │  │  ├─ test_infer_objects.py
   │     │  │  │  │  ├─ test_info.py
   │     │  │  │  │  ├─ test_interpolate.py
   │     │  │  │  │  ├─ test_isetitem.py
   │     │  │  │  │  ├─ test_isin.py
   │     │  │  │  │  ├─ test_is_homogeneous_dtype.py
   │     │  │  │  │  ├─ test_iterrows.py
   │     │  │  │  │  ├─ test_join.py
   │     │  │  │  │  ├─ test_map.py
   │     │  │  │  │  ├─ test_matmul.py
   │     │  │  │  │  ├─ test_nlargest.py
   │     │  │  │  │  ├─ test_pct_change.py
   │     │  │  │  │  ├─ test_pipe.py
   │     │  │  │  │  ├─ test_pop.py
   │     │  │  │  │  ├─ test_quantile.py
   │     │  │  │  │  ├─ test_rank.py
   │     │  │  │  │  ├─ test_reindex.py
   │     │  │  │  │  ├─ test_reindex_like.py
   │     │  │  │  │  ├─ test_rename.py
   │     │  │  │  │  ├─ test_rename_axis.py
   │     │  │  │  │  ├─ test_reorder_levels.py
   │     │  │  │  │  ├─ test_replace.py
   │     │  │  │  │  ├─ test_reset_index.py
   │     │  │  │  │  ├─ test_round.py
   │     │  │  │  │  ├─ test_sample.py
   │     │  │  │  │  ├─ test_select_dtypes.py
   │     │  │  │  │  ├─ test_set_axis.py
   │     │  │  │  │  ├─ test_set_index.py
   │     │  │  │  │  ├─ test_shift.py
   │     │  │  │  │  ├─ test_size.py
   │     │  │  │  │  ├─ test_sort_index.py
   │     │  │  │  │  ├─ test_sort_values.py
   │     │  │  │  │  ├─ test_swapaxes.py
   │     │  │  │  │  ├─ test_swaplevel.py
   │     │  │  │  │  ├─ test_to_csv.py
   │     │  │  │  │  ├─ test_to_dict.py
   │     │  │  │  │  ├─ test_to_dict_of_blocks.py
   │     │  │  │  │  ├─ test_to_numpy.py
   │     │  │  │  │  ├─ test_to_period.py
   │     │  │  │  │  ├─ test_to_records.py
   │     │  │  │  │  ├─ test_to_timestamp.py
   │     │  │  │  │  ├─ test_transpose.py
   │     │  │  │  │  ├─ test_truncate.py
   │     │  │  │  │  ├─ test_tz_convert.py
   │     │  │  │  │  ├─ test_tz_localize.py
   │     │  │  │  │  ├─ test_update.py
   │     │  │  │  │  ├─ test_values.py
   │     │  │  │  │  ├─ test_value_counts.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_alter_axes.py
   │     │  │  │  ├─ test_api.py
   │     │  │  │  ├─ test_arithmetic.py
   │     │  │  │  ├─ test_arrow_interface.py
   │     │  │  │  ├─ test_block_internals.py
   │     │  │  │  ├─ test_constructors.py
   │     │  │  │  ├─ test_cumulative.py
   │     │  │  │  ├─ test_iteration.py
   │     │  │  │  ├─ test_logical_ops.py
   │     │  │  │  ├─ test_nonunique_indexes.py
   │     │  │  │  ├─ test_npfuncs.py
   │     │  │  │  ├─ test_query_eval.py
   │     │  │  │  ├─ test_reductions.py
   │     │  │  │  ├─ test_repr.py
   │     │  │  │  ├─ test_stack_unstack.py
   │     │  │  │  ├─ test_subclass.py
   │     │  │  │  ├─ test_ufunc.py
   │     │  │  │  ├─ test_unary.py
   │     │  │  │  ├─ test_validate.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ generic
   │     │  │  │  ├─ test_duplicate_labels.py
   │     │  │  │  ├─ test_finalize.py
   │     │  │  │  ├─ test_frame.py
   │     │  │  │  ├─ test_generic.py
   │     │  │  │  ├─ test_label_or_level_utils.py
   │     │  │  │  ├─ test_series.py
   │     │  │  │  ├─ test_to_xarray.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ groupby
   │     │  │  │  ├─ aggregate
   │     │  │  │  │  ├─ test_aggregate.py
   │     │  │  │  │  ├─ test_cython.py
   │     │  │  │  │  ├─ test_numba.py
   │     │  │  │  │  ├─ test_other.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ conftest.py
   │     │  │  │  ├─ methods
   │     │  │  │  │  ├─ test_corrwith.py
   │     │  │  │  │  ├─ test_describe.py
   │     │  │  │  │  ├─ test_groupby_shift_diff.py
   │     │  │  │  │  ├─ test_is_monotonic.py
   │     │  │  │  │  ├─ test_nlargest_nsmallest.py
   │     │  │  │  │  ├─ test_nth.py
   │     │  │  │  │  ├─ test_quantile.py
   │     │  │  │  │  ├─ test_rank.py
   │     │  │  │  │  ├─ test_sample.py
   │     │  │  │  │  ├─ test_size.py
   │     │  │  │  │  ├─ test_skew.py
   │     │  │  │  │  ├─ test_value_counts.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_all_methods.py
   │     │  │  │  ├─ test_api.py
   │     │  │  │  ├─ test_apply.py
   │     │  │  │  ├─ test_apply_mutate.py
   │     │  │  │  ├─ test_bin_groupby.py
   │     │  │  │  ├─ test_categorical.py
   │     │  │  │  ├─ test_counting.py
   │     │  │  │  ├─ test_cumulative.py
   │     │  │  │  ├─ test_filters.py
   │     │  │  │  ├─ test_groupby.py
   │     │  │  │  ├─ test_groupby_dropna.py
   │     │  │  │  ├─ test_groupby_subclass.py
   │     │  │  │  ├─ test_grouping.py
   │     │  │  │  ├─ test_indexing.py
   │     │  │  │  ├─ test_index_as_string.py
   │     │  │  │  ├─ test_libgroupby.py
   │     │  │  │  ├─ test_missing.py
   │     │  │  │  ├─ test_numba.py
   │     │  │  │  ├─ test_numeric_only.py
   │     │  │  │  ├─ test_pipe.py
   │     │  │  │  ├─ test_raises.py
   │     │  │  │  ├─ test_reductions.py
   │     │  │  │  ├─ test_timegrouper.py
   │     │  │  │  ├─ transform
   │     │  │  │  │  ├─ test_numba.py
   │     │  │  │  │  ├─ test_transform.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ indexes
   │     │  │  │  ├─ base_class
   │     │  │  │  │  ├─ test_constructors.py
   │     │  │  │  │  ├─ test_formats.py
   │     │  │  │  │  ├─ test_indexing.py
   │     │  │  │  │  ├─ test_pickle.py
   │     │  │  │  │  ├─ test_reshape.py
   │     │  │  │  │  ├─ test_setops.py
   │     │  │  │  │  ├─ test_where.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ categorical
   │     │  │  │  │  ├─ test_append.py
   │     │  │  │  │  ├─ test_astype.py
   │     │  │  │  │  ├─ test_category.py
   │     │  │  │  │  ├─ test_constructors.py
   │     │  │  │  │  ├─ test_equals.py
   │     │  │  │  │  ├─ test_fillna.py
   │     │  │  │  │  ├─ test_formats.py
   │     │  │  │  │  ├─ test_indexing.py
   │     │  │  │  │  ├─ test_map.py
   │     │  │  │  │  ├─ test_reindex.py
   │     │  │  │  │  ├─ test_setops.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ conftest.py
   │     │  │  │  ├─ datetimelike_
   │     │  │  │  │  ├─ test_drop_duplicates.py
   │     │  │  │  │  ├─ test_equals.py
   │     │  │  │  │  ├─ test_indexing.py
   │     │  │  │  │  ├─ test_is_monotonic.py
   │     │  │  │  │  ├─ test_nat.py
   │     │  │  │  │  ├─ test_sort_values.py
   │     │  │  │  │  ├─ test_value_counts.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ datetimes
   │     │  │  │  │  ├─ methods
   │     │  │  │  │  │  ├─ test_asof.py
   │     │  │  │  │  │  ├─ test_astype.py
   │     │  │  │  │  │  ├─ test_delete.py
   │     │  │  │  │  │  ├─ test_factorize.py
   │     │  │  │  │  │  ├─ test_fillna.py
   │     │  │  │  │  │  ├─ test_insert.py
   │     │  │  │  │  │  ├─ test_isocalendar.py
   │     │  │  │  │  │  ├─ test_map.py
   │     │  │  │  │  │  ├─ test_normalize.py
   │     │  │  │  │  │  ├─ test_repeat.py
   │     │  │  │  │  │  ├─ test_resolution.py
   │     │  │  │  │  │  ├─ test_round.py
   │     │  │  │  │  │  ├─ test_shift.py
   │     │  │  │  │  │  ├─ test_snap.py
   │     │  │  │  │  │  ├─ test_to_frame.py
   │     │  │  │  │  │  ├─ test_to_julian_date.py
   │     │  │  │  │  │  ├─ test_to_period.py
   │     │  │  │  │  │  ├─ test_to_pydatetime.py
   │     │  │  │  │  │  ├─ test_to_series.py
   │     │  │  │  │  │  ├─ test_tz_convert.py
   │     │  │  │  │  │  ├─ test_tz_localize.py
   │     │  │  │  │  │  ├─ test_unique.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ test_arithmetic.py
   │     │  │  │  │  ├─ test_constructors.py
   │     │  │  │  │  ├─ test_datetime.py
   │     │  │  │  │  ├─ test_date_range.py
   │     │  │  │  │  ├─ test_formats.py
   │     │  │  │  │  ├─ test_freq_attr.py
   │     │  │  │  │  ├─ test_indexing.py
   │     │  │  │  │  ├─ test_iter.py
   │     │  │  │  │  ├─ test_join.py
   │     │  │  │  │  ├─ test_npfuncs.py
   │     │  │  │  │  ├─ test_ops.py
   │     │  │  │  │  ├─ test_partial_slicing.py
   │     │  │  │  │  ├─ test_pickle.py
   │     │  │  │  │  ├─ test_reindex.py
   │     │  │  │  │  ├─ test_scalar_compat.py
   │     │  │  │  │  ├─ test_setops.py
   │     │  │  │  │  ├─ test_timezones.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ interval
   │     │  │  │  │  ├─ test_astype.py
   │     │  │  │  │  ├─ test_constructors.py
   │     │  │  │  │  ├─ test_equals.py
   │     │  │  │  │  ├─ test_formats.py
   │     │  │  │  │  ├─ test_indexing.py
   │     │  │  │  │  ├─ test_interval.py
   │     │  │  │  │  ├─ test_interval_range.py
   │     │  │  │  │  ├─ test_interval_tree.py
   │     │  │  │  │  ├─ test_join.py
   │     │  │  │  │  ├─ test_pickle.py
   │     │  │  │  │  ├─ test_setops.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ multi
   │     │  │  │  │  ├─ conftest.py
   │     │  │  │  │  ├─ test_analytics.py
   │     │  │  │  │  ├─ test_astype.py
   │     │  │  │  │  ├─ test_compat.py
   │     │  │  │  │  ├─ test_constructors.py
   │     │  │  │  │  ├─ test_conversion.py
   │     │  │  │  │  ├─ test_copy.py
   │     │  │  │  │  ├─ test_drop.py
   │     │  │  │  │  ├─ test_duplicates.py
   │     │  │  │  │  ├─ test_equivalence.py
   │     │  │  │  │  ├─ test_formats.py
   │     │  │  │  │  ├─ test_get_level_values.py
   │     │  │  │  │  ├─ test_get_set.py
   │     │  │  │  │  ├─ test_indexing.py
   │     │  │  │  │  ├─ test_integrity.py
   │     │  │  │  │  ├─ test_isin.py
   │     │  │  │  │  ├─ test_join.py
   │     │  │  │  │  ├─ test_lexsort.py
   │     │  │  │  │  ├─ test_missing.py
   │     │  │  │  │  ├─ test_monotonic.py
   │     │  │  │  │  ├─ test_names.py
   │     │  │  │  │  ├─ test_partial_indexing.py
   │     │  │  │  │  ├─ test_pickle.py
   │     │  │  │  │  ├─ test_reindex.py
   │     │  │  │  │  ├─ test_reshape.py
   │     │  │  │  │  ├─ test_setops.py
   │     │  │  │  │  ├─ test_sorting.py
   │     │  │  │  │  ├─ test_take.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ numeric
   │     │  │  │  │  ├─ test_astype.py
   │     │  │  │  │  ├─ test_indexing.py
   │     │  │  │  │  ├─ test_join.py
   │     │  │  │  │  ├─ test_numeric.py
   │     │  │  │  │  ├─ test_setops.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ object
   │     │  │  │  │  ├─ test_astype.py
   │     │  │  │  │  ├─ test_indexing.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ period
   │     │  │  │  │  ├─ methods
   │     │  │  │  │  │  ├─ test_asfreq.py
   │     │  │  │  │  │  ├─ test_astype.py
   │     │  │  │  │  │  ├─ test_factorize.py
   │     │  │  │  │  │  ├─ test_fillna.py
   │     │  │  │  │  │  ├─ test_insert.py
   │     │  │  │  │  │  ├─ test_is_full.py
   │     │  │  │  │  │  ├─ test_repeat.py
   │     │  │  │  │  │  ├─ test_shift.py
   │     │  │  │  │  │  ├─ test_to_timestamp.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ test_constructors.py
   │     │  │  │  │  ├─ test_formats.py
   │     │  │  │  │  ├─ test_freq_attr.py
   │     │  │  │  │  ├─ test_indexing.py
   │     │  │  │  │  ├─ test_join.py
   │     │  │  │  │  ├─ test_monotonic.py
   │     │  │  │  │  ├─ test_partial_slicing.py
   │     │  │  │  │  ├─ test_period.py
   │     │  │  │  │  ├─ test_period_range.py
   │     │  │  │  │  ├─ test_pickle.py
   │     │  │  │  │  ├─ test_resolution.py
   │     │  │  │  │  ├─ test_scalar_compat.py
   │     │  │  │  │  ├─ test_searchsorted.py
   │     │  │  │  │  ├─ test_setops.py
   │     │  │  │  │  ├─ test_tools.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ ranges
   │     │  │  │  │  ├─ test_constructors.py
   │     │  │  │  │  ├─ test_indexing.py
   │     │  │  │  │  ├─ test_join.py
   │     │  │  │  │  ├─ test_range.py
   │     │  │  │  │  ├─ test_setops.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_any_index.py
   │     │  │  │  ├─ test_base.py
   │     │  │  │  ├─ test_common.py
   │     │  │  │  ├─ test_datetimelike.py
   │     │  │  │  ├─ test_engines.py
   │     │  │  │  ├─ test_frozen.py
   │     │  │  │  ├─ test_indexing.py
   │     │  │  │  ├─ test_index_new.py
   │     │  │  │  ├─ test_numpy_compat.py
   │     │  │  │  ├─ test_old_base.py
   │     │  │  │  ├─ test_setops.py
   │     │  │  │  ├─ test_subclass.py
   │     │  │  │  ├─ timedeltas
   │     │  │  │  │  ├─ methods
   │     │  │  │  │  │  ├─ test_astype.py
   │     │  │  │  │  │  ├─ test_factorize.py
   │     │  │  │  │  │  ├─ test_fillna.py
   │     │  │  │  │  │  ├─ test_insert.py
   │     │  │  │  │  │  ├─ test_repeat.py
   │     │  │  │  │  │  ├─ test_shift.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ test_arithmetic.py
   │     │  │  │  │  ├─ test_constructors.py
   │     │  │  │  │  ├─ test_delete.py
   │     │  │  │  │  ├─ test_formats.py
   │     │  │  │  │  ├─ test_freq_attr.py
   │     │  │  │  │  ├─ test_indexing.py
   │     │  │  │  │  ├─ test_join.py
   │     │  │  │  │  ├─ test_ops.py
   │     │  │  │  │  ├─ test_pickle.py
   │     │  │  │  │  ├─ test_scalar_compat.py
   │     │  │  │  │  ├─ test_searchsorted.py
   │     │  │  │  │  ├─ test_setops.py
   │     │  │  │  │  ├─ test_timedelta.py
   │     │  │  │  │  ├─ test_timedelta_range.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ indexing
   │     │  │  │  ├─ common.py
   │     │  │  │  ├─ conftest.py
   │     │  │  │  ├─ interval
   │     │  │  │  │  ├─ test_interval.py
   │     │  │  │  │  ├─ test_interval_new.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ multiindex
   │     │  │  │  │  ├─ test_chaining_and_caching.py
   │     │  │  │  │  ├─ test_datetime.py
   │     │  │  │  │  ├─ test_getitem.py
   │     │  │  │  │  ├─ test_iloc.py
   │     │  │  │  │  ├─ test_indexing_slow.py
   │     │  │  │  │  ├─ test_loc.py
   │     │  │  │  │  ├─ test_multiindex.py
   │     │  │  │  │  ├─ test_partial.py
   │     │  │  │  │  ├─ test_setitem.py
   │     │  │  │  │  ├─ test_slice.py
   │     │  │  │  │  ├─ test_sorted.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_at.py
   │     │  │  │  ├─ test_categorical.py
   │     │  │  │  ├─ test_chaining_and_caching.py
   │     │  │  │  ├─ test_check_indexer.py
   │     │  │  │  ├─ test_coercion.py
   │     │  │  │  ├─ test_datetime.py
   │     │  │  │  ├─ test_floats.py
   │     │  │  │  ├─ test_iat.py
   │     │  │  │  ├─ test_iloc.py
   │     │  │  │  ├─ test_indexers.py
   │     │  │  │  ├─ test_indexing.py
   │     │  │  │  ├─ test_loc.py
   │     │  │  │  ├─ test_na_indexing.py
   │     │  │  │  ├─ test_partial.py
   │     │  │  │  ├─ test_scalar.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ interchange
   │     │  │  │  ├─ test_impl.py
   │     │  │  │  ├─ test_spec_conformance.py
   │     │  │  │  ├─ test_utils.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ internals
   │     │  │  │  ├─ test_api.py
   │     │  │  │  ├─ test_internals.py
   │     │  │  │  ├─ test_managers.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ io
   │     │  │  │  ├─ conftest.py
   │     │  │  │  ├─ excel
   │     │  │  │  │  ├─ test_odf.py
   │     │  │  │  │  ├─ test_odswriter.py
   │     │  │  │  │  ├─ test_openpyxl.py
   │     │  │  │  │  ├─ test_readers.py
   │     │  │  │  │  ├─ test_style.py
   │     │  │  │  │  ├─ test_writers.py
   │     │  │  │  │  ├─ test_xlrd.py
   │     │  │  │  │  ├─ test_xlsxwriter.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ formats
   │     │  │  │  │  ├─ style
   │     │  │  │  │  │  ├─ test_bar.py
   │     │  │  │  │  │  ├─ test_exceptions.py
   │     │  │  │  │  │  ├─ test_format.py
   │     │  │  │  │  │  ├─ test_highlight.py
   │     │  │  │  │  │  ├─ test_html.py
   │     │  │  │  │  │  ├─ test_matplotlib.py
   │     │  │  │  │  │  ├─ test_non_unique.py
   │     │  │  │  │  │  ├─ test_style.py
   │     │  │  │  │  │  ├─ test_tooltip.py
   │     │  │  │  │  │  ├─ test_to_latex.py
   │     │  │  │  │  │  ├─ test_to_string.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ test_console.py
   │     │  │  │  │  ├─ test_css.py
   │     │  │  │  │  ├─ test_eng_formatting.py
   │     │  │  │  │  ├─ test_format.py
   │     │  │  │  │  ├─ test_ipython_compat.py
   │     │  │  │  │  ├─ test_printing.py
   │     │  │  │  │  ├─ test_to_csv.py
   │     │  │  │  │  ├─ test_to_excel.py
   │     │  │  │  │  ├─ test_to_html.py
   │     │  │  │  │  ├─ test_to_latex.py
   │     │  │  │  │  ├─ test_to_markdown.py
   │     │  │  │  │  ├─ test_to_string.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ generate_legacy_storage_files.py
   │     │  │  │  ├─ json
   │     │  │  │  │  ├─ conftest.py
   │     │  │  │  │  ├─ test_compression.py
   │     │  │  │  │  ├─ test_deprecated_kwargs.py
   │     │  │  │  │  ├─ test_json_table_schema.py
   │     │  │  │  │  ├─ test_json_table_schema_ext_dtype.py
   │     │  │  │  │  ├─ test_normalize.py
   │     │  │  │  │  ├─ test_pandas.py
   │     │  │  │  │  ├─ test_readlines.py
   │     │  │  │  │  ├─ test_ujson.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ parser
   │     │  │  │  │  ├─ common
   │     │  │  │  │  │  ├─ test_chunksize.py
   │     │  │  │  │  │  ├─ test_common_basic.py
   │     │  │  │  │  │  ├─ test_data_list.py
   │     │  │  │  │  │  ├─ test_decimal.py
   │     │  │  │  │  │  ├─ test_file_buffer_url.py
   │     │  │  │  │  │  ├─ test_float.py
   │     │  │  │  │  │  ├─ test_index.py
   │     │  │  │  │  │  ├─ test_inf.py
   │     │  │  │  │  │  ├─ test_ints.py
   │     │  │  │  │  │  ├─ test_iterator.py
   │     │  │  │  │  │  ├─ test_read_errors.py
   │     │  │  │  │  │  ├─ test_verbose.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ conftest.py
   │     │  │  │  │  ├─ dtypes
   │     │  │  │  │  │  ├─ test_categorical.py
   │     │  │  │  │  │  ├─ test_dtypes_basic.py
   │     │  │  │  │  │  ├─ test_empty.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ test_comment.py
   │     │  │  │  │  ├─ test_compression.py
   │     │  │  │  │  ├─ test_concatenate_chunks.py
   │     │  │  │  │  ├─ test_converters.py
   │     │  │  │  │  ├─ test_c_parser_only.py
   │     │  │  │  │  ├─ test_dialect.py
   │     │  │  │  │  ├─ test_encoding.py
   │     │  │  │  │  ├─ test_header.py
   │     │  │  │  │  ├─ test_index_col.py
   │     │  │  │  │  ├─ test_mangle_dupes.py
   │     │  │  │  │  ├─ test_multi_thread.py
   │     │  │  │  │  ├─ test_na_values.py
   │     │  │  │  │  ├─ test_network.py
   │     │  │  │  │  ├─ test_parse_dates.py
   │     │  │  │  │  ├─ test_python_parser_only.py
   │     │  │  │  │  ├─ test_quoting.py
   │     │  │  │  │  ├─ test_read_fwf.py
   │     │  │  │  │  ├─ test_skiprows.py
   │     │  │  │  │  ├─ test_textreader.py
   │     │  │  │  │  ├─ test_unsupported.py
   │     │  │  │  │  ├─ test_upcast.py
   │     │  │  │  │  ├─ usecols
   │     │  │  │  │  │  ├─ test_parse_dates.py
   │     │  │  │  │  │  ├─ test_strings.py
   │     │  │  │  │  │  ├─ test_usecols_basic.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ pytables
   │     │  │  │  │  ├─ common.py
   │     │  │  │  │  ├─ conftest.py
   │     │  │  │  │  ├─ test_append.py
   │     │  │  │  │  ├─ test_categorical.py
   │     │  │  │  │  ├─ test_compat.py
   │     │  │  │  │  ├─ test_complex.py
   │     │  │  │  │  ├─ test_errors.py
   │     │  │  │  │  ├─ test_file_handling.py
   │     │  │  │  │  ├─ test_keys.py
   │     │  │  │  │  ├─ test_put.py
   │     │  │  │  │  ├─ test_pytables_missing.py
   │     │  │  │  │  ├─ test_read.py
   │     │  │  │  │  ├─ test_retain_attributes.py
   │     │  │  │  │  ├─ test_round_trip.py
   │     │  │  │  │  ├─ test_select.py
   │     │  │  │  │  ├─ test_store.py
   │     │  │  │  │  ├─ test_subclass.py
   │     │  │  │  │  ├─ test_timezones.py
   │     │  │  │  │  ├─ test_time_series.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ sas
   │     │  │  │  │  ├─ test_byteswap.py
   │     │  │  │  │  ├─ test_sas.py
   │     │  │  │  │  ├─ test_sas7bdat.py
   │     │  │  │  │  ├─ test_xport.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_clipboard.py
   │     │  │  │  ├─ test_common.py
   │     │  │  │  ├─ test_compression.py
   │     │  │  │  ├─ test_feather.py
   │     │  │  │  ├─ test_fsspec.py
   │     │  │  │  ├─ test_gbq.py
   │     │  │  │  ├─ test_gcs.py
   │     │  │  │  ├─ test_html.py
   │     │  │  │  ├─ test_http_headers.py
   │     │  │  │  ├─ test_orc.py
   │     │  │  │  ├─ test_parquet.py
   │     │  │  │  ├─ test_pickle.py
   │     │  │  │  ├─ test_s3.py
   │     │  │  │  ├─ test_spss.py
   │     │  │  │  ├─ test_sql.py
   │     │  │  │  ├─ test_stata.py
   │     │  │  │  ├─ xml
   │     │  │  │  │  ├─ conftest.py
   │     │  │  │  │  ├─ test_to_xml.py
   │     │  │  │  │  ├─ test_xml.py
   │     │  │  │  │  ├─ test_xml_dtypes.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ libs
   │     │  │  │  ├─ test_hashtable.py
   │     │  │  │  ├─ test_join.py
   │     │  │  │  ├─ test_lib.py
   │     │  │  │  ├─ test_libalgos.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ plotting
   │     │  │  │  ├─ common.py
   │     │  │  │  ├─ conftest.py
   │     │  │  │  ├─ frame
   │     │  │  │  │  ├─ test_frame.py
   │     │  │  │  │  ├─ test_frame_color.py
   │     │  │  │  │  ├─ test_frame_groupby.py
   │     │  │  │  │  ├─ test_frame_legend.py
   │     │  │  │  │  ├─ test_frame_subplots.py
   │     │  │  │  │  ├─ test_hist_box_by.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_backend.py
   │     │  │  │  ├─ test_boxplot_method.py
   │     │  │  │  ├─ test_common.py
   │     │  │  │  ├─ test_converter.py
   │     │  │  │  ├─ test_datetimelike.py
   │     │  │  │  ├─ test_groupby.py
   │     │  │  │  ├─ test_hist_method.py
   │     │  │  │  ├─ test_misc.py
   │     │  │  │  ├─ test_series.py
   │     │  │  │  ├─ test_style.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ reductions
   │     │  │  │  ├─ test_reductions.py
   │     │  │  │  ├─ test_stat_reductions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ resample
   │     │  │  │  ├─ conftest.py
   │     │  │  │  ├─ test_base.py
   │     │  │  │  ├─ test_datetime_index.py
   │     │  │  │  ├─ test_period_index.py
   │     │  │  │  ├─ test_resampler_grouper.py
   │     │  │  │  ├─ test_resample_api.py
   │     │  │  │  ├─ test_timedelta.py
   │     │  │  │  ├─ test_time_grouper.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ reshape
   │     │  │  │  ├─ concat
   │     │  │  │  │  ├─ conftest.py
   │     │  │  │  │  ├─ test_append.py
   │     │  │  │  │  ├─ test_append_common.py
   │     │  │  │  │  ├─ test_categorical.py
   │     │  │  │  │  ├─ test_concat.py
   │     │  │  │  │  ├─ test_dataframe.py
   │     │  │  │  │  ├─ test_datetimes.py
   │     │  │  │  │  ├─ test_empty.py
   │     │  │  │  │  ├─ test_index.py
   │     │  │  │  │  ├─ test_invalid.py
   │     │  │  │  │  ├─ test_series.py
   │     │  │  │  │  ├─ test_sort.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ merge
   │     │  │  │  │  ├─ test_join.py
   │     │  │  │  │  ├─ test_merge.py
   │     │  │  │  │  ├─ test_merge_asof.py
   │     │  │  │  │  ├─ test_merge_cross.py
   │     │  │  │  │  ├─ test_merge_index_as_string.py
   │     │  │  │  │  ├─ test_merge_ordered.py
   │     │  │  │  │  ├─ test_multi.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_crosstab.py
   │     │  │  │  ├─ test_cut.py
   │     │  │  │  ├─ test_from_dummies.py
   │     │  │  │  ├─ test_get_dummies.py
   │     │  │  │  ├─ test_melt.py
   │     │  │  │  ├─ test_pivot.py
   │     │  │  │  ├─ test_pivot_multilevel.py
   │     │  │  │  ├─ test_qcut.py
   │     │  │  │  ├─ test_union_categoricals.py
   │     │  │  │  ├─ test_util.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ scalar
   │     │  │  │  ├─ interval
   │     │  │  │  │  ├─ test_arithmetic.py
   │     │  │  │  │  ├─ test_constructors.py
   │     │  │  │  │  ├─ test_contains.py
   │     │  │  │  │  ├─ test_formats.py
   │     │  │  │  │  ├─ test_interval.py
   │     │  │  │  │  ├─ test_overlaps.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ period
   │     │  │  │  │  ├─ test_arithmetic.py
   │     │  │  │  │  ├─ test_asfreq.py
   │     │  │  │  │  ├─ test_period.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_nat.py
   │     │  │  │  ├─ test_na_scalar.py
   │     │  │  │  ├─ timedelta
   │     │  │  │  │  ├─ methods
   │     │  │  │  │  │  ├─ test_as_unit.py
   │     │  │  │  │  │  ├─ test_round.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ test_arithmetic.py
   │     │  │  │  │  ├─ test_constructors.py
   │     │  │  │  │  ├─ test_formats.py
   │     │  │  │  │  ├─ test_timedelta.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ timestamp
   │     │  │  │  │  ├─ methods
   │     │  │  │  │  │  ├─ test_as_unit.py
   │     │  │  │  │  │  ├─ test_normalize.py
   │     │  │  │  │  │  ├─ test_replace.py
   │     │  │  │  │  │  ├─ test_round.py
   │     │  │  │  │  │  ├─ test_timestamp_method.py
   │     │  │  │  │  │  ├─ test_to_julian_date.py
   │     │  │  │  │  │  ├─ test_to_pydatetime.py
   │     │  │  │  │  │  ├─ test_tz_convert.py
   │     │  │  │  │  │  ├─ test_tz_localize.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ test_arithmetic.py
   │     │  │  │  │  ├─ test_comparisons.py
   │     │  │  │  │  ├─ test_constructors.py
   │     │  │  │  │  ├─ test_formats.py
   │     │  │  │  │  ├─ test_timestamp.py
   │     │  │  │  │  ├─ test_timezones.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ series
   │     │  │  │  ├─ accessors
   │     │  │  │  │  ├─ test_cat_accessor.py
   │     │  │  │  │  ├─ test_dt_accessor.py
   │     │  │  │  │  ├─ test_list_accessor.py
   │     │  │  │  │  ├─ test_sparse_accessor.py
   │     │  │  │  │  ├─ test_struct_accessor.py
   │     │  │  │  │  ├─ test_str_accessor.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ indexing
   │     │  │  │  │  ├─ test_datetime.py
   │     │  │  │  │  ├─ test_delitem.py
   │     │  │  │  │  ├─ test_get.py
   │     │  │  │  │  ├─ test_getitem.py
   │     │  │  │  │  ├─ test_indexing.py
   │     │  │  │  │  ├─ test_mask.py
   │     │  │  │  │  ├─ test_setitem.py
   │     │  │  │  │  ├─ test_set_value.py
   │     │  │  │  │  ├─ test_take.py
   │     │  │  │  │  ├─ test_where.py
   │     │  │  │  │  ├─ test_xs.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ methods
   │     │  │  │  │  ├─ test_add_prefix_suffix.py
   │     │  │  │  │  ├─ test_align.py
   │     │  │  │  │  ├─ test_argsort.py
   │     │  │  │  │  ├─ test_asof.py
   │     │  │  │  │  ├─ test_astype.py
   │     │  │  │  │  ├─ test_autocorr.py
   │     │  │  │  │  ├─ test_between.py
   │     │  │  │  │  ├─ test_case_when.py
   │     │  │  │  │  ├─ test_clip.py
   │     │  │  │  │  ├─ test_combine.py
   │     │  │  │  │  ├─ test_combine_first.py
   │     │  │  │  │  ├─ test_compare.py
   │     │  │  │  │  ├─ test_convert_dtypes.py
   │     │  │  │  │  ├─ test_copy.py
   │     │  │  │  │  ├─ test_count.py
   │     │  │  │  │  ├─ test_cov_corr.py
   │     │  │  │  │  ├─ test_describe.py
   │     │  │  │  │  ├─ test_diff.py
   │     │  │  │  │  ├─ test_drop.py
   │     │  │  │  │  ├─ test_dropna.py
   │     │  │  │  │  ├─ test_drop_duplicates.py
   │     │  │  │  │  ├─ test_dtypes.py
   │     │  │  │  │  ├─ test_duplicated.py
   │     │  │  │  │  ├─ test_equals.py
   │     │  │  │  │  ├─ test_explode.py
   │     │  │  │  │  ├─ test_fillna.py
   │     │  │  │  │  ├─ test_get_numeric_data.py
   │     │  │  │  │  ├─ test_head_tail.py
   │     │  │  │  │  ├─ test_infer_objects.py
   │     │  │  │  │  ├─ test_info.py
   │     │  │  │  │  ├─ test_interpolate.py
   │     │  │  │  │  ├─ test_isin.py
   │     │  │  │  │  ├─ test_isna.py
   │     │  │  │  │  ├─ test_is_monotonic.py
   │     │  │  │  │  ├─ test_is_unique.py
   │     │  │  │  │  ├─ test_item.py
   │     │  │  │  │  ├─ test_map.py
   │     │  │  │  │  ├─ test_matmul.py
   │     │  │  │  │  ├─ test_nlargest.py
   │     │  │  │  │  ├─ test_nunique.py
   │     │  │  │  │  ├─ test_pct_change.py
   │     │  │  │  │  ├─ test_pop.py
   │     │  │  │  │  ├─ test_quantile.py
   │     │  │  │  │  ├─ test_rank.py
   │     │  │  │  │  ├─ test_reindex.py
   │     │  │  │  │  ├─ test_reindex_like.py
   │     │  │  │  │  ├─ test_rename.py
   │     │  │  │  │  ├─ test_rename_axis.py
   │     │  │  │  │  ├─ test_repeat.py
   │     │  │  │  │  ├─ test_replace.py
   │     │  │  │  │  ├─ test_reset_index.py
   │     │  │  │  │  ├─ test_round.py
   │     │  │  │  │  ├─ test_searchsorted.py
   │     │  │  │  │  ├─ test_set_name.py
   │     │  │  │  │  ├─ test_size.py
   │     │  │  │  │  ├─ test_sort_index.py
   │     │  │  │  │  ├─ test_sort_values.py
   │     │  │  │  │  ├─ test_tolist.py
   │     │  │  │  │  ├─ test_to_csv.py
   │     │  │  │  │  ├─ test_to_dict.py
   │     │  │  │  │  ├─ test_to_frame.py
   │     │  │  │  │  ├─ test_to_numpy.py
   │     │  │  │  │  ├─ test_truncate.py
   │     │  │  │  │  ├─ test_tz_localize.py
   │     │  │  │  │  ├─ test_unique.py
   │     │  │  │  │  ├─ test_unstack.py
   │     │  │  │  │  ├─ test_update.py
   │     │  │  │  │  ├─ test_values.py
   │     │  │  │  │  ├─ test_value_counts.py
   │     │  │  │  │  ├─ test_view.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_api.py
   │     │  │  │  ├─ test_arithmetic.py
   │     │  │  │  ├─ test_constructors.py
   │     │  │  │  ├─ test_cumulative.py
   │     │  │  │  ├─ test_formats.py
   │     │  │  │  ├─ test_iteration.py
   │     │  │  │  ├─ test_logical_ops.py
   │     │  │  │  ├─ test_missing.py
   │     │  │  │  ├─ test_npfuncs.py
   │     │  │  │  ├─ test_reductions.py
   │     │  │  │  ├─ test_subclass.py
   │     │  │  │  ├─ test_ufunc.py
   │     │  │  │  ├─ test_unary.py
   │     │  │  │  ├─ test_validate.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ strings
   │     │  │  │  ├─ conftest.py
   │     │  │  │  ├─ test_api.py
   │     │  │  │  ├─ test_case_justify.py
   │     │  │  │  ├─ test_cat.py
   │     │  │  │  ├─ test_extract.py
   │     │  │  │  ├─ test_find_replace.py
   │     │  │  │  ├─ test_get_dummies.py
   │     │  │  │  ├─ test_split_partition.py
   │     │  │  │  ├─ test_strings.py
   │     │  │  │  ├─ test_string_array.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ test_aggregation.py
   │     │  │  ├─ test_algos.py
   │     │  │  ├─ test_common.py
   │     │  │  ├─ test_downstream.py
   │     │  │  ├─ test_errors.py
   │     │  │  ├─ test_expressions.py
   │     │  │  ├─ test_flags.py
   │     │  │  ├─ test_multilevel.py
   │     │  │  ├─ test_nanops.py
   │     │  │  ├─ test_optional_dependency.py
   │     │  │  ├─ test_register_accessor.py
   │     │  │  ├─ test_sorting.py
   │     │  │  ├─ test_take.py
   │     │  │  ├─ tools
   │     │  │  │  ├─ test_to_datetime.py
   │     │  │  │  ├─ test_to_numeric.py
   │     │  │  │  ├─ test_to_time.py
   │     │  │  │  ├─ test_to_timedelta.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ tseries
   │     │  │  │  ├─ frequencies
   │     │  │  │  │  ├─ test_frequencies.py
   │     │  │  │  │  ├─ test_freq_code.py
   │     │  │  │  │  ├─ test_inference.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ holiday
   │     │  │  │  │  ├─ test_calendar.py
   │     │  │  │  │  ├─ test_federal.py
   │     │  │  │  │  ├─ test_holiday.py
   │     │  │  │  │  ├─ test_observance.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ offsets
   │     │  │  │  │  ├─ common.py
   │     │  │  │  │  ├─ test_business_day.py
   │     │  │  │  │  ├─ test_business_hour.py
   │     │  │  │  │  ├─ test_business_month.py
   │     │  │  │  │  ├─ test_business_quarter.py
   │     │  │  │  │  ├─ test_business_year.py
   │     │  │  │  │  ├─ test_common.py
   │     │  │  │  │  ├─ test_custom_business_day.py
   │     │  │  │  │  ├─ test_custom_business_hour.py
   │     │  │  │  │  ├─ test_custom_business_month.py
   │     │  │  │  │  ├─ test_dst.py
   │     │  │  │  │  ├─ test_easter.py
   │     │  │  │  │  ├─ test_fiscal.py
   │     │  │  │  │  ├─ test_index.py
   │     │  │  │  │  ├─ test_month.py
   │     │  │  │  │  ├─ test_offsets.py
   │     │  │  │  │  ├─ test_offsets_properties.py
   │     │  │  │  │  ├─ test_quarter.py
   │     │  │  │  │  ├─ test_ticks.py
   │     │  │  │  │  ├─ test_week.py
   │     │  │  │  │  ├─ test_year.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ tslibs
   │     │  │  │  ├─ test_api.py
   │     │  │  │  ├─ test_array_to_datetime.py
   │     │  │  │  ├─ test_ccalendar.py
   │     │  │  │  ├─ test_conversion.py
   │     │  │  │  ├─ test_fields.py
   │     │  │  │  ├─ test_libfrequencies.py
   │     │  │  │  ├─ test_liboffsets.py
   │     │  │  │  ├─ test_npy_units.py
   │     │  │  │  ├─ test_np_datetime.py
   │     │  │  │  ├─ test_parse_iso8601.py
   │     │  │  │  ├─ test_parsing.py
   │     │  │  │  ├─ test_period.py
   │     │  │  │  ├─ test_resolution.py
   │     │  │  │  ├─ test_strptime.py
   │     │  │  │  ├─ test_timedeltas.py
   │     │  │  │  ├─ test_timezones.py
   │     │  │  │  ├─ test_to_offset.py
   │     │  │  │  ├─ test_tzconversion.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ util
   │     │  │  │  ├─ conftest.py
   │     │  │  │  ├─ test_assert_almost_equal.py
   │     │  │  │  ├─ test_assert_attr_equal.py
   │     │  │  │  ├─ test_assert_categorical_equal.py
   │     │  │  │  ├─ test_assert_extension_array_equal.py
   │     │  │  │  ├─ test_assert_frame_equal.py
   │     │  │  │  ├─ test_assert_index_equal.py
   │     │  │  │  ├─ test_assert_interval_array_equal.py
   │     │  │  │  ├─ test_assert_numpy_array_equal.py
   │     │  │  │  ├─ test_assert_produces_warning.py
   │     │  │  │  ├─ test_assert_series_equal.py
   │     │  │  │  ├─ test_deprecate.py
   │     │  │  │  ├─ test_deprecate_kwarg.py
   │     │  │  │  ├─ test_deprecate_nonkeyword_arguments.py
   │     │  │  │  ├─ test_doc.py
   │     │  │  │  ├─ test_hashing.py
   │     │  │  │  ├─ test_numba.py
   │     │  │  │  ├─ test_rewrite_warning.py
   │     │  │  │  ├─ test_shares_memory.py
   │     │  │  │  ├─ test_show_versions.py
   │     │  │  │  ├─ test_util.py
   │     │  │  │  ├─ test_validate_args.py
   │     │  │  │  ├─ test_validate_args_and_kwargs.py
   │     │  │  │  ├─ test_validate_inclusive.py
   │     │  │  │  ├─ test_validate_kwargs.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ window
   │     │  │  │  ├─ conftest.py
   │     │  │  │  ├─ moments
   │     │  │  │  │  ├─ conftest.py
   │     │  │  │  │  ├─ test_moments_consistency_ewm.py
   │     │  │  │  │  ├─ test_moments_consistency_expanding.py
   │     │  │  │  │  ├─ test_moments_consistency_rolling.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_api.py
   │     │  │  │  ├─ test_apply.py
   │     │  │  │  ├─ test_base_indexer.py
   │     │  │  │  ├─ test_cython_aggregations.py
   │     │  │  │  ├─ test_dtypes.py
   │     │  │  │  ├─ test_ewm.py
   │     │  │  │  ├─ test_expanding.py
   │     │  │  │  ├─ test_groupby.py
   │     │  │  │  ├─ test_numba.py
   │     │  │  │  ├─ test_online.py
   │     │  │  │  ├─ test_pairwise.py
   │     │  │  │  ├─ test_rolling.py
   │     │  │  │  ├─ test_rolling_functions.py
   │     │  │  │  ├─ test_rolling_quantile.py
   │     │  │  │  ├─ test_rolling_skew_kurt.py
   │     │  │  │  ├─ test_timeseries_window.py
   │     │  │  │  ├─ test_win_type.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ tseries
   │     │  │  ├─ api.py
   │     │  │  ├─ frequencies.py
   │     │  │  ├─ holiday.py
   │     │  │  ├─ offsets.py
   │     │  │  └─ __init__.py
   │     │  ├─ util
   │     │  │  ├─ version
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _decorators.py
   │     │  │  ├─ _doctools.py
   │     │  │  ├─ _exceptions.py
   │     │  │  ├─ _print_versions.py
   │     │  │  ├─ _tester.py
   │     │  │  ├─ _test_decorators.py
   │     │  │  ├─ _validators.py
   │     │  │  └─ __init__.py
   │     │  ├─ _config
   │     │  │  ├─ config.py
   │     │  │  ├─ dates.py
   │     │  │  ├─ display.py
   │     │  │  ├─ localization.py
   │     │  │  └─ __init__.py
   │     │  ├─ _libs
   │     │  │  ├─ algos.cp311-win_amd64.lib
   │     │  │  ├─ algos.cp311-win_amd64.pyd
   │     │  │  ├─ algos.pyi
   │     │  │  ├─ arrays.cp311-win_amd64.lib
   │     │  │  ├─ arrays.cp311-win_amd64.pyd
   │     │  │  ├─ arrays.pyi
   │     │  │  ├─ byteswap.cp311-win_amd64.lib
   │     │  │  ├─ byteswap.cp311-win_amd64.pyd
   │     │  │  ├─ byteswap.pyi
   │     │  │  ├─ groupby.cp311-win_amd64.lib
   │     │  │  ├─ groupby.cp311-win_amd64.pyd
   │     │  │  ├─ groupby.pyi
   │     │  │  ├─ hashing.cp311-win_amd64.lib
   │     │  │  ├─ hashing.cp311-win_amd64.pyd
   │     │  │  ├─ hashing.pyi
   │     │  │  ├─ hashtable.cp311-win_amd64.lib
   │     │  │  ├─ hashtable.cp311-win_amd64.pyd
   │     │  │  ├─ hashtable.pyi
   │     │  │  ├─ index.cp311-win_amd64.lib
   │     │  │  ├─ index.cp311-win_amd64.pyd
   │     │  │  ├─ index.pyi
   │     │  │  ├─ indexing.cp311-win_amd64.lib
   │     │  │  ├─ indexing.cp311-win_amd64.pyd
   │     │  │  ├─ indexing.pyi
   │     │  │  ├─ internals.cp311-win_amd64.lib
   │     │  │  ├─ internals.cp311-win_amd64.pyd
   │     │  │  ├─ internals.pyi
   │     │  │  ├─ interval.cp311-win_amd64.lib
   │     │  │  ├─ interval.cp311-win_amd64.pyd
   │     │  │  ├─ interval.pyi
   │     │  │  ├─ join.cp311-win_amd64.lib
   │     │  │  ├─ join.cp311-win_amd64.pyd
   │     │  │  ├─ join.pyi
   │     │  │  ├─ json.cp311-win_amd64.lib
   │     │  │  ├─ json.cp311-win_amd64.pyd
   │     │  │  ├─ json.pyi
   │     │  │  ├─ lib.cp311-win_amd64.lib
   │     │  │  ├─ lib.cp311-win_amd64.pyd
   │     │  │  ├─ lib.pyi
   │     │  │  ├─ missing.cp311-win_amd64.lib
   │     │  │  ├─ missing.cp311-win_amd64.pyd
   │     │  │  ├─ missing.pyi
   │     │  │  ├─ ops.cp311-win_amd64.lib
   │     │  │  ├─ ops.cp311-win_amd64.pyd
   │     │  │  ├─ ops.pyi
   │     │  │  ├─ ops_dispatch.cp311-win_amd64.lib
   │     │  │  ├─ ops_dispatch.cp311-win_amd64.pyd
   │     │  │  ├─ ops_dispatch.pyi
   │     │  │  ├─ pandas_datetime.cp311-win_amd64.lib
   │     │  │  ├─ pandas_datetime.cp311-win_amd64.pyd
   │     │  │  ├─ pandas_parser.cp311-win_amd64.lib
   │     │  │  ├─ pandas_parser.cp311-win_amd64.pyd
   │     │  │  ├─ parsers.cp311-win_amd64.lib
   │     │  │  ├─ parsers.cp311-win_amd64.pyd
   │     │  │  ├─ parsers.pyi
   │     │  │  ├─ properties.cp311-win_amd64.lib
   │     │  │  ├─ properties.cp311-win_amd64.pyd
   │     │  │  ├─ properties.pyi
   │     │  │  ├─ reshape.cp311-win_amd64.lib
   │     │  │  ├─ reshape.cp311-win_amd64.pyd
   │     │  │  ├─ reshape.pyi
   │     │  │  ├─ sas.cp311-win_amd64.lib
   │     │  │  ├─ sas.cp311-win_amd64.pyd
   │     │  │  ├─ sas.pyi
   │     │  │  ├─ sparse.cp311-win_amd64.lib
   │     │  │  ├─ sparse.cp311-win_amd64.pyd
   │     │  │  ├─ sparse.pyi
   │     │  │  ├─ testing.cp311-win_amd64.lib
   │     │  │  ├─ testing.cp311-win_amd64.pyd
   │     │  │  ├─ testing.pyi
   │     │  │  ├─ tslib.cp311-win_amd64.lib
   │     │  │  ├─ tslib.cp311-win_amd64.pyd
   │     │  │  ├─ tslib.pyi
   │     │  │  ├─ tslibs
   │     │  │  │  ├─ base.cp311-win_amd64.lib
   │     │  │  │  ├─ base.cp311-win_amd64.pyd
   │     │  │  │  ├─ ccalendar.cp311-win_amd64.lib
   │     │  │  │  ├─ ccalendar.cp311-win_amd64.pyd
   │     │  │  │  ├─ ccalendar.pyi
   │     │  │  │  ├─ conversion.cp311-win_amd64.lib
   │     │  │  │  ├─ conversion.cp311-win_amd64.pyd
   │     │  │  │  ├─ conversion.pyi
   │     │  │  │  ├─ dtypes.cp311-win_amd64.lib
   │     │  │  │  ├─ dtypes.cp311-win_amd64.pyd
   │     │  │  │  ├─ dtypes.pyi
   │     │  │  │  ├─ fields.cp311-win_amd64.lib
   │     │  │  │  ├─ fields.cp311-win_amd64.pyd
   │     │  │  │  ├─ fields.pyi
   │     │  │  │  ├─ nattype.cp311-win_amd64.lib
   │     │  │  │  ├─ nattype.cp311-win_amd64.pyd
   │     │  │  │  ├─ nattype.pyi
   │     │  │  │  ├─ np_datetime.cp311-win_amd64.lib
   │     │  │  │  ├─ np_datetime.cp311-win_amd64.pyd
   │     │  │  │  ├─ np_datetime.pyi
   │     │  │  │  ├─ offsets.cp311-win_amd64.lib
   │     │  │  │  ├─ offsets.cp311-win_amd64.pyd
   │     │  │  │  ├─ offsets.pyi
   │     │  │  │  ├─ parsing.cp311-win_amd64.lib
   │     │  │  │  ├─ parsing.cp311-win_amd64.pyd
   │     │  │  │  ├─ parsing.pyi
   │     │  │  │  ├─ period.cp311-win_amd64.lib
   │     │  │  │  ├─ period.cp311-win_amd64.pyd
   │     │  │  │  ├─ period.pyi
   │     │  │  │  ├─ strptime.cp311-win_amd64.lib
   │     │  │  │  ├─ strptime.cp311-win_amd64.pyd
   │     │  │  │  ├─ strptime.pyi
   │     │  │  │  ├─ timedeltas.cp311-win_amd64.lib
   │     │  │  │  ├─ timedeltas.cp311-win_amd64.pyd
   │     │  │  │  ├─ timedeltas.pyi
   │     │  │  │  ├─ timestamps.cp311-win_amd64.lib
   │     │  │  │  ├─ timestamps.cp311-win_amd64.pyd
   │     │  │  │  ├─ timestamps.pyi
   │     │  │  │  ├─ timezones.cp311-win_amd64.lib
   │     │  │  │  ├─ timezones.cp311-win_amd64.pyd
   │     │  │  │  ├─ timezones.pyi
   │     │  │  │  ├─ tzconversion.cp311-win_amd64.lib
   │     │  │  │  ├─ tzconversion.cp311-win_amd64.pyd
   │     │  │  │  ├─ tzconversion.pyi
   │     │  │  │  ├─ vectorized.cp311-win_amd64.lib
   │     │  │  │  ├─ vectorized.cp311-win_amd64.pyd
   │     │  │  │  ├─ vectorized.pyi
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ window
   │     │  │  │  ├─ aggregations.cp311-win_amd64.lib
   │     │  │  │  ├─ aggregations.cp311-win_amd64.pyd
   │     │  │  │  ├─ aggregations.pyi
   │     │  │  │  ├─ indexers.cp311-win_amd64.lib
   │     │  │  │  ├─ indexers.cp311-win_amd64.pyd
   │     │  │  │  ├─ indexers.pyi
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ writers.cp311-win_amd64.lib
   │     │  │  ├─ writers.cp311-win_amd64.pyd
   │     │  │  ├─ writers.pyi
   │     │  │  └─ __init__.py
   │     │  ├─ _testing
   │     │  │  ├─ asserters.py
   │     │  │  ├─ compat.py
   │     │  │  ├─ contexts.py
   │     │  │  ├─ _hypothesis.py
   │     │  │  ├─ _io.py
   │     │  │  ├─ _warnings.py
   │     │  │  └─ __init__.py
   │     │  ├─ _typing.py
   │     │  ├─ _version.py
   │     │  ├─ _version_meson.py
   │     │  └─ __init__.py
   │     ├─ pandas-2.2.3.dist-info
   │     │  ├─ DELVEWHEEL
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  └─ WHEEL
   │     ├─ pandas.libs
   │     │  └─ msvcp140-0f2ea95580b32bcfc81c235d5751ce78.dll
   │     ├─ pip
   │     │  ├─ py.typed
   │     │  ├─ _internal
   │     │  │  ├─ build_env.py
   │     │  │  ├─ cache.py
   │     │  │  ├─ cli
   │     │  │  │  ├─ autocompletion.py
   │     │  │  │  ├─ base_command.py
   │     │  │  │  ├─ cmdoptions.py
   │     │  │  │  ├─ command_context.py
   │     │  │  │  ├─ index_command.py
   │     │  │  │  ├─ main.py
   │     │  │  │  ├─ main_parser.py
   │     │  │  │  ├─ parser.py
   │     │  │  │  ├─ progress_bars.py
   │     │  │  │  ├─ req_command.py
   │     │  │  │  ├─ spinners.py
   │     │  │  │  ├─ status_codes.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ commands
   │     │  │  │  ├─ cache.py
   │     │  │  │  ├─ check.py
   │     │  │  │  ├─ completion.py
   │     │  │  │  ├─ configuration.py
   │     │  │  │  ├─ debug.py
   │     │  │  │  ├─ download.py
   │     │  │  │  ├─ freeze.py
   │     │  │  │  ├─ hash.py
   │     │  │  │  ├─ help.py
   │     │  │  │  ├─ index.py
   │     │  │  │  ├─ inspect.py
   │     │  │  │  ├─ install.py
   │     │  │  │  ├─ list.py
   │     │  │  │  ├─ search.py
   │     │  │  │  ├─ show.py
   │     │  │  │  ├─ uninstall.py
   │     │  │  │  ├─ wheel.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ configuration.py
   │     │  │  ├─ distributions
   │     │  │  │  ├─ base.py
   │     │  │  │  ├─ installed.py
   │     │  │  │  ├─ sdist.py
   │     │  │  │  ├─ wheel.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ exceptions.py
   │     │  │  ├─ index
   │     │  │  │  ├─ collector.py
   │     │  │  │  ├─ package_finder.py
   │     │  │  │  ├─ sources.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ locations
   │     │  │  │  ├─ base.py
   │     │  │  │  ├─ _distutils.py
   │     │  │  │  ├─ _sysconfig.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ main.py
   │     │  │  ├─ metadata
   │     │  │  │  ├─ base.py
   │     │  │  │  ├─ importlib
   │     │  │  │  │  ├─ _compat.py
   │     │  │  │  │  ├─ _dists.py
   │     │  │  │  │  ├─ _envs.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ pkg_resources.py
   │     │  │  │  ├─ _json.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ models
   │     │  │  │  ├─ candidate.py
   │     │  │  │  ├─ direct_url.py
   │     │  │  │  ├─ format_control.py
   │     │  │  │  ├─ index.py
   │     │  │  │  ├─ installation_report.py
   │     │  │  │  ├─ link.py
   │     │  │  │  ├─ scheme.py
   │     │  │  │  ├─ search_scope.py
   │     │  │  │  ├─ selection_prefs.py
   │     │  │  │  ├─ target_python.py
   │     │  │  │  ├─ wheel.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ network
   │     │  │  │  ├─ auth.py
   │     │  │  │  ├─ cache.py
   │     │  │  │  ├─ download.py
   │     │  │  │  ├─ lazy_wheel.py
   │     │  │  │  ├─ session.py
   │     │  │  │  ├─ utils.py
   │     │  │  │  ├─ xmlrpc.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ operations
   │     │  │  │  ├─ build
   │     │  │  │  │  ├─ build_tracker.py
   │     │  │  │  │  ├─ metadata.py
   │     │  │  │  │  ├─ metadata_editable.py
   │     │  │  │  │  ├─ metadata_legacy.py
   │     │  │  │  │  ├─ wheel.py
   │     │  │  │  │  ├─ wheel_editable.py
   │     │  │  │  │  ├─ wheel_legacy.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ check.py
   │     │  │  │  ├─ freeze.py
   │     │  │  │  ├─ install
   │     │  │  │  │  ├─ editable_legacy.py
   │     │  │  │  │  ├─ wheel.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ prepare.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ pyproject.py
   │     │  │  ├─ req
   │     │  │  │  ├─ constructors.py
   │     │  │  │  ├─ req_file.py
   │     │  │  │  ├─ req_install.py
   │     │  │  │  ├─ req_set.py
   │     │  │  │  ├─ req_uninstall.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ resolution
   │     │  │  │  ├─ base.py
   │     │  │  │  ├─ legacy
   │     │  │  │  │  ├─ resolver.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ resolvelib
   │     │  │  │  │  ├─ base.py
   │     │  │  │  │  ├─ candidates.py
   │     │  │  │  │  ├─ factory.py
   │     │  │  │  │  ├─ found_candidates.py
   │     │  │  │  │  ├─ provider.py
   │     │  │  │  │  ├─ reporter.py
   │     │  │  │  │  ├─ requirements.py
   │     │  │  │  │  ├─ resolver.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ self_outdated_check.py
   │     │  │  ├─ utils
   │     │  │  │  ├─ appdirs.py
   │     │  │  │  ├─ compat.py
   │     │  │  │  ├─ compatibility_tags.py
   │     │  │  │  ├─ datetime.py
   │     │  │  │  ├─ deprecation.py
   │     │  │  │  ├─ direct_url_helpers.py
   │     │  │  │  ├─ egg_link.py
   │     │  │  │  ├─ entrypoints.py
   │     │  │  │  ├─ filesystem.py
   │     │  │  │  ├─ filetypes.py
   │     │  │  │  ├─ glibc.py
   │     │  │  │  ├─ hashes.py
   │     │  │  │  ├─ logging.py
   │     │  │  │  ├─ misc.py
   │     │  │  │  ├─ packaging.py
   │     │  │  │  ├─ retry.py
   │     │  │  │  ├─ setuptools_build.py
   │     │  │  │  ├─ subprocess.py
   │     │  │  │  ├─ temp_dir.py
   │     │  │  │  ├─ unpacking.py
   │     │  │  │  ├─ urls.py
   │     │  │  │  ├─ virtualenv.py
   │     │  │  │  ├─ wheel.py
   │     │  │  │  ├─ _jaraco_text.py
   │     │  │  │  ├─ _log.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ vcs
   │     │  │  │  ├─ bazaar.py
   │     │  │  │  ├─ git.py
   │     │  │  │  ├─ mercurial.py
   │     │  │  │  ├─ subversion.py
   │     │  │  │  ├─ versioncontrol.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ wheel_builder.py
   │     │  │  └─ __init__.py
   │     │  ├─ _vendor
   │     │  │  ├─ cachecontrol
   │     │  │  │  ├─ adapter.py
   │     │  │  │  ├─ cache.py
   │     │  │  │  ├─ caches
   │     │  │  │  │  ├─ file_cache.py
   │     │  │  │  │  ├─ redis_cache.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ controller.py
   │     │  │  │  ├─ filewrapper.py
   │     │  │  │  ├─ heuristics.py
   │     │  │  │  ├─ py.typed
   │     │  │  │  ├─ serialize.py
   │     │  │  │  ├─ wrapper.py
   │     │  │  │  ├─ _cmd.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ certifi
   │     │  │  │  ├─ cacert.pem
   │     │  │  │  ├─ core.py
   │     │  │  │  ├─ py.typed
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __main__.py
   │     │  │  ├─ distlib
   │     │  │  │  ├─ compat.py
   │     │  │  │  ├─ database.py
   │     │  │  │  ├─ index.py
   │     │  │  │  ├─ locators.py
   │     │  │  │  ├─ manifest.py
   │     │  │  │  ├─ markers.py
   │     │  │  │  ├─ metadata.py
   │     │  │  │  ├─ resources.py
   │     │  │  │  ├─ scripts.py
   │     │  │  │  ├─ t32.exe
   │     │  │  │  ├─ t64-arm.exe
   │     │  │  │  ├─ t64.exe
   │     │  │  │  ├─ util.py
   │     │  │  │  ├─ version.py
   │     │  │  │  ├─ w32.exe
   │     │  │  │  ├─ w64-arm.exe
   │     │  │  │  ├─ w64.exe
   │     │  │  │  ├─ wheel.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ distro
   │     │  │  │  ├─ distro.py
   │     │  │  │  ├─ py.typed
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __main__.py
   │     │  │  ├─ idna
   │     │  │  │  ├─ codec.py
   │     │  │  │  ├─ compat.py
   │     │  │  │  ├─ core.py
   │     │  │  │  ├─ idnadata.py
   │     │  │  │  ├─ intranges.py
   │     │  │  │  ├─ package_data.py
   │     │  │  │  ├─ py.typed
   │     │  │  │  ├─ uts46data.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ msgpack
   │     │  │  │  ├─ exceptions.py
   │     │  │  │  ├─ ext.py
   │     │  │  │  ├─ fallback.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ packaging
   │     │  │  │  ├─ licenses
   │     │  │  │  │  ├─ _spdx.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ markers.py
   │     │  │  │  ├─ metadata.py
   │     │  │  │  ├─ py.typed
   │     │  │  │  ├─ requirements.py
   │     │  │  │  ├─ specifiers.py
   │     │  │  │  ├─ tags.py
   │     │  │  │  ├─ utils.py
   │     │  │  │  ├─ version.py
   │     │  │  │  ├─ _elffile.py
   │     │  │  │  ├─ _manylinux.py
   │     │  │  │  ├─ _musllinux.py
   │     │  │  │  ├─ _parser.py
   │     │  │  │  ├─ _structures.py
   │     │  │  │  ├─ _tokenizer.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ pkg_resources
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ platformdirs
   │     │  │  │  ├─ android.py
   │     │  │  │  ├─ api.py
   │     │  │  │  ├─ macos.py
   │     │  │  │  ├─ py.typed
   │     │  │  │  ├─ unix.py
   │     │  │  │  ├─ version.py
   │     │  │  │  ├─ windows.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __main__.py
   │     │  │  ├─ pygments
   │     │  │  │  ├─ cmdline.py
   │     │  │  │  ├─ console.py
   │     │  │  │  ├─ filter.py
   │     │  │  │  ├─ filters
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ formatter.py
   │     │  │  │  ├─ formatters
   │     │  │  │  │  ├─ bbcode.py
   │     │  │  │  │  ├─ groff.py
   │     │  │  │  │  ├─ html.py
   │     │  │  │  │  ├─ img.py
   │     │  │  │  │  ├─ irc.py
   │     │  │  │  │  ├─ latex.py
   │     │  │  │  │  ├─ other.py
   │     │  │  │  │  ├─ pangomarkup.py
   │     │  │  │  │  ├─ rtf.py
   │     │  │  │  │  ├─ svg.py
   │     │  │  │  │  ├─ terminal.py
   │     │  │  │  │  ├─ terminal256.py
   │     │  │  │  │  ├─ _mapping.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ lexer.py
   │     │  │  │  ├─ lexers
   │     │  │  │  │  ├─ python.py
   │     │  │  │  │  ├─ _mapping.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ modeline.py
   │     │  │  │  ├─ plugin.py
   │     │  │  │  ├─ regexopt.py
   │     │  │  │  ├─ scanner.py
   │     │  │  │  ├─ sphinxext.py
   │     │  │  │  ├─ style.py
   │     │  │  │  ├─ styles
   │     │  │  │  │  ├─ _mapping.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ token.py
   │     │  │  │  ├─ unistring.py
   │     │  │  │  ├─ util.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __main__.py
   │     │  │  ├─ pyproject_hooks
   │     │  │  │  ├─ py.typed
   │     │  │  │  ├─ _impl.py
   │     │  │  │  ├─ _in_process
   │     │  │  │  │  ├─ _in_process.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ requests
   │     │  │  │  ├─ adapters.py
   │     │  │  │  ├─ api.py
   │     │  │  │  ├─ auth.py
   │     │  │  │  ├─ certs.py
   │     │  │  │  ├─ compat.py
   │     │  │  │  ├─ cookies.py
   │     │  │  │  ├─ exceptions.py
   │     │  │  │  ├─ help.py
   │     │  │  │  ├─ hooks.py
   │     │  │  │  ├─ models.py
   │     │  │  │  ├─ packages.py
   │     │  │  │  ├─ sessions.py
   │     │  │  │  ├─ status_codes.py
   │     │  │  │  ├─ structures.py
   │     │  │  │  ├─ utils.py
   │     │  │  │  ├─ _internal_utils.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __version__.py
   │     │  │  ├─ resolvelib
   │     │  │  │  ├─ compat
   │     │  │  │  │  ├─ collections_abc.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ providers.py
   │     │  │  │  ├─ py.typed
   │     │  │  │  ├─ reporters.py
   │     │  │  │  ├─ resolvers.py
   │     │  │  │  ├─ structs.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ rich
   │     │  │  │  ├─ abc.py
   │     │  │  │  ├─ align.py
   │     │  │  │  ├─ ansi.py
   │     │  │  │  ├─ bar.py
   │     │  │  │  ├─ box.py
   │     │  │  │  ├─ cells.py
   │     │  │  │  ├─ color.py
   │     │  │  │  ├─ color_triplet.py
   │     │  │  │  ├─ columns.py
   │     │  │  │  ├─ console.py
   │     │  │  │  ├─ constrain.py
   │     │  │  │  ├─ containers.py
   │     │  │  │  ├─ control.py
   │     │  │  │  ├─ default_styles.py
   │     │  │  │  ├─ diagnose.py
   │     │  │  │  ├─ emoji.py
   │     │  │  │  ├─ errors.py
   │     │  │  │  ├─ filesize.py
   │     │  │  │  ├─ file_proxy.py
   │     │  │  │  ├─ highlighter.py
   │     │  │  │  ├─ json.py
   │     │  │  │  ├─ jupyter.py
   │     │  │  │  ├─ layout.py
   │     │  │  │  ├─ live.py
   │     │  │  │  ├─ live_render.py
   │     │  │  │  ├─ logging.py
   │     │  │  │  ├─ markup.py
   │     │  │  │  ├─ measure.py
   │     │  │  │  ├─ padding.py
   │     │  │  │  ├─ pager.py
   │     │  │  │  ├─ palette.py
   │     │  │  │  ├─ panel.py
   │     │  │  │  ├─ pretty.py
   │     │  │  │  ├─ progress.py
   │     │  │  │  ├─ progress_bar.py
   │     │  │  │  ├─ prompt.py
   │     │  │  │  ├─ protocol.py
   │     │  │  │  ├─ py.typed
   │     │  │  │  ├─ region.py
   │     │  │  │  ├─ repr.py
   │     │  │  │  ├─ rule.py
   │     │  │  │  ├─ scope.py
   │     │  │  │  ├─ screen.py
   │     │  │  │  ├─ segment.py
   │     │  │  │  ├─ spinner.py
   │     │  │  │  ├─ status.py
   │     │  │  │  ├─ style.py
   │     │  │  │  ├─ styled.py
   │     │  │  │  ├─ syntax.py
   │     │  │  │  ├─ table.py
   │     │  │  │  ├─ terminal_theme.py
   │     │  │  │  ├─ text.py
   │     │  │  │  ├─ theme.py
   │     │  │  │  ├─ themes.py
   │     │  │  │  ├─ traceback.py
   │     │  │  │  ├─ tree.py
   │     │  │  │  ├─ _cell_widths.py
   │     │  │  │  ├─ _emoji_codes.py
   │     │  │  │  ├─ _emoji_replace.py
   │     │  │  │  ├─ _export_format.py
   │     │  │  │  ├─ _extension.py
   │     │  │  │  ├─ _fileno.py
   │     │  │  │  ├─ _inspect.py
   │     │  │  │  ├─ _log_render.py
   │     │  │  │  ├─ _loop.py
   │     │  │  │  ├─ _null_file.py
   │     │  │  │  ├─ _palettes.py
   │     │  │  │  ├─ _pick.py
   │     │  │  │  ├─ _ratio.py
   │     │  │  │  ├─ _spinners.py
   │     │  │  │  ├─ _stack.py
   │     │  │  │  ├─ _timer.py
   │     │  │  │  ├─ _win32_console.py
   │     │  │  │  ├─ _windows.py
   │     │  │  │  ├─ _windows_renderer.py
   │     │  │  │  ├─ _wrap.py
   │     │  │  │  ├─ __init__.py
   │     │  │  │  └─ __main__.py
   │     │  │  ├─ tomli
   │     │  │  │  ├─ py.typed
   │     │  │  │  ├─ _parser.py
   │     │  │  │  ├─ _re.py
   │     │  │  │  ├─ _types.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ truststore
   │     │  │  │  ├─ py.typed
   │     │  │  │  ├─ _api.py
   │     │  │  │  ├─ _macos.py
   │     │  │  │  ├─ _openssl.py
   │     │  │  │  ├─ _ssl_constants.py
   │     │  │  │  ├─ _windows.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ typing_extensions.py
   │     │  │  ├─ urllib3
   │     │  │  │  ├─ connection.py
   │     │  │  │  ├─ connectionpool.py
   │     │  │  │  ├─ contrib
   │     │  │  │  │  ├─ appengine.py
   │     │  │  │  │  ├─ ntlmpool.py
   │     │  │  │  │  ├─ pyopenssl.py
   │     │  │  │  │  ├─ securetransport.py
   │     │  │  │  │  ├─ socks.py
   │     │  │  │  │  ├─ _appengine_environ.py
   │     │  │  │  │  ├─ _securetransport
   │     │  │  │  │  │  ├─ bindings.py
   │     │  │  │  │  │  ├─ low_level.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ exceptions.py
   │     │  │  │  ├─ fields.py
   │     │  │  │  ├─ filepost.py
   │     │  │  │  ├─ packages
   │     │  │  │  │  ├─ backports
   │     │  │  │  │  │  ├─ makefile.py
   │     │  │  │  │  │  ├─ weakref_finalize.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ six.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ poolmanager.py
   │     │  │  │  ├─ request.py
   │     │  │  │  ├─ response.py
   │     │  │  │  ├─ util
   │     │  │  │  │  ├─ connection.py
   │     │  │  │  │  ├─ proxy.py
   │     │  │  │  │  ├─ queue.py
   │     │  │  │  │  ├─ request.py
   │     │  │  │  │  ├─ response.py
   │     │  │  │  │  ├─ retry.py
   │     │  │  │  │  ├─ ssltransport.py
   │     │  │  │  │  ├─ ssl_.py
   │     │  │  │  │  ├─ ssl_match_hostname.py
   │     │  │  │  │  ├─ timeout.py
   │     │  │  │  │  ├─ url.py
   │     │  │  │  │  ├─ wait.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ _collections.py
   │     │  │  │  ├─ _version.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ vendor.txt
   │     │  │  └─ __init__.py
   │     │  ├─ __init__.py
   │     │  ├─ __main__.py
   │     │  └─ __pip-runner__.py
   │     ├─ pip-25.0.1.dist-info
   │     │  ├─ AUTHORS.txt
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE.txt
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ pkg_resources
   │     │  ├─ extern
   │     │  │  └─ __init__.py
   │     │  ├─ _vendor
   │     │  │  ├─ appdirs.py
   │     │  │  ├─ importlib_resources
   │     │  │  │  ├─ abc.py
   │     │  │  │  ├─ readers.py
   │     │  │  │  ├─ simple.py
   │     │  │  │  ├─ _adapters.py
   │     │  │  │  ├─ _common.py
   │     │  │  │  ├─ _compat.py
   │     │  │  │  ├─ _itertools.py
   │     │  │  │  ├─ _legacy.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ jaraco
   │     │  │  │  ├─ context.py
   │     │  │  │  ├─ functools.py
   │     │  │  │  ├─ text
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ more_itertools
   │     │  │  │  ├─ more.py
   │     │  │  │  ├─ recipes.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ packaging
   │     │  │  │  ├─ markers.py
   │     │  │  │  ├─ requirements.py
   │     │  │  │  ├─ specifiers.py
   │     │  │  │  ├─ tags.py
   │     │  │  │  ├─ utils.py
   │     │  │  │  ├─ version.py
   │     │  │  │  ├─ _manylinux.py
   │     │  │  │  ├─ _musllinux.py
   │     │  │  │  ├─ _structures.py
   │     │  │  │  ├─ __about__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ pyparsing
   │     │  │  │  ├─ actions.py
   │     │  │  │  ├─ common.py
   │     │  │  │  ├─ core.py
   │     │  │  │  ├─ diagram
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ exceptions.py
   │     │  │  │  ├─ helpers.py
   │     │  │  │  ├─ results.py
   │     │  │  │  ├─ testing.py
   │     │  │  │  ├─ unicode.py
   │     │  │  │  ├─ util.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ zipp.py
   │     │  │  └─ __init__.py
   │     │  └─ __init__.py
   │     ├─ preshed
   │     │  ├─ about.py
   │     │  ├─ bloom.cp311-win_amd64.pyd
   │     │  ├─ bloom.pxd
   │     │  ├─ bloom.pyx
   │     │  ├─ counter.cp311-win_amd64.pyd
   │     │  ├─ counter.pxd
   │     │  ├─ counter.pyx
   │     │  ├─ maps.cp311-win_amd64.pyd
   │     │  ├─ maps.pxd
   │     │  ├─ maps.pyx
   │     │  ├─ tests
   │     │  │  ├─ test_bloom.py
   │     │  │  ├─ test_counter.py
   │     │  │  ├─ test_hashing.py
   │     │  │  ├─ test_pop.py
   │     │  │  └─ __init__.py
   │     │  ├─ __init__.pxd
   │     │  └─ __init__.py
   │     ├─ preshed-3.0.9.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ proto
   │     │  ├─ datetime_helpers.py
   │     │  ├─ enums.py
   │     │  ├─ fields.py
   │     │  ├─ marshal
   │     │  │  ├─ collections
   │     │  │  │  ├─ maps.py
   │     │  │  │  ├─ repeated.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ compat.py
   │     │  │  ├─ marshal.py
   │     │  │  ├─ rules
   │     │  │  │  ├─ bytes.py
   │     │  │  │  ├─ dates.py
   │     │  │  │  ├─ enums.py
   │     │  │  │  ├─ field_mask.py
   │     │  │  │  ├─ message.py
   │     │  │  │  ├─ stringy_numbers.py
   │     │  │  │  ├─ struct.py
   │     │  │  │  ├─ wrappers.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ message.py
   │     │  ├─ modules.py
   │     │  ├─ primitives.py
   │     │  ├─ utils.py
   │     │  ├─ version.py
   │     │  ├─ _file_info.py
   │     │  ├─ _package_info.py
   │     │  └─ __init__.py
   │     ├─ protobuf-5.29.3.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  └─ WHEEL
   │     ├─ proto_plus-1.26.1.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ pyasn1
   │     │  ├─ codec
   │     │  │  ├─ ber
   │     │  │  │  ├─ decoder.py
   │     │  │  │  ├─ encoder.py
   │     │  │  │  ├─ eoo.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ cer
   │     │  │  │  ├─ decoder.py
   │     │  │  │  ├─ encoder.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ der
   │     │  │  │  ├─ decoder.py
   │     │  │  │  ├─ encoder.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ native
   │     │  │  │  ├─ decoder.py
   │     │  │  │  ├─ encoder.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ streaming.py
   │     │  │  └─ __init__.py
   │     │  ├─ compat
   │     │  │  ├─ integer.py
   │     │  │  └─ __init__.py
   │     │  ├─ debug.py
   │     │  ├─ error.py
   │     │  ├─ type
   │     │  │  ├─ base.py
   │     │  │  ├─ char.py
   │     │  │  ├─ constraint.py
   │     │  │  ├─ error.py
   │     │  │  ├─ namedtype.py
   │     │  │  ├─ namedval.py
   │     │  │  ├─ opentype.py
   │     │  │  ├─ tag.py
   │     │  │  ├─ tagmap.py
   │     │  │  ├─ univ.py
   │     │  │  ├─ useful.py
   │     │  │  └─ __init__.py
   │     │  └─ __init__.py
   │     ├─ pyasn1-0.6.1.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE.rst
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  ├─ WHEEL
   │     │  └─ zip-safe
   │     ├─ pyasn1_modules
   │     │  ├─ pem.py
   │     │  ├─ rfc1155.py
   │     │  ├─ rfc1157.py
   │     │  ├─ rfc1901.py
   │     │  ├─ rfc1902.py
   │     │  ├─ rfc1905.py
   │     │  ├─ rfc2251.py
   │     │  ├─ rfc2314.py
   │     │  ├─ rfc2315.py
   │     │  ├─ rfc2437.py
   │     │  ├─ rfc2459.py
   │     │  ├─ rfc2511.py
   │     │  ├─ rfc2560.py
   │     │  ├─ rfc2631.py
   │     │  ├─ rfc2634.py
   │     │  ├─ rfc2876.py
   │     │  ├─ rfc2985.py
   │     │  ├─ rfc2986.py
   │     │  ├─ rfc3058.py
   │     │  ├─ rfc3114.py
   │     │  ├─ rfc3125.py
   │     │  ├─ rfc3161.py
   │     │  ├─ rfc3274.py
   │     │  ├─ rfc3279.py
   │     │  ├─ rfc3280.py
   │     │  ├─ rfc3281.py
   │     │  ├─ rfc3370.py
   │     │  ├─ rfc3412.py
   │     │  ├─ rfc3414.py
   │     │  ├─ rfc3447.py
   │     │  ├─ rfc3537.py
   │     │  ├─ rfc3560.py
   │     │  ├─ rfc3565.py
   │     │  ├─ rfc3657.py
   │     │  ├─ rfc3709.py
   │     │  ├─ rfc3739.py
   │     │  ├─ rfc3770.py
   │     │  ├─ rfc3779.py
   │     │  ├─ rfc3820.py
   │     │  ├─ rfc3852.py
   │     │  ├─ rfc4010.py
   │     │  ├─ rfc4043.py
   │     │  ├─ rfc4055.py
   │     │  ├─ rfc4073.py
   │     │  ├─ rfc4108.py
   │     │  ├─ rfc4210.py
   │     │  ├─ rfc4211.py
   │     │  ├─ rfc4334.py
   │     │  ├─ rfc4357.py
   │     │  ├─ rfc4387.py
   │     │  ├─ rfc4476.py
   │     │  ├─ rfc4490.py
   │     │  ├─ rfc4491.py
   │     │  ├─ rfc4683.py
   │     │  ├─ rfc4985.py
   │     │  ├─ rfc5035.py
   │     │  ├─ rfc5083.py
   │     │  ├─ rfc5084.py
   │     │  ├─ rfc5126.py
   │     │  ├─ rfc5208.py
   │     │  ├─ rfc5275.py
   │     │  ├─ rfc5280.py
   │     │  ├─ rfc5480.py
   │     │  ├─ rfc5636.py
   │     │  ├─ rfc5639.py
   │     │  ├─ rfc5649.py
   │     │  ├─ rfc5652.py
   │     │  ├─ rfc5697.py
   │     │  ├─ rfc5751.py
   │     │  ├─ rfc5752.py
   │     │  ├─ rfc5753.py
   │     │  ├─ rfc5755.py
   │     │  ├─ rfc5913.py
   │     │  ├─ rfc5914.py
   │     │  ├─ rfc5915.py
   │     │  ├─ rfc5916.py
   │     │  ├─ rfc5917.py
   │     │  ├─ rfc5924.py
   │     │  ├─ rfc5934.py
   │     │  ├─ rfc5940.py
   │     │  ├─ rfc5958.py
   │     │  ├─ rfc5990.py
   │     │  ├─ rfc6010.py
   │     │  ├─ rfc6019.py
   │     │  ├─ rfc6031.py
   │     │  ├─ rfc6032.py
   │     │  ├─ rfc6120.py
   │     │  ├─ rfc6170.py
   │     │  ├─ rfc6187.py
   │     │  ├─ rfc6210.py
   │     │  ├─ rfc6211.py
   │     │  ├─ rfc6402.py
   │     │  ├─ rfc6482.py
   │     │  ├─ rfc6486.py
   │     │  ├─ rfc6487.py
   │     │  ├─ rfc6664.py
   │     │  ├─ rfc6955.py
   │     │  ├─ rfc6960.py
   │     │  ├─ rfc7030.py
   │     │  ├─ rfc7191.py
   │     │  ├─ rfc7229.py
   │     │  ├─ rfc7292.py
   │     │  ├─ rfc7296.py
   │     │  ├─ rfc7508.py
   │     │  ├─ rfc7585.py
   │     │  ├─ rfc7633.py
   │     │  ├─ rfc7773.py
   │     │  ├─ rfc7894.py
   │     │  ├─ rfc7906.py
   │     │  ├─ rfc7914.py
   │     │  ├─ rfc8017.py
   │     │  ├─ rfc8018.py
   │     │  ├─ rfc8103.py
   │     │  ├─ rfc8209.py
   │     │  ├─ rfc8226.py
   │     │  ├─ rfc8358.py
   │     │  ├─ rfc8360.py
   │     │  ├─ rfc8398.py
   │     │  ├─ rfc8410.py
   │     │  ├─ rfc8418.py
   │     │  ├─ rfc8419.py
   │     │  ├─ rfc8479.py
   │     │  ├─ rfc8494.py
   │     │  ├─ rfc8520.py
   │     │  ├─ rfc8619.py
   │     │  ├─ rfc8649.py
   │     │  ├─ rfc8692.py
   │     │  ├─ rfc8696.py
   │     │  ├─ rfc8702.py
   │     │  ├─ rfc8708.py
   │     │  ├─ rfc8769.py
   │     │  └─ __init__.py
   │     ├─ pyasn1_modules-0.4.1.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE.txt
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  ├─ WHEEL
   │     │  └─ zip-safe
   │     ├─ pycparser
   │     │  ├─ ast_transforms.py
   │     │  ├─ c_ast.py
   │     │  ├─ c_generator.py
   │     │  ├─ c_lexer.py
   │     │  ├─ c_parser.py
   │     │  ├─ lextab.py
   │     │  ├─ ply
   │     │  │  ├─ cpp.py
   │     │  │  ├─ ctokens.py
   │     │  │  ├─ lex.py
   │     │  │  ├─ yacc.py
   │     │  │  ├─ ygen.py
   │     │  │  └─ __init__.py
   │     │  ├─ plyparser.py
   │     │  ├─ yacctab.py
   │     │  ├─ _ast_gen.py
   │     │  ├─ _build_tables.py
   │     │  ├─ _c_ast.cfg
   │     │  └─ __init__.py
   │     ├─ pycparser-2.22.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ pydantic
   │     │  ├─ aliases.py
   │     │  ├─ alias_generators.py
   │     │  ├─ annotated_handlers.py
   │     │  ├─ class_validators.py
   │     │  ├─ color.py
   │     │  ├─ config.py
   │     │  ├─ dataclasses.py
   │     │  ├─ datetime_parse.py
   │     │  ├─ decorator.py
   │     │  ├─ deprecated
   │     │  │  ├─ class_validators.py
   │     │  │  ├─ config.py
   │     │  │  ├─ copy_internals.py
   │     │  │  ├─ decorator.py
   │     │  │  ├─ json.py
   │     │  │  ├─ parse.py
   │     │  │  ├─ tools.py
   │     │  │  └─ __init__.py
   │     │  ├─ env_settings.py
   │     │  ├─ errors.py
   │     │  ├─ error_wrappers.py
   │     │  ├─ experimental
   │     │  │  ├─ pipeline.py
   │     │  │  └─ __init__.py
   │     │  ├─ fields.py
   │     │  ├─ functional_serializers.py
   │     │  ├─ functional_validators.py
   │     │  ├─ generics.py
   │     │  ├─ json.py
   │     │  ├─ json_schema.py
   │     │  ├─ main.py
   │     │  ├─ mypy.py
   │     │  ├─ networks.py
   │     │  ├─ parse.py
   │     │  ├─ plugin
   │     │  │  ├─ _loader.py
   │     │  │  ├─ _schema_validator.py
   │     │  │  └─ __init__.py
   │     │  ├─ py.typed
   │     │  ├─ root_model.py
   │     │  ├─ schema.py
   │     │  ├─ tools.py
   │     │  ├─ types.py
   │     │  ├─ type_adapter.py
   │     │  ├─ typing.py
   │     │  ├─ utils.py
   │     │  ├─ v1
   │     │  │  ├─ annotated_types.py
   │     │  │  ├─ class_validators.py
   │     │  │  ├─ color.py
   │     │  │  ├─ config.py
   │     │  │  ├─ dataclasses.py
   │     │  │  ├─ datetime_parse.py
   │     │  │  ├─ decorator.py
   │     │  │  ├─ env_settings.py
   │     │  │  ├─ errors.py
   │     │  │  ├─ error_wrappers.py
   │     │  │  ├─ fields.py
   │     │  │  ├─ generics.py
   │     │  │  ├─ json.py
   │     │  │  ├─ main.py
   │     │  │  ├─ mypy.py
   │     │  │  ├─ networks.py
   │     │  │  ├─ parse.py
   │     │  │  ├─ py.typed
   │     │  │  ├─ schema.py
   │     │  │  ├─ tools.py
   │     │  │  ├─ types.py
   │     │  │  ├─ typing.py
   │     │  │  ├─ utils.py
   │     │  │  ├─ validators.py
   │     │  │  ├─ version.py
   │     │  │  ├─ _hypothesis_plugin.py
   │     │  │  └─ __init__.py
   │     │  ├─ validate_call_decorator.py
   │     │  ├─ validators.py
   │     │  ├─ version.py
   │     │  ├─ warnings.py
   │     │  ├─ _internal
   │     │  │  ├─ _config.py
   │     │  │  ├─ _core_metadata.py
   │     │  │  ├─ _core_utils.py
   │     │  │  ├─ _dataclasses.py
   │     │  │  ├─ _decorators.py
   │     │  │  ├─ _decorators_v1.py
   │     │  │  ├─ _discriminated_union.py
   │     │  │  ├─ _docs_extraction.py
   │     │  │  ├─ _fields.py
   │     │  │  ├─ _forward_ref.py
   │     │  │  ├─ _generate_schema.py
   │     │  │  ├─ _generics.py
   │     │  │  ├─ _git.py
   │     │  │  ├─ _import_utils.py
   │     │  │  ├─ _internal_dataclass.py
   │     │  │  ├─ _known_annotated_metadata.py
   │     │  │  ├─ _mock_val_ser.py
   │     │  │  ├─ _model_construction.py
   │     │  │  ├─ _namespace_utils.py
   │     │  │  ├─ _repr.py
   │     │  │  ├─ _schema_generation_shared.py
   │     │  │  ├─ _serializers.py
   │     │  │  ├─ _signature.py
   │     │  │  ├─ _std_types_schema.py
   │     │  │  ├─ _typing_extra.py
   │     │  │  ├─ _utils.py
   │     │  │  ├─ _validate_call.py
   │     │  │  ├─ _validators.py
   │     │  │  └─ __init__.py
   │     │  ├─ _migration.py
   │     │  └─ __init__.py
   │     ├─ pydantic-2.10.6.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  └─ WHEEL
   │     ├─ pydantic_core
   │     │  ├─ core_schema.py
   │     │  ├─ py.typed
   │     │  ├─ _pydantic_core.cp311-win_amd64.pyd
   │     │  ├─ _pydantic_core.pyi
   │     │  └─ __init__.py
   │     ├─ pydantic_core-2.27.2.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  └─ WHEEL
   │     ├─ pygments
   │     │  ├─ cmdline.py
   │     │  ├─ console.py
   │     │  ├─ filter.py
   │     │  ├─ filters
   │     │  │  └─ __init__.py
   │     │  ├─ formatter.py
   │     │  ├─ formatters
   │     │  │  ├─ bbcode.py
   │     │  │  ├─ groff.py
   │     │  │  ├─ html.py
   │     │  │  ├─ img.py
   │     │  │  ├─ irc.py
   │     │  │  ├─ latex.py
   │     │  │  ├─ other.py
   │     │  │  ├─ pangomarkup.py
   │     │  │  ├─ rtf.py
   │     │  │  ├─ svg.py
   │     │  │  ├─ terminal.py
   │     │  │  ├─ terminal256.py
   │     │  │  ├─ _mapping.py
   │     │  │  └─ __init__.py
   │     │  ├─ lexer.py
   │     │  ├─ lexers
   │     │  │  ├─ actionscript.py
   │     │  │  ├─ ada.py
   │     │  │  ├─ agile.py
   │     │  │  ├─ algebra.py
   │     │  │  ├─ ambient.py
   │     │  │  ├─ amdgpu.py
   │     │  │  ├─ ampl.py
   │     │  │  ├─ apdlexer.py
   │     │  │  ├─ apl.py
   │     │  │  ├─ archetype.py
   │     │  │  ├─ arrow.py
   │     │  │  ├─ arturo.py
   │     │  │  ├─ asc.py
   │     │  │  ├─ asm.py
   │     │  │  ├─ asn1.py
   │     │  │  ├─ automation.py
   │     │  │  ├─ bare.py
   │     │  │  ├─ basic.py
   │     │  │  ├─ bdd.py
   │     │  │  ├─ berry.py
   │     │  │  ├─ bibtex.py
   │     │  │  ├─ blueprint.py
   │     │  │  ├─ boa.py
   │     │  │  ├─ bqn.py
   │     │  │  ├─ business.py
   │     │  │  ├─ capnproto.py
   │     │  │  ├─ carbon.py
   │     │  │  ├─ cddl.py
   │     │  │  ├─ chapel.py
   │     │  │  ├─ clean.py
   │     │  │  ├─ codeql.py
   │     │  │  ├─ comal.py
   │     │  │  ├─ compiled.py
   │     │  │  ├─ configs.py
   │     │  │  ├─ console.py
   │     │  │  ├─ cplint.py
   │     │  │  ├─ crystal.py
   │     │  │  ├─ csound.py
   │     │  │  ├─ css.py
   │     │  │  ├─ c_cpp.py
   │     │  │  ├─ c_like.py
   │     │  │  ├─ d.py
   │     │  │  ├─ dalvik.py
   │     │  │  ├─ data.py
   │     │  │  ├─ dax.py
   │     │  │  ├─ devicetree.py
   │     │  │  ├─ diff.py
   │     │  │  ├─ dns.py
   │     │  │  ├─ dotnet.py
   │     │  │  ├─ dsls.py
   │     │  │  ├─ dylan.py
   │     │  │  ├─ ecl.py
   │     │  │  ├─ eiffel.py
   │     │  │  ├─ elm.py
   │     │  │  ├─ elpi.py
   │     │  │  ├─ email.py
   │     │  │  ├─ erlang.py
   │     │  │  ├─ esoteric.py
   │     │  │  ├─ ezhil.py
   │     │  │  ├─ factor.py
   │     │  │  ├─ fantom.py
   │     │  │  ├─ felix.py
   │     │  │  ├─ fift.py
   │     │  │  ├─ floscript.py
   │     │  │  ├─ forth.py
   │     │  │  ├─ fortran.py
   │     │  │  ├─ foxpro.py
   │     │  │  ├─ freefem.py
   │     │  │  ├─ func.py
   │     │  │  ├─ functional.py
   │     │  │  ├─ futhark.py
   │     │  │  ├─ gcodelexer.py
   │     │  │  ├─ gdscript.py
   │     │  │  ├─ gleam.py
   │     │  │  ├─ go.py
   │     │  │  ├─ grammar_notation.py
   │     │  │  ├─ graph.py
   │     │  │  ├─ graphics.py
   │     │  │  ├─ graphql.py
   │     │  │  ├─ graphviz.py
   │     │  │  ├─ gsql.py
   │     │  │  ├─ hare.py
   │     │  │  ├─ haskell.py
   │     │  │  ├─ haxe.py
   │     │  │  ├─ hdl.py
   │     │  │  ├─ hexdump.py
   │     │  │  ├─ html.py
   │     │  │  ├─ idl.py
   │     │  │  ├─ igor.py
   │     │  │  ├─ inferno.py
   │     │  │  ├─ installers.py
   │     │  │  ├─ int_fiction.py
   │     │  │  ├─ iolang.py
   │     │  │  ├─ j.py
   │     │  │  ├─ javascript.py
   │     │  │  ├─ jmespath.py
   │     │  │  ├─ jslt.py
   │     │  │  ├─ json5.py
   │     │  │  ├─ jsonnet.py
   │     │  │  ├─ jsx.py
   │     │  │  ├─ julia.py
   │     │  │  ├─ jvm.py
   │     │  │  ├─ kuin.py
   │     │  │  ├─ kusto.py
   │     │  │  ├─ ldap.py
   │     │  │  ├─ lean.py
   │     │  │  ├─ lilypond.py
   │     │  │  ├─ lisp.py
   │     │  │  ├─ macaulay2.py
   │     │  │  ├─ make.py
   │     │  │  ├─ maple.py
   │     │  │  ├─ markup.py
   │     │  │  ├─ math.py
   │     │  │  ├─ matlab.py
   │     │  │  ├─ maxima.py
   │     │  │  ├─ meson.py
   │     │  │  ├─ mime.py
   │     │  │  ├─ minecraft.py
   │     │  │  ├─ mips.py
   │     │  │  ├─ ml.py
   │     │  │  ├─ modeling.py
   │     │  │  ├─ modula2.py
   │     │  │  ├─ mojo.py
   │     │  │  ├─ monte.py
   │     │  │  ├─ mosel.py
   │     │  │  ├─ ncl.py
   │     │  │  ├─ nimrod.py
   │     │  │  ├─ nit.py
   │     │  │  ├─ nix.py
   │     │  │  ├─ numbair.py
   │     │  │  ├─ oberon.py
   │     │  │  ├─ objective.py
   │     │  │  ├─ ooc.py
   │     │  │  ├─ openscad.py
   │     │  │  ├─ other.py
   │     │  │  ├─ parasail.py
   │     │  │  ├─ parsers.py
   │     │  │  ├─ pascal.py
   │     │  │  ├─ pawn.py
   │     │  │  ├─ pddl.py
   │     │  │  ├─ perl.py
   │     │  │  ├─ phix.py
   │     │  │  ├─ php.py
   │     │  │  ├─ pointless.py
   │     │  │  ├─ pony.py
   │     │  │  ├─ praat.py
   │     │  │  ├─ procfile.py
   │     │  │  ├─ prolog.py
   │     │  │  ├─ promql.py
   │     │  │  ├─ prql.py
   │     │  │  ├─ ptx.py
   │     │  │  ├─ python.py
   │     │  │  ├─ q.py
   │     │  │  ├─ qlik.py
   │     │  │  ├─ qvt.py
   │     │  │  ├─ r.py
   │     │  │  ├─ rdf.py
   │     │  │  ├─ rebol.py
   │     │  │  ├─ rego.py
   │     │  │  ├─ resource.py
   │     │  │  ├─ ride.py
   │     │  │  ├─ rita.py
   │     │  │  ├─ rnc.py
   │     │  │  ├─ roboconf.py
   │     │  │  ├─ robotframework.py
   │     │  │  ├─ ruby.py
   │     │  │  ├─ rust.py
   │     │  │  ├─ sas.py
   │     │  │  ├─ savi.py
   │     │  │  ├─ scdoc.py
   │     │  │  ├─ scripting.py
   │     │  │  ├─ sgf.py
   │     │  │  ├─ shell.py
   │     │  │  ├─ sieve.py
   │     │  │  ├─ slash.py
   │     │  │  ├─ smalltalk.py
   │     │  │  ├─ smithy.py
   │     │  │  ├─ smv.py
   │     │  │  ├─ snobol.py
   │     │  │  ├─ solidity.py
   │     │  │  ├─ soong.py
   │     │  │  ├─ sophia.py
   │     │  │  ├─ special.py
   │     │  │  ├─ spice.py
   │     │  │  ├─ sql.py
   │     │  │  ├─ srcinfo.py
   │     │  │  ├─ stata.py
   │     │  │  ├─ supercollider.py
   │     │  │  ├─ tablegen.py
   │     │  │  ├─ tact.py
   │     │  │  ├─ tal.py
   │     │  │  ├─ tcl.py
   │     │  │  ├─ teal.py
   │     │  │  ├─ templates.py
   │     │  │  ├─ teraterm.py
   │     │  │  ├─ testing.py
   │     │  │  ├─ text.py
   │     │  │  ├─ textedit.py
   │     │  │  ├─ textfmts.py
   │     │  │  ├─ theorem.py
   │     │  │  ├─ thingsdb.py
   │     │  │  ├─ tlb.py
   │     │  │  ├─ tls.py
   │     │  │  ├─ tnt.py
   │     │  │  ├─ trafficscript.py
   │     │  │  ├─ typoscript.py
   │     │  │  ├─ typst.py
   │     │  │  ├─ ul4.py
   │     │  │  ├─ unicon.py
   │     │  │  ├─ urbi.py
   │     │  │  ├─ usd.py
   │     │  │  ├─ varnish.py
   │     │  │  ├─ verification.py
   │     │  │  ├─ verifpal.py
   │     │  │  ├─ vip.py
   │     │  │  ├─ vyper.py
   │     │  │  ├─ web.py
   │     │  │  ├─ webassembly.py
   │     │  │  ├─ webidl.py
   │     │  │  ├─ webmisc.py
   │     │  │  ├─ wgsl.py
   │     │  │  ├─ whiley.py
   │     │  │  ├─ wowtoc.py
   │     │  │  ├─ wren.py
   │     │  │  ├─ x10.py
   │     │  │  ├─ xorg.py
   │     │  │  ├─ yang.py
   │     │  │  ├─ yara.py
   │     │  │  ├─ zig.py
   │     │  │  ├─ _ada_builtins.py
   │     │  │  ├─ _asy_builtins.py
   │     │  │  ├─ _cl_builtins.py
   │     │  │  ├─ _cocoa_builtins.py
   │     │  │  ├─ _csound_builtins.py
   │     │  │  ├─ _css_builtins.py
   │     │  │  ├─ _googlesql_builtins.py
   │     │  │  ├─ _julia_builtins.py
   │     │  │  ├─ _lasso_builtins.py
   │     │  │  ├─ _lilypond_builtins.py
   │     │  │  ├─ _luau_builtins.py
   │     │  │  ├─ _lua_builtins.py
   │     │  │  ├─ _mapping.py
   │     │  │  ├─ _mql_builtins.py
   │     │  │  ├─ _mysql_builtins.py
   │     │  │  ├─ _openedge_builtins.py
   │     │  │  ├─ _php_builtins.py
   │     │  │  ├─ _postgres_builtins.py
   │     │  │  ├─ _qlik_builtins.py
   │     │  │  ├─ _scheme_builtins.py
   │     │  │  ├─ _scilab_builtins.py
   │     │  │  ├─ _sourcemod_builtins.py
   │     │  │  ├─ _stan_builtins.py
   │     │  │  ├─ _stata_builtins.py
   │     │  │  ├─ _tsql_builtins.py
   │     │  │  ├─ _usd_builtins.py
   │     │  │  ├─ _vbscript_builtins.py
   │     │  │  ├─ _vim_builtins.py
   │     │  │  └─ __init__.py
   │     │  ├─ modeline.py
   │     │  ├─ plugin.py
   │     │  ├─ regexopt.py
   │     │  ├─ scanner.py
   │     │  ├─ sphinxext.py
   │     │  ├─ style.py
   │     │  ├─ styles
   │     │  │  ├─ abap.py
   │     │  │  ├─ algol.py
   │     │  │  ├─ algol_nu.py
   │     │  │  ├─ arduino.py
   │     │  │  ├─ autumn.py
   │     │  │  ├─ borland.py
   │     │  │  ├─ bw.py
   │     │  │  ├─ coffee.py
   │     │  │  ├─ colorful.py
   │     │  │  ├─ default.py
   │     │  │  ├─ dracula.py
   │     │  │  ├─ emacs.py
   │     │  │  ├─ friendly.py
   │     │  │  ├─ friendly_grayscale.py
   │     │  │  ├─ fruity.py
   │     │  │  ├─ gh_dark.py
   │     │  │  ├─ gruvbox.py
   │     │  │  ├─ igor.py
   │     │  │  ├─ inkpot.py
   │     │  │  ├─ lightbulb.py
   │     │  │  ├─ lilypond.py
   │     │  │  ├─ lovelace.py
   │     │  │  ├─ manni.py
   │     │  │  ├─ material.py
   │     │  │  ├─ monokai.py
   │     │  │  ├─ murphy.py
   │     │  │  ├─ native.py
   │     │  │  ├─ nord.py
   │     │  │  ├─ onedark.py
   │     │  │  ├─ paraiso_dark.py
   │     │  │  ├─ paraiso_light.py
   │     │  │  ├─ pastie.py
   │     │  │  ├─ perldoc.py
   │     │  │  ├─ rainbow_dash.py
   │     │  │  ├─ rrt.py
   │     │  │  ├─ sas.py
   │     │  │  ├─ solarized.py
   │     │  │  ├─ staroffice.py
   │     │  │  ├─ stata_dark.py
   │     │  │  ├─ stata_light.py
   │     │  │  ├─ tango.py
   │     │  │  ├─ trac.py
   │     │  │  ├─ vim.py
   │     │  │  ├─ vs.py
   │     │  │  ├─ xcode.py
   │     │  │  ├─ zenburn.py
   │     │  │  ├─ _mapping.py
   │     │  │  └─ __init__.py
   │     │  ├─ token.py
   │     │  ├─ unistring.py
   │     │  ├─ util.py
   │     │  ├─ __init__.py
   │     │  └─ __main__.py
   │     ├─ pygments-2.19.1.dist-info
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  ├─ AUTHORS
   │     │  │  └─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  └─ WHEEL
   │     ├─ pymupdf
   │     │  ├─ extra.py
   │     │  ├─ mupdf-devel
   │     │  │  ├─ include
   │     │  │  │  └─ mupdf
   │     │  │  │     ├─ classes.h
   │     │  │  │     ├─ classes2.h
   │     │  │  │     ├─ exceptions.h
   │     │  │  │     ├─ extra.h
   │     │  │  │     ├─ fitz
   │     │  │  │     │  ├─ archive.h
   │     │  │  │     │  ├─ band-writer.h
   │     │  │  │     │  ├─ bidi.h
   │     │  │  │     │  ├─ bitmap.h
   │     │  │  │     │  ├─ buffer.h
   │     │  │  │     │  ├─ color.h
   │     │  │  │     │  ├─ compress.h
   │     │  │  │     │  ├─ compressed-buffer.h
   │     │  │  │     │  ├─ config.h
   │     │  │  │     │  ├─ context.h
   │     │  │  │     │  ├─ crypt.h
   │     │  │  │     │  ├─ deskew.h
   │     │  │  │     │  ├─ device.h
   │     │  │  │     │  ├─ display-list.h
   │     │  │  │     │  ├─ document.h
   │     │  │  │     │  ├─ export.h
   │     │  │  │     │  ├─ filter.h
   │     │  │  │     │  ├─ font.h
   │     │  │  │     │  ├─ geometry.h
   │     │  │  │     │  ├─ getopt.h
   │     │  │  │     │  ├─ glyph-cache.h
   │     │  │  │     │  ├─ glyph.h
   │     │  │  │     │  ├─ hash.h
   │     │  │  │     │  ├─ heap-imp.h
   │     │  │  │     │  ├─ heap.h
   │     │  │  │     │  ├─ image.h
   │     │  │  │     │  ├─ link.h
   │     │  │  │     │  ├─ log.h
   │     │  │  │     │  ├─ outline.h
   │     │  │  │     │  ├─ output-svg.h
   │     │  │  │     │  ├─ output.h
   │     │  │  │     │  ├─ path.h
   │     │  │  │     │  ├─ pixmap.h
   │     │  │  │     │  ├─ pool.h
   │     │  │  │     │  ├─ separation.h
   │     │  │  │     │  ├─ shade.h
   │     │  │  │     │  ├─ store.h
   │     │  │  │     │  ├─ story-writer.h
   │     │  │  │     │  ├─ story.h
   │     │  │  │     │  ├─ stream.h
   │     │  │  │     │  ├─ string-util.h
   │     │  │  │     │  ├─ structured-text.h
   │     │  │  │     │  ├─ system.h
   │     │  │  │     │  ├─ text.h
   │     │  │  │     │  ├─ track-usage.h
   │     │  │  │     │  ├─ transition.h
   │     │  │  │     │  ├─ tree.h
   │     │  │  │     │  ├─ types.h
   │     │  │  │     │  ├─ util.h
   │     │  │  │     │  ├─ version.h
   │     │  │  │     │  ├─ write-pixmap.h
   │     │  │  │     │  ├─ writer.h
   │     │  │  │     │  └─ xml.h
   │     │  │  │     ├─ fitz.h
   │     │  │  │     ├─ functions.h
   │     │  │  │     ├─ helpers
   │     │  │  │     │  ├─ mu-office-lib.h
   │     │  │  │     │  ├─ mu-threads.h
   │     │  │  │     │  └─ pkcs7-openssl.h
   │     │  │  │     ├─ html.h
   │     │  │  │     ├─ internal.h
   │     │  │  │     ├─ memento.h
   │     │  │  │     ├─ pdf
   │     │  │  │     │  ├─ annot.h
   │     │  │  │     │  ├─ clean.h
   │     │  │  │     │  ├─ cmap.h
   │     │  │  │     │  ├─ crypt.h
   │     │  │  │     │  ├─ document.h
   │     │  │  │     │  ├─ event.h
   │     │  │  │     │  ├─ font.h
   │     │  │  │     │  ├─ form.h
   │     │  │  │     │  ├─ image-rewriter.h
   │     │  │  │     │  ├─ interpret.h
   │     │  │  │     │  ├─ javascript.h
   │     │  │  │     │  ├─ name-table.h
   │     │  │  │     │  ├─ object.h
   │     │  │  │     │  ├─ page.h
   │     │  │  │     │  ├─ parse.h
   │     │  │  │     │  ├─ recolor.h
   │     │  │  │     │  ├─ resource.h
   │     │  │  │     │  ├─ xref.h
   │     │  │  │     │  └─ zugferd.h
   │     │  │  │     ├─ pdf.h
   │     │  │  │     └─ ucdn.h
   │     │  │  └─ lib
   │     │  │     └─ mupdfcpp64.lib
   │     │  ├─ mupdf.py
   │     │  ├─ mupdfcpp64.dll
   │     │  ├─ pymupdf.py
   │     │  ├─ table.py
   │     │  ├─ utils.py
   │     │  ├─ _apply_pages.py
   │     │  ├─ _build.py
   │     │  ├─ _extra.pyd
   │     │  ├─ _mupdf.pyd
   │     │  ├─ _wxcolors.py
   │     │  ├─ __init__.py
   │     │  └─ __main__.py
   │     ├─ pymupdf-1.25.4.dist-info
   │     │  ├─ COPYING
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ METADATA
   │     │  ├─ README.md
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  └─ WHEEL
   │     ├─ pyparsing
   │     │  ├─ actions.py
   │     │  ├─ common.py
   │     │  ├─ core.py
   │     │  ├─ diagram
   │     │  │  └─ __init__.py
   │     │  ├─ exceptions.py
   │     │  ├─ helpers.py
   │     │  ├─ py.typed
   │     │  ├─ results.py
   │     │  ├─ testing.py
   │     │  ├─ unicode.py
   │     │  ├─ util.py
   │     │  └─ __init__.py
   │     ├─ pyparsing-3.2.1.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  └─ WHEEL
   │     ├─ PySocks-1.7.1.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ python_dateutil-2.9.0.post0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  ├─ WHEEL
   │     │  └─ zip-safe
   │     ├─ python_docx-1.1.2.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ python_dotenv-1.0.1.dist-info
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ pytz
   │     │  ├─ exceptions.py
   │     │  ├─ lazy.py
   │     │  ├─ reference.py
   │     │  ├─ tzfile.py
   │     │  ├─ tzinfo.py
   │     │  ├─ zoneinfo
   │     │  │  ├─ Africa
   │     │  │  │  ├─ Abidjan
   │     │  │  │  ├─ Accra
   │     │  │  │  ├─ Addis_Ababa
   │     │  │  │  ├─ Algiers
   │     │  │  │  ├─ Asmara
   │     │  │  │  ├─ Asmera
   │     │  │  │  ├─ Bamako
   │     │  │  │  ├─ Bangui
   │     │  │  │  ├─ Banjul
   │     │  │  │  ├─ Bissau
   │     │  │  │  ├─ Blantyre
   │     │  │  │  ├─ Brazzaville
   │     │  │  │  ├─ Bujumbura
   │     │  │  │  ├─ Cairo
   │     │  │  │  ├─ Casablanca
   │     │  │  │  ├─ Ceuta
   │     │  │  │  ├─ Conakry
   │     │  │  │  ├─ Dakar
   │     │  │  │  ├─ Dar_es_Salaam
   │     │  │  │  ├─ Djibouti
   │     │  │  │  ├─ Douala
   │     │  │  │  ├─ El_Aaiun
   │     │  │  │  ├─ Freetown
   │     │  │  │  ├─ Gaborone
   │     │  │  │  ├─ Harare
   │     │  │  │  ├─ Johannesburg
   │     │  │  │  ├─ Juba
   │     │  │  │  ├─ Kampala
   │     │  │  │  ├─ Khartoum
   │     │  │  │  ├─ Kigali
   │     │  │  │  ├─ Kinshasa
   │     │  │  │  ├─ Lagos
   │     │  │  │  ├─ Libreville
   │     │  │  │  ├─ Lome
   │     │  │  │  ├─ Luanda
   │     │  │  │  ├─ Lubumbashi
   │     │  │  │  ├─ Lusaka
   │     │  │  │  ├─ Malabo
   │     │  │  │  ├─ Maputo
   │     │  │  │  ├─ Maseru
   │     │  │  │  ├─ Mbabane
   │     │  │  │  ├─ Mogadishu
   │     │  │  │  ├─ Monrovia
   │     │  │  │  ├─ Nairobi
   │     │  │  │  ├─ Ndjamena
   │     │  │  │  ├─ Niamey
   │     │  │  │  ├─ Nouakchott
   │     │  │  │  ├─ Ouagadougou
   │     │  │  │  ├─ Porto-Novo
   │     │  │  │  ├─ Sao_Tome
   │     │  │  │  ├─ Timbuktu
   │     │  │  │  ├─ Tripoli
   │     │  │  │  ├─ Tunis
   │     │  │  │  └─ Windhoek
   │     │  │  ├─ America
   │     │  │  │  ├─ Adak
   │     │  │  │  ├─ Anchorage
   │     │  │  │  ├─ Anguilla
   │     │  │  │  ├─ Antigua
   │     │  │  │  ├─ Araguaina
   │     │  │  │  ├─ Argentina
   │     │  │  │  │  ├─ Buenos_Aires
   │     │  │  │  │  ├─ Catamarca
   │     │  │  │  │  ├─ ComodRivadavia
   │     │  │  │  │  ├─ Cordoba
   │     │  │  │  │  ├─ Jujuy
   │     │  │  │  │  ├─ La_Rioja
   │     │  │  │  │  ├─ Mendoza
   │     │  │  │  │  ├─ Rio_Gallegos
   │     │  │  │  │  ├─ Salta
   │     │  │  │  │  ├─ San_Juan
   │     │  │  │  │  ├─ San_Luis
   │     │  │  │  │  ├─ Tucuman
   │     │  │  │  │  └─ Ushuaia
   │     │  │  │  ├─ Aruba
   │     │  │  │  ├─ Asuncion
   │     │  │  │  ├─ Atikokan
   │     │  │  │  ├─ Atka
   │     │  │  │  ├─ Bahia
   │     │  │  │  ├─ Bahia_Banderas
   │     │  │  │  ├─ Barbados
   │     │  │  │  ├─ Belem
   │     │  │  │  ├─ Belize
   │     │  │  │  ├─ Blanc-Sablon
   │     │  │  │  ├─ Boa_Vista
   │     │  │  │  ├─ Bogota
   │     │  │  │  ├─ Boise
   │     │  │  │  ├─ Buenos_Aires
   │     │  │  │  ├─ Cambridge_Bay
   │     │  │  │  ├─ Campo_Grande
   │     │  │  │  ├─ Cancun
   │     │  │  │  ├─ Caracas
   │     │  │  │  ├─ Catamarca
   │     │  │  │  ├─ Cayenne
   │     │  │  │  ├─ Cayman
   │     │  │  │  ├─ Chicago
   │     │  │  │  ├─ Chihuahua
   │     │  │  │  ├─ Ciudad_Juarez
   │     │  │  │  ├─ Coral_Harbour
   │     │  │  │  ├─ Cordoba
   │     │  │  │  ├─ Costa_Rica
   │     │  │  │  ├─ Creston
   │     │  │  │  ├─ Cuiaba
   │     │  │  │  ├─ Curacao
   │     │  │  │  ├─ Danmarkshavn
   │     │  │  │  ├─ Dawson
   │     │  │  │  ├─ Dawson_Creek
   │     │  │  │  ├─ Denver
   │     │  │  │  ├─ Detroit
   │     │  │  │  ├─ Dominica
   │     │  │  │  ├─ Edmonton
   │     │  │  │  ├─ Eirunepe
   │     │  │  │  ├─ El_Salvador
   │     │  │  │  ├─ Ensenada
   │     │  │  │  ├─ Fortaleza
   │     │  │  │  ├─ Fort_Nelson
   │     │  │  │  ├─ Fort_Wayne
   │     │  │  │  ├─ Glace_Bay
   │     │  │  │  ├─ Godthab
   │     │  │  │  ├─ Goose_Bay
   │     │  │  │  ├─ Grand_Turk
   │     │  │  │  ├─ Grenada
   │     │  │  │  ├─ Guadeloupe
   │     │  │  │  ├─ Guatemala
   │     │  │  │  ├─ Guayaquil
   │     │  │  │  ├─ Guyana
   │     │  │  │  ├─ Halifax
   │     │  │  │  ├─ Havana
   │     │  │  │  ├─ Hermosillo
   │     │  │  │  ├─ Indiana
   │     │  │  │  │  ├─ Indianapolis
   │     │  │  │  │  ├─ Knox
   │     │  │  │  │  ├─ Marengo
   │     │  │  │  │  ├─ Petersburg
   │     │  │  │  │  ├─ Tell_City
   │     │  │  │  │  ├─ Vevay
   │     │  │  │  │  ├─ Vincennes
   │     │  │  │  │  └─ Winamac
   │     │  │  │  ├─ Indianapolis
   │     │  │  │  ├─ Inuvik
   │     │  │  │  ├─ Iqaluit
   │     │  │  │  ├─ Jamaica
   │     │  │  │  ├─ Jujuy
   │     │  │  │  ├─ Juneau
   │     │  │  │  ├─ Kentucky
   │     │  │  │  │  ├─ Louisville
   │     │  │  │  │  └─ Monticello
   │     │  │  │  ├─ Knox_IN
   │     │  │  │  ├─ Kralendijk
   │     │  │  │  ├─ La_Paz
   │     │  │  │  ├─ Lima
   │     │  │  │  ├─ Los_Angeles
   │     │  │  │  ├─ Louisville
   │     │  │  │  ├─ Lower_Princes
   │     │  │  │  ├─ Maceio
   │     │  │  │  ├─ Managua
   │     │  │  │  ├─ Manaus
   │     │  │  │  ├─ Marigot
   │     │  │  │  ├─ Martinique
   │     │  │  │  ├─ Matamoros
   │     │  │  │  ├─ Mazatlan
   │     │  │  │  ├─ Mendoza
   │     │  │  │  ├─ Menominee
   │     │  │  │  ├─ Merida
   │     │  │  │  ├─ Metlakatla
   │     │  │  │  ├─ Mexico_City
   │     │  │  │  ├─ Miquelon
   │     │  │  │  ├─ Moncton
   │     │  │  │  ├─ Monterrey
   │     │  │  │  ├─ Montevideo
   │     │  │  │  ├─ Montreal
   │     │  │  │  ├─ Montserrat
   │     │  │  │  ├─ Nassau
   │     │  │  │  ├─ New_York
   │     │  │  │  ├─ Nipigon
   │     │  │  │  ├─ Nome
   │     │  │  │  ├─ Noronha
   │     │  │  │  ├─ North_Dakota
   │     │  │  │  │  ├─ Beulah
   │     │  │  │  │  ├─ Center
   │     │  │  │  │  └─ New_Salem
   │     │  │  │  ├─ Nuuk
   │     │  │  │  ├─ Ojinaga
   │     │  │  │  ├─ Panama
   │     │  │  │  ├─ Pangnirtung
   │     │  │  │  ├─ Paramaribo
   │     │  │  │  ├─ Phoenix
   │     │  │  │  ├─ Port-au-Prince
   │     │  │  │  ├─ Porto_Acre
   │     │  │  │  ├─ Porto_Velho
   │     │  │  │  ├─ Port_of_Spain
   │     │  │  │  ├─ Puerto_Rico
   │     │  │  │  ├─ Punta_Arenas
   │     │  │  │  ├─ Rainy_River
   │     │  │  │  ├─ Rankin_Inlet
   │     │  │  │  ├─ Recife
   │     │  │  │  ├─ Regina
   │     │  │  │  ├─ Resolute
   │     │  │  │  ├─ Rio_Branco
   │     │  │  │  ├─ Rosario
   │     │  │  │  ├─ Santarem
   │     │  │  │  ├─ Santa_Isabel
   │     │  │  │  ├─ Santiago
   │     │  │  │  ├─ Santo_Domingo
   │     │  │  │  ├─ Sao_Paulo
   │     │  │  │  ├─ Scoresbysund
   │     │  │  │  ├─ Shiprock
   │     │  │  │  ├─ Sitka
   │     │  │  │  ├─ St_Barthelemy
   │     │  │  │  ├─ St_Johns
   │     │  │  │  ├─ St_Kitts
   │     │  │  │  ├─ St_Lucia
   │     │  │  │  ├─ St_Thomas
   │     │  │  │  ├─ St_Vincent
   │     │  │  │  ├─ Swift_Current
   │     │  │  │  ├─ Tegucigalpa
   │     │  │  │  ├─ Thule
   │     │  │  │  ├─ Thunder_Bay
   │     │  │  │  ├─ Tijuana
   │     │  │  │  ├─ Toronto
   │     │  │  │  ├─ Tortola
   │     │  │  │  ├─ Vancouver
   │     │  │  │  ├─ Virgin
   │     │  │  │  ├─ Whitehorse
   │     │  │  │  ├─ Winnipeg
   │     │  │  │  ├─ Yakutat
   │     │  │  │  └─ Yellowknife
   │     │  │  ├─ Antarctica
   │     │  │  │  ├─ Casey
   │     │  │  │  ├─ Davis
   │     │  │  │  ├─ DumontDUrville
   │     │  │  │  ├─ Macquarie
   │     │  │  │  ├─ Mawson
   │     │  │  │  ├─ McMurdo
   │     │  │  │  ├─ Palmer
   │     │  │  │  ├─ Rothera
   │     │  │  │  ├─ South_Pole
   │     │  │  │  ├─ Syowa
   │     │  │  │  ├─ Troll
   │     │  │  │  └─ Vostok
   │     │  │  ├─ Arctic
   │     │  │  │  └─ Longyearbyen
   │     │  │  ├─ Asia
   │     │  │  │  ├─ Aden
   │     │  │  │  ├─ Almaty
   │     │  │  │  ├─ Amman
   │     │  │  │  ├─ Anadyr
   │     │  │  │  ├─ Aqtau
   │     │  │  │  ├─ Aqtobe
   │     │  │  │  ├─ Ashgabat
   │     │  │  │  ├─ Ashkhabad
   │     │  │  │  ├─ Atyrau
   │     │  │  │  ├─ Baghdad
   │     │  │  │  ├─ Bahrain
   │     │  │  │  ├─ Baku
   │     │  │  │  ├─ Bangkok
   │     │  │  │  ├─ Barnaul
   │     │  │  │  ├─ Beirut
   │     │  │  │  ├─ Bishkek
   │     │  │  │  ├─ Brunei
   │     │  │  │  ├─ Calcutta
   │     │  │  │  ├─ Chita
   │     │  │  │  ├─ Choibalsan
   │     │  │  │  ├─ Chongqing
   │     │  │  │  ├─ Chungking
   │     │  │  │  ├─ Colombo
   │     │  │  │  ├─ Dacca
   │     │  │  │  ├─ Damascus
   │     │  │  │  ├─ Dhaka
   │     │  │  │  ├─ Dili
   │     │  │  │  ├─ Dubai
   │     │  │  │  ├─ Dushanbe
   │     │  │  │  ├─ Famagusta
   │     │  │  │  ├─ Gaza
   │     │  │  │  ├─ Harbin
   │     │  │  │  ├─ Hebron
   │     │  │  │  ├─ Hong_Kong
   │     │  │  │  ├─ Hovd
   │     │  │  │  ├─ Ho_Chi_Minh
   │     │  │  │  ├─ Irkutsk
   │     │  │  │  ├─ Istanbul
   │     │  │  │  ├─ Jakarta
   │     │  │  │  ├─ Jayapura
   │     │  │  │  ├─ Jerusalem
   │     │  │  │  ├─ Kabul
   │     │  │  │  ├─ Kamchatka
   │     │  │  │  ├─ Karachi
   │     │  │  │  ├─ Kashgar
   │     │  │  │  ├─ Kathmandu
   │     │  │  │  ├─ Katmandu
   │     │  │  │  ├─ Khandyga
   │     │  │  │  ├─ Kolkata
   │     │  │  │  ├─ Krasnoyarsk
   │     │  │  │  ├─ Kuala_Lumpur
   │     │  │  │  ├─ Kuching
   │     │  │  │  ├─ Kuwait
   │     │  │  │  ├─ Macao
   │     │  │  │  ├─ Macau
   │     │  │  │  ├─ Magadan
   │     │  │  │  ├─ Makassar
   │     │  │  │  ├─ Manila
   │     │  │  │  ├─ Muscat
   │     │  │  │  ├─ Nicosia
   │     │  │  │  ├─ Novokuznetsk
   │     │  │  │  ├─ Novosibirsk
   │     │  │  │  ├─ Omsk
   │     │  │  │  ├─ Oral
   │     │  │  │  ├─ Phnom_Penh
   │     │  │  │  ├─ Pontianak
   │     │  │  │  ├─ Pyongyang
   │     │  │  │  ├─ Qatar
   │     │  │  │  ├─ Qostanay
   │     │  │  │  ├─ Qyzylorda
   │     │  │  │  ├─ Rangoon
   │     │  │  │  ├─ Riyadh
   │     │  │  │  ├─ Saigon
   │     │  │  │  ├─ Sakhalin
   │     │  │  │  ├─ Samarkand
   │     │  │  │  ├─ Seoul
   │     │  │  │  ├─ Shanghai
   │     │  │  │  ├─ Singapore
   │     │  │  │  ├─ Srednekolymsk
   │     │  │  │  ├─ Taipei
   │     │  │  │  ├─ Tashkent
   │     │  │  │  ├─ Tbilisi
   │     │  │  │  ├─ Tehran
   │     │  │  │  ├─ Tel_Aviv
   │     │  │  │  ├─ Thimbu
   │     │  │  │  ├─ Thimphu
   │     │  │  │  ├─ Tokyo
   │     │  │  │  ├─ Tomsk
   │     │  │  │  ├─ Ujung_Pandang
   │     │  │  │  ├─ Ulaanbaatar
   │     │  │  │  ├─ Ulan_Bator
   │     │  │  │  ├─ Urumqi
   │     │  │  │  ├─ Ust-Nera
   │     │  │  │  ├─ Vientiane
   │     │  │  │  ├─ Vladivostok
   │     │  │  │  ├─ Yakutsk
   │     │  │  │  ├─ Yangon
   │     │  │  │  ├─ Yekaterinburg
   │     │  │  │  └─ Yerevan
   │     │  │  ├─ Atlantic
   │     │  │  │  ├─ Azores
   │     │  │  │  ├─ Bermuda
   │     │  │  │  ├─ Canary
   │     │  │  │  ├─ Cape_Verde
   │     │  │  │  ├─ Faeroe
   │     │  │  │  ├─ Faroe
   │     │  │  │  ├─ Jan_Mayen
   │     │  │  │  ├─ Madeira
   │     │  │  │  ├─ Reykjavik
   │     │  │  │  ├─ South_Georgia
   │     │  │  │  ├─ Stanley
   │     │  │  │  └─ St_Helena
   │     │  │  ├─ Australia
   │     │  │  │  ├─ ACT
   │     │  │  │  ├─ Adelaide
   │     │  │  │  ├─ Brisbane
   │     │  │  │  ├─ Broken_Hill
   │     │  │  │  ├─ Canberra
   │     │  │  │  ├─ Currie
   │     │  │  │  ├─ Darwin
   │     │  │  │  ├─ Eucla
   │     │  │  │  ├─ Hobart
   │     │  │  │  ├─ LHI
   │     │  │  │  ├─ Lindeman
   │     │  │  │  ├─ Lord_Howe
   │     │  │  │  ├─ Melbourne
   │     │  │  │  ├─ North
   │     │  │  │  ├─ NSW
   │     │  │  │  ├─ Perth
   │     │  │  │  ├─ Queensland
   │     │  │  │  ├─ South
   │     │  │  │  ├─ Sydney
   │     │  │  │  ├─ Tasmania
   │     │  │  │  ├─ Victoria
   │     │  │  │  ├─ West
   │     │  │  │  └─ Yancowinna
   │     │  │  ├─ Brazil
   │     │  │  │  ├─ Acre
   │     │  │  │  ├─ DeNoronha
   │     │  │  │  ├─ East
   │     │  │  │  └─ West
   │     │  │  ├─ Canada
   │     │  │  │  ├─ Atlantic
   │     │  │  │  ├─ Central
   │     │  │  │  ├─ Eastern
   │     │  │  │  ├─ Mountain
   │     │  │  │  ├─ Newfoundland
   │     │  │  │  ├─ Pacific
   │     │  │  │  ├─ Saskatchewan
   │     │  │  │  └─ Yukon
   │     │  │  ├─ CET
   │     │  │  ├─ Chile
   │     │  │  │  ├─ Continental
   │     │  │  │  └─ EasterIsland
   │     │  │  ├─ CST6CDT
   │     │  │  ├─ Cuba
   │     │  │  ├─ EET
   │     │  │  ├─ Egypt
   │     │  │  ├─ Eire
   │     │  │  ├─ EST
   │     │  │  ├─ EST5EDT
   │     │  │  ├─ Etc
   │     │  │  │  ├─ GMT
   │     │  │  │  ├─ GMT+0
   │     │  │  │  ├─ GMT+1
   │     │  │  │  ├─ GMT+10
   │     │  │  │  ├─ GMT+11
   │     │  │  │  ├─ GMT+12
   │     │  │  │  ├─ GMT+2
   │     │  │  │  ├─ GMT+3
   │     │  │  │  ├─ GMT+4
   │     │  │  │  ├─ GMT+5
   │     │  │  │  ├─ GMT+6
   │     │  │  │  ├─ GMT+7
   │     │  │  │  ├─ GMT+8
   │     │  │  │  ├─ GMT+9
   │     │  │  │  ├─ GMT-0
   │     │  │  │  ├─ GMT-1
   │     │  │  │  ├─ GMT-10
   │     │  │  │  ├─ GMT-11
   │     │  │  │  ├─ GMT-12
   │     │  │  │  ├─ GMT-13
   │     │  │  │  ├─ GMT-14
   │     │  │  │  ├─ GMT-2
   │     │  │  │  ├─ GMT-3
   │     │  │  │  ├─ GMT-4
   │     │  │  │  ├─ GMT-5
   │     │  │  │  ├─ GMT-6
   │     │  │  │  ├─ GMT-7
   │     │  │  │  ├─ GMT-8
   │     │  │  │  ├─ GMT-9
   │     │  │  │  ├─ GMT0
   │     │  │  │  ├─ Greenwich
   │     │  │  │  ├─ UCT
   │     │  │  │  ├─ Universal
   │     │  │  │  ├─ UTC
   │     │  │  │  └─ Zulu
   │     │  │  ├─ Europe
   │     │  │  │  ├─ Amsterdam
   │     │  │  │  ├─ Andorra
   │     │  │  │  ├─ Astrakhan
   │     │  │  │  ├─ Athens
   │     │  │  │  ├─ Belfast
   │     │  │  │  ├─ Belgrade
   │     │  │  │  ├─ Berlin
   │     │  │  │  ├─ Bratislava
   │     │  │  │  ├─ Brussels
   │     │  │  │  ├─ Bucharest
   │     │  │  │  ├─ Budapest
   │     │  │  │  ├─ Busingen
   │     │  │  │  ├─ Chisinau
   │     │  │  │  ├─ Copenhagen
   │     │  │  │  ├─ Dublin
   │     │  │  │  ├─ Gibraltar
   │     │  │  │  ├─ Guernsey
   │     │  │  │  ├─ Helsinki
   │     │  │  │  ├─ Isle_of_Man
   │     │  │  │  ├─ Istanbul
   │     │  │  │  ├─ Jersey
   │     │  │  │  ├─ Kaliningrad
   │     │  │  │  ├─ Kiev
   │     │  │  │  ├─ Kirov
   │     │  │  │  ├─ Kyiv
   │     │  │  │  ├─ Lisbon
   │     │  │  │  ├─ Ljubljana
   │     │  │  │  ├─ London
   │     │  │  │  ├─ Luxembourg
   │     │  │  │  ├─ Madrid
   │     │  │  │  ├─ Malta
   │     │  │  │  ├─ Mariehamn
   │     │  │  │  ├─ Minsk
   │     │  │  │  ├─ Monaco
   │     │  │  │  ├─ Moscow
   │     │  │  │  ├─ Nicosia
   │     │  │  │  ├─ Oslo
   │     │  │  │  ├─ Paris
   │     │  │  │  ├─ Podgorica
   │     │  │  │  ├─ Prague
   │     │  │  │  ├─ Riga
   │     │  │  │  ├─ Rome
   │     │  │  │  ├─ Samara
   │     │  │  │  ├─ San_Marino
   │     │  │  │  ├─ Sarajevo
   │     │  │  │  ├─ Saratov
   │     │  │  │  ├─ Simferopol
   │     │  │  │  ├─ Skopje
   │     │  │  │  ├─ Sofia
   │     │  │  │  ├─ Stockholm
   │     │  │  │  ├─ Tallinn
   │     │  │  │  ├─ Tirane
   │     │  │  │  ├─ Tiraspol
   │     │  │  │  ├─ Ulyanovsk
   │     │  │  │  ├─ Uzhgorod
   │     │  │  │  ├─ Vaduz
   │     │  │  │  ├─ Vatican
   │     │  │  │  ├─ Vienna
   │     │  │  │  ├─ Vilnius
   │     │  │  │  ├─ Volgograd
   │     │  │  │  ├─ Warsaw
   │     │  │  │  ├─ Zagreb
   │     │  │  │  ├─ Zaporozhye
   │     │  │  │  └─ Zurich
   │     │  │  ├─ Factory
   │     │  │  ├─ GB
   │     │  │  ├─ GB-Eire
   │     │  │  ├─ GMT
   │     │  │  ├─ GMT+0
   │     │  │  ├─ GMT-0
   │     │  │  ├─ GMT0
   │     │  │  ├─ Greenwich
   │     │  │  ├─ Hongkong
   │     │  │  ├─ HST
   │     │  │  ├─ Iceland
   │     │  │  ├─ Indian
   │     │  │  │  ├─ Antananarivo
   │     │  │  │  ├─ Chagos
   │     │  │  │  ├─ Christmas
   │     │  │  │  ├─ Cocos
   │     │  │  │  ├─ Comoro
   │     │  │  │  ├─ Kerguelen
   │     │  │  │  ├─ Mahe
   │     │  │  │  ├─ Maldives
   │     │  │  │  ├─ Mauritius
   │     │  │  │  ├─ Mayotte
   │     │  │  │  └─ Reunion
   │     │  │  ├─ Iran
   │     │  │  ├─ iso3166.tab
   │     │  │  ├─ Israel
   │     │  │  ├─ Jamaica
   │     │  │  ├─ Japan
   │     │  │  ├─ Kwajalein
   │     │  │  ├─ leapseconds
   │     │  │  ├─ Libya
   │     │  │  ├─ MET
   │     │  │  ├─ Mexico
   │     │  │  │  ├─ BajaNorte
   │     │  │  │  ├─ BajaSur
   │     │  │  │  └─ General
   │     │  │  ├─ MST
   │     │  │  ├─ MST7MDT
   │     │  │  ├─ Navajo
   │     │  │  ├─ NZ
   │     │  │  ├─ NZ-CHAT
   │     │  │  ├─ Pacific
   │     │  │  │  ├─ Apia
   │     │  │  │  ├─ Auckland
   │     │  │  │  ├─ Bougainville
   │     │  │  │  ├─ Chatham
   │     │  │  │  ├─ Chuuk
   │     │  │  │  ├─ Easter
   │     │  │  │  ├─ Efate
   │     │  │  │  ├─ Enderbury
   │     │  │  │  ├─ Fakaofo
   │     │  │  │  ├─ Fiji
   │     │  │  │  ├─ Funafuti
   │     │  │  │  ├─ Galapagos
   │     │  │  │  ├─ Gambier
   │     │  │  │  ├─ Guadalcanal
   │     │  │  │  ├─ Guam
   │     │  │  │  ├─ Honolulu
   │     │  │  │  ├─ Johnston
   │     │  │  │  ├─ Kanton
   │     │  │  │  ├─ Kiritimati
   │     │  │  │  ├─ Kosrae
   │     │  │  │  ├─ Kwajalein
   │     │  │  │  ├─ Majuro
   │     │  │  │  ├─ Marquesas
   │     │  │  │  ├─ Midway
   │     │  │  │  ├─ Nauru
   │     │  │  │  ├─ Niue
   │     │  │  │  ├─ Norfolk
   │     │  │  │  ├─ Noumea
   │     │  │  │  ├─ Pago_Pago
   │     │  │  │  ├─ Palau
   │     │  │  │  ├─ Pitcairn
   │     │  │  │  ├─ Pohnpei
   │     │  │  │  ├─ Ponape
   │     │  │  │  ├─ Port_Moresby
   │     │  │  │  ├─ Rarotonga
   │     │  │  │  ├─ Saipan
   │     │  │  │  ├─ Samoa
   │     │  │  │  ├─ Tahiti
   │     │  │  │  ├─ Tarawa
   │     │  │  │  ├─ Tongatapu
   │     │  │  │  ├─ Truk
   │     │  │  │  ├─ Wake
   │     │  │  │  ├─ Wallis
   │     │  │  │  └─ Yap
   │     │  │  ├─ Poland
   │     │  │  ├─ Portugal
   │     │  │  ├─ PRC
   │     │  │  ├─ PST8PDT
   │     │  │  ├─ ROC
   │     │  │  ├─ ROK
   │     │  │  ├─ Singapore
   │     │  │  ├─ Turkey
   │     │  │  ├─ tzdata.zi
   │     │  │  ├─ UCT
   │     │  │  ├─ Universal
   │     │  │  ├─ US
   │     │  │  │  ├─ Alaska
   │     │  │  │  ├─ Aleutian
   │     │  │  │  ├─ Arizona
   │     │  │  │  ├─ Central
   │     │  │  │  ├─ East-Indiana
   │     │  │  │  ├─ Eastern
   │     │  │  │  ├─ Hawaii
   │     │  │  │  ├─ Indiana-Starke
   │     │  │  │  ├─ Michigan
   │     │  │  │  ├─ Mountain
   │     │  │  │  ├─ Pacific
   │     │  │  │  └─ Samoa
   │     │  │  ├─ UTC
   │     │  │  ├─ W-SU
   │     │  │  ├─ WET
   │     │  │  ├─ zone.tab
   │     │  │  ├─ zone1970.tab
   │     │  │  ├─ zonenow.tab
   │     │  │  └─ Zulu
   │     │  └─ __init__.py
   │     ├─ pytz-2025.1.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE.txt
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  ├─ WHEEL
   │     │  └─ zip-safe
   │     ├─ regex
   │     │  ├─ regex.py
   │     │  ├─ test_regex.py
   │     │  ├─ _regex.cp311-win_amd64.pyd
   │     │  ├─ _regex_core.py
   │     │  └─ __init__.py
   │     ├─ regex-2024.11.6.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE.txt
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ requests
   │     │  ├─ adapters.py
   │     │  ├─ api.py
   │     │  ├─ auth.py
   │     │  ├─ certs.py
   │     │  ├─ compat.py
   │     │  ├─ cookies.py
   │     │  ├─ exceptions.py
   │     │  ├─ help.py
   │     │  ├─ hooks.py
   │     │  ├─ models.py
   │     │  ├─ packages.py
   │     │  ├─ sessions.py
   │     │  ├─ status_codes.py
   │     │  ├─ structures.py
   │     │  ├─ utils.py
   │     │  ├─ _internal_utils.py
   │     │  ├─ __init__.py
   │     │  └─ __version__.py
   │     ├─ requests-2.32.3.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ requests_oauthlib
   │     │  ├─ compliance_fixes
   │     │  │  ├─ douban.py
   │     │  │  ├─ ebay.py
   │     │  │  ├─ facebook.py
   │     │  │  ├─ fitbit.py
   │     │  │  ├─ instagram.py
   │     │  │  ├─ mailchimp.py
   │     │  │  ├─ plentymarkets.py
   │     │  │  ├─ slack.py
   │     │  │  ├─ weibo.py
   │     │  │  └─ __init__.py
   │     │  ├─ oauth1_auth.py
   │     │  ├─ oauth1_session.py
   │     │  ├─ oauth2_auth.py
   │     │  ├─ oauth2_session.py
   │     │  └─ __init__.py
   │     ├─ requests_oauthlib-2.0.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ rich
   │     │  ├─ abc.py
   │     │  ├─ align.py
   │     │  ├─ ansi.py
   │     │  ├─ bar.py
   │     │  ├─ box.py
   │     │  ├─ cells.py
   │     │  ├─ color.py
   │     │  ├─ color_triplet.py
   │     │  ├─ columns.py
   │     │  ├─ console.py
   │     │  ├─ constrain.py
   │     │  ├─ containers.py
   │     │  ├─ control.py
   │     │  ├─ default_styles.py
   │     │  ├─ diagnose.py
   │     │  ├─ emoji.py
   │     │  ├─ errors.py
   │     │  ├─ filesize.py
   │     │  ├─ file_proxy.py
   │     │  ├─ highlighter.py
   │     │  ├─ json.py
   │     │  ├─ jupyter.py
   │     │  ├─ layout.py
   │     │  ├─ live.py
   │     │  ├─ live_render.py
   │     │  ├─ logging.py
   │     │  ├─ markdown.py
   │     │  ├─ markup.py
   │     │  ├─ measure.py
   │     │  ├─ padding.py
   │     │  ├─ pager.py
   │     │  ├─ palette.py
   │     │  ├─ panel.py
   │     │  ├─ pretty.py
   │     │  ├─ progress.py
   │     │  ├─ progress_bar.py
   │     │  ├─ prompt.py
   │     │  ├─ protocol.py
   │     │  ├─ py.typed
   │     │  ├─ region.py
   │     │  ├─ repr.py
   │     │  ├─ rule.py
   │     │  ├─ scope.py
   │     │  ├─ screen.py
   │     │  ├─ segment.py
   │     │  ├─ spinner.py
   │     │  ├─ status.py
   │     │  ├─ style.py
   │     │  ├─ styled.py
   │     │  ├─ syntax.py
   │     │  ├─ table.py
   │     │  ├─ terminal_theme.py
   │     │  ├─ text.py
   │     │  ├─ theme.py
   │     │  ├─ themes.py
   │     │  ├─ traceback.py
   │     │  ├─ tree.py
   │     │  ├─ _cell_widths.py
   │     │  ├─ _emoji_codes.py
   │     │  ├─ _emoji_replace.py
   │     │  ├─ _export_format.py
   │     │  ├─ _extension.py
   │     │  ├─ _fileno.py
   │     │  ├─ _inspect.py
   │     │  ├─ _log_render.py
   │     │  ├─ _loop.py
   │     │  ├─ _null_file.py
   │     │  ├─ _palettes.py
   │     │  ├─ _pick.py
   │     │  ├─ _ratio.py
   │     │  ├─ _spinners.py
   │     │  ├─ _stack.py
   │     │  ├─ _timer.py
   │     │  ├─ _win32_console.py
   │     │  ├─ _windows.py
   │     │  ├─ _windows_renderer.py
   │     │  ├─ _wrap.py
   │     │  ├─ __init__.py
   │     │  └─ __main__.py
   │     ├─ rich-13.9.4.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  └─ WHEEL
   │     ├─ rsa
   │     │  ├─ asn1.py
   │     │  ├─ cli.py
   │     │  ├─ common.py
   │     │  ├─ core.py
   │     │  ├─ key.py
   │     │  ├─ parallel.py
   │     │  ├─ pem.py
   │     │  ├─ pkcs1.py
   │     │  ├─ pkcs1_v2.py
   │     │  ├─ prime.py
   │     │  ├─ py.typed
   │     │  ├─ randnum.py
   │     │  ├─ transform.py
   │     │  ├─ util.py
   │     │  └─ __init__.py
   │     ├─ rsa-4.9.dist-info
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  └─ WHEEL
   │     ├─ scikit_learn-1.6.1.dist-info
   │     │  ├─ COPYING
   │     │  ├─ INSTALLER
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  └─ WHEEL
   │     ├─ scipy
   │     │  ├─ cluster
   │     │  │  ├─ hierarchy.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ hierarchy_test_data.py
   │     │  │  │  ├─ test_disjoint_set.py
   │     │  │  │  ├─ test_hierarchy.py
   │     │  │  │  ├─ test_vq.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ vq.py
   │     │  │  ├─ _hierarchy.cp311-win_amd64.dll.a
   │     │  │  ├─ _hierarchy.cp311-win_amd64.pyd
   │     │  │  ├─ _optimal_leaf_ordering.cp311-win_amd64.dll.a
   │     │  │  ├─ _optimal_leaf_ordering.cp311-win_amd64.pyd
   │     │  │  ├─ _vq.cp311-win_amd64.dll.a
   │     │  │  ├─ _vq.cp311-win_amd64.pyd
   │     │  │  └─ __init__.py
   │     │  ├─ conftest.py
   │     │  ├─ constants
   │     │  │  ├─ codata.py
   │     │  │  ├─ constants.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_codata.py
   │     │  │  │  ├─ test_constants.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _codata.py
   │     │  │  ├─ _constants.py
   │     │  │  └─ __init__.py
   │     │  ├─ datasets
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_data.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _download_all.py
   │     │  │  ├─ _fetchers.py
   │     │  │  ├─ _registry.py
   │     │  │  ├─ _utils.py
   │     │  │  └─ __init__.py
   │     │  ├─ differentiate
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_differentiate.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _differentiate.py
   │     │  │  └─ __init__.py
   │     │  ├─ fft
   │     │  │  ├─ tests
   │     │  │  │  ├─ mock_backend.py
   │     │  │  │  ├─ test_backend.py
   │     │  │  │  ├─ test_basic.py
   │     │  │  │  ├─ test_fftlog.py
   │     │  │  │  ├─ test_helper.py
   │     │  │  │  ├─ test_multithreading.py
   │     │  │  │  ├─ test_real_transforms.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _backend.py
   │     │  │  ├─ _basic.py
   │     │  │  ├─ _basic_backend.py
   │     │  │  ├─ _debug_backends.py
   │     │  │  ├─ _fftlog.py
   │     │  │  ├─ _fftlog_backend.py
   │     │  │  ├─ _helper.py
   │     │  │  ├─ _pocketfft
   │     │  │  │  ├─ basic.py
   │     │  │  │  ├─ helper.py
   │     │  │  │  ├─ LICENSE.md
   │     │  │  │  ├─ pypocketfft.cp311-win_amd64.dll.a
   │     │  │  │  ├─ pypocketfft.cp311-win_amd64.pyd
   │     │  │  │  ├─ realtransforms.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ test_basic.py
   │     │  │  │  │  ├─ test_real_transforms.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _realtransforms.py
   │     │  │  ├─ _realtransforms_backend.py
   │     │  │  └─ __init__.py
   │     │  ├─ fftpack
   │     │  │  ├─ basic.py
   │     │  │  ├─ convolve.cp311-win_amd64.dll.a
   │     │  │  ├─ convolve.cp311-win_amd64.pyd
   │     │  │  ├─ helper.py
   │     │  │  ├─ pseudo_diffs.py
   │     │  │  ├─ realtransforms.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ fftw_double_ref.npz
   │     │  │  │  ├─ fftw_longdouble_ref.npz
   │     │  │  │  ├─ fftw_single_ref.npz
   │     │  │  │  ├─ test.npz
   │     │  │  │  ├─ test_basic.py
   │     │  │  │  ├─ test_helper.py
   │     │  │  │  ├─ test_import.py
   │     │  │  │  ├─ test_pseudo_diffs.py
   │     │  │  │  ├─ test_real_transforms.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _basic.py
   │     │  │  ├─ _helper.py
   │     │  │  ├─ _pseudo_diffs.py
   │     │  │  ├─ _realtransforms.py
   │     │  │  └─ __init__.py
   │     │  ├─ integrate
   │     │  │  ├─ dop.py
   │     │  │  ├─ lsoda.py
   │     │  │  ├─ odepack.py
   │     │  │  ├─ quadpack.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_banded_ode_solvers.py
   │     │  │  │  ├─ test_bvp.py
   │     │  │  │  ├─ test_cubature.py
   │     │  │  │  ├─ test_integrate.py
   │     │  │  │  ├─ test_odeint_jac.py
   │     │  │  │  ├─ test_quadpack.py
   │     │  │  │  ├─ test_quadrature.py
   │     │  │  │  ├─ test_tanhsinh.py
   │     │  │  │  ├─ test__quad_vec.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ vode.py
   │     │  │  ├─ _bvp.py
   │     │  │  ├─ _cubature.py
   │     │  │  ├─ _dop.cp311-win_amd64.dll.a
   │     │  │  ├─ _dop.cp311-win_amd64.pyd
   │     │  │  ├─ _ivp
   │     │  │  │  ├─ base.py
   │     │  │  │  ├─ bdf.py
   │     │  │  │  ├─ common.py
   │     │  │  │  ├─ dop853_coefficients.py
   │     │  │  │  ├─ ivp.py
   │     │  │  │  ├─ lsoda.py
   │     │  │  │  ├─ radau.py
   │     │  │  │  ├─ rk.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ test_ivp.py
   │     │  │  │  │  ├─ test_rk.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _lebedev.py
   │     │  │  ├─ _lsoda.cp311-win_amd64.dll.a
   │     │  │  ├─ _lsoda.cp311-win_amd64.pyd
   │     │  │  ├─ _ode.py
   │     │  │  ├─ _odepack.cp311-win_amd64.dll.a
   │     │  │  ├─ _odepack.cp311-win_amd64.pyd
   │     │  │  ├─ _odepack_py.py
   │     │  │  ├─ _quadpack.cp311-win_amd64.dll.a
   │     │  │  ├─ _quadpack.cp311-win_amd64.pyd
   │     │  │  ├─ _quadpack_py.py
   │     │  │  ├─ _quadrature.py
   │     │  │  ├─ _quad_vec.py
   │     │  │  ├─ _rules
   │     │  │  │  ├─ _base.py
   │     │  │  │  ├─ _gauss_kronrod.py
   │     │  │  │  ├─ _gauss_legendre.py
   │     │  │  │  ├─ _genz_malik.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _tanhsinh.py
   │     │  │  ├─ _test_multivariate.cp311-win_amd64.dll.a
   │     │  │  ├─ _test_multivariate.cp311-win_amd64.pyd
   │     │  │  ├─ _test_odeint_banded.cp311-win_amd64.dll.a
   │     │  │  ├─ _test_odeint_banded.cp311-win_amd64.pyd
   │     │  │  ├─ _vode.cp311-win_amd64.dll.a
   │     │  │  ├─ _vode.cp311-win_amd64.pyd
   │     │  │  └─ __init__.py
   │     │  ├─ interpolate
   │     │  │  ├─ dfitpack.py
   │     │  │  ├─ fitpack.py
   │     │  │  ├─ fitpack2.py
   │     │  │  ├─ interpnd.py
   │     │  │  ├─ interpolate.py
   │     │  │  ├─ ndgriddata.py
   │     │  │  ├─ polyint.py
   │     │  │  ├─ rbf.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ data
   │     │  │  │  │  ├─ bug-1310.npz
   │     │  │  │  │  ├─ estimate_gradients_hang.npy
   │     │  │  │  │  └─ gcvspl.npz
   │     │  │  │  ├─ test_bary_rational.py
   │     │  │  │  ├─ test_bsplines.py
   │     │  │  │  ├─ test_fitpack.py
   │     │  │  │  ├─ test_fitpack2.py
   │     │  │  │  ├─ test_gil.py
   │     │  │  │  ├─ test_interpnd.py
   │     │  │  │  ├─ test_interpolate.py
   │     │  │  │  ├─ test_ndgriddata.py
   │     │  │  │  ├─ test_pade.py
   │     │  │  │  ├─ test_polyint.py
   │     │  │  │  ├─ test_rbf.py
   │     │  │  │  ├─ test_rbfinterp.py
   │     │  │  │  ├─ test_rgi.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _bary_rational.py
   │     │  │  ├─ _bspl.cp311-win_amd64.dll.a
   │     │  │  ├─ _bspl.cp311-win_amd64.pyd
   │     │  │  ├─ _bsplines.py
   │     │  │  ├─ _cubic.py
   │     │  │  ├─ _dfitpack.cp311-win_amd64.dll.a
   │     │  │  ├─ _dfitpack.cp311-win_amd64.pyd
   │     │  │  ├─ _dierckx.cp311-win_amd64.dll.a
   │     │  │  ├─ _dierckx.cp311-win_amd64.pyd
   │     │  │  ├─ _fitpack.cp311-win_amd64.dll.a
   │     │  │  ├─ _fitpack.cp311-win_amd64.pyd
   │     │  │  ├─ _fitpack2.py
   │     │  │  ├─ _fitpack_impl.py
   │     │  │  ├─ _fitpack_py.py
   │     │  │  ├─ _fitpack_repro.py
   │     │  │  ├─ _interpnd.cp311-win_amd64.dll.a
   │     │  │  ├─ _interpnd.cp311-win_amd64.pyd
   │     │  │  ├─ _interpolate.py
   │     │  │  ├─ _ndbspline.py
   │     │  │  ├─ _ndgriddata.py
   │     │  │  ├─ _pade.py
   │     │  │  ├─ _polyint.py
   │     │  │  ├─ _ppoly.cp311-win_amd64.dll.a
   │     │  │  ├─ _ppoly.cp311-win_amd64.pyd
   │     │  │  ├─ _rbf.py
   │     │  │  ├─ _rbfinterp.py
   │     │  │  ├─ _rbfinterp_pythran.cp311-win_amd64.dll.a
   │     │  │  ├─ _rbfinterp_pythran.cp311-win_amd64.pyd
   │     │  │  ├─ _rgi.py
   │     │  │  ├─ _rgi_cython.cp311-win_amd64.dll.a
   │     │  │  ├─ _rgi_cython.cp311-win_amd64.pyd
   │     │  │  └─ __init__.py
   │     │  ├─ io
   │     │  │  ├─ arff
   │     │  │  │  ├─ arffread.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ data
   │     │  │  │  │  │  ├─ iris.arff
   │     │  │  │  │  │  ├─ missing.arff
   │     │  │  │  │  │  ├─ nodata.arff
   │     │  │  │  │  │  ├─ quoted_nominal.arff
   │     │  │  │  │  │  ├─ quoted_nominal_spaces.arff
   │     │  │  │  │  │  ├─ test1.arff
   │     │  │  │  │  │  ├─ test10.arff
   │     │  │  │  │  │  ├─ test11.arff
   │     │  │  │  │  │  ├─ test2.arff
   │     │  │  │  │  │  ├─ test3.arff
   │     │  │  │  │  │  ├─ test4.arff
   │     │  │  │  │  │  ├─ test5.arff
   │     │  │  │  │  │  ├─ test6.arff
   │     │  │  │  │  │  ├─ test7.arff
   │     │  │  │  │  │  ├─ test8.arff
   │     │  │  │  │  │  └─ test9.arff
   │     │  │  │  │  ├─ test_arffread.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ _arffread.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ harwell_boeing.py
   │     │  │  ├─ idl.py
   │     │  │  ├─ matlab
   │     │  │  │  ├─ byteordercodes.py
   │     │  │  │  ├─ mio.py
   │     │  │  │  ├─ mio4.py
   │     │  │  │  ├─ mio5.py
   │     │  │  │  ├─ mio5_params.py
   │     │  │  │  ├─ mio5_utils.py
   │     │  │  │  ├─ miobase.py
   │     │  │  │  ├─ mio_utils.py
   │     │  │  │  ├─ streams.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ data
   │     │  │  │  │  │  ├─ bad_miuint32.mat
   │     │  │  │  │  │  ├─ bad_miutf8_array_name.mat
   │     │  │  │  │  │  ├─ big_endian.mat
   │     │  │  │  │  │  ├─ broken_utf8.mat
   │     │  │  │  │  │  ├─ corrupted_zlib_checksum.mat
   │     │  │  │  │  │  ├─ corrupted_zlib_data.mat
   │     │  │  │  │  │  ├─ debigged_m4.mat
   │     │  │  │  │  │  ├─ japanese_utf8.txt
   │     │  │  │  │  │  ├─ little_endian.mat
   │     │  │  │  │  │  ├─ logical_sparse.mat
   │     │  │  │  │  │  ├─ malformed1.mat
   │     │  │  │  │  │  ├─ miuint32_for_miint32.mat
   │     │  │  │  │  │  ├─ miutf8_array_name.mat
   │     │  │  │  │  │  ├─ nasty_duplicate_fieldnames.mat
   │     │  │  │  │  │  ├─ one_by_zero_char.mat
   │     │  │  │  │  │  ├─ parabola.mat
   │     │  │  │  │  │  ├─ single_empty_string.mat
   │     │  │  │  │  │  ├─ some_functions.mat
   │     │  │  │  │  │  ├─ sqr.mat
   │     │  │  │  │  │  ├─ test3dmatrix_6.1_SOL2.mat
   │     │  │  │  │  │  ├─ test3dmatrix_6.5.1_GLNX86.mat
   │     │  │  │  │  │  ├─ test3dmatrix_7.1_GLNX86.mat
   │     │  │  │  │  │  ├─ test3dmatrix_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ testbool_8_WIN64.mat
   │     │  │  │  │  │  ├─ testcellnest_6.1_SOL2.mat
   │     │  │  │  │  │  ├─ testcellnest_6.5.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testcellnest_7.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testcellnest_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ testcell_6.1_SOL2.mat
   │     │  │  │  │  │  ├─ testcell_6.5.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testcell_7.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testcell_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ testcomplex_4.2c_SOL2.mat
   │     │  │  │  │  │  ├─ testcomplex_6.1_SOL2.mat
   │     │  │  │  │  │  ├─ testcomplex_6.5.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testcomplex_7.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testcomplex_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ testdouble_4.2c_SOL2.mat
   │     │  │  │  │  │  ├─ testdouble_6.1_SOL2.mat
   │     │  │  │  │  │  ├─ testdouble_6.5.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testdouble_7.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testdouble_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ testemptycell_5.3_SOL2.mat
   │     │  │  │  │  │  ├─ testemptycell_6.5.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testemptycell_7.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testemptycell_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ testfunc_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ testhdf5_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ testmatrix_4.2c_SOL2.mat
   │     │  │  │  │  │  ├─ testmatrix_6.1_SOL2.mat
   │     │  │  │  │  │  ├─ testmatrix_6.5.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testmatrix_7.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testmatrix_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ testminus_4.2c_SOL2.mat
   │     │  │  │  │  │  ├─ testminus_6.1_SOL2.mat
   │     │  │  │  │  │  ├─ testminus_6.5.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testminus_7.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testminus_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ testmulti_4.2c_SOL2.mat
   │     │  │  │  │  │  ├─ testmulti_7.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testmulti_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ testobject_6.1_SOL2.mat
   │     │  │  │  │  │  ├─ testobject_6.5.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testobject_7.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testobject_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ testonechar_4.2c_SOL2.mat
   │     │  │  │  │  │  ├─ testonechar_6.1_SOL2.mat
   │     │  │  │  │  │  ├─ testonechar_6.5.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testonechar_7.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testonechar_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ testscalarcell_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ testsimplecell.mat
   │     │  │  │  │  │  ├─ testsparsecomplex_4.2c_SOL2.mat
   │     │  │  │  │  │  ├─ testsparsecomplex_6.1_SOL2.mat
   │     │  │  │  │  │  ├─ testsparsecomplex_6.5.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testsparsecomplex_7.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testsparsecomplex_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ testsparsefloat_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ testsparse_4.2c_SOL2.mat
   │     │  │  │  │  │  ├─ testsparse_6.1_SOL2.mat
   │     │  │  │  │  │  ├─ testsparse_6.5.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testsparse_7.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testsparse_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ teststringarray_4.2c_SOL2.mat
   │     │  │  │  │  │  ├─ teststringarray_6.1_SOL2.mat
   │     │  │  │  │  │  ├─ teststringarray_6.5.1_GLNX86.mat
   │     │  │  │  │  │  ├─ teststringarray_7.1_GLNX86.mat
   │     │  │  │  │  │  ├─ teststringarray_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ teststring_4.2c_SOL2.mat
   │     │  │  │  │  │  ├─ teststring_6.1_SOL2.mat
   │     │  │  │  │  │  ├─ teststring_6.5.1_GLNX86.mat
   │     │  │  │  │  │  ├─ teststring_7.1_GLNX86.mat
   │     │  │  │  │  │  ├─ teststring_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ teststructarr_6.1_SOL2.mat
   │     │  │  │  │  │  ├─ teststructarr_6.5.1_GLNX86.mat
   │     │  │  │  │  │  ├─ teststructarr_7.1_GLNX86.mat
   │     │  │  │  │  │  ├─ teststructarr_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ teststructnest_6.1_SOL2.mat
   │     │  │  │  │  │  ├─ teststructnest_6.5.1_GLNX86.mat
   │     │  │  │  │  │  ├─ teststructnest_7.1_GLNX86.mat
   │     │  │  │  │  │  ├─ teststructnest_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ teststruct_6.1_SOL2.mat
   │     │  │  │  │  │  ├─ teststruct_6.5.1_GLNX86.mat
   │     │  │  │  │  │  ├─ teststruct_7.1_GLNX86.mat
   │     │  │  │  │  │  ├─ teststruct_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ testunicode_7.1_GLNX86.mat
   │     │  │  │  │  │  ├─ testunicode_7.4_GLNX86.mat
   │     │  │  │  │  │  ├─ testvec_4_GLNX86.mat
   │     │  │  │  │  │  ├─ test_empty_struct.mat
   │     │  │  │  │  │  ├─ test_mat4_le_floats.mat
   │     │  │  │  │  │  └─ test_skip_variable.mat
   │     │  │  │  │  ├─ test_byteordercodes.py
   │     │  │  │  │  ├─ test_mio.py
   │     │  │  │  │  ├─ test_mio5_utils.py
   │     │  │  │  │  ├─ test_miobase.py
   │     │  │  │  │  ├─ test_mio_funcs.py
   │     │  │  │  │  ├─ test_mio_utils.py
   │     │  │  │  │  ├─ test_pathological.py
   │     │  │  │  │  ├─ test_streams.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ _byteordercodes.py
   │     │  │  │  ├─ _mio.py
   │     │  │  │  ├─ _mio4.py
   │     │  │  │  ├─ _mio5.py
   │     │  │  │  ├─ _mio5_params.py
   │     │  │  │  ├─ _mio5_utils.cp311-win_amd64.dll.a
   │     │  │  │  ├─ _mio5_utils.cp311-win_amd64.pyd
   │     │  │  │  ├─ _miobase.py
   │     │  │  │  ├─ _mio_utils.cp311-win_amd64.dll.a
   │     │  │  │  ├─ _mio_utils.cp311-win_amd64.pyd
   │     │  │  │  ├─ _streams.cp311-win_amd64.dll.a
   │     │  │  │  ├─ _streams.cp311-win_amd64.pyd
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ mmio.py
   │     │  │  ├─ netcdf.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ data
   │     │  │  │  │  ├─ array_float32_1d.sav
   │     │  │  │  │  ├─ array_float32_2d.sav
   │     │  │  │  │  ├─ array_float32_3d.sav
   │     │  │  │  │  ├─ array_float32_4d.sav
   │     │  │  │  │  ├─ array_float32_5d.sav
   │     │  │  │  │  ├─ array_float32_6d.sav
   │     │  │  │  │  ├─ array_float32_7d.sav
   │     │  │  │  │  ├─ array_float32_8d.sav
   │     │  │  │  │  ├─ array_float32_pointer_1d.sav
   │     │  │  │  │  ├─ array_float32_pointer_2d.sav
   │     │  │  │  │  ├─ array_float32_pointer_3d.sav
   │     │  │  │  │  ├─ array_float32_pointer_4d.sav
   │     │  │  │  │  ├─ array_float32_pointer_5d.sav
   │     │  │  │  │  ├─ array_float32_pointer_6d.sav
   │     │  │  │  │  ├─ array_float32_pointer_7d.sav
   │     │  │  │  │  ├─ array_float32_pointer_8d.sav
   │     │  │  │  │  ├─ example_1.nc
   │     │  │  │  │  ├─ example_2.nc
   │     │  │  │  │  ├─ example_3_maskedvals.nc
   │     │  │  │  │  ├─ fortran-3x3d-2i.dat
   │     │  │  │  │  ├─ fortran-mixed.dat
   │     │  │  │  │  ├─ fortran-sf8-11x1x10.dat
   │     │  │  │  │  ├─ fortran-sf8-15x10x22.dat
   │     │  │  │  │  ├─ fortran-sf8-1x1x1.dat
   │     │  │  │  │  ├─ fortran-sf8-1x1x5.dat
   │     │  │  │  │  ├─ fortran-sf8-1x1x7.dat
   │     │  │  │  │  ├─ fortran-sf8-1x3x5.dat
   │     │  │  │  │  ├─ fortran-si4-11x1x10.dat
   │     │  │  │  │  ├─ fortran-si4-15x10x22.dat
   │     │  │  │  │  ├─ fortran-si4-1x1x1.dat
   │     │  │  │  │  ├─ fortran-si4-1x1x5.dat
   │     │  │  │  │  ├─ fortran-si4-1x1x7.dat
   │     │  │  │  │  ├─ fortran-si4-1x3x5.dat
   │     │  │  │  │  ├─ invalid_pointer.sav
   │     │  │  │  │  ├─ null_pointer.sav
   │     │  │  │  │  ├─ scalar_byte.sav
   │     │  │  │  │  ├─ scalar_byte_descr.sav
   │     │  │  │  │  ├─ scalar_complex32.sav
   │     │  │  │  │  ├─ scalar_complex64.sav
   │     │  │  │  │  ├─ scalar_float32.sav
   │     │  │  │  │  ├─ scalar_float64.sav
   │     │  │  │  │  ├─ scalar_heap_pointer.sav
   │     │  │  │  │  ├─ scalar_int16.sav
   │     │  │  │  │  ├─ scalar_int32.sav
   │     │  │  │  │  ├─ scalar_int64.sav
   │     │  │  │  │  ├─ scalar_string.sav
   │     │  │  │  │  ├─ scalar_uint16.sav
   │     │  │  │  │  ├─ scalar_uint32.sav
   │     │  │  │  │  ├─ scalar_uint64.sav
   │     │  │  │  │  ├─ struct_arrays.sav
   │     │  │  │  │  ├─ struct_arrays_byte_idl80.sav
   │     │  │  │  │  ├─ struct_arrays_replicated.sav
   │     │  │  │  │  ├─ struct_arrays_replicated_3d.sav
   │     │  │  │  │  ├─ struct_inherit.sav
   │     │  │  │  │  ├─ struct_pointers.sav
   │     │  │  │  │  ├─ struct_pointers_replicated.sav
   │     │  │  │  │  ├─ struct_pointers_replicated_3d.sav
   │     │  │  │  │  ├─ struct_pointer_arrays.sav
   │     │  │  │  │  ├─ struct_pointer_arrays_replicated.sav
   │     │  │  │  │  ├─ struct_pointer_arrays_replicated_3d.sav
   │     │  │  │  │  ├─ struct_scalars.sav
   │     │  │  │  │  ├─ struct_scalars_replicated.sav
   │     │  │  │  │  ├─ struct_scalars_replicated_3d.sav
   │     │  │  │  │  ├─ test-1234Hz-le-1ch-10S-20bit-extra.wav
   │     │  │  │  │  ├─ test-44100Hz-2ch-32bit-float-be.wav
   │     │  │  │  │  ├─ test-44100Hz-2ch-32bit-float-le.wav
   │     │  │  │  │  ├─ test-44100Hz-be-1ch-4bytes.wav
   │     │  │  │  │  ├─ test-44100Hz-le-1ch-4bytes-early-eof-no-data.wav
   │     │  │  │  │  ├─ test-44100Hz-le-1ch-4bytes-early-eof.wav
   │     │  │  │  │  ├─ test-44100Hz-le-1ch-4bytes-incomplete-chunk.wav
   │     │  │  │  │  ├─ test-44100Hz-le-1ch-4bytes-rf64.wav
   │     │  │  │  │  ├─ test-44100Hz-le-1ch-4bytes.wav
   │     │  │  │  │  ├─ test-48000Hz-2ch-64bit-float-le-wavex.wav
   │     │  │  │  │  ├─ test-8000Hz-be-3ch-5S-24bit.wav
   │     │  │  │  │  ├─ test-8000Hz-le-1ch-1byte-ulaw.wav
   │     │  │  │  │  ├─ test-8000Hz-le-2ch-1byteu.wav
   │     │  │  │  │  ├─ test-8000Hz-le-3ch-5S-24bit-inconsistent.wav
   │     │  │  │  │  ├─ test-8000Hz-le-3ch-5S-24bit-rf64.wav
   │     │  │  │  │  ├─ test-8000Hz-le-3ch-5S-24bit.wav
   │     │  │  │  │  ├─ test-8000Hz-le-3ch-5S-36bit.wav
   │     │  │  │  │  ├─ test-8000Hz-le-3ch-5S-45bit.wav
   │     │  │  │  │  ├─ test-8000Hz-le-3ch-5S-53bit.wav
   │     │  │  │  │  ├─ test-8000Hz-le-3ch-5S-64bit.wav
   │     │  │  │  │  ├─ test-8000Hz-le-4ch-9S-12bit.wav
   │     │  │  │  │  ├─ test-8000Hz-le-5ch-9S-5bit.wav
   │     │  │  │  │  ├─ Transparent Busy.ani
   │     │  │  │  │  └─ various_compressed.sav
   │     │  │  │  ├─ test_fortran.py
   │     │  │  │  ├─ test_idl.py
   │     │  │  │  ├─ test_mmio.py
   │     │  │  │  ├─ test_netcdf.py
   │     │  │  │  ├─ test_paths.py
   │     │  │  │  ├─ test_wavfile.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ wavfile.py
   │     │  │  ├─ _fast_matrix_market
   │     │  │  │  ├─ _fmm_core.cp311-win_amd64.dll.a
   │     │  │  │  ├─ _fmm_core.cp311-win_amd64.pyd
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _fortran.py
   │     │  │  ├─ _harwell_boeing
   │     │  │  │  ├─ hb.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ test_fortran_format.py
   │     │  │  │  │  ├─ test_hb.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ _fortran_format_parser.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _idl.py
   │     │  │  ├─ _mmio.py
   │     │  │  ├─ _netcdf.py
   │     │  │  ├─ _test_fortran.cp311-win_amd64.dll.a
   │     │  │  ├─ _test_fortran.cp311-win_amd64.pyd
   │     │  │  └─ __init__.py
   │     │  ├─ linalg
   │     │  │  ├─ basic.py
   │     │  │  ├─ blas.py
   │     │  │  ├─ cython_blas.cp311-win_amd64.dll.a
   │     │  │  ├─ cython_blas.cp311-win_amd64.pyd
   │     │  │  ├─ cython_blas.pxd
   │     │  │  ├─ cython_blas.pyx
   │     │  │  ├─ cython_lapack.cp311-win_amd64.dll.a
   │     │  │  ├─ cython_lapack.cp311-win_amd64.pyd
   │     │  │  ├─ cython_lapack.pxd
   │     │  │  ├─ cython_lapack.pyx
   │     │  │  ├─ decomp.py
   │     │  │  ├─ decomp_cholesky.py
   │     │  │  ├─ decomp_lu.py
   │     │  │  ├─ decomp_qr.py
   │     │  │  ├─ decomp_schur.py
   │     │  │  ├─ decomp_svd.py
   │     │  │  ├─ interpolative.py
   │     │  │  ├─ lapack.py
   │     │  │  ├─ matfuncs.py
   │     │  │  ├─ misc.py
   │     │  │  ├─ special_matrices.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ data
   │     │  │  │  │  ├─ carex_15_data.npz
   │     │  │  │  │  ├─ carex_18_data.npz
   │     │  │  │  │  ├─ carex_19_data.npz
   │     │  │  │  │  ├─ carex_20_data.npz
   │     │  │  │  │  ├─ carex_6_data.npz
   │     │  │  │  │  └─ gendare_20170120_data.npz
   │     │  │  │  ├─ test_basic.py
   │     │  │  │  ├─ test_blas.py
   │     │  │  │  ├─ test_cythonized_array_utils.py
   │     │  │  │  ├─ test_cython_blas.py
   │     │  │  │  ├─ test_cython_lapack.py
   │     │  │  │  ├─ test_decomp.py
   │     │  │  │  ├─ test_decomp_cholesky.py
   │     │  │  │  ├─ test_decomp_cossin.py
   │     │  │  │  ├─ test_decomp_ldl.py
   │     │  │  │  ├─ test_decomp_lu.py
   │     │  │  │  ├─ test_decomp_polar.py
   │     │  │  │  ├─ test_decomp_update.py
   │     │  │  │  ├─ test_extending.py
   │     │  │  │  ├─ test_fblas.py
   │     │  │  │  ├─ test_interpolative.py
   │     │  │  │  ├─ test_lapack.py
   │     │  │  │  ├─ test_matfuncs.py
   │     │  │  │  ├─ test_matmul_toeplitz.py
   │     │  │  │  ├─ test_procrustes.py
   │     │  │  │  ├─ test_sketches.py
   │     │  │  │  ├─ test_solvers.py
   │     │  │  │  ├─ test_solve_toeplitz.py
   │     │  │  │  ├─ test_special_matrices.py
   │     │  │  │  ├─ _cython_examples
   │     │  │  │  │  ├─ extending.pyx
   │     │  │  │  │  └─ meson.build
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _basic.py
   │     │  │  ├─ _blas_subroutines.h
   │     │  │  ├─ _cythonized_array_utils.cp311-win_amd64.dll.a
   │     │  │  ├─ _cythonized_array_utils.cp311-win_amd64.pyd
   │     │  │  ├─ _cythonized_array_utils.pxd
   │     │  │  ├─ _cythonized_array_utils.pyi
   │     │  │  ├─ _decomp.py
   │     │  │  ├─ _decomp_cholesky.py
   │     │  │  ├─ _decomp_cossin.py
   │     │  │  ├─ _decomp_interpolative.cp311-win_amd64.dll.a
   │     │  │  ├─ _decomp_interpolative.cp311-win_amd64.pyd
   │     │  │  ├─ _decomp_ldl.py
   │     │  │  ├─ _decomp_lu.py
   │     │  │  ├─ _decomp_lu_cython.cp311-win_amd64.dll.a
   │     │  │  ├─ _decomp_lu_cython.cp311-win_amd64.pyd
   │     │  │  ├─ _decomp_lu_cython.pyi
   │     │  │  ├─ _decomp_polar.py
   │     │  │  ├─ _decomp_qr.py
   │     │  │  ├─ _decomp_qz.py
   │     │  │  ├─ _decomp_schur.py
   │     │  │  ├─ _decomp_svd.py
   │     │  │  ├─ _decomp_update.cp311-win_amd64.dll.a
   │     │  │  ├─ _decomp_update.cp311-win_amd64.pyd
   │     │  │  ├─ _expm_frechet.py
   │     │  │  ├─ _fblas.cp311-win_amd64.dll.a
   │     │  │  ├─ _fblas.cp311-win_amd64.pyd
   │     │  │  ├─ _flapack.cp311-win_amd64.dll.a
   │     │  │  ├─ _flapack.cp311-win_amd64.pyd
   │     │  │  ├─ _lapack_subroutines.h
   │     │  │  ├─ _linalg_pythran.cp311-win_amd64.dll.a
   │     │  │  ├─ _linalg_pythran.cp311-win_amd64.pyd
   │     │  │  ├─ _matfuncs.py
   │     │  │  ├─ _matfuncs_expm.cp311-win_amd64.dll.a
   │     │  │  ├─ _matfuncs_expm.cp311-win_amd64.pyd
   │     │  │  ├─ _matfuncs_expm.pyi
   │     │  │  ├─ _matfuncs_inv_ssq.py
   │     │  │  ├─ _matfuncs_sqrtm.py
   │     │  │  ├─ _matfuncs_sqrtm_triu.cp311-win_amd64.dll.a
   │     │  │  ├─ _matfuncs_sqrtm_triu.cp311-win_amd64.pyd
   │     │  │  ├─ _misc.py
   │     │  │  ├─ _procrustes.py
   │     │  │  ├─ _sketches.py
   │     │  │  ├─ _solvers.py
   │     │  │  ├─ _solve_toeplitz.cp311-win_amd64.dll.a
   │     │  │  ├─ _solve_toeplitz.cp311-win_amd64.pyd
   │     │  │  ├─ _special_matrices.py
   │     │  │  ├─ _testutils.py
   │     │  │  ├─ __init__.pxd
   │     │  │  └─ __init__.py
   │     │  ├─ misc
   │     │  │  ├─ common.py
   │     │  │  ├─ doccer.py
   │     │  │  └─ __init__.py
   │     │  ├─ ndimage
   │     │  │  ├─ filters.py
   │     │  │  ├─ fourier.py
   │     │  │  ├─ interpolation.py
   │     │  │  ├─ measurements.py
   │     │  │  ├─ morphology.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ data
   │     │  │  │  │  ├─ label_inputs.txt
   │     │  │  │  │  ├─ label_results.txt
   │     │  │  │  │  └─ label_strels.txt
   │     │  │  │  ├─ dots.png
   │     │  │  │  ├─ test_c_api.py
   │     │  │  │  ├─ test_datatypes.py
   │     │  │  │  ├─ test_filters.py
   │     │  │  │  ├─ test_fourier.py
   │     │  │  │  ├─ test_interpolation.py
   │     │  │  │  ├─ test_measurements.py
   │     │  │  │  ├─ test_morphology.py
   │     │  │  │  ├─ test_ni_support.py
   │     │  │  │  ├─ test_splines.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _ctest.cp311-win_amd64.dll.a
   │     │  │  ├─ _ctest.cp311-win_amd64.pyd
   │     │  │  ├─ _cytest.cp311-win_amd64.dll.a
   │     │  │  ├─ _cytest.cp311-win_amd64.pyd
   │     │  │  ├─ _delegators.py
   │     │  │  ├─ _filters.py
   │     │  │  ├─ _fourier.py
   │     │  │  ├─ _interpolation.py
   │     │  │  ├─ _measurements.py
   │     │  │  ├─ _morphology.py
   │     │  │  ├─ _ndimage_api.py
   │     │  │  ├─ _nd_image.cp311-win_amd64.dll.a
   │     │  │  ├─ _nd_image.cp311-win_amd64.pyd
   │     │  │  ├─ _ni_docstrings.py
   │     │  │  ├─ _ni_label.cp311-win_amd64.dll.a
   │     │  │  ├─ _ni_label.cp311-win_amd64.pyd
   │     │  │  ├─ _ni_support.py
   │     │  │  ├─ _rank_filter_1d.cp311-win_amd64.dll.a
   │     │  │  ├─ _rank_filter_1d.cp311-win_amd64.pyd
   │     │  │  ├─ _support_alternative_backends.py
   │     │  │  └─ __init__.py
   │     │  ├─ odr
   │     │  │  ├─ models.py
   │     │  │  ├─ odrpack.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_odr.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _add_newdocs.py
   │     │  │  ├─ _models.py
   │     │  │  ├─ _odrpack.py
   │     │  │  ├─ __init__.py
   │     │  │  ├─ __odrpack.cp311-win_amd64.dll.a
   │     │  │  └─ __odrpack.cp311-win_amd64.pyd
   │     │  ├─ optimize
   │     │  │  ├─ cobyla.py
   │     │  │  ├─ cython_optimize
   │     │  │  │  ├─ c_zeros.pxd
   │     │  │  │  ├─ _zeros.cp311-win_amd64.dll.a
   │     │  │  │  ├─ _zeros.cp311-win_amd64.pyd
   │     │  │  │  ├─ _zeros.pxd
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ cython_optimize.pxd
   │     │  │  ├─ elementwise.py
   │     │  │  ├─ lbfgsb.py
   │     │  │  ├─ linesearch.py
   │     │  │  ├─ minpack.py
   │     │  │  ├─ minpack2.py
   │     │  │  ├─ moduleTNC.py
   │     │  │  ├─ nonlin.py
   │     │  │  ├─ optimize.py
   │     │  │  ├─ slsqp.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_bracket.py
   │     │  │  │  ├─ test_chandrupatla.py
   │     │  │  │  ├─ test_cobyla.py
   │     │  │  │  ├─ test_cobyqa.py
   │     │  │  │  ├─ test_constraints.py
   │     │  │  │  ├─ test_constraint_conversion.py
   │     │  │  │  ├─ test_cython_optimize.py
   │     │  │  │  ├─ test_differentiable_functions.py
   │     │  │  │  ├─ test_direct.py
   │     │  │  │  ├─ test_extending.py
   │     │  │  │  ├─ test_hessian_update_strategy.py
   │     │  │  │  ├─ test_isotonic_regression.py
   │     │  │  │  ├─ test_lbfgsb_hessinv.py
   │     │  │  │  ├─ test_lbfgsb_setulb.py
   │     │  │  │  ├─ test_least_squares.py
   │     │  │  │  ├─ test_linear_assignment.py
   │     │  │  │  ├─ test_linesearch.py
   │     │  │  │  ├─ test_linprog.py
   │     │  │  │  ├─ test_lsq_common.py
   │     │  │  │  ├─ test_lsq_linear.py
   │     │  │  │  ├─ test_milp.py
   │     │  │  │  ├─ test_minimize_constrained.py
   │     │  │  │  ├─ test_minpack.py
   │     │  │  │  ├─ test_nnls.py
   │     │  │  │  ├─ test_nonlin.py
   │     │  │  │  ├─ test_optimize.py
   │     │  │  │  ├─ test_quadratic_assignment.py
   │     │  │  │  ├─ test_regression.py
   │     │  │  │  ├─ test_slsqp.py
   │     │  │  │  ├─ test_tnc.py
   │     │  │  │  ├─ test_trustregion.py
   │     │  │  │  ├─ test_trustregion_exact.py
   │     │  │  │  ├─ test_trustregion_krylov.py
   │     │  │  │  ├─ test_zeros.py
   │     │  │  │  ├─ test__basinhopping.py
   │     │  │  │  ├─ test__differential_evolution.py
   │     │  │  │  ├─ test__dual_annealing.py
   │     │  │  │  ├─ test__linprog_clean_inputs.py
   │     │  │  │  ├─ test__numdiff.py
   │     │  │  │  ├─ test__remove_redundancy.py
   │     │  │  │  ├─ test__root.py
   │     │  │  │  ├─ test__shgo.py
   │     │  │  │  ├─ test__spectral.py
   │     │  │  │  ├─ _cython_examples
   │     │  │  │  │  ├─ extending.pyx
   │     │  │  │  │  └─ meson.build
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ tnc.py
   │     │  │  ├─ zeros.py
   │     │  │  ├─ _basinhopping.py
   │     │  │  ├─ _bglu_dense.cp311-win_amd64.dll.a
   │     │  │  ├─ _bglu_dense.cp311-win_amd64.pyd
   │     │  │  ├─ _bracket.py
   │     │  │  ├─ _chandrupatla.py
   │     │  │  ├─ _cobyla.cp311-win_amd64.dll.a
   │     │  │  ├─ _cobyla.cp311-win_amd64.pyd
   │     │  │  ├─ _cobyla_py.py
   │     │  │  ├─ _cobyqa_py.py
   │     │  │  ├─ _constraints.py
   │     │  │  ├─ _cython_nnls.cp311-win_amd64.dll.a
   │     │  │  ├─ _cython_nnls.cp311-win_amd64.pyd
   │     │  │  ├─ _dcsrch.py
   │     │  │  ├─ _differentiable_functions.py
   │     │  │  ├─ _differentialevolution.py
   │     │  │  ├─ _direct.cp311-win_amd64.dll.a
   │     │  │  ├─ _direct.cp311-win_amd64.pyd
   │     │  │  ├─ _direct_py.py
   │     │  │  ├─ _dual_annealing.py
   │     │  │  ├─ _elementwise.py
   │     │  │  ├─ _group_columns.cp311-win_amd64.dll.a
   │     │  │  ├─ _group_columns.cp311-win_amd64.pyd
   │     │  │  ├─ _hessian_update_strategy.py
   │     │  │  ├─ _highspy
   │     │  │  │  ├─ _core.cp311-win_amd64.dll.a
   │     │  │  │  ├─ _core.cp311-win_amd64.pyd
   │     │  │  │  ├─ _highs_options.cp311-win_amd64.dll.a
   │     │  │  │  ├─ _highs_options.cp311-win_amd64.pyd
   │     │  │  │  ├─ _highs_wrapper.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _isotonic.py
   │     │  │  ├─ _lbfgsb.cp311-win_amd64.dll.a
   │     │  │  ├─ _lbfgsb.cp311-win_amd64.pyd
   │     │  │  ├─ _lbfgsb_py.py
   │     │  │  ├─ _linesearch.py
   │     │  │  ├─ _linprog.py
   │     │  │  ├─ _linprog_doc.py
   │     │  │  ├─ _linprog_highs.py
   │     │  │  ├─ _linprog_ip.py
   │     │  │  ├─ _linprog_rs.py
   │     │  │  ├─ _linprog_simplex.py
   │     │  │  ├─ _linprog_util.py
   │     │  │  ├─ _lsap.cp311-win_amd64.dll.a
   │     │  │  ├─ _lsap.cp311-win_amd64.pyd
   │     │  │  ├─ _lsq
   │     │  │  │  ├─ bvls.py
   │     │  │  │  ├─ common.py
   │     │  │  │  ├─ dogbox.py
   │     │  │  │  ├─ givens_elimination.cp311-win_amd64.dll.a
   │     │  │  │  ├─ givens_elimination.cp311-win_amd64.pyd
   │     │  │  │  ├─ least_squares.py
   │     │  │  │  ├─ lsq_linear.py
   │     │  │  │  ├─ trf.py
   │     │  │  │  ├─ trf_linear.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _milp.py
   │     │  │  ├─ _minimize.py
   │     │  │  ├─ _minpack.cp311-win_amd64.dll.a
   │     │  │  ├─ _minpack.cp311-win_amd64.pyd
   │     │  │  ├─ _minpack_py.py
   │     │  │  ├─ _moduleTNC.cp311-win_amd64.dll.a
   │     │  │  ├─ _moduleTNC.cp311-win_amd64.pyd
   │     │  │  ├─ _nnls.py
   │     │  │  ├─ _nonlin.py
   │     │  │  ├─ _numdiff.py
   │     │  │  ├─ _optimize.py
   │     │  │  ├─ _pava_pybind.cp311-win_amd64.dll.a
   │     │  │  ├─ _pava_pybind.cp311-win_amd64.pyd
   │     │  │  ├─ _qap.py
   │     │  │  ├─ _remove_redundancy.py
   │     │  │  ├─ _root.py
   │     │  │  ├─ _root_scalar.py
   │     │  │  ├─ _shgo.py
   │     │  │  ├─ _shgo_lib
   │     │  │  │  ├─ _complex.py
   │     │  │  │  ├─ _vertex.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _slsqp.cp311-win_amd64.dll.a
   │     │  │  ├─ _slsqp.cp311-win_amd64.pyd
   │     │  │  ├─ _slsqp_py.py
   │     │  │  ├─ _spectral.py
   │     │  │  ├─ _tnc.py
   │     │  │  ├─ _trlib
   │     │  │  │  ├─ _trlib.cp311-win_amd64.dll.a
   │     │  │  │  ├─ _trlib.cp311-win_amd64.pyd
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _trustregion.py
   │     │  │  ├─ _trustregion_constr
   │     │  │  │  ├─ canonical_constraint.py
   │     │  │  │  ├─ equality_constrained_sqp.py
   │     │  │  │  ├─ minimize_trustregion_constr.py
   │     │  │  │  ├─ projections.py
   │     │  │  │  ├─ qp_subproblem.py
   │     │  │  │  ├─ report.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ test_canonical_constraint.py
   │     │  │  │  │  ├─ test_nested_minimize.py
   │     │  │  │  │  ├─ test_projections.py
   │     │  │  │  │  ├─ test_qp_subproblem.py
   │     │  │  │  │  ├─ test_report.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ tr_interior_point.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _trustregion_dogleg.py
   │     │  │  ├─ _trustregion_exact.py
   │     │  │  ├─ _trustregion_krylov.py
   │     │  │  ├─ _trustregion_ncg.py
   │     │  │  ├─ _tstutils.py
   │     │  │  ├─ _zeros.cp311-win_amd64.dll.a
   │     │  │  ├─ _zeros.cp311-win_amd64.pyd
   │     │  │  ├─ _zeros_py.py
   │     │  │  ├─ __init__.pxd
   │     │  │  └─ __init__.py
   │     │  ├─ signal
   │     │  │  ├─ bsplines.py
   │     │  │  ├─ filter_design.py
   │     │  │  ├─ fir_filter_design.py
   │     │  │  ├─ ltisys.py
   │     │  │  ├─ lti_conversion.py
   │     │  │  ├─ signaltools.py
   │     │  │  ├─ spectral.py
   │     │  │  ├─ spline.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ mpsig.py
   │     │  │  │  ├─ test_array_tools.py
   │     │  │  │  ├─ test_bsplines.py
   │     │  │  │  ├─ test_cont2discrete.py
   │     │  │  │  ├─ test_czt.py
   │     │  │  │  ├─ test_dltisys.py
   │     │  │  │  ├─ test_filter_design.py
   │     │  │  │  ├─ test_fir_filter_design.py
   │     │  │  │  ├─ test_ltisys.py
   │     │  │  │  ├─ test_max_len_seq.py
   │     │  │  │  ├─ test_peak_finding.py
   │     │  │  │  ├─ test_result_type.py
   │     │  │  │  ├─ test_savitzky_golay.py
   │     │  │  │  ├─ test_short_time_fft.py
   │     │  │  │  ├─ test_signaltools.py
   │     │  │  │  ├─ test_spectral.py
   │     │  │  │  ├─ test_splines.py
   │     │  │  │  ├─ test_upfirdn.py
   │     │  │  │  ├─ test_waveforms.py
   │     │  │  │  ├─ test_wavelets.py
   │     │  │  │  ├─ test_windows.py
   │     │  │  │  ├─ _scipy_spectral_test_shim.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ waveforms.py
   │     │  │  ├─ wavelets.py
   │     │  │  ├─ windows
   │     │  │  │  ├─ windows.py
   │     │  │  │  ├─ _windows.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _arraytools.py
   │     │  │  ├─ _czt.py
   │     │  │  ├─ _filter_design.py
   │     │  │  ├─ _fir_filter_design.py
   │     │  │  ├─ _ltisys.py
   │     │  │  ├─ _lti_conversion.py
   │     │  │  ├─ _max_len_seq.py
   │     │  │  ├─ _max_len_seq_inner.cp311-win_amd64.dll.a
   │     │  │  ├─ _max_len_seq_inner.cp311-win_amd64.pyd
   │     │  │  ├─ _peak_finding.py
   │     │  │  ├─ _peak_finding_utils.cp311-win_amd64.dll.a
   │     │  │  ├─ _peak_finding_utils.cp311-win_amd64.pyd
   │     │  │  ├─ _savitzky_golay.py
   │     │  │  ├─ _short_time_fft.py
   │     │  │  ├─ _signaltools.py
   │     │  │  ├─ _sigtools.cp311-win_amd64.dll.a
   │     │  │  ├─ _sigtools.cp311-win_amd64.pyd
   │     │  │  ├─ _sosfilt.cp311-win_amd64.dll.a
   │     │  │  ├─ _sosfilt.cp311-win_amd64.pyd
   │     │  │  ├─ _spectral_py.py
   │     │  │  ├─ _spline.cp311-win_amd64.dll.a
   │     │  │  ├─ _spline.cp311-win_amd64.pyd
   │     │  │  ├─ _spline.pyi
   │     │  │  ├─ _spline_filters.py
   │     │  │  ├─ _upfirdn.py
   │     │  │  ├─ _upfirdn_apply.cp311-win_amd64.dll.a
   │     │  │  ├─ _upfirdn_apply.cp311-win_amd64.pyd
   │     │  │  ├─ _waveforms.py
   │     │  │  ├─ _wavelets.py
   │     │  │  └─ __init__.py
   │     │  ├─ sparse
   │     │  │  ├─ base.py
   │     │  │  ├─ bsr.py
   │     │  │  ├─ compressed.py
   │     │  │  ├─ construct.py
   │     │  │  ├─ coo.py
   │     │  │  ├─ csc.py
   │     │  │  ├─ csgraph
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ test_connected_components.py
   │     │  │  │  │  ├─ test_conversions.py
   │     │  │  │  │  ├─ test_flow.py
   │     │  │  │  │  ├─ test_graph_laplacian.py
   │     │  │  │  │  ├─ test_matching.py
   │     │  │  │  │  ├─ test_pydata_sparse.py
   │     │  │  │  │  ├─ test_reordering.py
   │     │  │  │  │  ├─ test_shortest_path.py
   │     │  │  │  │  ├─ test_spanning_tree.py
   │     │  │  │  │  ├─ test_traversal.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ _flow.cp311-win_amd64.dll.a
   │     │  │  │  ├─ _flow.cp311-win_amd64.pyd
   │     │  │  │  ├─ _laplacian.py
   │     │  │  │  ├─ _matching.cp311-win_amd64.dll.a
   │     │  │  │  ├─ _matching.cp311-win_amd64.pyd
   │     │  │  │  ├─ _min_spanning_tree.cp311-win_amd64.dll.a
   │     │  │  │  ├─ _min_spanning_tree.cp311-win_amd64.pyd
   │     │  │  │  ├─ _reordering.cp311-win_amd64.dll.a
   │     │  │  │  ├─ _reordering.cp311-win_amd64.pyd
   │     │  │  │  ├─ _shortest_path.cp311-win_amd64.dll.a
   │     │  │  │  ├─ _shortest_path.cp311-win_amd64.pyd
   │     │  │  │  ├─ _tools.cp311-win_amd64.dll.a
   │     │  │  │  ├─ _tools.cp311-win_amd64.pyd
   │     │  │  │  ├─ _traversal.cp311-win_amd64.dll.a
   │     │  │  │  ├─ _traversal.cp311-win_amd64.pyd
   │     │  │  │  ├─ _validation.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ csr.py
   │     │  │  ├─ data.py
   │     │  │  ├─ dia.py
   │     │  │  ├─ dok.py
   │     │  │  ├─ extract.py
   │     │  │  ├─ lil.py
   │     │  │  ├─ linalg
   │     │  │  │  ├─ dsolve.py
   │     │  │  │  ├─ eigen.py
   │     │  │  │  ├─ interface.py
   │     │  │  │  ├─ isolve.py
   │     │  │  │  ├─ matfuncs.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ propack_test_data.npz
   │     │  │  │  │  ├─ test_expm_multiply.py
   │     │  │  │  │  ├─ test_interface.py
   │     │  │  │  │  ├─ test_matfuncs.py
   │     │  │  │  │  ├─ test_norm.py
   │     │  │  │  │  ├─ test_onenormest.py
   │     │  │  │  │  ├─ test_propack.py
   │     │  │  │  │  ├─ test_pydata_sparse.py
   │     │  │  │  │  ├─ test_special_sparse_arrays.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ _dsolve
   │     │  │  │  │  ├─ linsolve.py
   │     │  │  │  │  ├─ tests
   │     │  │  │  │  │  ├─ test_linsolve.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ _add_newdocs.py
   │     │  │  │  │  ├─ _superlu.cp311-win_amd64.dll.a
   │     │  │  │  │  ├─ _superlu.cp311-win_amd64.pyd
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ _eigen
   │     │  │  │  │  ├─ arpack
   │     │  │  │  │  │  ├─ arpack.py
   │     │  │  │  │  │  ├─ COPYING
   │     │  │  │  │  │  ├─ tests
   │     │  │  │  │  │  │  ├─ test_arpack.py
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  ├─ _arpack.cp311-win_amd64.dll.a
   │     │  │  │  │  │  ├─ _arpack.cp311-win_amd64.pyd
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ lobpcg
   │     │  │  │  │  │  ├─ lobpcg.py
   │     │  │  │  │  │  ├─ tests
   │     │  │  │  │  │  │  ├─ test_lobpcg.py
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ tests
   │     │  │  │  │  │  ├─ test_svds.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ _svds.py
   │     │  │  │  │  ├─ _svds_doc.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ _expm_multiply.py
   │     │  │  │  ├─ _interface.py
   │     │  │  │  ├─ _isolve
   │     │  │  │  │  ├─ iterative.py
   │     │  │  │  │  ├─ lgmres.py
   │     │  │  │  │  ├─ lsmr.py
   │     │  │  │  │  ├─ lsqr.py
   │     │  │  │  │  ├─ minres.py
   │     │  │  │  │  ├─ tests
   │     │  │  │  │  │  ├─ test_gcrotmk.py
   │     │  │  │  │  │  ├─ test_iterative.py
   │     │  │  │  │  │  ├─ test_lgmres.py
   │     │  │  │  │  │  ├─ test_lsmr.py
   │     │  │  │  │  │  ├─ test_lsqr.py
   │     │  │  │  │  │  ├─ test_minres.py
   │     │  │  │  │  │  ├─ test_utils.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ tfqmr.py
   │     │  │  │  │  ├─ utils.py
   │     │  │  │  │  ├─ _gcrotmk.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ _matfuncs.py
   │     │  │  │  ├─ _norm.py
   │     │  │  │  ├─ _onenormest.py
   │     │  │  │  ├─ _propack
   │     │  │  │  │  ├─ _cpropack.cp311-win_amd64.dll.a
   │     │  │  │  │  ├─ _cpropack.cp311-win_amd64.pyd
   │     │  │  │  │  ├─ _dpropack.cp311-win_amd64.dll.a
   │     │  │  │  │  ├─ _dpropack.cp311-win_amd64.pyd
   │     │  │  │  │  ├─ _spropack.cp311-win_amd64.dll.a
   │     │  │  │  │  ├─ _spropack.cp311-win_amd64.pyd
   │     │  │  │  │  ├─ _zpropack.cp311-win_amd64.dll.a
   │     │  │  │  │  └─ _zpropack.cp311-win_amd64.pyd
   │     │  │  │  ├─ _special_sparse_arrays.py
   │     │  │  │  ├─ _svdp.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ sparsetools.py
   │     │  │  ├─ spfuncs.py
   │     │  │  ├─ sputils.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ data
   │     │  │  │  │  ├─ csc_py2.npz
   │     │  │  │  │  └─ csc_py3.npz
   │     │  │  │  ├─ test_arithmetic1d.py
   │     │  │  │  ├─ test_array_api.py
   │     │  │  │  ├─ test_base.py
   │     │  │  │  ├─ test_common1d.py
   │     │  │  │  ├─ test_construct.py
   │     │  │  │  ├─ test_coo.py
   │     │  │  │  ├─ test_csc.py
   │     │  │  │  ├─ test_csr.py
   │     │  │  │  ├─ test_dok.py
   │     │  │  │  ├─ test_extract.py
   │     │  │  │  ├─ test_indexing1d.py
   │     │  │  │  ├─ test_matrix_io.py
   │     │  │  │  ├─ test_minmax1d.py
   │     │  │  │  ├─ test_sparsetools.py
   │     │  │  │  ├─ test_spfuncs.py
   │     │  │  │  ├─ test_sputils.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _base.py
   │     │  │  ├─ _bsr.py
   │     │  │  ├─ _compressed.py
   │     │  │  ├─ _construct.py
   │     │  │  ├─ _coo.py
   │     │  │  ├─ _csc.py
   │     │  │  ├─ _csparsetools.cp311-win_amd64.dll.a
   │     │  │  ├─ _csparsetools.cp311-win_amd64.pyd
   │     │  │  ├─ _csr.py
   │     │  │  ├─ _data.py
   │     │  │  ├─ _dia.py
   │     │  │  ├─ _dok.py
   │     │  │  ├─ _extract.py
   │     │  │  ├─ _index.py
   │     │  │  ├─ _lil.py
   │     │  │  ├─ _matrix.py
   │     │  │  ├─ _matrix_io.py
   │     │  │  ├─ _sparsetools.cp311-win_amd64.dll.a
   │     │  │  ├─ _sparsetools.cp311-win_amd64.pyd
   │     │  │  ├─ _spfuncs.py
   │     │  │  ├─ _sputils.py
   │     │  │  └─ __init__.py
   │     │  ├─ spatial
   │     │  │  ├─ ckdtree.py
   │     │  │  ├─ distance.py
   │     │  │  ├─ distance.pyi
   │     │  │  ├─ kdtree.py
   │     │  │  ├─ qhull.py
   │     │  │  ├─ qhull_src
   │     │  │  │  └─ COPYING.txt
   │     │  │  ├─ tests
   │     │  │  │  ├─ data
   │     │  │  │  │  ├─ cdist-X1.txt
   │     │  │  │  │  ├─ cdist-X2.txt
   │     │  │  │  │  ├─ degenerate_pointset.npz
   │     │  │  │  │  ├─ iris.txt
   │     │  │  │  │  ├─ pdist-boolean-inp.txt
   │     │  │  │  │  ├─ pdist-chebyshev-ml-iris.txt
   │     │  │  │  │  ├─ pdist-chebyshev-ml.txt
   │     │  │  │  │  ├─ pdist-cityblock-ml-iris.txt
   │     │  │  │  │  ├─ pdist-cityblock-ml.txt
   │     │  │  │  │  ├─ pdist-correlation-ml-iris.txt
   │     │  │  │  │  ├─ pdist-correlation-ml.txt
   │     │  │  │  │  ├─ pdist-cosine-ml-iris.txt
   │     │  │  │  │  ├─ pdist-cosine-ml.txt
   │     │  │  │  │  ├─ pdist-double-inp.txt
   │     │  │  │  │  ├─ pdist-euclidean-ml-iris.txt
   │     │  │  │  │  ├─ pdist-euclidean-ml.txt
   │     │  │  │  │  ├─ pdist-hamming-ml.txt
   │     │  │  │  │  ├─ pdist-jaccard-ml.txt
   │     │  │  │  │  ├─ pdist-jensenshannon-ml-iris.txt
   │     │  │  │  │  ├─ pdist-jensenshannon-ml.txt
   │     │  │  │  │  ├─ pdist-minkowski-3.2-ml-iris.txt
   │     │  │  │  │  ├─ pdist-minkowski-3.2-ml.txt
   │     │  │  │  │  ├─ pdist-minkowski-5.8-ml-iris.txt
   │     │  │  │  │  ├─ pdist-seuclidean-ml-iris.txt
   │     │  │  │  │  ├─ pdist-seuclidean-ml.txt
   │     │  │  │  │  ├─ pdist-spearman-ml.txt
   │     │  │  │  │  ├─ random-bool-data.txt
   │     │  │  │  │  ├─ random-double-data.txt
   │     │  │  │  │  ├─ random-int-data.txt
   │     │  │  │  │  ├─ random-uint-data.txt
   │     │  │  │  │  └─ selfdual-4d-polytope.txt
   │     │  │  │  ├─ test_distance.py
   │     │  │  │  ├─ test_hausdorff.py
   │     │  │  │  ├─ test_kdtree.py
   │     │  │  │  ├─ test_qhull.py
   │     │  │  │  ├─ test_slerp.py
   │     │  │  │  ├─ test_spherical_voronoi.py
   │     │  │  │  ├─ test__plotutils.py
   │     │  │  │  ├─ test__procrustes.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ transform
   │     │  │  │  ├─ rotation.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ test_rotation.py
   │     │  │  │  │  ├─ test_rotation_groups.py
   │     │  │  │  │  ├─ test_rotation_spline.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ _rotation.cp311-win_amd64.dll.a
   │     │  │  │  ├─ _rotation.cp311-win_amd64.pyd
   │     │  │  │  ├─ _rotation_groups.py
   │     │  │  │  ├─ _rotation_spline.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _ckdtree.cp311-win_amd64.dll.a
   │     │  │  ├─ _ckdtree.cp311-win_amd64.pyd
   │     │  │  ├─ _distance_pybind.cp311-win_amd64.dll.a
   │     │  │  ├─ _distance_pybind.cp311-win_amd64.pyd
   │     │  │  ├─ _distance_wrap.cp311-win_amd64.dll.a
   │     │  │  ├─ _distance_wrap.cp311-win_amd64.pyd
   │     │  │  ├─ _geometric_slerp.py
   │     │  │  ├─ _hausdorff.cp311-win_amd64.dll.a
   │     │  │  ├─ _hausdorff.cp311-win_amd64.pyd
   │     │  │  ├─ _kdtree.py
   │     │  │  ├─ _plotutils.py
   │     │  │  ├─ _procrustes.py
   │     │  │  ├─ _qhull.cp311-win_amd64.dll.a
   │     │  │  ├─ _qhull.cp311-win_amd64.pyd
   │     │  │  ├─ _qhull.pyi
   │     │  │  ├─ _spherical_voronoi.py
   │     │  │  ├─ _voronoi.cp311-win_amd64.dll.a
   │     │  │  ├─ _voronoi.cp311-win_amd64.pyd
   │     │  │  ├─ _voronoi.pyi
   │     │  │  └─ __init__.py
   │     │  ├─ special
   │     │  │  ├─ add_newdocs.py
   │     │  │  ├─ basic.py
   │     │  │  ├─ cython_special.cp311-win_amd64.dll.a
   │     │  │  ├─ cython_special.cp311-win_amd64.pyd
   │     │  │  ├─ cython_special.pxd
   │     │  │  ├─ cython_special.pyi
   │     │  │  ├─ libsf_error_state.dll
   │     │  │  ├─ libsf_error_state.dll.a
   │     │  │  ├─ orthogonal.py
   │     │  │  ├─ sf_error.py
   │     │  │  ├─ specfun.py
   │     │  │  ├─ spfun_stats.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ data
   │     │  │  │  │  ├─ boost.npz
   │     │  │  │  │  ├─ gsl.npz
   │     │  │  │  │  ├─ local.npz
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_basic.py
   │     │  │  │  ├─ test_bdtr.py
   │     │  │  │  ├─ test_boost_ufuncs.py
   │     │  │  │  ├─ test_boxcox.py
   │     │  │  │  ├─ test_cdflib.py
   │     │  │  │  ├─ test_cdft_asymptotic.py
   │     │  │  │  ├─ test_cephes_intp_cast.py
   │     │  │  │  ├─ test_cosine_distr.py
   │     │  │  │  ├─ test_cython_special.py
   │     │  │  │  ├─ test_data.py
   │     │  │  │  ├─ test_dd.py
   │     │  │  │  ├─ test_digamma.py
   │     │  │  │  ├─ test_ellip_harm.py
   │     │  │  │  ├─ test_erfinv.py
   │     │  │  │  ├─ test_exponential_integrals.py
   │     │  │  │  ├─ test_extending.py
   │     │  │  │  ├─ test_faddeeva.py
   │     │  │  │  ├─ test_gamma.py
   │     │  │  │  ├─ test_gammainc.py
   │     │  │  │  ├─ test_hyp2f1.py
   │     │  │  │  ├─ test_hypergeometric.py
   │     │  │  │  ├─ test_iv_ratio.py
   │     │  │  │  ├─ test_kolmogorov.py
   │     │  │  │  ├─ test_lambertw.py
   │     │  │  │  ├─ test_legendre.py
   │     │  │  │  ├─ test_loggamma.py
   │     │  │  │  ├─ test_logit.py
   │     │  │  │  ├─ test_logsumexp.py
   │     │  │  │  ├─ test_log_softmax.py
   │     │  │  │  ├─ test_mpmath.py
   │     │  │  │  ├─ test_nan_inputs.py
   │     │  │  │  ├─ test_ndtr.py
   │     │  │  │  ├─ test_ndtri_exp.py
   │     │  │  │  ├─ test_orthogonal.py
   │     │  │  │  ├─ test_orthogonal_eval.py
   │     │  │  │  ├─ test_owens_t.py
   │     │  │  │  ├─ test_pcf.py
   │     │  │  │  ├─ test_pdtr.py
   │     │  │  │  ├─ test_powm1.py
   │     │  │  │  ├─ test_precompute_expn_asy.py
   │     │  │  │  ├─ test_precompute_gammainc.py
   │     │  │  │  ├─ test_precompute_utils.py
   │     │  │  │  ├─ test_round.py
   │     │  │  │  ├─ test_sf_error.py
   │     │  │  │  ├─ test_sici.py
   │     │  │  │  ├─ test_specfun.py
   │     │  │  │  ├─ test_spence.py
   │     │  │  │  ├─ test_spfun_stats.py
   │     │  │  │  ├─ test_spherical_bessel.py
   │     │  │  │  ├─ test_sph_harm.py
   │     │  │  │  ├─ test_support_alternative_backends.py
   │     │  │  │  ├─ test_trig.py
   │     │  │  │  ├─ test_ufunc_signatures.py
   │     │  │  │  ├─ test_wrightomega.py
   │     │  │  │  ├─ test_wright_bessel.py
   │     │  │  │  ├─ test_xsf_cuda.py
   │     │  │  │  ├─ test_zeta.py
   │     │  │  │  ├─ _cython_examples
   │     │  │  │  │  ├─ extending.pyx
   │     │  │  │  │  └─ meson.build
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ xsf
   │     │  │  │  ├─ binom.h
   │     │  │  │  ├─ cdflib.h
   │     │  │  │  ├─ cephes
   │     │  │  │  │  ├─ airy.h
   │     │  │  │  │  ├─ besselpoly.h
   │     │  │  │  │  ├─ beta.h
   │     │  │  │  │  ├─ cbrt.h
   │     │  │  │  │  ├─ chbevl.h
   │     │  │  │  │  ├─ chdtr.h
   │     │  │  │  │  ├─ const.h
   │     │  │  │  │  ├─ ellie.h
   │     │  │  │  │  ├─ ellik.h
   │     │  │  │  │  ├─ ellpe.h
   │     │  │  │  │  ├─ ellpk.h
   │     │  │  │  │  ├─ expn.h
   │     │  │  │  │  ├─ gamma.h
   │     │  │  │  │  ├─ hyp2f1.h
   │     │  │  │  │  ├─ hyperg.h
   │     │  │  │  │  ├─ i0.h
   │     │  │  │  │  ├─ i1.h
   │     │  │  │  │  ├─ igam.h
   │     │  │  │  │  ├─ igami.h
   │     │  │  │  │  ├─ igam_asymp_coeff.h
   │     │  │  │  │  ├─ j0.h
   │     │  │  │  │  ├─ j1.h
   │     │  │  │  │  ├─ jv.h
   │     │  │  │  │  ├─ k0.h
   │     │  │  │  │  ├─ k1.h
   │     │  │  │  │  ├─ kn.h
   │     │  │  │  │  ├─ lanczos.h
   │     │  │  │  │  ├─ ndtr.h
   │     │  │  │  │  ├─ poch.h
   │     │  │  │  │  ├─ polevl.h
   │     │  │  │  │  ├─ psi.h
   │     │  │  │  │  ├─ rgamma.h
   │     │  │  │  │  ├─ scipy_iv.h
   │     │  │  │  │  ├─ shichi.h
   │     │  │  │  │  ├─ sici.h
   │     │  │  │  │  ├─ sindg.h
   │     │  │  │  │  ├─ tandg.h
   │     │  │  │  │  ├─ trig.h
   │     │  │  │  │  ├─ unity.h
   │     │  │  │  │  └─ zeta.h
   │     │  │  │  ├─ config.h
   │     │  │  │  ├─ digamma.h
   │     │  │  │  ├─ error.h
   │     │  │  │  ├─ evalpoly.h
   │     │  │  │  ├─ expint.h
   │     │  │  │  ├─ hyp2f1.h
   │     │  │  │  ├─ iv_ratio.h
   │     │  │  │  ├─ lambertw.h
   │     │  │  │  ├─ loggamma.h
   │     │  │  │  ├─ sici.h
   │     │  │  │  ├─ tools.h
   │     │  │  │  ├─ trig.h
   │     │  │  │  ├─ wright_bessel.h
   │     │  │  │  └─ zlog1.h
   │     │  │  ├─ _add_newdocs.py
   │     │  │  ├─ _basic.py
   │     │  │  ├─ _comb.cp311-win_amd64.dll.a
   │     │  │  ├─ _comb.cp311-win_amd64.pyd
   │     │  │  ├─ _ellip_harm.py
   │     │  │  ├─ _ellip_harm_2.cp311-win_amd64.dll.a
   │     │  │  ├─ _ellip_harm_2.cp311-win_amd64.pyd
   │     │  │  ├─ _gufuncs.cp311-win_amd64.dll.a
   │     │  │  ├─ _gufuncs.cp311-win_amd64.pyd
   │     │  │  ├─ _input_validation.py
   │     │  │  ├─ _lambertw.py
   │     │  │  ├─ _logsumexp.py
   │     │  │  ├─ _mptestutils.py
   │     │  │  ├─ _multiufuncs.py
   │     │  │  ├─ _orthogonal.py
   │     │  │  ├─ _orthogonal.pyi
   │     │  │  ├─ _precompute
   │     │  │  │  ├─ cosine_cdf.py
   │     │  │  │  ├─ expn_asy.py
   │     │  │  │  ├─ gammainc_asy.py
   │     │  │  │  ├─ gammainc_data.py
   │     │  │  │  ├─ hyp2f1_data.py
   │     │  │  │  ├─ lambertw.py
   │     │  │  │  ├─ loggamma.py
   │     │  │  │  ├─ struve_convergence.py
   │     │  │  │  ├─ utils.py
   │     │  │  │  ├─ wrightomega.py
   │     │  │  │  ├─ wright_bessel.py
   │     │  │  │  ├─ wright_bessel_data.py
   │     │  │  │  ├─ zetac.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _sf_error.py
   │     │  │  ├─ _specfun.cp311-win_amd64.dll.a
   │     │  │  ├─ _specfun.cp311-win_amd64.pyd
   │     │  │  ├─ _special_ufuncs.cp311-win_amd64.dll.a
   │     │  │  ├─ _special_ufuncs.cp311-win_amd64.pyd
   │     │  │  ├─ _spfun_stats.py
   │     │  │  ├─ _spherical_bessel.py
   │     │  │  ├─ _support_alternative_backends.py
   │     │  │  ├─ _testutils.py
   │     │  │  ├─ _test_internal.cp311-win_amd64.dll.a
   │     │  │  ├─ _test_internal.cp311-win_amd64.pyd
   │     │  │  ├─ _test_internal.pyi
   │     │  │  ├─ _ufuncs.cp311-win_amd64.dll.a
   │     │  │  ├─ _ufuncs.cp311-win_amd64.pyd
   │     │  │  ├─ _ufuncs.pyi
   │     │  │  ├─ _ufuncs.pyx
   │     │  │  ├─ _ufuncs_cxx.cp311-win_amd64.dll.a
   │     │  │  ├─ _ufuncs_cxx.cp311-win_amd64.pyd
   │     │  │  ├─ _ufuncs_cxx.pxd
   │     │  │  ├─ _ufuncs_cxx.pyx
   │     │  │  ├─ _ufuncs_cxx_defs.h
   │     │  │  ├─ _ufuncs_defs.h
   │     │  │  ├─ __init__.pxd
   │     │  │  └─ __init__.py
   │     │  ├─ stats
   │     │  │  ├─ biasedurn.py
   │     │  │  ├─ contingency.py
   │     │  │  ├─ distributions.py
   │     │  │  ├─ kde.py
   │     │  │  ├─ morestats.py
   │     │  │  ├─ mstats.py
   │     │  │  ├─ mstats_basic.py
   │     │  │  ├─ mstats_extras.py
   │     │  │  ├─ mvn.py
   │     │  │  ├─ qmc.py
   │     │  │  ├─ sampling.py
   │     │  │  ├─ stats.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ common_tests.py
   │     │  │  │  ├─ data
   │     │  │  │  │  ├─ fisher_exact_results_from_r.py
   │     │  │  │  │  ├─ jf_skew_t_gamlss_pdf_data.npy
   │     │  │  │  │  ├─ levy_stable
   │     │  │  │  │  │  ├─ stable-loc-scale-sample-data.npy
   │     │  │  │  │  │  ├─ stable-Z1-cdf-sample-data.npy
   │     │  │  │  │  │  └─ stable-Z1-pdf-sample-data.npy
   │     │  │  │  │  ├─ nist_anova
   │     │  │  │  │  │  ├─ AtmWtAg.dat
   │     │  │  │  │  │  ├─ SiRstv.dat
   │     │  │  │  │  │  ├─ SmLs01.dat
   │     │  │  │  │  │  ├─ SmLs02.dat
   │     │  │  │  │  │  ├─ SmLs03.dat
   │     │  │  │  │  │  ├─ SmLs04.dat
   │     │  │  │  │  │  ├─ SmLs05.dat
   │     │  │  │  │  │  ├─ SmLs06.dat
   │     │  │  │  │  │  ├─ SmLs07.dat
   │     │  │  │  │  │  ├─ SmLs08.dat
   │     │  │  │  │  │  └─ SmLs09.dat
   │     │  │  │  │  ├─ nist_linregress
   │     │  │  │  │  │  └─ Norris.dat
   │     │  │  │  │  ├─ rel_breitwigner_pdf_sample_data_ROOT.npy
   │     │  │  │  │  ├─ studentized_range_mpmath_ref.json
   │     │  │  │  │  └─ _mvt.py
   │     │  │  │  ├─ test_axis_nan_policy.py
   │     │  │  │  ├─ test_binned_statistic.py
   │     │  │  │  ├─ test_censored_data.py
   │     │  │  │  ├─ test_contingency.py
   │     │  │  │  ├─ test_continuous.py
   │     │  │  │  ├─ test_continuous_basic.py
   │     │  │  │  ├─ test_continuous_fit_censored.py
   │     │  │  │  ├─ test_correlation.py
   │     │  │  │  ├─ test_crosstab.py
   │     │  │  │  ├─ test_discrete_basic.py
   │     │  │  │  ├─ test_discrete_distns.py
   │     │  │  │  ├─ test_distributions.py
   │     │  │  │  ├─ test_entropy.py
   │     │  │  │  ├─ test_fast_gen_inversion.py
   │     │  │  │  ├─ test_fit.py
   │     │  │  │  ├─ test_hypotests.py
   │     │  │  │  ├─ test_kdeoth.py
   │     │  │  │  ├─ test_mgc.py
   │     │  │  │  ├─ test_morestats.py
   │     │  │  │  ├─ test_mstats_basic.py
   │     │  │  │  ├─ test_mstats_extras.py
   │     │  │  │  ├─ test_multicomp.py
   │     │  │  │  ├─ test_multivariate.py
   │     │  │  │  ├─ test_odds_ratio.py
   │     │  │  │  ├─ test_qmc.py
   │     │  │  │  ├─ test_rank.py
   │     │  │  │  ├─ test_relative_risk.py
   │     │  │  │  ├─ test_resampling.py
   │     │  │  │  ├─ test_sampling.py
   │     │  │  │  ├─ test_sensitivity_analysis.py
   │     │  │  │  ├─ test_stats.py
   │     │  │  │  ├─ test_survival.py
   │     │  │  │  ├─ test_tukeylambda_stats.py
   │     │  │  │  ├─ test_variation.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _ansari_swilk_statistics.cp311-win_amd64.dll.a
   │     │  │  ├─ _ansari_swilk_statistics.cp311-win_amd64.pyd
   │     │  │  ├─ _axis_nan_policy.py
   │     │  │  ├─ _biasedurn.cp311-win_amd64.dll.a
   │     │  │  ├─ _biasedurn.cp311-win_amd64.pyd
   │     │  │  ├─ _biasedurn.pxd
   │     │  │  ├─ _binned_statistic.py
   │     │  │  ├─ _binomtest.py
   │     │  │  ├─ _bws_test.py
   │     │  │  ├─ _censored_data.py
   │     │  │  ├─ _common.py
   │     │  │  ├─ _constants.py
   │     │  │  ├─ _continuous_distns.py
   │     │  │  ├─ _correlation.py
   │     │  │  ├─ _covariance.py
   │     │  │  ├─ _crosstab.py
   │     │  │  ├─ _discrete_distns.py
   │     │  │  ├─ _distn_infrastructure.py
   │     │  │  ├─ _distribution_infrastructure.py
   │     │  │  ├─ _distr_params.py
   │     │  │  ├─ _entropy.py
   │     │  │  ├─ _fit.py
   │     │  │  ├─ _hypotests.py
   │     │  │  ├─ _kde.py
   │     │  │  ├─ _ksstats.py
   │     │  │  ├─ _levy_stable
   │     │  │  │  ├─ levyst.cp311-win_amd64.dll.a
   │     │  │  │  ├─ levyst.cp311-win_amd64.pyd
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _mannwhitneyu.py
   │     │  │  ├─ _mgc.py
   │     │  │  ├─ _morestats.py
   │     │  │  ├─ _mstats_basic.py
   │     │  │  ├─ _mstats_extras.py
   │     │  │  ├─ _multicomp.py
   │     │  │  ├─ _multivariate.py
   │     │  │  ├─ _mvn.cp311-win_amd64.dll.a
   │     │  │  ├─ _mvn.cp311-win_amd64.pyd
   │     │  │  ├─ _new_distributions.py
   │     │  │  ├─ _odds_ratio.py
   │     │  │  ├─ _page_trend_test.py
   │     │  │  ├─ _probability_distribution.py
   │     │  │  ├─ _qmc.py
   │     │  │  ├─ _qmc_cy.cp311-win_amd64.dll.a
   │     │  │  ├─ _qmc_cy.cp311-win_amd64.pyd
   │     │  │  ├─ _qmc_cy.pyi
   │     │  │  ├─ _qmvnt.py
   │     │  │  ├─ _rcont
   │     │  │  │  ├─ rcont.cp311-win_amd64.dll.a
   │     │  │  │  ├─ rcont.cp311-win_amd64.pyd
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _relative_risk.py
   │     │  │  ├─ _resampling.py
   │     │  │  ├─ _result_classes.py
   │     │  │  ├─ _sampling.py
   │     │  │  ├─ _sensitivity_analysis.py
   │     │  │  ├─ _sobol.cp311-win_amd64.dll.a
   │     │  │  ├─ _sobol.cp311-win_amd64.pyd
   │     │  │  ├─ _sobol.pyi
   │     │  │  ├─ _sobol_direction_numbers.npz
   │     │  │  ├─ _stats.cp311-win_amd64.dll.a
   │     │  │  ├─ _stats.cp311-win_amd64.pyd
   │     │  │  ├─ _stats.pxd
   │     │  │  ├─ _stats_mstats_common.py
   │     │  │  ├─ _stats_py.py
   │     │  │  ├─ _stats_pythran.cp311-win_amd64.dll.a
   │     │  │  ├─ _stats_pythran.cp311-win_amd64.pyd
   │     │  │  ├─ _survival.py
   │     │  │  ├─ _tukeylambda_stats.py
   │     │  │  ├─ _unuran
   │     │  │  │  ├─ unuran_wrapper.cp311-win_amd64.dll.a
   │     │  │  │  ├─ unuran_wrapper.cp311-win_amd64.pyd
   │     │  │  │  ├─ unuran_wrapper.pyi
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _variation.py
   │     │  │  ├─ _warnings_errors.py
   │     │  │  ├─ _wilcoxon.py
   │     │  │  └─ __init__.py
   │     │  ├─ version.py
   │     │  ├─ _distributor_init.py
   │     │  ├─ _lib
   │     │  │  ├─ array_api_compat
   │     │  │  │  ├─ common
   │     │  │  │  │  ├─ _aliases.py
   │     │  │  │  │  ├─ _fft.py
   │     │  │  │  │  ├─ _helpers.py
   │     │  │  │  │  ├─ _linalg.py
   │     │  │  │  │  ├─ _typing.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ cupy
   │     │  │  │  │  ├─ fft.py
   │     │  │  │  │  ├─ linalg.py
   │     │  │  │  │  ├─ _aliases.py
   │     │  │  │  │  ├─ _info.py
   │     │  │  │  │  ├─ _typing.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ dask
   │     │  │  │  │  ├─ array
   │     │  │  │  │  │  ├─ fft.py
   │     │  │  │  │  │  ├─ linalg.py
   │     │  │  │  │  │  ├─ _aliases.py
   │     │  │  │  │  │  ├─ _info.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ numpy
   │     │  │  │  │  ├─ fft.py
   │     │  │  │  │  ├─ linalg.py
   │     │  │  │  │  ├─ _aliases.py
   │     │  │  │  │  ├─ _info.py
   │     │  │  │  │  ├─ _typing.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ torch
   │     │  │  │  │  ├─ fft.py
   │     │  │  │  │  ├─ linalg.py
   │     │  │  │  │  ├─ _aliases.py
   │     │  │  │  │  ├─ _info.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ _internal.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ array_api_extra
   │     │  │  │  ├─ _funcs.py
   │     │  │  │  ├─ _typing.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ cobyqa
   │     │  │  │  ├─ framework.py
   │     │  │  │  ├─ main.py
   │     │  │  │  ├─ models.py
   │     │  │  │  ├─ problem.py
   │     │  │  │  ├─ settings.py
   │     │  │  │  ├─ subsolvers
   │     │  │  │  │  ├─ geometry.py
   │     │  │  │  │  ├─ optim.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ utils
   │     │  │  │  │  ├─ exceptions.py
   │     │  │  │  │  ├─ math.py
   │     │  │  │  │  ├─ versions.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ decorator.py
   │     │  │  ├─ deprecation.py
   │     │  │  ├─ doccer.py
   │     │  │  ├─ messagestream.cp311-win_amd64.dll.a
   │     │  │  ├─ messagestream.cp311-win_amd64.pyd
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_array_api.py
   │     │  │  │  ├─ test_bunch.py
   │     │  │  │  ├─ test_ccallback.py
   │     │  │  │  ├─ test_config.py
   │     │  │  │  ├─ test_deprecation.py
   │     │  │  │  ├─ test_doccer.py
   │     │  │  │  ├─ test_import_cycles.py
   │     │  │  │  ├─ test_public_api.py
   │     │  │  │  ├─ test_scipy_version.py
   │     │  │  │  ├─ test_tmpdirs.py
   │     │  │  │  ├─ test_warnings.py
   │     │  │  │  ├─ test__gcutils.py
   │     │  │  │  ├─ test__pep440.py
   │     │  │  │  ├─ test__testutils.py
   │     │  │  │  ├─ test__threadsafety.py
   │     │  │  │  ├─ test__util.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ uarray.py
   │     │  │  ├─ _array_api.py
   │     │  │  ├─ _array_api_no_0d.py
   │     │  │  ├─ _bunch.py
   │     │  │  ├─ _ccallback.py
   │     │  │  ├─ _ccallback_c.cp311-win_amd64.dll.a
   │     │  │  ├─ _ccallback_c.cp311-win_amd64.pyd
   │     │  │  ├─ _disjoint_set.py
   │     │  │  ├─ _docscrape.py
   │     │  │  ├─ _elementwise_iterative_method.py
   │     │  │  ├─ _finite_differences.py
   │     │  │  ├─ _fpumode.cp311-win_amd64.dll.a
   │     │  │  ├─ _fpumode.cp311-win_amd64.pyd
   │     │  │  ├─ _gcutils.py
   │     │  │  ├─ _pep440.py
   │     │  │  ├─ _testutils.py
   │     │  │  ├─ _test_ccallback.cp311-win_amd64.dll.a
   │     │  │  ├─ _test_ccallback.cp311-win_amd64.pyd
   │     │  │  ├─ _test_deprecation_call.cp311-win_amd64.dll.a
   │     │  │  ├─ _test_deprecation_call.cp311-win_amd64.pyd
   │     │  │  ├─ _test_deprecation_def.cp311-win_amd64.dll.a
   │     │  │  ├─ _test_deprecation_def.cp311-win_amd64.pyd
   │     │  │  ├─ _threadsafety.py
   │     │  │  ├─ _tmpdirs.py
   │     │  │  ├─ _uarray
   │     │  │  │  ├─ LICENSE
   │     │  │  │  ├─ _backend.py
   │     │  │  │  ├─ _uarray.cp311-win_amd64.dll.a
   │     │  │  │  ├─ _uarray.cp311-win_amd64.pyd
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _util.py
   │     │  │  └─ __init__.py
   │     │  ├─ __config__.py
   │     │  └─ __init__.py
   │     ├─ scipy-1.15.2-cp311-cp311-win_amd64.whl
   │     ├─ scipy-1.15.2.dist-info
   │     │  ├─ DELVEWHEEL
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE.txt
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  └─ WHEEL
   │     ├─ scipy.libs
   │     │  └─ libscipy_openblas-f07f5a5d207a3a47104dca54d6d0c86a.dll
   │     ├─ scripts
   │     │  └─ readme-gen
   │     │     └─ readme_gen.py
   │     ├─ selenium
   │     │  ├─ common
   │     │  │  ├─ exceptions.py
   │     │  │  └─ __init__.py
   │     │  ├─ py.typed
   │     │  ├─ types.py
   │     │  ├─ webdriver
   │     │  │  ├─ chrome
   │     │  │  │  ├─ options.py
   │     │  │  │  ├─ remote_connection.py
   │     │  │  │  ├─ service.py
   │     │  │  │  ├─ webdriver.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ chromium
   │     │  │  │  ├─ options.py
   │     │  │  │  ├─ remote_connection.py
   │     │  │  │  ├─ service.py
   │     │  │  │  ├─ webdriver.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ common
   │     │  │  │  ├─ actions
   │     │  │  │  │  ├─ action_builder.py
   │     │  │  │  │  ├─ input_device.py
   │     │  │  │  │  ├─ interaction.py
   │     │  │  │  │  ├─ key_actions.py
   │     │  │  │  │  ├─ key_input.py
   │     │  │  │  │  ├─ mouse_button.py
   │     │  │  │  │  ├─ pointer_actions.py
   │     │  │  │  │  ├─ pointer_input.py
   │     │  │  │  │  ├─ wheel_actions.py
   │     │  │  │  │  ├─ wheel_input.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ action_chains.py
   │     │  │  │  ├─ alert.py
   │     │  │  │  ├─ bidi
   │     │  │  │  │  ├─ cdp.py
   │     │  │  │  │  ├─ console.py
   │     │  │  │  │  ├─ script.py
   │     │  │  │  │  ├─ session.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ by.py
   │     │  │  │  ├─ desired_capabilities.py
   │     │  │  │  ├─ devtools
   │     │  │  │  │  ├─ v131
   │     │  │  │  │  │  ├─ accessibility.py
   │     │  │  │  │  │  ├─ animation.py
   │     │  │  │  │  │  ├─ audits.py
   │     │  │  │  │  │  ├─ autofill.py
   │     │  │  │  │  │  ├─ background_service.py
   │     │  │  │  │  │  ├─ bluetooth_emulation.py
   │     │  │  │  │  │  ├─ browser.py
   │     │  │  │  │  │  ├─ cache_storage.py
   │     │  │  │  │  │  ├─ cast.py
   │     │  │  │  │  │  ├─ console.py
   │     │  │  │  │  │  ├─ css.py
   │     │  │  │  │  │  ├─ database.py
   │     │  │  │  │  │  ├─ debugger.py
   │     │  │  │  │  │  ├─ device_access.py
   │     │  │  │  │  │  ├─ device_orientation.py
   │     │  │  │  │  │  ├─ dom.py
   │     │  │  │  │  │  ├─ dom_debugger.py
   │     │  │  │  │  │  ├─ dom_snapshot.py
   │     │  │  │  │  │  ├─ dom_storage.py
   │     │  │  │  │  │  ├─ emulation.py
   │     │  │  │  │  │  ├─ event_breakpoints.py
   │     │  │  │  │  │  ├─ extensions.py
   │     │  │  │  │  │  ├─ fed_cm.py
   │     │  │  │  │  │  ├─ fetch.py
   │     │  │  │  │  │  ├─ file_system.py
   │     │  │  │  │  │  ├─ headless_experimental.py
   │     │  │  │  │  │  ├─ heap_profiler.py
   │     │  │  │  │  │  ├─ indexed_db.py
   │     │  │  │  │  │  ├─ input_.py
   │     │  │  │  │  │  ├─ inspector.py
   │     │  │  │  │  │  ├─ io.py
   │     │  │  │  │  │  ├─ layer_tree.py
   │     │  │  │  │  │  ├─ log.py
   │     │  │  │  │  │  ├─ media.py
   │     │  │  │  │  │  ├─ memory.py
   │     │  │  │  │  │  ├─ network.py
   │     │  │  │  │  │  ├─ overlay.py
   │     │  │  │  │  │  ├─ page.py
   │     │  │  │  │  │  ├─ performance.py
   │     │  │  │  │  │  ├─ performance_timeline.py
   │     │  │  │  │  │  ├─ preload.py
   │     │  │  │  │  │  ├─ profiler.py
   │     │  │  │  │  │  ├─ pwa.py
   │     │  │  │  │  │  ├─ py.typed
   │     │  │  │  │  │  ├─ runtime.py
   │     │  │  │  │  │  ├─ schema.py
   │     │  │  │  │  │  ├─ security.py
   │     │  │  │  │  │  ├─ service_worker.py
   │     │  │  │  │  │  ├─ storage.py
   │     │  │  │  │  │  ├─ system_info.py
   │     │  │  │  │  │  ├─ target.py
   │     │  │  │  │  │  ├─ tethering.py
   │     │  │  │  │  │  ├─ tracing.py
   │     │  │  │  │  │  ├─ util.py
   │     │  │  │  │  │  ├─ web_audio.py
   │     │  │  │  │  │  ├─ web_authn.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ v132
   │     │  │  │  │  │  ├─ accessibility.py
   │     │  │  │  │  │  ├─ animation.py
   │     │  │  │  │  │  ├─ audits.py
   │     │  │  │  │  │  ├─ autofill.py
   │     │  │  │  │  │  ├─ background_service.py
   │     │  │  │  │  │  ├─ bluetooth_emulation.py
   │     │  │  │  │  │  ├─ browser.py
   │     │  │  │  │  │  ├─ cache_storage.py
   │     │  │  │  │  │  ├─ cast.py
   │     │  │  │  │  │  ├─ console.py
   │     │  │  │  │  │  ├─ css.py
   │     │  │  │  │  │  ├─ database.py
   │     │  │  │  │  │  ├─ debugger.py
   │     │  │  │  │  │  ├─ device_access.py
   │     │  │  │  │  │  ├─ device_orientation.py
   │     │  │  │  │  │  ├─ dom.py
   │     │  │  │  │  │  ├─ dom_debugger.py
   │     │  │  │  │  │  ├─ dom_snapshot.py
   │     │  │  │  │  │  ├─ dom_storage.py
   │     │  │  │  │  │  ├─ emulation.py
   │     │  │  │  │  │  ├─ event_breakpoints.py
   │     │  │  │  │  │  ├─ extensions.py
   │     │  │  │  │  │  ├─ fed_cm.py
   │     │  │  │  │  │  ├─ fetch.py
   │     │  │  │  │  │  ├─ file_system.py
   │     │  │  │  │  │  ├─ headless_experimental.py
   │     │  │  │  │  │  ├─ heap_profiler.py
   │     │  │  │  │  │  ├─ indexed_db.py
   │     │  │  │  │  │  ├─ input_.py
   │     │  │  │  │  │  ├─ inspector.py
   │     │  │  │  │  │  ├─ io.py
   │     │  │  │  │  │  ├─ layer_tree.py
   │     │  │  │  │  │  ├─ log.py
   │     │  │  │  │  │  ├─ media.py
   │     │  │  │  │  │  ├─ memory.py
   │     │  │  │  │  │  ├─ network.py
   │     │  │  │  │  │  ├─ overlay.py
   │     │  │  │  │  │  ├─ page.py
   │     │  │  │  │  │  ├─ performance.py
   │     │  │  │  │  │  ├─ performance_timeline.py
   │     │  │  │  │  │  ├─ preload.py
   │     │  │  │  │  │  ├─ profiler.py
   │     │  │  │  │  │  ├─ pwa.py
   │     │  │  │  │  │  ├─ py.typed
   │     │  │  │  │  │  ├─ runtime.py
   │     │  │  │  │  │  ├─ schema.py
   │     │  │  │  │  │  ├─ security.py
   │     │  │  │  │  │  ├─ service_worker.py
   │     │  │  │  │  │  ├─ storage.py
   │     │  │  │  │  │  ├─ system_info.py
   │     │  │  │  │  │  ├─ target.py
   │     │  │  │  │  │  ├─ tethering.py
   │     │  │  │  │  │  ├─ tracing.py
   │     │  │  │  │  │  ├─ util.py
   │     │  │  │  │  │  ├─ web_audio.py
   │     │  │  │  │  │  ├─ web_authn.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ v133
   │     │  │  │  │  │  ├─ accessibility.py
   │     │  │  │  │  │  ├─ animation.py
   │     │  │  │  │  │  ├─ audits.py
   │     │  │  │  │  │  ├─ autofill.py
   │     │  │  │  │  │  ├─ background_service.py
   │     │  │  │  │  │  ├─ bluetooth_emulation.py
   │     │  │  │  │  │  ├─ browser.py
   │     │  │  │  │  │  ├─ cache_storage.py
   │     │  │  │  │  │  ├─ cast.py
   │     │  │  │  │  │  ├─ console.py
   │     │  │  │  │  │  ├─ css.py
   │     │  │  │  │  │  ├─ database.py
   │     │  │  │  │  │  ├─ debugger.py
   │     │  │  │  │  │  ├─ device_access.py
   │     │  │  │  │  │  ├─ device_orientation.py
   │     │  │  │  │  │  ├─ dom.py
   │     │  │  │  │  │  ├─ dom_debugger.py
   │     │  │  │  │  │  ├─ dom_snapshot.py
   │     │  │  │  │  │  ├─ dom_storage.py
   │     │  │  │  │  │  ├─ emulation.py
   │     │  │  │  │  │  ├─ event_breakpoints.py
   │     │  │  │  │  │  ├─ extensions.py
   │     │  │  │  │  │  ├─ fed_cm.py
   │     │  │  │  │  │  ├─ fetch.py
   │     │  │  │  │  │  ├─ file_system.py
   │     │  │  │  │  │  ├─ headless_experimental.py
   │     │  │  │  │  │  ├─ heap_profiler.py
   │     │  │  │  │  │  ├─ indexed_db.py
   │     │  │  │  │  │  ├─ input_.py
   │     │  │  │  │  │  ├─ inspector.py
   │     │  │  │  │  │  ├─ io.py
   │     │  │  │  │  │  ├─ layer_tree.py
   │     │  │  │  │  │  ├─ log.py
   │     │  │  │  │  │  ├─ media.py
   │     │  │  │  │  │  ├─ memory.py
   │     │  │  │  │  │  ├─ network.py
   │     │  │  │  │  │  ├─ overlay.py
   │     │  │  │  │  │  ├─ page.py
   │     │  │  │  │  │  ├─ performance.py
   │     │  │  │  │  │  ├─ performance_timeline.py
   │     │  │  │  │  │  ├─ preload.py
   │     │  │  │  │  │  ├─ profiler.py
   │     │  │  │  │  │  ├─ pwa.py
   │     │  │  │  │  │  ├─ py.typed
   │     │  │  │  │  │  ├─ runtime.py
   │     │  │  │  │  │  ├─ schema.py
   │     │  │  │  │  │  ├─ security.py
   │     │  │  │  │  │  ├─ service_worker.py
   │     │  │  │  │  │  ├─ storage.py
   │     │  │  │  │  │  ├─ system_info.py
   │     │  │  │  │  │  ├─ target.py
   │     │  │  │  │  │  ├─ tethering.py
   │     │  │  │  │  │  ├─ tracing.py
   │     │  │  │  │  │  ├─ util.py
   │     │  │  │  │  │  ├─ web_audio.py
   │     │  │  │  │  │  ├─ web_authn.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  └─ v85
   │     │  │  │  │     ├─ accessibility.py
   │     │  │  │  │     ├─ animation.py
   │     │  │  │  │     ├─ application_cache.py
   │     │  │  │  │     ├─ audits.py
   │     │  │  │  │     ├─ background_service.py
   │     │  │  │  │     ├─ browser.py
   │     │  │  │  │     ├─ cache_storage.py
   │     │  │  │  │     ├─ cast.py
   │     │  │  │  │     ├─ console.py
   │     │  │  │  │     ├─ css.py
   │     │  │  │  │     ├─ database.py
   │     │  │  │  │     ├─ debugger.py
   │     │  │  │  │     ├─ device_orientation.py
   │     │  │  │  │     ├─ dom.py
   │     │  │  │  │     ├─ dom_debugger.py
   │     │  │  │  │     ├─ dom_snapshot.py
   │     │  │  │  │     ├─ dom_storage.py
   │     │  │  │  │     ├─ emulation.py
   │     │  │  │  │     ├─ fetch.py
   │     │  │  │  │     ├─ headless_experimental.py
   │     │  │  │  │     ├─ heap_profiler.py
   │     │  │  │  │     ├─ indexed_db.py
   │     │  │  │  │     ├─ input_.py
   │     │  │  │  │     ├─ inspector.py
   │     │  │  │  │     ├─ io.py
   │     │  │  │  │     ├─ layer_tree.py
   │     │  │  │  │     ├─ log.py
   │     │  │  │  │     ├─ media.py
   │     │  │  │  │     ├─ memory.py
   │     │  │  │  │     ├─ network.py
   │     │  │  │  │     ├─ overlay.py
   │     │  │  │  │     ├─ page.py
   │     │  │  │  │     ├─ performance.py
   │     │  │  │  │     ├─ profiler.py
   │     │  │  │  │     ├─ py.typed
   │     │  │  │  │     ├─ runtime.py
   │     │  │  │  │     ├─ schema.py
   │     │  │  │  │     ├─ security.py
   │     │  │  │  │     ├─ service_worker.py
   │     │  │  │  │     ├─ storage.py
   │     │  │  │  │     ├─ system_info.py
   │     │  │  │  │     ├─ target.py
   │     │  │  │  │     ├─ tethering.py
   │     │  │  │  │     ├─ tracing.py
   │     │  │  │  │     ├─ util.py
   │     │  │  │  │     ├─ web_audio.py
   │     │  │  │  │     ├─ web_authn.py
   │     │  │  │  │     └─ __init__.py
   │     │  │  │  ├─ driver_finder.py
   │     │  │  │  ├─ fedcm
   │     │  │  │  │  ├─ account.py
   │     │  │  │  │  ├─ dialog.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ keys.py
   │     │  │  │  ├─ linux
   │     │  │  │  │  └─ selenium-manager
   │     │  │  │  ├─ log.py
   │     │  │  │  ├─ macos
   │     │  │  │  │  └─ selenium-manager
   │     │  │  │  ├─ mutation-listener.js
   │     │  │  │  ├─ options.py
   │     │  │  │  ├─ print_page_options.py
   │     │  │  │  ├─ proxy.py
   │     │  │  │  ├─ selenium_manager.py
   │     │  │  │  ├─ service.py
   │     │  │  │  ├─ timeouts.py
   │     │  │  │  ├─ utils.py
   │     │  │  │  ├─ virtual_authenticator.py
   │     │  │  │  ├─ window.py
   │     │  │  │  ├─ windows
   │     │  │  │  │  └─ selenium-manager.exe
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ edge
   │     │  │  │  ├─ options.py
   │     │  │  │  ├─ remote_connection.py
   │     │  │  │  ├─ service.py
   │     │  │  │  ├─ webdriver.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ firefox
   │     │  │  │  ├─ firefox_binary.py
   │     │  │  │  ├─ firefox_profile.py
   │     │  │  │  ├─ options.py
   │     │  │  │  ├─ remote_connection.py
   │     │  │  │  ├─ service.py
   │     │  │  │  ├─ webdriver.py
   │     │  │  │  ├─ webdriver_prefs.json
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ ie
   │     │  │  │  ├─ options.py
   │     │  │  │  ├─ service.py
   │     │  │  │  ├─ webdriver.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ remote
   │     │  │  │  ├─ bidi_connection.py
   │     │  │  │  ├─ client_config.py
   │     │  │  │  ├─ command.py
   │     │  │  │  ├─ errorhandler.py
   │     │  │  │  ├─ fedcm.py
   │     │  │  │  ├─ file_detector.py
   │     │  │  │  ├─ findElements.js
   │     │  │  │  ├─ getAttribute.js
   │     │  │  │  ├─ isDisplayed.js
   │     │  │  │  ├─ locator_converter.py
   │     │  │  │  ├─ mobile.py
   │     │  │  │  ├─ remote_connection.py
   │     │  │  │  ├─ script_key.py
   │     │  │  │  ├─ shadowroot.py
   │     │  │  │  ├─ switch_to.py
   │     │  │  │  ├─ utils.py
   │     │  │  │  ├─ webdriver.py
   │     │  │  │  ├─ webelement.py
   │     │  │  │  ├─ websocket_connection.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ safari
   │     │  │  │  ├─ options.py
   │     │  │  │  ├─ permissions.py
   │     │  │  │  ├─ remote_connection.py
   │     │  │  │  ├─ service.py
   │     │  │  │  ├─ webdriver.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ support
   │     │  │  │  ├─ abstract_event_listener.py
   │     │  │  │  ├─ color.py
   │     │  │  │  ├─ events.py
   │     │  │  │  ├─ event_firing_webdriver.py
   │     │  │  │  ├─ expected_conditions.py
   │     │  │  │  ├─ relative_locator.py
   │     │  │  │  ├─ select.py
   │     │  │  │  ├─ ui.py
   │     │  │  │  ├─ wait.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ webkitgtk
   │     │  │  │  ├─ options.py
   │     │  │  │  ├─ service.py
   │     │  │  │  ├─ webdriver.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ wpewebkit
   │     │  │  │  ├─ options.py
   │     │  │  │  ├─ service.py
   │     │  │  │  ├─ webdriver.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  └─ __init__.py
   │     ├─ selenium-4.29.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  └─ WHEEL
   │     ├─ setuptools
   │     │  ├─ archive_util.py
   │     │  ├─ build_meta.py
   │     │  ├─ cli-32.exe
   │     │  ├─ cli-64.exe
   │     │  ├─ cli-arm64.exe
   │     │  ├─ cli.exe
   │     │  ├─ command
   │     │  │  ├─ alias.py
   │     │  │  ├─ bdist_egg.py
   │     │  │  ├─ bdist_rpm.py
   │     │  │  ├─ build.py
   │     │  │  ├─ build_clib.py
   │     │  │  ├─ build_ext.py
   │     │  │  ├─ build_py.py
   │     │  │  ├─ develop.py
   │     │  │  ├─ dist_info.py
   │     │  │  ├─ easy_install.py
   │     │  │  ├─ editable_wheel.py
   │     │  │  ├─ egg_info.py
   │     │  │  ├─ install.py
   │     │  │  ├─ install_egg_info.py
   │     │  │  ├─ install_lib.py
   │     │  │  ├─ install_scripts.py
   │     │  │  ├─ launcher manifest.xml
   │     │  │  ├─ py36compat.py
   │     │  │  ├─ register.py
   │     │  │  ├─ rotate.py
   │     │  │  ├─ saveopts.py
   │     │  │  ├─ sdist.py
   │     │  │  ├─ setopt.py
   │     │  │  ├─ test.py
   │     │  │  ├─ upload.py
   │     │  │  ├─ upload_docs.py
   │     │  │  └─ __init__.py
   │     │  ├─ config
   │     │  │  ├─ expand.py
   │     │  │  ├─ pyprojecttoml.py
   │     │  │  ├─ setupcfg.py
   │     │  │  ├─ _apply_pyprojecttoml.py
   │     │  │  ├─ _validate_pyproject
   │     │  │  │  ├─ error_reporting.py
   │     │  │  │  ├─ extra_validations.py
   │     │  │  │  ├─ fastjsonschema_exceptions.py
   │     │  │  │  ├─ fastjsonschema_validations.py
   │     │  │  │  ├─ formats.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ depends.py
   │     │  ├─ dep_util.py
   │     │  ├─ discovery.py
   │     │  ├─ dist.py
   │     │  ├─ errors.py
   │     │  ├─ extension.py
   │     │  ├─ extern
   │     │  │  └─ __init__.py
   │     │  ├─ glob.py
   │     │  ├─ gui-32.exe
   │     │  ├─ gui-64.exe
   │     │  ├─ gui-arm64.exe
   │     │  ├─ gui.exe
   │     │  ├─ installer.py
   │     │  ├─ launch.py
   │     │  ├─ logging.py
   │     │  ├─ monkey.py
   │     │  ├─ msvc.py
   │     │  ├─ namespaces.py
   │     │  ├─ package_index.py
   │     │  ├─ py34compat.py
   │     │  ├─ sandbox.py
   │     │  ├─ script (dev).tmpl
   │     │  ├─ script.tmpl
   │     │  ├─ unicode_utils.py
   │     │  ├─ version.py
   │     │  ├─ wheel.py
   │     │  ├─ windows_support.py
   │     │  ├─ _deprecation_warning.py
   │     │  ├─ _distutils
   │     │  │  ├─ archive_util.py
   │     │  │  ├─ bcppcompiler.py
   │     │  │  ├─ ccompiler.py
   │     │  │  ├─ cmd.py
   │     │  │  ├─ command
   │     │  │  │  ├─ bdist.py
   │     │  │  │  ├─ bdist_dumb.py
   │     │  │  │  ├─ bdist_rpm.py
   │     │  │  │  ├─ build.py
   │     │  │  │  ├─ build_clib.py
   │     │  │  │  ├─ build_ext.py
   │     │  │  │  ├─ build_py.py
   │     │  │  │  ├─ build_scripts.py
   │     │  │  │  ├─ check.py
   │     │  │  │  ├─ clean.py
   │     │  │  │  ├─ config.py
   │     │  │  │  ├─ install.py
   │     │  │  │  ├─ install_data.py
   │     │  │  │  ├─ install_egg_info.py
   │     │  │  │  ├─ install_headers.py
   │     │  │  │  ├─ install_lib.py
   │     │  │  │  ├─ install_scripts.py
   │     │  │  │  ├─ py37compat.py
   │     │  │  │  ├─ register.py
   │     │  │  │  ├─ sdist.py
   │     │  │  │  ├─ upload.py
   │     │  │  │  ├─ _framework_compat.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ config.py
   │     │  │  ├─ core.py
   │     │  │  ├─ cygwinccompiler.py
   │     │  │  ├─ debug.py
   │     │  │  ├─ dep_util.py
   │     │  │  ├─ dir_util.py
   │     │  │  ├─ dist.py
   │     │  │  ├─ errors.py
   │     │  │  ├─ extension.py
   │     │  │  ├─ fancy_getopt.py
   │     │  │  ├─ filelist.py
   │     │  │  ├─ file_util.py
   │     │  │  ├─ log.py
   │     │  │  ├─ msvc9compiler.py
   │     │  │  ├─ msvccompiler.py
   │     │  │  ├─ py38compat.py
   │     │  │  ├─ py39compat.py
   │     │  │  ├─ spawn.py
   │     │  │  ├─ sysconfig.py
   │     │  │  ├─ text_file.py
   │     │  │  ├─ unixccompiler.py
   │     │  │  ├─ util.py
   │     │  │  ├─ version.py
   │     │  │  ├─ versionpredicate.py
   │     │  │  ├─ _collections.py
   │     │  │  ├─ _functools.py
   │     │  │  ├─ _macos_compat.py
   │     │  │  ├─ _msvccompiler.py
   │     │  │  └─ __init__.py
   │     │  ├─ _entry_points.py
   │     │  ├─ _imp.py
   │     │  ├─ _importlib.py
   │     │  ├─ _itertools.py
   │     │  ├─ _path.py
   │     │  ├─ _reqs.py
   │     │  ├─ _vendor
   │     │  │  ├─ importlib_metadata
   │     │  │  │  ├─ _adapters.py
   │     │  │  │  ├─ _collections.py
   │     │  │  │  ├─ _compat.py
   │     │  │  │  ├─ _functools.py
   │     │  │  │  ├─ _itertools.py
   │     │  │  │  ├─ _meta.py
   │     │  │  │  ├─ _text.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ importlib_resources
   │     │  │  │  ├─ abc.py
   │     │  │  │  ├─ readers.py
   │     │  │  │  ├─ simple.py
   │     │  │  │  ├─ _adapters.py
   │     │  │  │  ├─ _common.py
   │     │  │  │  ├─ _compat.py
   │     │  │  │  ├─ _itertools.py
   │     │  │  │  ├─ _legacy.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ jaraco
   │     │  │  │  ├─ context.py
   │     │  │  │  ├─ functools.py
   │     │  │  │  ├─ text
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ more_itertools
   │     │  │  │  ├─ more.py
   │     │  │  │  ├─ recipes.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ ordered_set.py
   │     │  │  ├─ packaging
   │     │  │  │  ├─ markers.py
   │     │  │  │  ├─ requirements.py
   │     │  │  │  ├─ specifiers.py
   │     │  │  │  ├─ tags.py
   │     │  │  │  ├─ utils.py
   │     │  │  │  ├─ version.py
   │     │  │  │  ├─ _manylinux.py
   │     │  │  │  ├─ _musllinux.py
   │     │  │  │  ├─ _structures.py
   │     │  │  │  ├─ __about__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ pyparsing
   │     │  │  │  ├─ actions.py
   │     │  │  │  ├─ common.py
   │     │  │  │  ├─ core.py
   │     │  │  │  ├─ diagram
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ exceptions.py
   │     │  │  │  ├─ helpers.py
   │     │  │  │  ├─ results.py
   │     │  │  │  ├─ testing.py
   │     │  │  │  ├─ unicode.py
   │     │  │  │  ├─ util.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ tomli
   │     │  │  │  ├─ _parser.py
   │     │  │  │  ├─ _re.py
   │     │  │  │  ├─ _types.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ typing_extensions.py
   │     │  │  ├─ zipp.py
   │     │  │  └─ __init__.py
   │     │  └─ __init__.py
   │     ├─ setuptools-65.5.0.dist-info
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ shellingham
   │     │  ├─ nt.py
   │     │  ├─ posix
   │     │  │  ├─ proc.py
   │     │  │  ├─ ps.py
   │     │  │  ├─ _core.py
   │     │  │  └─ __init__.py
   │     │  ├─ _core.py
   │     │  └─ __init__.py
   │     ├─ shellingham-1.5.4.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  ├─ WHEEL
   │     │  └─ zip-safe
   │     ├─ six-1.17.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ six.py
   │     ├─ sklearn
   │     │  ├─ .libs
   │     │  │  ├─ msvcp140.dll
   │     │  │  └─ vcomp140.dll
   │     │  ├─ base.py
   │     │  ├─ calibration.py
   │     │  ├─ cluster
   │     │  │  ├─ meson.build
   │     │  │  ├─ tests
   │     │  │  │  ├─ common.py
   │     │  │  │  ├─ test_affinity_propagation.py
   │     │  │  │  ├─ test_bicluster.py
   │     │  │  │  ├─ test_birch.py
   │     │  │  │  ├─ test_bisect_k_means.py
   │     │  │  │  ├─ test_dbscan.py
   │     │  │  │  ├─ test_feature_agglomeration.py
   │     │  │  │  ├─ test_hdbscan.py
   │     │  │  │  ├─ test_hierarchical.py
   │     │  │  │  ├─ test_k_means.py
   │     │  │  │  ├─ test_mean_shift.py
   │     │  │  │  ├─ test_optics.py
   │     │  │  │  ├─ test_spectral.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _affinity_propagation.py
   │     │  │  ├─ _agglomerative.py
   │     │  │  ├─ _bicluster.py
   │     │  │  ├─ _birch.py
   │     │  │  ├─ _bisect_k_means.py
   │     │  │  ├─ _dbscan.py
   │     │  │  ├─ _dbscan_inner.cp311-win_amd64.lib
   │     │  │  ├─ _dbscan_inner.cp311-win_amd64.pyd
   │     │  │  ├─ _dbscan_inner.pyx
   │     │  │  ├─ _feature_agglomeration.py
   │     │  │  ├─ _hdbscan
   │     │  │  │  ├─ hdbscan.py
   │     │  │  │  ├─ meson.build
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ test_reachibility.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ _linkage.cp311-win_amd64.lib
   │     │  │  │  ├─ _linkage.cp311-win_amd64.pyd
   │     │  │  │  ├─ _linkage.pyx
   │     │  │  │  ├─ _reachability.cp311-win_amd64.lib
   │     │  │  │  ├─ _reachability.cp311-win_amd64.pyd
   │     │  │  │  ├─ _reachability.pyx
   │     │  │  │  ├─ _tree.cp311-win_amd64.lib
   │     │  │  │  ├─ _tree.cp311-win_amd64.pyd
   │     │  │  │  ├─ _tree.pxd
   │     │  │  │  ├─ _tree.pyx
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _hierarchical_fast.cp311-win_amd64.lib
   │     │  │  ├─ _hierarchical_fast.cp311-win_amd64.pyd
   │     │  │  ├─ _hierarchical_fast.pxd
   │     │  │  ├─ _hierarchical_fast.pyx
   │     │  │  ├─ _kmeans.py
   │     │  │  ├─ _k_means_common.cp311-win_amd64.lib
   │     │  │  ├─ _k_means_common.cp311-win_amd64.pyd
   │     │  │  ├─ _k_means_common.pxd
   │     │  │  ├─ _k_means_common.pyx
   │     │  │  ├─ _k_means_elkan.cp311-win_amd64.lib
   │     │  │  ├─ _k_means_elkan.cp311-win_amd64.pyd
   │     │  │  ├─ _k_means_elkan.pyx
   │     │  │  ├─ _k_means_lloyd.cp311-win_amd64.lib
   │     │  │  ├─ _k_means_lloyd.cp311-win_amd64.pyd
   │     │  │  ├─ _k_means_lloyd.pyx
   │     │  │  ├─ _k_means_minibatch.cp311-win_amd64.lib
   │     │  │  ├─ _k_means_minibatch.cp311-win_amd64.pyd
   │     │  │  ├─ _k_means_minibatch.pyx
   │     │  │  ├─ _mean_shift.py
   │     │  │  ├─ _optics.py
   │     │  │  ├─ _spectral.py
   │     │  │  └─ __init__.py
   │     │  ├─ compose
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_column_transformer.py
   │     │  │  │  ├─ test_target.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _column_transformer.py
   │     │  │  ├─ _target.py
   │     │  │  └─ __init__.py
   │     │  ├─ conftest.py
   │     │  ├─ covariance
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_covariance.py
   │     │  │  │  ├─ test_elliptic_envelope.py
   │     │  │  │  ├─ test_graphical_lasso.py
   │     │  │  │  ├─ test_robust_covariance.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _elliptic_envelope.py
   │     │  │  ├─ _empirical_covariance.py
   │     │  │  ├─ _graph_lasso.py
   │     │  │  ├─ _robust_covariance.py
   │     │  │  ├─ _shrunk_covariance.py
   │     │  │  └─ __init__.py
   │     │  ├─ cross_decomposition
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_pls.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _pls.py
   │     │  │  └─ __init__.py
   │     │  ├─ datasets
   │     │  │  ├─ data
   │     │  │  │  ├─ boston_house_prices.csv
   │     │  │  │  ├─ breast_cancer.csv
   │     │  │  │  ├─ diabetes_data_raw.csv.gz
   │     │  │  │  ├─ diabetes_target.csv.gz
   │     │  │  │  ├─ digits.csv.gz
   │     │  │  │  ├─ iris.csv
   │     │  │  │  ├─ linnerud_exercise.csv
   │     │  │  │  ├─ linnerud_physiological.csv
   │     │  │  │  ├─ wine_data.csv
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ descr
   │     │  │  │  ├─ breast_cancer.rst
   │     │  │  │  ├─ california_housing.rst
   │     │  │  │  ├─ covtype.rst
   │     │  │  │  ├─ diabetes.rst
   │     │  │  │  ├─ digits.rst
   │     │  │  │  ├─ iris.rst
   │     │  │  │  ├─ kddcup99.rst
   │     │  │  │  ├─ lfw.rst
   │     │  │  │  ├─ linnerud.rst
   │     │  │  │  ├─ olivetti_faces.rst
   │     │  │  │  ├─ rcv1.rst
   │     │  │  │  ├─ species_distributions.rst
   │     │  │  │  ├─ twenty_newsgroups.rst
   │     │  │  │  ├─ wine_data.rst
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ images
   │     │  │  │  ├─ china.jpg
   │     │  │  │  ├─ flower.jpg
   │     │  │  │  ├─ README.txt
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ meson.build
   │     │  │  ├─ tests
   │     │  │  │  ├─ data
   │     │  │  │  │  ├─ openml
   │     │  │  │  │  │  ├─ id_1
   │     │  │  │  │  │  │  ├─ api-v1-jd-1.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdf-1.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdq-1.json.gz
   │     │  │  │  │  │  │  ├─ data-v1-dl-1.arff.gz
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  ├─ id_1119
   │     │  │  │  │  │  │  ├─ api-v1-jd-1119.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdf-1119.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-adult-census-l-2-dv-1.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-adult-census-l-2-s-act-.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdq-1119.json.gz
   │     │  │  │  │  │  │  ├─ data-v1-dl-54002.arff.gz
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  ├─ id_1590
   │     │  │  │  │  │  │  ├─ api-v1-jd-1590.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdf-1590.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdq-1590.json.gz
   │     │  │  │  │  │  │  ├─ data-v1-dl-1595261.arff.gz
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  ├─ id_2
   │     │  │  │  │  │  │  ├─ api-v1-jd-2.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdf-2.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-anneal-l-2-dv-1.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-anneal-l-2-s-act-.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdq-2.json.gz
   │     │  │  │  │  │  │  ├─ data-v1-dl-1666876.arff.gz
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  ├─ id_292
   │     │  │  │  │  │  │  ├─ api-v1-jd-292.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jd-40981.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdf-292.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdf-40981.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-australian-l-2-dv-1-s-dact.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-australian-l-2-dv-1.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-australian-l-2-s-act-.json.gz
   │     │  │  │  │  │  │  ├─ data-v1-dl-49822.arff.gz
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  ├─ id_3
   │     │  │  │  │  │  │  ├─ api-v1-jd-3.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdf-3.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdq-3.json.gz
   │     │  │  │  │  │  │  ├─ data-v1-dl-3.arff.gz
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  ├─ id_40589
   │     │  │  │  │  │  │  ├─ api-v1-jd-40589.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdf-40589.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-emotions-l-2-dv-3.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-emotions-l-2-s-act-.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdq-40589.json.gz
   │     │  │  │  │  │  │  ├─ data-v1-dl-4644182.arff.gz
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  ├─ id_40675
   │     │  │  │  │  │  │  ├─ api-v1-jd-40675.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdf-40675.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-glass2-l-2-dv-1-s-dact.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-glass2-l-2-dv-1.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-glass2-l-2-s-act-.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdq-40675.json.gz
   │     │  │  │  │  │  │  ├─ data-v1-dl-4965250.arff.gz
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  ├─ id_40945
   │     │  │  │  │  │  │  ├─ api-v1-jd-40945.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdf-40945.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdq-40945.json.gz
   │     │  │  │  │  │  │  ├─ data-v1-dl-16826755.arff.gz
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  ├─ id_40966
   │     │  │  │  │  │  │  ├─ api-v1-jd-40966.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdf-40966.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-miceprotein-l-2-dv-4.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-miceprotein-l-2-s-act-.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdq-40966.json.gz
   │     │  │  │  │  │  │  ├─ data-v1-dl-17928620.arff.gz
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  ├─ id_42074
   │     │  │  │  │  │  │  ├─ api-v1-jd-42074.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdf-42074.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdq-42074.json.gz
   │     │  │  │  │  │  │  ├─ data-v1-dl-21552912.arff.gz
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  ├─ id_42585
   │     │  │  │  │  │  │  ├─ api-v1-jd-42585.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdf-42585.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdq-42585.json.gz
   │     │  │  │  │  │  │  ├─ data-v1-dl-21854866.arff.gz
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  ├─ id_561
   │     │  │  │  │  │  │  ├─ api-v1-jd-561.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdf-561.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-cpu-l-2-dv-1.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-cpu-l-2-s-act-.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdq-561.json.gz
   │     │  │  │  │  │  │  ├─ data-v1-dl-52739.arff.gz
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  ├─ id_61
   │     │  │  │  │  │  │  ├─ api-v1-jd-61.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdf-61.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-iris-l-2-dv-1.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdl-dn-iris-l-2-s-act-.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdq-61.json.gz
   │     │  │  │  │  │  │  ├─ data-v1-dl-61.arff.gz
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  ├─ id_62
   │     │  │  │  │  │  │  ├─ api-v1-jd-62.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdf-62.json.gz
   │     │  │  │  │  │  │  ├─ api-v1-jdq-62.json.gz
   │     │  │  │  │  │  │  ├─ data-v1-dl-52352.arff.gz
   │     │  │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  ├─ svmlight_classification.txt
   │     │  │  │  │  ├─ svmlight_invalid.txt
   │     │  │  │  │  ├─ svmlight_invalid_order.txt
   │     │  │  │  │  ├─ svmlight_multilabel.txt
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_20news.py
   │     │  │  │  ├─ test_arff_parser.py
   │     │  │  │  ├─ test_base.py
   │     │  │  │  ├─ test_california_housing.py
   │     │  │  │  ├─ test_common.py
   │     │  │  │  ├─ test_covtype.py
   │     │  │  │  ├─ test_kddcup99.py
   │     │  │  │  ├─ test_lfw.py
   │     │  │  │  ├─ test_olivetti_faces.py
   │     │  │  │  ├─ test_openml.py
   │     │  │  │  ├─ test_rcv1.py
   │     │  │  │  ├─ test_samples_generator.py
   │     │  │  │  ├─ test_svmlight_format.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _arff_parser.py
   │     │  │  ├─ _base.py
   │     │  │  ├─ _california_housing.py
   │     │  │  ├─ _covtype.py
   │     │  │  ├─ _kddcup99.py
   │     │  │  ├─ _lfw.py
   │     │  │  ├─ _olivetti_faces.py
   │     │  │  ├─ _openml.py
   │     │  │  ├─ _rcv1.py
   │     │  │  ├─ _samples_generator.py
   │     │  │  ├─ _species_distributions.py
   │     │  │  ├─ _svmlight_format_fast.cp311-win_amd64.lib
   │     │  │  ├─ _svmlight_format_fast.cp311-win_amd64.pyd
   │     │  │  ├─ _svmlight_format_fast.pyx
   │     │  │  ├─ _svmlight_format_io.py
   │     │  │  ├─ _twenty_newsgroups.py
   │     │  │  └─ __init__.py
   │     │  ├─ decomposition
   │     │  │  ├─ meson.build
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_dict_learning.py
   │     │  │  │  ├─ test_factor_analysis.py
   │     │  │  │  ├─ test_fastica.py
   │     │  │  │  ├─ test_incremental_pca.py
   │     │  │  │  ├─ test_kernel_pca.py
   │     │  │  │  ├─ test_nmf.py
   │     │  │  │  ├─ test_online_lda.py
   │     │  │  │  ├─ test_pca.py
   │     │  │  │  ├─ test_sparse_pca.py
   │     │  │  │  ├─ test_truncated_svd.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _base.py
   │     │  │  ├─ _cdnmf_fast.cp311-win_amd64.lib
   │     │  │  ├─ _cdnmf_fast.cp311-win_amd64.pyd
   │     │  │  ├─ _cdnmf_fast.pyx
   │     │  │  ├─ _dict_learning.py
   │     │  │  ├─ _factor_analysis.py
   │     │  │  ├─ _fastica.py
   │     │  │  ├─ _incremental_pca.py
   │     │  │  ├─ _kernel_pca.py
   │     │  │  ├─ _lda.py
   │     │  │  ├─ _nmf.py
   │     │  │  ├─ _online_lda_fast.cp311-win_amd64.lib
   │     │  │  ├─ _online_lda_fast.cp311-win_amd64.pyd
   │     │  │  ├─ _online_lda_fast.pyx
   │     │  │  ├─ _pca.py
   │     │  │  ├─ _sparse_pca.py
   │     │  │  ├─ _truncated_svd.py
   │     │  │  └─ __init__.py
   │     │  ├─ discriminant_analysis.py
   │     │  ├─ dummy.py
   │     │  ├─ ensemble
   │     │  │  ├─ meson.build
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_bagging.py
   │     │  │  │  ├─ test_base.py
   │     │  │  │  ├─ test_common.py
   │     │  │  │  ├─ test_forest.py
   │     │  │  │  ├─ test_gradient_boosting.py
   │     │  │  │  ├─ test_iforest.py
   │     │  │  │  ├─ test_stacking.py
   │     │  │  │  ├─ test_voting.py
   │     │  │  │  ├─ test_weight_boosting.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _bagging.py
   │     │  │  ├─ _base.py
   │     │  │  ├─ _forest.py
   │     │  │  ├─ _gb.py
   │     │  │  ├─ _gradient_boosting.cp311-win_amd64.lib
   │     │  │  ├─ _gradient_boosting.cp311-win_amd64.pyd
   │     │  │  ├─ _gradient_boosting.pyx
   │     │  │  ├─ _hist_gradient_boosting
   │     │  │  │  ├─ binning.py
   │     │  │  │  ├─ common.cp311-win_amd64.lib
   │     │  │  │  ├─ common.cp311-win_amd64.pyd
   │     │  │  │  ├─ common.pxd
   │     │  │  │  ├─ common.pyx
   │     │  │  │  ├─ gradient_boosting.py
   │     │  │  │  ├─ grower.py
   │     │  │  │  ├─ histogram.cp311-win_amd64.lib
   │     │  │  │  ├─ histogram.cp311-win_amd64.pyd
   │     │  │  │  ├─ histogram.pyx
   │     │  │  │  ├─ meson.build
   │     │  │  │  ├─ predictor.py
   │     │  │  │  ├─ splitting.cp311-win_amd64.lib
   │     │  │  │  ├─ splitting.cp311-win_amd64.pyd
   │     │  │  │  ├─ splitting.pyx
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ test_binning.py
   │     │  │  │  │  ├─ test_bitset.py
   │     │  │  │  │  ├─ test_compare_lightgbm.py
   │     │  │  │  │  ├─ test_gradient_boosting.py
   │     │  │  │  │  ├─ test_grower.py
   │     │  │  │  │  ├─ test_histogram.py
   │     │  │  │  │  ├─ test_monotonic_constraints.py
   │     │  │  │  │  ├─ test_predictor.py
   │     │  │  │  │  ├─ test_splitting.py
   │     │  │  │  │  ├─ test_warm_start.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ utils.py
   │     │  │  │  ├─ _binning.cp311-win_amd64.lib
   │     │  │  │  ├─ _binning.cp311-win_amd64.pyd
   │     │  │  │  ├─ _binning.pyx
   │     │  │  │  ├─ _bitset.cp311-win_amd64.lib
   │     │  │  │  ├─ _bitset.cp311-win_amd64.pyd
   │     │  │  │  ├─ _bitset.pxd
   │     │  │  │  ├─ _bitset.pyx
   │     │  │  │  ├─ _gradient_boosting.cp311-win_amd64.lib
   │     │  │  │  ├─ _gradient_boosting.cp311-win_amd64.pyd
   │     │  │  │  ├─ _gradient_boosting.pyx
   │     │  │  │  ├─ _predictor.cp311-win_amd64.lib
   │     │  │  │  ├─ _predictor.cp311-win_amd64.pyd
   │     │  │  │  ├─ _predictor.pyx
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _iforest.py
   │     │  │  ├─ _stacking.py
   │     │  │  ├─ _voting.py
   │     │  │  ├─ _weight_boosting.py
   │     │  │  └─ __init__.py
   │     │  ├─ exceptions.py
   │     │  ├─ experimental
   │     │  │  ├─ enable_halving_search_cv.py
   │     │  │  ├─ enable_hist_gradient_boosting.py
   │     │  │  ├─ enable_iterative_imputer.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_enable_hist_gradient_boosting.py
   │     │  │  │  ├─ test_enable_iterative_imputer.py
   │     │  │  │  ├─ test_enable_successive_halving.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ externals
   │     │  │  ├─ conftest.py
   │     │  │  ├─ README
   │     │  │  ├─ _arff.py
   │     │  │  ├─ _packaging
   │     │  │  │  ├─ version.py
   │     │  │  │  ├─ _structures.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _scipy
   │     │  │  │  ├─ sparse
   │     │  │  │  │  ├─ csgraph
   │     │  │  │  │  │  ├─ _laplacian.py
   │     │  │  │  │  │  └─ __init__.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ feature_extraction
   │     │  │  ├─ image.py
   │     │  │  ├─ meson.build
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_dict_vectorizer.py
   │     │  │  │  ├─ test_feature_hasher.py
   │     │  │  │  ├─ test_image.py
   │     │  │  │  ├─ test_text.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ text.py
   │     │  │  ├─ _dict_vectorizer.py
   │     │  │  ├─ _hash.py
   │     │  │  ├─ _hashing_fast.cp311-win_amd64.lib
   │     │  │  ├─ _hashing_fast.cp311-win_amd64.pyd
   │     │  │  ├─ _hashing_fast.pyx
   │     │  │  ├─ _stop_words.py
   │     │  │  └─ __init__.py
   │     │  ├─ feature_selection
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_base.py
   │     │  │  │  ├─ test_chi2.py
   │     │  │  │  ├─ test_feature_select.py
   │     │  │  │  ├─ test_from_model.py
   │     │  │  │  ├─ test_mutual_info.py
   │     │  │  │  ├─ test_rfe.py
   │     │  │  │  ├─ test_sequential.py
   │     │  │  │  ├─ test_variance_threshold.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _base.py
   │     │  │  ├─ _from_model.py
   │     │  │  ├─ _mutual_info.py
   │     │  │  ├─ _rfe.py
   │     │  │  ├─ _sequential.py
   │     │  │  ├─ _univariate_selection.py
   │     │  │  ├─ _variance_threshold.py
   │     │  │  └─ __init__.py
   │     │  ├─ frozen
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_frozen.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _frozen.py
   │     │  │  └─ __init__.py
   │     │  ├─ gaussian_process
   │     │  │  ├─ kernels.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_gpc.py
   │     │  │  │  ├─ test_gpr.py
   │     │  │  │  ├─ test_kernels.py
   │     │  │  │  ├─ _mini_sequence_kernel.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _gpc.py
   │     │  │  ├─ _gpr.py
   │     │  │  └─ __init__.py
   │     │  ├─ impute
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_base.py
   │     │  │  │  ├─ test_common.py
   │     │  │  │  ├─ test_impute.py
   │     │  │  │  ├─ test_knn.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _base.py
   │     │  │  ├─ _iterative.py
   │     │  │  ├─ _knn.py
   │     │  │  └─ __init__.py
   │     │  ├─ inspection
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_partial_dependence.py
   │     │  │  │  ├─ test_pd_utils.py
   │     │  │  │  ├─ test_permutation_importance.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _partial_dependence.py
   │     │  │  ├─ _pd_utils.py
   │     │  │  ├─ _permutation_importance.py
   │     │  │  ├─ _plot
   │     │  │  │  ├─ decision_boundary.py
   │     │  │  │  ├─ partial_dependence.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ test_boundary_decision_display.py
   │     │  │  │  │  ├─ test_plot_partial_dependence.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ isotonic.py
   │     │  ├─ kernel_approximation.py
   │     │  ├─ kernel_ridge.py
   │     │  ├─ linear_model
   │     │  │  ├─ meson.build
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_base.py
   │     │  │  │  ├─ test_bayes.py
   │     │  │  │  ├─ test_common.py
   │     │  │  │  ├─ test_coordinate_descent.py
   │     │  │  │  ├─ test_huber.py
   │     │  │  │  ├─ test_least_angle.py
   │     │  │  │  ├─ test_linear_loss.py
   │     │  │  │  ├─ test_logistic.py
   │     │  │  │  ├─ test_omp.py
   │     │  │  │  ├─ test_passive_aggressive.py
   │     │  │  │  ├─ test_perceptron.py
   │     │  │  │  ├─ test_quantile.py
   │     │  │  │  ├─ test_ransac.py
   │     │  │  │  ├─ test_ridge.py
   │     │  │  │  ├─ test_sag.py
   │     │  │  │  ├─ test_sgd.py
   │     │  │  │  ├─ test_sparse_coordinate_descent.py
   │     │  │  │  ├─ test_theil_sen.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _base.py
   │     │  │  ├─ _bayes.py
   │     │  │  ├─ _cd_fast.cp311-win_amd64.lib
   │     │  │  ├─ _cd_fast.cp311-win_amd64.pyd
   │     │  │  ├─ _cd_fast.pyx
   │     │  │  ├─ _coordinate_descent.py
   │     │  │  ├─ _glm
   │     │  │  │  ├─ glm.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ test_glm.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ _newton_solver.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _huber.py
   │     │  │  ├─ _least_angle.py
   │     │  │  ├─ _linear_loss.py
   │     │  │  ├─ _logistic.py
   │     │  │  ├─ _omp.py
   │     │  │  ├─ _passive_aggressive.py
   │     │  │  ├─ _perceptron.py
   │     │  │  ├─ _quantile.py
   │     │  │  ├─ _ransac.py
   │     │  │  ├─ _ridge.py
   │     │  │  ├─ _sag.py
   │     │  │  ├─ _sag_fast.cp311-win_amd64.lib
   │     │  │  ├─ _sag_fast.cp311-win_amd64.pyd
   │     │  │  ├─ _sag_fast.pyx.tp
   │     │  │  ├─ _sgd_fast.cp311-win_amd64.lib
   │     │  │  ├─ _sgd_fast.cp311-win_amd64.pyd
   │     │  │  ├─ _sgd_fast.pyx.tp
   │     │  │  ├─ _stochastic_gradient.py
   │     │  │  ├─ _theil_sen.py
   │     │  │  └─ __init__.py
   │     │  ├─ manifold
   │     │  │  ├─ meson.build
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_isomap.py
   │     │  │  │  ├─ test_locally_linear.py
   │     │  │  │  ├─ test_mds.py
   │     │  │  │  ├─ test_spectral_embedding.py
   │     │  │  │  ├─ test_t_sne.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _barnes_hut_tsne.cp311-win_amd64.lib
   │     │  │  ├─ _barnes_hut_tsne.cp311-win_amd64.pyd
   │     │  │  ├─ _barnes_hut_tsne.pyx
   │     │  │  ├─ _isomap.py
   │     │  │  ├─ _locally_linear.py
   │     │  │  ├─ _mds.py
   │     │  │  ├─ _spectral_embedding.py
   │     │  │  ├─ _t_sne.py
   │     │  │  ├─ _utils.cp311-win_amd64.lib
   │     │  │  ├─ _utils.cp311-win_amd64.pyd
   │     │  │  ├─ _utils.pyx
   │     │  │  └─ __init__.py
   │     │  ├─ meson.build
   │     │  ├─ metrics
   │     │  │  ├─ cluster
   │     │  │  │  ├─ meson.build
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ test_bicluster.py
   │     │  │  │  │  ├─ test_common.py
   │     │  │  │  │  ├─ test_supervised.py
   │     │  │  │  │  ├─ test_unsupervised.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ _bicluster.py
   │     │  │  │  ├─ _expected_mutual_info_fast.cp311-win_amd64.lib
   │     │  │  │  ├─ _expected_mutual_info_fast.cp311-win_amd64.pyd
   │     │  │  │  ├─ _expected_mutual_info_fast.pyx
   │     │  │  │  ├─ _supervised.py
   │     │  │  │  ├─ _unsupervised.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ meson.build
   │     │  │  ├─ pairwise.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_classification.py
   │     │  │  │  ├─ test_common.py
   │     │  │  │  ├─ test_dist_metrics.py
   │     │  │  │  ├─ test_pairwise.py
   │     │  │  │  ├─ test_pairwise_distances_reduction.py
   │     │  │  │  ├─ test_ranking.py
   │     │  │  │  ├─ test_regression.py
   │     │  │  │  ├─ test_score_objects.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _base.py
   │     │  │  ├─ _classification.py
   │     │  │  ├─ _dist_metrics.cp311-win_amd64.lib
   │     │  │  ├─ _dist_metrics.cp311-win_amd64.pyd
   │     │  │  ├─ _dist_metrics.pxd
   │     │  │  ├─ _dist_metrics.pxd.tp
   │     │  │  ├─ _dist_metrics.pyx.tp
   │     │  │  ├─ _pairwise_distances_reduction
   │     │  │  │  ├─ meson.build
   │     │  │  │  ├─ _argkmin.cp311-win_amd64.lib
   │     │  │  │  ├─ _argkmin.cp311-win_amd64.pyd
   │     │  │  │  ├─ _argkmin.pxd.tp
   │     │  │  │  ├─ _argkmin.pyx.tp
   │     │  │  │  ├─ _argkmin_classmode.cp311-win_amd64.lib
   │     │  │  │  ├─ _argkmin_classmode.cp311-win_amd64.pyd
   │     │  │  │  ├─ _argkmin_classmode.pyx.tp
   │     │  │  │  ├─ _base.cp311-win_amd64.lib
   │     │  │  │  ├─ _base.cp311-win_amd64.pyd
   │     │  │  │  ├─ _base.pxd.tp
   │     │  │  │  ├─ _base.pyx.tp
   │     │  │  │  ├─ _classmode.pxd
   │     │  │  │  ├─ _datasets_pair.cp311-win_amd64.lib
   │     │  │  │  ├─ _datasets_pair.cp311-win_amd64.pyd
   │     │  │  │  ├─ _datasets_pair.pxd.tp
   │     │  │  │  ├─ _datasets_pair.pyx.tp
   │     │  │  │  ├─ _dispatcher.py
   │     │  │  │  ├─ _middle_term_computer.cp311-win_amd64.lib
   │     │  │  │  ├─ _middle_term_computer.cp311-win_amd64.pyd
   │     │  │  │  ├─ _middle_term_computer.pxd.tp
   │     │  │  │  ├─ _middle_term_computer.pyx.tp
   │     │  │  │  ├─ _radius_neighbors.cp311-win_amd64.lib
   │     │  │  │  ├─ _radius_neighbors.cp311-win_amd64.pyd
   │     │  │  │  ├─ _radius_neighbors.pxd.tp
   │     │  │  │  ├─ _radius_neighbors.pyx.tp
   │     │  │  │  ├─ _radius_neighbors_classmode.cp311-win_amd64.lib
   │     │  │  │  ├─ _radius_neighbors_classmode.cp311-win_amd64.pyd
   │     │  │  │  ├─ _radius_neighbors_classmode.pyx.tp
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _pairwise_fast.cp311-win_amd64.lib
   │     │  │  ├─ _pairwise_fast.cp311-win_amd64.pyd
   │     │  │  ├─ _pairwise_fast.pyx
   │     │  │  ├─ _plot
   │     │  │  │  ├─ confusion_matrix.py
   │     │  │  │  ├─ det_curve.py
   │     │  │  │  ├─ precision_recall_curve.py
   │     │  │  │  ├─ regression.py
   │     │  │  │  ├─ roc_curve.py
   │     │  │  │  ├─ tests
   │     │  │  │  │  ├─ test_common_curve_display.py
   │     │  │  │  │  ├─ test_confusion_matrix_display.py
   │     │  │  │  │  ├─ test_det_curve_display.py
   │     │  │  │  │  ├─ test_precision_recall_display.py
   │     │  │  │  │  ├─ test_predict_error_display.py
   │     │  │  │  │  ├─ test_roc_curve_display.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _ranking.py
   │     │  │  ├─ _regression.py
   │     │  │  ├─ _scorer.py
   │     │  │  └─ __init__.py
   │     │  ├─ mixture
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_bayesian_mixture.py
   │     │  │  │  ├─ test_gaussian_mixture.py
   │     │  │  │  ├─ test_mixture.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _base.py
   │     │  │  ├─ _bayesian_mixture.py
   │     │  │  ├─ _gaussian_mixture.py
   │     │  │  └─ __init__.py
   │     │  ├─ model_selection
   │     │  │  ├─ tests
   │     │  │  │  ├─ common.py
   │     │  │  │  ├─ test_classification_threshold.py
   │     │  │  │  ├─ test_plot.py
   │     │  │  │  ├─ test_search.py
   │     │  │  │  ├─ test_split.py
   │     │  │  │  ├─ test_successive_halving.py
   │     │  │  │  ├─ test_validation.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _classification_threshold.py
   │     │  │  ├─ _plot.py
   │     │  │  ├─ _search.py
   │     │  │  ├─ _search_successive_halving.py
   │     │  │  ├─ _split.py
   │     │  │  ├─ _validation.py
   │     │  │  └─ __init__.py
   │     │  ├─ multiclass.py
   │     │  ├─ multioutput.py
   │     │  ├─ naive_bayes.py
   │     │  ├─ neighbors
   │     │  │  ├─ meson.build
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_ball_tree.py
   │     │  │  │  ├─ test_graph.py
   │     │  │  │  ├─ test_kde.py
   │     │  │  │  ├─ test_kd_tree.py
   │     │  │  │  ├─ test_lof.py
   │     │  │  │  ├─ test_nca.py
   │     │  │  │  ├─ test_nearest_centroid.py
   │     │  │  │  ├─ test_neighbors.py
   │     │  │  │  ├─ test_neighbors_pipeline.py
   │     │  │  │  ├─ test_neighbors_tree.py
   │     │  │  │  ├─ test_quad_tree.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _ball_tree.cp311-win_amd64.lib
   │     │  │  ├─ _ball_tree.cp311-win_amd64.pyd
   │     │  │  ├─ _ball_tree.pyx.tp
   │     │  │  ├─ _base.py
   │     │  │  ├─ _binary_tree.pxi.tp
   │     │  │  ├─ _classification.py
   │     │  │  ├─ _graph.py
   │     │  │  ├─ _kde.py
   │     │  │  ├─ _kd_tree.cp311-win_amd64.lib
   │     │  │  ├─ _kd_tree.cp311-win_amd64.pyd
   │     │  │  ├─ _kd_tree.pyx.tp
   │     │  │  ├─ _lof.py
   │     │  │  ├─ _nca.py
   │     │  │  ├─ _nearest_centroid.py
   │     │  │  ├─ _partition_nodes.cp311-win_amd64.lib
   │     │  │  ├─ _partition_nodes.cp311-win_amd64.pyd
   │     │  │  ├─ _partition_nodes.pxd
   │     │  │  ├─ _partition_nodes.pyx
   │     │  │  ├─ _quad_tree.cp311-win_amd64.lib
   │     │  │  ├─ _quad_tree.cp311-win_amd64.pyd
   │     │  │  ├─ _quad_tree.pxd
   │     │  │  ├─ _quad_tree.pyx
   │     │  │  ├─ _regression.py
   │     │  │  ├─ _unsupervised.py
   │     │  │  └─ __init__.py
   │     │  ├─ neural_network
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_base.py
   │     │  │  │  ├─ test_mlp.py
   │     │  │  │  ├─ test_rbm.py
   │     │  │  │  ├─ test_stochastic_optimizers.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _base.py
   │     │  │  ├─ _multilayer_perceptron.py
   │     │  │  ├─ _rbm.py
   │     │  │  ├─ _stochastic_optimizers.py
   │     │  │  └─ __init__.py
   │     │  ├─ pipeline.py
   │     │  ├─ preprocessing
   │     │  │  ├─ meson.build
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_common.py
   │     │  │  │  ├─ test_data.py
   │     │  │  │  ├─ test_discretization.py
   │     │  │  │  ├─ test_encoders.py
   │     │  │  │  ├─ test_function_transformer.py
   │     │  │  │  ├─ test_label.py
   │     │  │  │  ├─ test_polynomial.py
   │     │  │  │  ├─ test_target_encoder.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _csr_polynomial_expansion.cp311-win_amd64.lib
   │     │  │  ├─ _csr_polynomial_expansion.cp311-win_amd64.pyd
   │     │  │  ├─ _csr_polynomial_expansion.pyx
   │     │  │  ├─ _data.py
   │     │  │  ├─ _discretization.py
   │     │  │  ├─ _encoders.py
   │     │  │  ├─ _function_transformer.py
   │     │  │  ├─ _label.py
   │     │  │  ├─ _polynomial.py
   │     │  │  ├─ _target_encoder.py
   │     │  │  ├─ _target_encoder_fast.cp311-win_amd64.lib
   │     │  │  ├─ _target_encoder_fast.cp311-win_amd64.pyd
   │     │  │  ├─ _target_encoder_fast.pyx
   │     │  │  └─ __init__.py
   │     │  ├─ random_projection.py
   │     │  ├─ semi_supervised
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_label_propagation.py
   │     │  │  │  ├─ test_self_training.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _label_propagation.py
   │     │  │  ├─ _self_training.py
   │     │  │  └─ __init__.py
   │     │  ├─ svm
   │     │  │  ├─ meson.build
   │     │  │  ├─ src
   │     │  │  │  ├─ liblinear
   │     │  │  │  │  ├─ COPYRIGHT
   │     │  │  │  │  ├─ liblinear_helper.c
   │     │  │  │  │  ├─ linear.cpp
   │     │  │  │  │  ├─ linear.h
   │     │  │  │  │  ├─ tron.cpp
   │     │  │  │  │  ├─ tron.h
   │     │  │  │  │  └─ _cython_blas_helpers.h
   │     │  │  │  ├─ libsvm
   │     │  │  │  │  ├─ LIBSVM_CHANGES
   │     │  │  │  │  ├─ libsvm_helper.c
   │     │  │  │  │  ├─ libsvm_sparse_helper.c
   │     │  │  │  │  ├─ libsvm_template.cpp
   │     │  │  │  │  ├─ svm.cpp
   │     │  │  │  │  ├─ svm.h
   │     │  │  │  │  └─ _svm_cython_blas_helpers.h
   │     │  │  │  └─ newrand
   │     │  │  │     └─ newrand.h
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_bounds.py
   │     │  │  │  ├─ test_sparse.py
   │     │  │  │  ├─ test_svm.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _base.py
   │     │  │  ├─ _bounds.py
   │     │  │  ├─ _classes.py
   │     │  │  ├─ _liblinear.cp311-win_amd64.lib
   │     │  │  ├─ _liblinear.cp311-win_amd64.pyd
   │     │  │  ├─ _liblinear.pxi
   │     │  │  ├─ _liblinear.pyx
   │     │  │  ├─ _libsvm.cp311-win_amd64.lib
   │     │  │  ├─ _libsvm.cp311-win_amd64.pyd
   │     │  │  ├─ _libsvm.pxi
   │     │  │  ├─ _libsvm.pyx
   │     │  │  ├─ _libsvm_sparse.cp311-win_amd64.lib
   │     │  │  ├─ _libsvm_sparse.cp311-win_amd64.pyd
   │     │  │  ├─ _libsvm_sparse.pyx
   │     │  │  ├─ _newrand.cp311-win_amd64.lib
   │     │  │  ├─ _newrand.cp311-win_amd64.pyd
   │     │  │  ├─ _newrand.pyx
   │     │  │  └─ __init__.py
   │     │  ├─ tests
   │     │  │  ├─ metadata_routing_common.py
   │     │  │  ├─ test_base.py
   │     │  │  ├─ test_build.py
   │     │  │  ├─ test_calibration.py
   │     │  │  ├─ test_check_build.py
   │     │  │  ├─ test_common.py
   │     │  │  ├─ test_config.py
   │     │  │  ├─ test_discriminant_analysis.py
   │     │  │  ├─ test_docstrings.py
   │     │  │  ├─ test_docstring_parameters.py
   │     │  │  ├─ test_dummy.py
   │     │  │  ├─ test_init.py
   │     │  │  ├─ test_isotonic.py
   │     │  │  ├─ test_kernel_approximation.py
   │     │  │  ├─ test_kernel_ridge.py
   │     │  │  ├─ test_metadata_routing.py
   │     │  │  ├─ test_metaestimators.py
   │     │  │  ├─ test_metaestimators_metadata_routing.py
   │     │  │  ├─ test_min_dependencies_readme.py
   │     │  │  ├─ test_multiclass.py
   │     │  │  ├─ test_multioutput.py
   │     │  │  ├─ test_naive_bayes.py
   │     │  │  ├─ test_pipeline.py
   │     │  │  ├─ test_public_functions.py
   │     │  │  ├─ test_random_projection.py
   │     │  │  └─ __init__.py
   │     │  ├─ tree
   │     │  │  ├─ meson.build
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_export.py
   │     │  │  │  ├─ test_monotonic_tree.py
   │     │  │  │  ├─ test_reingold_tilford.py
   │     │  │  │  ├─ test_tree.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _classes.py
   │     │  │  ├─ _criterion.cp311-win_amd64.lib
   │     │  │  ├─ _criterion.cp311-win_amd64.pyd
   │     │  │  ├─ _criterion.pxd
   │     │  │  ├─ _criterion.pyx
   │     │  │  ├─ _export.py
   │     │  │  ├─ _partitioner.cp311-win_amd64.lib
   │     │  │  ├─ _partitioner.cp311-win_amd64.pyd
   │     │  │  ├─ _partitioner.pxd
   │     │  │  ├─ _partitioner.pyx
   │     │  │  ├─ _reingold_tilford.py
   │     │  │  ├─ _splitter.cp311-win_amd64.lib
   │     │  │  ├─ _splitter.cp311-win_amd64.pyd
   │     │  │  ├─ _splitter.pxd
   │     │  │  ├─ _splitter.pyx
   │     │  │  ├─ _tree.cp311-win_amd64.lib
   │     │  │  ├─ _tree.cp311-win_amd64.pyd
   │     │  │  ├─ _tree.pxd
   │     │  │  ├─ _tree.pyx
   │     │  │  ├─ _utils.cp311-win_amd64.lib
   │     │  │  ├─ _utils.cp311-win_amd64.pyd
   │     │  │  ├─ _utils.pxd
   │     │  │  ├─ _utils.pyx
   │     │  │  └─ __init__.py
   │     │  ├─ utils
   │     │  │  ├─ arrayfuncs.cp311-win_amd64.lib
   │     │  │  ├─ arrayfuncs.cp311-win_amd64.pyd
   │     │  │  ├─ arrayfuncs.pyx
   │     │  │  ├─ class_weight.py
   │     │  │  ├─ deprecation.py
   │     │  │  ├─ discovery.py
   │     │  │  ├─ estimator_checks.py
   │     │  │  ├─ extmath.py
   │     │  │  ├─ fixes.py
   │     │  │  ├─ graph.py
   │     │  │  ├─ meson.build
   │     │  │  ├─ metadata_routing.py
   │     │  │  ├─ metaestimators.py
   │     │  │  ├─ multiclass.py
   │     │  │  ├─ murmurhash.cp311-win_amd64.lib
   │     │  │  ├─ murmurhash.cp311-win_amd64.pyd
   │     │  │  ├─ murmurhash.pxd
   │     │  │  ├─ murmurhash.pyx
   │     │  │  ├─ optimize.py
   │     │  │  ├─ parallel.py
   │     │  │  ├─ random.py
   │     │  │  ├─ sparsefuncs.py
   │     │  │  ├─ sparsefuncs_fast.cp311-win_amd64.lib
   │     │  │  ├─ sparsefuncs_fast.cp311-win_amd64.pyd
   │     │  │  ├─ sparsefuncs_fast.pyx
   │     │  │  ├─ src
   │     │  │  │  ├─ MurmurHash3.cpp
   │     │  │  │  └─ MurmurHash3.h
   │     │  │  ├─ stats.py
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_arpack.py
   │     │  │  │  ├─ test_arrayfuncs.py
   │     │  │  │  ├─ test_array_api.py
   │     │  │  │  ├─ test_bunch.py
   │     │  │  │  ├─ test_chunking.py
   │     │  │  │  ├─ test_class_weight.py
   │     │  │  │  ├─ test_cython_blas.py
   │     │  │  │  ├─ test_deprecation.py
   │     │  │  │  ├─ test_encode.py
   │     │  │  │  ├─ test_estimator_checks.py
   │     │  │  │  ├─ test_estimator_html_repr.py
   │     │  │  │  ├─ test_extmath.py
   │     │  │  │  ├─ test_fast_dict.py
   │     │  │  │  ├─ test_fixes.py
   │     │  │  │  ├─ test_graph.py
   │     │  │  │  ├─ test_indexing.py
   │     │  │  │  ├─ test_mask.py
   │     │  │  │  ├─ test_metaestimators.py
   │     │  │  │  ├─ test_missing.py
   │     │  │  │  ├─ test_mocking.py
   │     │  │  │  ├─ test_multiclass.py
   │     │  │  │  ├─ test_murmurhash.py
   │     │  │  │  ├─ test_optimize.py
   │     │  │  │  ├─ test_parallel.py
   │     │  │  │  ├─ test_param_validation.py
   │     │  │  │  ├─ test_plotting.py
   │     │  │  │  ├─ test_pprint.py
   │     │  │  │  ├─ test_random.py
   │     │  │  │  ├─ test_response.py
   │     │  │  │  ├─ test_seq_dataset.py
   │     │  │  │  ├─ test_set_output.py
   │     │  │  │  ├─ test_shortest_path.py
   │     │  │  │  ├─ test_show_versions.py
   │     │  │  │  ├─ test_sparsefuncs.py
   │     │  │  │  ├─ test_stats.py
   │     │  │  │  ├─ test_tags.py
   │     │  │  │  ├─ test_testing.py
   │     │  │  │  ├─ test_typedefs.py
   │     │  │  │  ├─ test_unique.py
   │     │  │  │  ├─ test_user_interface.py
   │     │  │  │  ├─ test_utils.py
   │     │  │  │  ├─ test_validation.py
   │     │  │  │  ├─ test_weight_vector.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ validation.py
   │     │  │  ├─ _arpack.py
   │     │  │  ├─ _array_api.py
   │     │  │  ├─ _available_if.py
   │     │  │  ├─ _bunch.py
   │     │  │  ├─ _chunking.py
   │     │  │  ├─ _cython_blas.cp311-win_amd64.lib
   │     │  │  ├─ _cython_blas.cp311-win_amd64.pyd
   │     │  │  ├─ _cython_blas.pxd
   │     │  │  ├─ _cython_blas.pyx
   │     │  │  ├─ _encode.py
   │     │  │  ├─ _estimator_html_repr.css
   │     │  │  ├─ _estimator_html_repr.py
   │     │  │  ├─ _fast_dict.cp311-win_amd64.lib
   │     │  │  ├─ _fast_dict.cp311-win_amd64.pyd
   │     │  │  ├─ _fast_dict.pxd
   │     │  │  ├─ _fast_dict.pyx
   │     │  │  ├─ _heap.cp311-win_amd64.lib
   │     │  │  ├─ _heap.cp311-win_amd64.pyd
   │     │  │  ├─ _heap.pxd
   │     │  │  ├─ _heap.pyx
   │     │  │  ├─ _indexing.py
   │     │  │  ├─ _isfinite.cp311-win_amd64.lib
   │     │  │  ├─ _isfinite.cp311-win_amd64.pyd
   │     │  │  ├─ _isfinite.pyx
   │     │  │  ├─ _joblib.py
   │     │  │  ├─ _mask.py
   │     │  │  ├─ _metadata_requests.py
   │     │  │  ├─ _missing.py
   │     │  │  ├─ _mocking.py
   │     │  │  ├─ _openmp_helpers.cp311-win_amd64.lib
   │     │  │  ├─ _openmp_helpers.cp311-win_amd64.pyd
   │     │  │  ├─ _openmp_helpers.pxd
   │     │  │  ├─ _openmp_helpers.pyx
   │     │  │  ├─ _optional_dependencies.py
   │     │  │  ├─ _param_validation.py
   │     │  │  ├─ _plotting.py
   │     │  │  ├─ _pprint.py
   │     │  │  ├─ _random.cp311-win_amd64.lib
   │     │  │  ├─ _random.cp311-win_amd64.pyd
   │     │  │  ├─ _random.pxd
   │     │  │  ├─ _random.pyx
   │     │  │  ├─ _response.py
   │     │  │  ├─ _seq_dataset.cp311-win_amd64.lib
   │     │  │  ├─ _seq_dataset.cp311-win_amd64.pyd
   │     │  │  ├─ _seq_dataset.pxd.tp
   │     │  │  ├─ _seq_dataset.pyx.tp
   │     │  │  ├─ _set_output.py
   │     │  │  ├─ _show_versions.py
   │     │  │  ├─ _sorting.cp311-win_amd64.lib
   │     │  │  ├─ _sorting.cp311-win_amd64.pyd
   │     │  │  ├─ _sorting.pxd
   │     │  │  ├─ _sorting.pyx
   │     │  │  ├─ _tags.py
   │     │  │  ├─ _testing.py
   │     │  │  ├─ _test_common
   │     │  │  │  ├─ instance_generator.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _typedefs.cp311-win_amd64.lib
   │     │  │  ├─ _typedefs.cp311-win_amd64.pyd
   │     │  │  ├─ _typedefs.pxd
   │     │  │  ├─ _typedefs.pyx
   │     │  │  ├─ _unique.py
   │     │  │  ├─ _user_interface.py
   │     │  │  ├─ _vector_sentinel.cp311-win_amd64.lib
   │     │  │  ├─ _vector_sentinel.cp311-win_amd64.pyd
   │     │  │  ├─ _vector_sentinel.pxd
   │     │  │  ├─ _vector_sentinel.pyx
   │     │  │  ├─ _weight_vector.cp311-win_amd64.lib
   │     │  │  ├─ _weight_vector.cp311-win_amd64.pyd
   │     │  │  ├─ _weight_vector.pxd.tp
   │     │  │  ├─ _weight_vector.pyx.tp
   │     │  │  └─ __init__.py
   │     │  ├─ _build_utils
   │     │  │  ├─ tempita.py
   │     │  │  ├─ version.py
   │     │  │  └─ __init__.py
   │     │  ├─ _built_with_meson.py
   │     │  ├─ _config.py
   │     │  ├─ _distributor_init.py
   │     │  ├─ _isotonic.cp311-win_amd64.lib
   │     │  ├─ _isotonic.cp311-win_amd64.pyd
   │     │  ├─ _isotonic.pyx
   │     │  ├─ _loss
   │     │  │  ├─ link.py
   │     │  │  ├─ loss.py
   │     │  │  ├─ meson.build
   │     │  │  ├─ tests
   │     │  │  │  ├─ test_link.py
   │     │  │  │  ├─ test_loss.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _loss.cp311-win_amd64.lib
   │     │  │  ├─ _loss.cp311-win_amd64.pyd
   │     │  │  ├─ _loss.pxd
   │     │  │  ├─ _loss.pyx.tp
   │     │  │  └─ __init__.py
   │     │  ├─ _min_dependencies.py
   │     │  ├─ __check_build
   │     │  │  ├─ meson.build
   │     │  │  ├─ _check_build.cp311-win_amd64.lib
   │     │  │  ├─ _check_build.cp311-win_amd64.pyd
   │     │  │  ├─ _check_build.pyx
   │     │  │  └─ __init__.py
   │     │  └─ __init__.py
   │     ├─ smart_open
   │     │  ├─ azure.py
   │     │  ├─ bytebuffer.py
   │     │  ├─ compression.py
   │     │  ├─ concurrency.py
   │     │  ├─ constants.py
   │     │  ├─ doctools.py
   │     │  ├─ ftp.py
   │     │  ├─ gcs.py
   │     │  ├─ hdfs.py
   │     │  ├─ http.py
   │     │  ├─ local_file.py
   │     │  ├─ s3.py
   │     │  ├─ smart_open_lib.py
   │     │  ├─ ssh.py
   │     │  ├─ transport.py
   │     │  ├─ utils.py
   │     │  ├─ version.py
   │     │  ├─ webhdfs.py
   │     │  └─ __init__.py
   │     ├─ smart_open-7.1.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ sniffio
   │     │  ├─ py.typed
   │     │  ├─ _impl.py
   │     │  ├─ _tests
   │     │  │  ├─ test_sniffio.py
   │     │  │  └─ __init__.py
   │     │  ├─ _version.py
   │     │  └─ __init__.py
   │     ├─ sniffio-1.3.1.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ LICENSE.APACHE2
   │     │  ├─ LICENSE.MIT
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ socks.py
   │     ├─ sockshandler.py
   │     ├─ sortedcontainers
   │     │  ├─ sorteddict.py
   │     │  ├─ sortedlist.py
   │     │  ├─ sortedset.py
   │     │  └─ __init__.py
   │     ├─ sortedcontainers-2.4.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ soupsieve
   │     │  ├─ css_match.py
   │     │  ├─ css_parser.py
   │     │  ├─ css_types.py
   │     │  ├─ pretty.py
   │     │  ├─ py.typed
   │     │  ├─ util.py
   │     │  ├─ __init__.py
   │     │  └─ __meta__.py
   │     ├─ soupsieve-2.6.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE.md
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  └─ WHEEL
   │     ├─ spacy
   │     │  ├─ about.py
   │     │  ├─ attrs.cp311-win_amd64.pyd
   │     │  ├─ attrs.cpp
   │     │  ├─ attrs.pxd
   │     │  ├─ attrs.pyx
   │     │  ├─ cli
   │     │  │  ├─ apply.py
   │     │  │  ├─ assemble.py
   │     │  │  ├─ benchmark_speed.py
   │     │  │  ├─ convert.py
   │     │  │  ├─ debug_config.py
   │     │  │  ├─ debug_data.py
   │     │  │  ├─ debug_diff.py
   │     │  │  ├─ debug_model.py
   │     │  │  ├─ download.py
   │     │  │  ├─ evaluate.py
   │     │  │  ├─ find_function.py
   │     │  │  ├─ find_threshold.py
   │     │  │  ├─ info.py
   │     │  │  ├─ init_config.py
   │     │  │  ├─ init_pipeline.py
   │     │  │  ├─ package.py
   │     │  │  ├─ pretrain.py
   │     │  │  ├─ profile.py
   │     │  │  ├─ project
   │     │  │  │  ├─ assets.py
   │     │  │  │  ├─ clone.py
   │     │  │  │  ├─ document.py
   │     │  │  │  ├─ dvc.py
   │     │  │  │  ├─ pull.py
   │     │  │  │  ├─ push.py
   │     │  │  │  ├─ remote_storage.py
   │     │  │  │  ├─ run.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ templates
   │     │  │  │  ├─ quickstart_training.jinja
   │     │  │  │  └─ quickstart_training_recommendations.yml
   │     │  │  ├─ train.py
   │     │  │  ├─ validate.py
   │     │  │  ├─ _util.py
   │     │  │  └─ __init__.py
   │     │  ├─ compat.py
   │     │  ├─ default_config.cfg
   │     │  ├─ default_config_pretraining.cfg
   │     │  ├─ displacy
   │     │  │  ├─ render.py
   │     │  │  ├─ templates.py
   │     │  │  └─ __init__.py
   │     │  ├─ errors.py
   │     │  ├─ git_info.py
   │     │  ├─ glossary.py
   │     │  ├─ kb
   │     │  │  ├─ candidate.cp311-win_amd64.pyd
   │     │  │  ├─ candidate.cpp
   │     │  │  ├─ candidate.pxd
   │     │  │  ├─ candidate.pyx
   │     │  │  ├─ kb.cp311-win_amd64.pyd
   │     │  │  ├─ kb.cpp
   │     │  │  ├─ kb.pxd
   │     │  │  ├─ kb.pyx
   │     │  │  ├─ kb_in_memory.cp311-win_amd64.pyd
   │     │  │  ├─ kb_in_memory.cpp
   │     │  │  ├─ kb_in_memory.pxd
   │     │  │  ├─ kb_in_memory.pyx
   │     │  │  └─ __init__.py
   │     │  ├─ lang
   │     │  │  ├─ af
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ am
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ punctuation.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ ar
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ punctuation.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ az
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ bg
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ bn
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ punctuation.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ bo
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ ca
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lemmatizer.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ punctuation.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ syntax_iterators.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ char_classes.py
   │     │  │  ├─ cs
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ da
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ punctuation.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ syntax_iterators.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ de
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ punctuation.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ syntax_iterators.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ dsb
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ el
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ get_pos_from_wiktionary.py
   │     │  │  │  ├─ lemmatizer.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ punctuation.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ syntax_iterators.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ en
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lemmatizer.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ punctuation.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ syntax_iterators.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ es
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lemmatizer.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ punctuation.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ syntax_iterators.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ et
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ eu
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ punctuation.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ fa
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ generate_verbs_exc.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ punctuation.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ syntax_iterators.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ fi
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ punctuation.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ syntax_iterators.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ fo
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ fr
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lemmatizer.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ punctuation.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ syntax_iterators.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  ├─ _tokenizer_exceptions_list.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ ga
   │     │  │  │  ├─ lemmatizer.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ gd
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ grc
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ punctuation.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ gu
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ he
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ hi
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ hr
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lemma_lookup_license.txt
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ hsb
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ hu
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ punctuation.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ hy
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ id
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ punctuation.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ syntax_iterators.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  ├─ _tokenizer_exceptions_list.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ is
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ it
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lemmatizer.py
   │     │  │  │  ├─ punctuation.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ syntax_iterators.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ ja
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ syntax_iterators.py
   │     │  │  │  ├─ tag_bigram_map.py
   │     │  │  │  ├─ tag_map.py
   │     │  │  │  ├─ tag_orth_map.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ kmr
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ kn
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ ko
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ punctuation.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ tag_map.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ ky
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ punctuation.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ la
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ syntax_iterators.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ lb
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ punctuation.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ lex_attrs.py
   │     │  │  ├─ lg
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ punctuation.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ lij
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ punctuation.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ lt
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ punctuation.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ lv
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ mk
   │     │  │  │  ├─ lemmatizer.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ ml
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ mr
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ ms
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ punctuation.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ syntax_iterators.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  ├─ _tokenizer_exceptions_list.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ nb
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ punctuation.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ syntax_iterators.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ ne
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ nl
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lemmatizer.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ punctuation.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ syntax_iterators.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ nn
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ punctuation.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ norm_exceptions.py
   │     │  │  ├─ pl
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lemmatizer.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ punctuation.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ pt
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ punctuation.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ syntax_iterators.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ punctuation.py
   │     │  │  ├─ ro
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ punctuation.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ ru
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lemmatizer.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ sa
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ si
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ sk
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ sl
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ punctuation.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ sq
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ sr
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lemma_lookup_licence.txt
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ punctuation.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ sv
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ punctuation.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ syntax_iterators.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ ta
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ te
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ th
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ ti
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ punctuation.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ tl
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ tn
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ punctuation.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ tokenizer_exceptions.py
   │     │  │  ├─ tr
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ syntax_iterators.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ tt
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ punctuation.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ uk
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lemmatizer.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  ├─ tokenizer_exceptions.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ ur
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ punctuation.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ vi
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ xx
   │     │  │  │  ├─ examples.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ yo
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ zh
   │     │  │  │  ├─ examples.py
   │     │  │  │  ├─ lex_attrs.py
   │     │  │  │  ├─ stop_words.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ language.py
   │     │  ├─ lexeme.cp311-win_amd64.pyd
   │     │  ├─ lexeme.cpp
   │     │  ├─ lexeme.pxd
   │     │  ├─ lexeme.pyi
   │     │  ├─ lexeme.pyx
   │     │  ├─ lookups.py
   │     │  ├─ matcher
   │     │  │  ├─ dependencymatcher.cp311-win_amd64.pyd
   │     │  │  ├─ dependencymatcher.cpp
   │     │  │  ├─ dependencymatcher.pyi
   │     │  │  ├─ dependencymatcher.pyx
   │     │  │  ├─ levenshtein.c
   │     │  │  ├─ levenshtein.cp311-win_amd64.pyd
   │     │  │  ├─ levenshtein.pyx
   │     │  │  ├─ matcher.cp311-win_amd64.pyd
   │     │  │  ├─ matcher.cpp
   │     │  │  ├─ matcher.pxd
   │     │  │  ├─ matcher.pyi
   │     │  │  ├─ matcher.pyx
   │     │  │  ├─ phrasematcher.cp311-win_amd64.pyd
   │     │  │  ├─ phrasematcher.cpp
   │     │  │  ├─ phrasematcher.pxd
   │     │  │  ├─ phrasematcher.pyi
   │     │  │  ├─ phrasematcher.pyx
   │     │  │  ├─ polyleven.c
   │     │  │  └─ __init__.py
   │     │  ├─ ml
   │     │  │  ├─ callbacks.py
   │     │  │  ├─ extract_ngrams.py
   │     │  │  ├─ extract_spans.py
   │     │  │  ├─ featureextractor.py
   │     │  │  ├─ models
   │     │  │  │  ├─ entity_linker.py
   │     │  │  │  ├─ multi_task.py
   │     │  │  │  ├─ parser.py
   │     │  │  │  ├─ spancat.py
   │     │  │  │  ├─ span_finder.py
   │     │  │  │  ├─ tagger.py
   │     │  │  │  ├─ textcat.py
   │     │  │  │  ├─ tok2vec.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ parser_model.cp311-win_amd64.pyd
   │     │  │  ├─ parser_model.cpp
   │     │  │  ├─ parser_model.pxd
   │     │  │  ├─ parser_model.pyx
   │     │  │  ├─ staticvectors.py
   │     │  │  ├─ tb_framework.py
   │     │  │  ├─ _character_embed.py
   │     │  │  ├─ _precomputable_affine.py
   │     │  │  └─ __init__.py
   │     │  ├─ morphology.cp311-win_amd64.pyd
   │     │  ├─ morphology.cpp
   │     │  ├─ morphology.pxd
   │     │  ├─ morphology.pyx
   │     │  ├─ parts_of_speech.cp311-win_amd64.pyd
   │     │  ├─ parts_of_speech.cpp
   │     │  ├─ parts_of_speech.pxd
   │     │  ├─ parts_of_speech.pyx
   │     │  ├─ pipeline
   │     │  │  ├─ attributeruler.py
   │     │  │  ├─ dep_parser.cp311-win_amd64.pyd
   │     │  │  ├─ dep_parser.cpp
   │     │  │  ├─ dep_parser.pyx
   │     │  │  ├─ edit_tree_lemmatizer.py
   │     │  │  ├─ entityruler.py
   │     │  │  ├─ entity_linker.py
   │     │  │  ├─ functions.py
   │     │  │  ├─ legacy
   │     │  │  │  ├─ entity_linker.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ lemmatizer.py
   │     │  │  ├─ morphologizer.cp311-win_amd64.pyd
   │     │  │  ├─ morphologizer.cpp
   │     │  │  ├─ morphologizer.pyx
   │     │  │  ├─ multitask.cp311-win_amd64.pyd
   │     │  │  ├─ multitask.cpp
   │     │  │  ├─ multitask.pyx
   │     │  │  ├─ ner.cp311-win_amd64.pyd
   │     │  │  ├─ ner.cpp
   │     │  │  ├─ ner.pyx
   │     │  │  ├─ pipe.cp311-win_amd64.pyd
   │     │  │  ├─ pipe.cpp
   │     │  │  ├─ pipe.pxd
   │     │  │  ├─ pipe.pyi
   │     │  │  ├─ pipe.pyx
   │     │  │  ├─ sentencizer.cp311-win_amd64.pyd
   │     │  │  ├─ sentencizer.cpp
   │     │  │  ├─ sentencizer.pyx
   │     │  │  ├─ senter.cp311-win_amd64.pyd
   │     │  │  ├─ senter.cpp
   │     │  │  ├─ senter.pyx
   │     │  │  ├─ spancat.py
   │     │  │  ├─ span_finder.py
   │     │  │  ├─ span_ruler.py
   │     │  │  ├─ tagger.cp311-win_amd64.pyd
   │     │  │  ├─ tagger.cpp
   │     │  │  ├─ tagger.pyx
   │     │  │  ├─ textcat.py
   │     │  │  ├─ textcat_multilabel.py
   │     │  │  ├─ tok2vec.py
   │     │  │  ├─ trainable_pipe.cp311-win_amd64.pyd
   │     │  │  ├─ trainable_pipe.cpp
   │     │  │  ├─ trainable_pipe.pxd
   │     │  │  ├─ trainable_pipe.pyx
   │     │  │  ├─ transition_parser.cp311-win_amd64.pyd
   │     │  │  ├─ transition_parser.cpp
   │     │  │  ├─ transition_parser.pxd
   │     │  │  ├─ transition_parser.pyx
   │     │  │  ├─ _edit_tree_internals
   │     │  │  │  ├─ edit_trees.cp311-win_amd64.pyd
   │     │  │  │  ├─ edit_trees.cpp
   │     │  │  │  ├─ edit_trees.pxd
   │     │  │  │  ├─ edit_trees.pyx
   │     │  │  │  ├─ schemas.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _parser_internals
   │     │  │  │  ├─ arc_eager.cp311-win_amd64.pyd
   │     │  │  │  ├─ arc_eager.cpp
   │     │  │  │  ├─ arc_eager.pxd
   │     │  │  │  ├─ arc_eager.pyx
   │     │  │  │  ├─ ner.cp311-win_amd64.pyd
   │     │  │  │  ├─ ner.cpp
   │     │  │  │  ├─ ner.pxd
   │     │  │  │  ├─ ner.pyx
   │     │  │  │  ├─ nonproj.cp311-win_amd64.pyd
   │     │  │  │  ├─ nonproj.cpp
   │     │  │  │  ├─ nonproj.hh
   │     │  │  │  ├─ nonproj.pxd
   │     │  │  │  ├─ nonproj.pyx
   │     │  │  │  ├─ stateclass.cp311-win_amd64.pyd
   │     │  │  │  ├─ stateclass.cpp
   │     │  │  │  ├─ stateclass.pxd
   │     │  │  │  ├─ stateclass.pyx
   │     │  │  │  ├─ transition_system.cp311-win_amd64.pyd
   │     │  │  │  ├─ transition_system.cpp
   │     │  │  │  ├─ transition_system.pxd
   │     │  │  │  ├─ transition_system.pyx
   │     │  │  │  ├─ _beam_utils.cp311-win_amd64.pyd
   │     │  │  │  ├─ _beam_utils.cpp
   │     │  │  │  ├─ _beam_utils.pxd
   │     │  │  │  ├─ _beam_utils.pyx
   │     │  │  │  ├─ _state.cp311-win_amd64.pyd
   │     │  │  │  ├─ _state.cpp
   │     │  │  │  ├─ _state.pxd
   │     │  │  │  ├─ _state.pyx
   │     │  │  │  ├─ __init__.pxd
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ pipe_analysis.py
   │     │  ├─ py.typed
   │     │  ├─ schemas.py
   │     │  ├─ scorer.py
   │     │  ├─ strings.cp311-win_amd64.pyd
   │     │  ├─ strings.cpp
   │     │  ├─ strings.pxd
   │     │  ├─ strings.pyi
   │     │  ├─ strings.pyx
   │     │  ├─ structs.pxd
   │     │  ├─ symbols.cp311-win_amd64.pyd
   │     │  ├─ symbols.cpp
   │     │  ├─ symbols.pxd
   │     │  ├─ symbols.pyx
   │     │  ├─ tests
   │     │  │  ├─ conftest.py
   │     │  │  ├─ doc
   │     │  │  │  ├─ test_add_entities.py
   │     │  │  │  ├─ test_array.py
   │     │  │  │  ├─ test_creation.py
   │     │  │  │  ├─ test_doc_api.py
   │     │  │  │  ├─ test_graph.py
   │     │  │  │  ├─ test_json_doc_conversion.py
   │     │  │  │  ├─ test_morphanalysis.py
   │     │  │  │  ├─ test_pickle_doc.py
   │     │  │  │  ├─ test_retokenize_merge.py
   │     │  │  │  ├─ test_retokenize_split.py
   │     │  │  │  ├─ test_span.py
   │     │  │  │  ├─ test_span_group.py
   │     │  │  │  ├─ test_token_api.py
   │     │  │  │  ├─ test_underscore.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ enable_gpu.py
   │     │  │  ├─ lang
   │     │  │  │  ├─ af
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  ├─ test_tokenizer.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ am
   │     │  │  │  │  ├─ test_exception.py
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ ar
   │     │  │  │  │  ├─ test_exceptions.py
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ bn
   │     │  │  │  │  ├─ test_tokenizer.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ bo
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ ca
   │     │  │  │  │  ├─ test_exception.py
   │     │  │  │  │  ├─ test_prefix_suffix_infix.py
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ cs
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ da
   │     │  │  │  │  ├─ test_exceptions.py
   │     │  │  │  │  ├─ test_noun_chunks.py
   │     │  │  │  │  ├─ test_prefix_suffix_infix.py
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ de
   │     │  │  │  │  ├─ test_exceptions.py
   │     │  │  │  │  ├─ test_noun_chunks.py
   │     │  │  │  │  ├─ test_parser.py
   │     │  │  │  │  ├─ test_prefix_suffix_infix.py
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ dsb
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  ├─ test_tokenizer.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ el
   │     │  │  │  │  ├─ test_exception.py
   │     │  │  │  │  ├─ test_noun_chunks.py
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ en
   │     │  │  │  │  ├─ test_customized_tokenizer.py
   │     │  │  │  │  ├─ test_exceptions.py
   │     │  │  │  │  ├─ test_indices.py
   │     │  │  │  │  ├─ test_noun_chunks.py
   │     │  │  │  │  ├─ test_parser.py
   │     │  │  │  │  ├─ test_prefix_suffix_infix.py
   │     │  │  │  │  ├─ test_punct.py
   │     │  │  │  │  ├─ test_sbd.py
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  ├─ test_tokenizer.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ es
   │     │  │  │  │  ├─ test_exception.py
   │     │  │  │  │  ├─ test_noun_chunks.py
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ et
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  ├─ test_tokenizer.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ eu
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ fa
   │     │  │  │  │  ├─ test_noun_chunks.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ fi
   │     │  │  │  │  ├─ test_noun_chunks.py
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  ├─ test_tokenizer.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ fo
   │     │  │  │  │  ├─ test_tokenizer.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ fr
   │     │  │  │  │  ├─ test_exceptions.py
   │     │  │  │  │  ├─ test_noun_chunks.py
   │     │  │  │  │  ├─ test_prefix_suffix_infix.py
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ ga
   │     │  │  │  │  ├─ test_tokenizer.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ grc
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  ├─ test_tokenizer.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ gu
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ he
   │     │  │  │  │  ├─ test_tokenizer.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ hi
   │     │  │  │  │  ├─ test_lex_attrs.py
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ hr
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  ├─ test_tokenizer.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ hsb
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  ├─ test_tokenizer.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ hu
   │     │  │  │  │  ├─ test_tokenizer.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ hy
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  ├─ test_tokenizer.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ id
   │     │  │  │  │  ├─ test_noun_chunks.py
   │     │  │  │  │  ├─ test_prefix_suffix_infix.py
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ is
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  ├─ test_tokenizer.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ it
   │     │  │  │  │  ├─ test_noun_chunks.py
   │     │  │  │  │  ├─ test_prefix_suffix_infix.py
   │     │  │  │  │  ├─ test_stopwords.py
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ ja
   │     │  │  │  │  ├─ test_lemmatization.py
   │     │  │  │  │  ├─ test_morphologizer_factory.py
   │     │  │  │  │  ├─ test_serialize.py
   │     │  │  │  │  ├─ test_tokenizer.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ kmr
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ ko
   │     │  │  │  │  ├─ test_lemmatization.py
   │     │  │  │  │  ├─ test_serialize.py
   │     │  │  │  │  ├─ test_tokenizer.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ ky
   │     │  │  │  │  ├─ test_tokenizer.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ la
   │     │  │  │  │  ├─ test_exception.py
   │     │  │  │  │  ├─ test_noun_chunks.py
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ lb
   │     │  │  │  │  ├─ test_exceptions.py
   │     │  │  │  │  ├─ test_prefix_suffix_infix.py
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ lg
   │     │  │  │  │  ├─ test_tokenizer.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ lt
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ lv
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  ├─ test_tokenizer.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ mk
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ ml
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ ms
   │     │  │  │  │  ├─ test_noun_chunks.py
   │     │  │  │  │  ├─ test_prefix_suffix_infix.py
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ nb
   │     │  │  │  │  ├─ test_noun_chunks.py
   │     │  │  │  │  ├─ test_tokenizer.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ ne
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ nl
   │     │  │  │  │  ├─ test_noun_chunks.py
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ nn
   │     │  │  │  │  ├─ test_tokenizer.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ pl
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  ├─ test_tokenizer.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ pt
   │     │  │  │  │  ├─ test_noun_chunks.py
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ ro
   │     │  │  │  │  ├─ test_tokenizer.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ ru
   │     │  │  │  │  ├─ test_exceptions.py
   │     │  │  │  │  ├─ test_lemmatizer.py
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  ├─ test_tokenizer.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ sa
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ sk
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  ├─ test_tokenizer.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ sl
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  ├─ test_tokenizer.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ sq
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  ├─ test_tokenizer.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ sr
   │     │  │  │  │  ├─ test_exceptions.py
   │     │  │  │  │  ├─ test_tokenizer.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ sv
   │     │  │  │  │  ├─ test_exceptions.py
   │     │  │  │  │  ├─ test_lex_attrs.py
   │     │  │  │  │  ├─ test_noun_chunks.py
   │     │  │  │  │  ├─ test_prefix_suffix_infix.py
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  ├─ test_tokenizer.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ ta
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  ├─ test_tokenizer.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_attrs.py
   │     │  │  │  ├─ test_initialize.py
   │     │  │  │  ├─ test_lemmatizers.py
   │     │  │  │  ├─ th
   │     │  │  │  │  ├─ test_serialize.py
   │     │  │  │  │  ├─ test_tokenizer.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ ti
   │     │  │  │  │  ├─ test_exception.py
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ tl
   │     │  │  │  │  ├─ test_indices.py
   │     │  │  │  │  ├─ test_punct.py
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ tr
   │     │  │  │  │  ├─ test_noun_chunks.py
   │     │  │  │  │  ├─ test_parser.py
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  ├─ test_tokenizer.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ tt
   │     │  │  │  │  ├─ test_tokenizer.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ uk
   │     │  │  │  │  ├─ test_lemmatizer.py
   │     │  │  │  │  ├─ test_tokenizer.py
   │     │  │  │  │  ├─ test_tokenizer_exc.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ ur
   │     │  │  │  │  ├─ test_prefix_suffix_infix.py
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ vi
   │     │  │  │  │  ├─ test_serialize.py
   │     │  │  │  │  ├─ test_tokenizer.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ xx
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  ├─ test_tokenizer.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ yo
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ zh
   │     │  │  │  │  ├─ test_serialize.py
   │     │  │  │  │  ├─ test_text.py
   │     │  │  │  │  ├─ test_tokenizer.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ matcher
   │     │  │  │  ├─ test_dependency_matcher.py
   │     │  │  │  ├─ test_levenshtein.py
   │     │  │  │  ├─ test_matcher_api.py
   │     │  │  │  ├─ test_matcher_logic.py
   │     │  │  │  ├─ test_pattern_validation.py
   │     │  │  │  ├─ test_phrase_matcher.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ morphology
   │     │  │  │  ├─ test_morph_converters.py
   │     │  │  │  ├─ test_morph_features.py
   │     │  │  │  ├─ test_morph_pickle.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ package
   │     │  │  │  ├─ pyproject.toml
   │     │  │  │  ├─ requirements.txt
   │     │  │  │  ├─ setup.cfg
   │     │  │  │  ├─ test_requirements.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ parser
   │     │  │  │  ├─ test_add_label.py
   │     │  │  │  ├─ test_arc_eager_oracle.py
   │     │  │  │  ├─ test_ner.py
   │     │  │  │  ├─ test_neural_parser.py
   │     │  │  │  ├─ test_nn_beam.py
   │     │  │  │  ├─ test_nonproj.py
   │     │  │  │  ├─ test_parse.py
   │     │  │  │  ├─ test_parse_navigate.py
   │     │  │  │  ├─ test_preset_sbd.py
   │     │  │  │  ├─ test_space_attachment.py
   │     │  │  │  ├─ test_state.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ pipeline
   │     │  │  │  ├─ test_analysis.py
   │     │  │  │  ├─ test_annotates_on_update.py
   │     │  │  │  ├─ test_attributeruler.py
   │     │  │  │  ├─ test_edit_tree_lemmatizer.py
   │     │  │  │  ├─ test_entity_linker.py
   │     │  │  │  ├─ test_entity_ruler.py
   │     │  │  │  ├─ test_functions.py
   │     │  │  │  ├─ test_initialize.py
   │     │  │  │  ├─ test_lemmatizer.py
   │     │  │  │  ├─ test_models.py
   │     │  │  │  ├─ test_morphologizer.py
   │     │  │  │  ├─ test_pipe_factories.py
   │     │  │  │  ├─ test_pipe_methods.py
   │     │  │  │  ├─ test_sentencizer.py
   │     │  │  │  ├─ test_senter.py
   │     │  │  │  ├─ test_spancat.py
   │     │  │  │  ├─ test_span_finder.py
   │     │  │  │  ├─ test_span_ruler.py
   │     │  │  │  ├─ test_tagger.py
   │     │  │  │  ├─ test_textcat.py
   │     │  │  │  ├─ test_tok2vec.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ serialize
   │     │  │  │  ├─ test_resource_warning.py
   │     │  │  │  ├─ test_serialize_config.py
   │     │  │  │  ├─ test_serialize_doc.py
   │     │  │  │  ├─ test_serialize_docbin.py
   │     │  │  │  ├─ test_serialize_extension_attrs.py
   │     │  │  │  ├─ test_serialize_kb.py
   │     │  │  │  ├─ test_serialize_language.py
   │     │  │  │  ├─ test_serialize_pipeline.py
   │     │  │  │  ├─ test_serialize_span_groups.py
   │     │  │  │  ├─ test_serialize_tokenizer.py
   │     │  │  │  ├─ test_serialize_vocab_strings.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ test_architectures.py
   │     │  │  ├─ test_cli.py
   │     │  │  ├─ test_cli_app.py
   │     │  │  ├─ test_displacy.py
   │     │  │  ├─ test_errors.py
   │     │  │  ├─ test_language.py
   │     │  │  ├─ test_misc.py
   │     │  │  ├─ test_models.py
   │     │  │  ├─ test_pickles.py
   │     │  │  ├─ test_scorer.py
   │     │  │  ├─ test_ty.py
   │     │  │  ├─ tok2vec.py
   │     │  │  ├─ tokenizer
   │     │  │  │  ├─ sun.txt
   │     │  │  │  ├─ test_exceptions.py
   │     │  │  │  ├─ test_explain.py
   │     │  │  │  ├─ test_naughty_strings.py
   │     │  │  │  ├─ test_tokenizer.py
   │     │  │  │  ├─ test_urls.py
   │     │  │  │  ├─ test_whitespace.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ training
   │     │  │  │  ├─ test_augmenters.py
   │     │  │  │  ├─ test_corpus.py
   │     │  │  │  ├─ test_logger.py
   │     │  │  │  ├─ test_new_example.py
   │     │  │  │  ├─ test_pretraining.py
   │     │  │  │  ├─ test_readers.py
   │     │  │  │  ├─ test_rehearse.py
   │     │  │  │  ├─ test_training.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ util.py
   │     │  │  ├─ vocab_vectors
   │     │  │  │  ├─ test_lexeme.py
   │     │  │  │  ├─ test_lookups.py
   │     │  │  │  ├─ test_memory_zone.py
   │     │  │  │  ├─ test_similarity.py
   │     │  │  │  ├─ test_stringstore.py
   │     │  │  │  ├─ test_vectors.py
   │     │  │  │  ├─ test_vocab_api.py
   │     │  │  │  └─ __init__.py
   │     │  │  └─ __init__.py
   │     │  ├─ tokenizer.cp311-win_amd64.pyd
   │     │  ├─ tokenizer.cpp
   │     │  ├─ tokenizer.pxd
   │     │  ├─ tokenizer.pyx
   │     │  ├─ tokens
   │     │  │  ├─ doc.cp311-win_amd64.pyd
   │     │  │  ├─ doc.cpp
   │     │  │  ├─ doc.pxd
   │     │  │  ├─ doc.pyi
   │     │  │  ├─ doc.pyx
   │     │  │  ├─ graph.cp311-win_amd64.pyd
   │     │  │  ├─ graph.cpp
   │     │  │  ├─ graph.pxd
   │     │  │  ├─ graph.pyx
   │     │  │  ├─ morphanalysis.cp311-win_amd64.pyd
   │     │  │  ├─ morphanalysis.cpp
   │     │  │  ├─ morphanalysis.pxd
   │     │  │  ├─ morphanalysis.pyi
   │     │  │  ├─ morphanalysis.pyx
   │     │  │  ├─ span.cp311-win_amd64.pyd
   │     │  │  ├─ span.cpp
   │     │  │  ├─ span.pxd
   │     │  │  ├─ span.pyi
   │     │  │  ├─ span.pyx
   │     │  │  ├─ span_group.cp311-win_amd64.pyd
   │     │  │  ├─ span_group.cpp
   │     │  │  ├─ span_group.pxd
   │     │  │  ├─ span_group.pyi
   │     │  │  ├─ span_group.pyx
   │     │  │  ├─ token.cp311-win_amd64.pyd
   │     │  │  ├─ token.cpp
   │     │  │  ├─ token.pxd
   │     │  │  ├─ token.pyi
   │     │  │  ├─ token.pyx
   │     │  │  ├─ underscore.py
   │     │  │  ├─ _dict_proxies.py
   │     │  │  ├─ _retokenize.cp311-win_amd64.pyd
   │     │  │  ├─ _retokenize.cpp
   │     │  │  ├─ _retokenize.pyi
   │     │  │  ├─ _retokenize.pyx
   │     │  │  ├─ _serialize.py
   │     │  │  ├─ __init__.pxd
   │     │  │  └─ __init__.py
   │     │  ├─ training
   │     │  │  ├─ align.cp311-win_amd64.pyd
   │     │  │  ├─ align.cpp
   │     │  │  ├─ align.pyx
   │     │  │  ├─ alignment.py
   │     │  │  ├─ alignment_array.cp311-win_amd64.pyd
   │     │  │  ├─ alignment_array.cpp
   │     │  │  ├─ alignment_array.pxd
   │     │  │  ├─ alignment_array.pyx
   │     │  │  ├─ augment.py
   │     │  │  ├─ batchers.py
   │     │  │  ├─ callbacks.py
   │     │  │  ├─ converters
   │     │  │  │  ├─ conllu_to_docs.py
   │     │  │  │  ├─ conll_ner_to_docs.py
   │     │  │  │  ├─ iob_to_docs.py
   │     │  │  │  ├─ json_to_docs.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ corpus.py
   │     │  │  ├─ example.cp311-win_amd64.pyd
   │     │  │  ├─ example.cpp
   │     │  │  ├─ example.pxd
   │     │  │  ├─ example.pyi
   │     │  │  ├─ example.pyx
   │     │  │  ├─ gold_io.cp311-win_amd64.pyd
   │     │  │  ├─ gold_io.cpp
   │     │  │  ├─ gold_io.pyx
   │     │  │  ├─ initialize.py
   │     │  │  ├─ iob_utils.py
   │     │  │  ├─ loggers.py
   │     │  │  ├─ loop.py
   │     │  │  ├─ pretrain.py
   │     │  │  ├─ __init__.pxd
   │     │  │  └─ __init__.py
   │     │  ├─ ty.py
   │     │  ├─ typedefs.pxd
   │     │  ├─ typedefs.pyx
   │     │  ├─ util.py
   │     │  ├─ vectors.cp311-win_amd64.pyd
   │     │  ├─ vectors.cpp
   │     │  ├─ vectors.pyx
   │     │  ├─ vocab.cp311-win_amd64.pyd
   │     │  ├─ vocab.cpp
   │     │  ├─ vocab.pxd
   │     │  ├─ vocab.pyi
   │     │  ├─ vocab.pyx
   │     │  ├─ __init__.pxd
   │     │  ├─ __init__.py
   │     │  └─ __main__.py
   │     ├─ spacy-3.8.4.dist-info
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ spacy_legacy
   │     │  ├─ architectures
   │     │  │  ├─ entity_linker.py
   │     │  │  ├─ parser.py
   │     │  │  ├─ tagger.py
   │     │  │  ├─ textcat.py
   │     │  │  ├─ tok2vec.py
   │     │  │  └─ __init__.py
   │     │  ├─ components
   │     │  │  ├─ entity_linker.py
   │     │  │  └─ __init__.py
   │     │  ├─ layers
   │     │  │  ├─ staticvectors_v1.py
   │     │  │  └─ __init__.py
   │     │  ├─ loggers.py
   │     │  ├─ scorers.py
   │     │  ├─ tests
   │     │  │  ├─ parser
   │     │  │  │  ├─ test_parser.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ pipeline
   │     │  │  │  ├─ test_tagger.py
   │     │  │  │  ├─ test_textcat.py
   │     │  │  │  ├─ test_tok2vec.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ test_layer.py
   │     │  │  ├─ test_legacy.py
   │     │  │  ├─ test_logger.py
   │     │  │  ├─ test_scorers.py
   │     │  │  └─ __init__.py
   │     │  └─ __init__.py
   │     ├─ spacy_legacy-3.0.12.dist-info
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  ├─ WHEEL
   │     │  └─ zip-safe
   │     ├─ spacy_loggers
   │     │  ├─ chain.py
   │     │  ├─ clearml.py
   │     │  ├─ cupy.py
   │     │  ├─ lookup.py
   │     │  ├─ mlflow.py
   │     │  ├─ pytorch.py
   │     │  ├─ tests
   │     │  │  ├─ test_chain.py
   │     │  │  ├─ test_cupy.py
   │     │  │  ├─ test_lookup.py
   │     │  │  ├─ test_registry.py
   │     │  │  ├─ util.py
   │     │  │  └─ __init__.py
   │     │  ├─ util.py
   │     │  ├─ wandb.py
   │     │  └─ __init__.py
   │     ├─ spacy_loggers-1.0.5.dist-info
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  ├─ WHEEL
   │     │  └─ zip-safe
   │     ├─ srsly
   │     │  ├─ about.py
   │     │  ├─ cloudpickle
   │     │  │  ├─ cloudpickle.py
   │     │  │  ├─ cloudpickle_fast.py
   │     │  │  ├─ compat.py
   │     │  │  └─ __init__.py
   │     │  ├─ msgpack
   │     │  │  ├─ exceptions.py
   │     │  │  ├─ ext.py
   │     │  │  ├─ fallback.py
   │     │  │  ├─ pack.h
   │     │  │  ├─ pack_template.h
   │     │  │  ├─ sysdep.h
   │     │  │  ├─ unpack.h
   │     │  │  ├─ unpack_container_header.h
   │     │  │  ├─ unpack_define.h
   │     │  │  ├─ unpack_template.h
   │     │  │  ├─ util.py
   │     │  │  ├─ _epoch.cp311-win_amd64.pyd
   │     │  │  ├─ _epoch.cpp
   │     │  │  ├─ _epoch.pyx
   │     │  │  ├─ _msgpack_numpy.py
   │     │  │  ├─ _packer.cp311-win_amd64.pyd
   │     │  │  ├─ _packer.cpp
   │     │  │  ├─ _packer.pyx
   │     │  │  ├─ _unpacker.cp311-win_amd64.pyd
   │     │  │  ├─ _unpacker.cpp
   │     │  │  ├─ _unpacker.pyx
   │     │  │  ├─ _version.py
   │     │  │  └─ __init__.py
   │     │  ├─ ruamel_yaml
   │     │  │  ├─ anchor.py
   │     │  │  ├─ comments.py
   │     │  │  ├─ compat.py
   │     │  │  ├─ composer.py
   │     │  │  ├─ configobjwalker.py
   │     │  │  ├─ constructor.py
   │     │  │  ├─ cyaml.py
   │     │  │  ├─ dumper.py
   │     │  │  ├─ emitter.py
   │     │  │  ├─ error.py
   │     │  │  ├─ events.py
   │     │  │  ├─ loader.py
   │     │  │  ├─ main.py
   │     │  │  ├─ nodes.py
   │     │  │  ├─ parser.py
   │     │  │  ├─ py.typed
   │     │  │  ├─ reader.py
   │     │  │  ├─ representer.py
   │     │  │  ├─ resolver.py
   │     │  │  ├─ scalarbool.py
   │     │  │  ├─ scalarfloat.py
   │     │  │  ├─ scalarint.py
   │     │  │  ├─ scalarstring.py
   │     │  │  ├─ scanner.py
   │     │  │  ├─ serializer.py
   │     │  │  ├─ timestamp.py
   │     │  │  ├─ tokens.py
   │     │  │  ├─ util.py
   │     │  │  └─ __init__.py
   │     │  ├─ tests
   │     │  │  ├─ cloudpickle
   │     │  │  │  ├─ cloudpickle_file_test.py
   │     │  │  │  ├─ cloudpickle_test.py
   │     │  │  │  ├─ testutils.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ msgpack
   │     │  │  │  ├─ test_buffer.py
   │     │  │  │  ├─ test_case.py
   │     │  │  │  ├─ test_except.py
   │     │  │  │  ├─ test_extension.py
   │     │  │  │  ├─ test_format.py
   │     │  │  │  ├─ test_limits.py
   │     │  │  │  ├─ test_memoryview.py
   │     │  │  │  ├─ test_newspec.py
   │     │  │  │  ├─ test_numpy.py
   │     │  │  │  ├─ test_pack.py
   │     │  │  │  ├─ test_read_size.py
   │     │  │  │  ├─ test_seq.py
   │     │  │  │  ├─ test_sequnpack.py
   │     │  │  │  ├─ test_stricttype.py
   │     │  │  │  ├─ test_subtype.py
   │     │  │  │  ├─ test_unpack.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ ruamel_yaml
   │     │  │  │  ├─ roundtrip.py
   │     │  │  │  ├─ test_add_xxx.py
   │     │  │  │  ├─ test_anchor.py
   │     │  │  │  ├─ test_api_change.py
   │     │  │  │  ├─ test_appliance.py
   │     │  │  │  ├─ test_a_dedent.py
   │     │  │  │  ├─ test_class_register.py
   │     │  │  │  ├─ test_collections.py
   │     │  │  │  ├─ test_comments.py
   │     │  │  │  ├─ test_comment_manipulation.py
   │     │  │  │  ├─ test_contextmanager.py
   │     │  │  │  ├─ test_copy.py
   │     │  │  │  ├─ test_datetime.py
   │     │  │  │  ├─ test_deprecation.py
   │     │  │  │  ├─ test_documents.py
   │     │  │  │  ├─ test_fail.py
   │     │  │  │  ├─ test_float.py
   │     │  │  │  ├─ test_flowsequencekey.py
   │     │  │  │  ├─ test_indentation.py
   │     │  │  │  ├─ test_int.py
   │     │  │  │  ├─ test_issues.py
   │     │  │  │  ├─ test_json_numbers.py
   │     │  │  │  ├─ test_line_col.py
   │     │  │  │  ├─ test_literal.py
   │     │  │  │  ├─ test_none.py
   │     │  │  │  ├─ test_numpy.py
   │     │  │  │  ├─ test_program_config.py
   │     │  │  │  ├─ test_spec_examples.py
   │     │  │  │  ├─ test_string.py
   │     │  │  │  ├─ test_tag.py
   │     │  │  │  ├─ test_version.py
   │     │  │  │  ├─ test_yamlfile.py
   │     │  │  │  ├─ test_yamlobject.py
   │     │  │  │  ├─ test_z_check_debug_leftovers.py
   │     │  │  │  ├─ test_z_data.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ test_json_api.py
   │     │  │  ├─ test_msgpack_api.py
   │     │  │  ├─ test_pickle_api.py
   │     │  │  ├─ test_yaml_api.py
   │     │  │  ├─ ujson
   │     │  │  │  ├─ 334-reproducer.json
   │     │  │  │  ├─ test_ujson.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ util.py
   │     │  │  └─ __init__.py
   │     │  ├─ ujson
   │     │  │  ├─ JSONtoObj.c
   │     │  │  ├─ lib
   │     │  │  │  ├─ dconv_wrapper.cc
   │     │  │  │  ├─ ultrajson.h
   │     │  │  │  ├─ ultrajsondec.c
   │     │  │  │  └─ ultrajsonenc.c
   │     │  │  ├─ objToJSON.c
   │     │  │  ├─ py_defines.h
   │     │  │  ├─ ujson.c
   │     │  │  ├─ ujson.cp311-win_amd64.pyd
   │     │  │  ├─ version.h
   │     │  │  └─ __init__.py
   │     │  ├─ util.py
   │     │  ├─ _json_api.py
   │     │  ├─ _msgpack_api.py
   │     │  ├─ _pickle_api.py
   │     │  ├─ _yaml_api.py
   │     │  └─ __init__.py
   │     ├─ srsly-2.5.1.dist-info
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  ├─ WHEEL
   │     │  └─ zip-safe
   │     ├─ thinc
   │     │  ├─ about.py
   │     │  ├─ api.py
   │     │  ├─ backends
   │     │  │  ├─ cblas.cp311-win_amd64.pyd
   │     │  │  ├─ cblas.cpp
   │     │  │  ├─ cblas.pxd
   │     │  │  ├─ cblas.pyx
   │     │  │  ├─ cpu_kernels.hh
   │     │  │  ├─ cupy_ops.py
   │     │  │  ├─ linalg.cp311-win_amd64.pyd
   │     │  │  ├─ linalg.cpp
   │     │  │  ├─ linalg.pxd
   │     │  │  ├─ linalg.pyx
   │     │  │  ├─ mps_ops.py
   │     │  │  ├─ numpy_ops.cp311-win_amd64.pyd
   │     │  │  ├─ numpy_ops.cpp
   │     │  │  ├─ numpy_ops.pxd
   │     │  │  ├─ numpy_ops.pyx
   │     │  │  ├─ ops.py
   │     │  │  ├─ _cupy_allocators.py
   │     │  │  ├─ _custom_kernels.cu
   │     │  │  ├─ _custom_kernels.py
   │     │  │  ├─ _murmur3.cu
   │     │  │  ├─ _param_server.py
   │     │  │  ├─ __init__.pxd
   │     │  │  └─ __init__.py
   │     │  ├─ compat.py
   │     │  ├─ config.py
   │     │  ├─ extra
   │     │  │  ├─ search.cp311-win_amd64.pyd
   │     │  │  ├─ search.cpp
   │     │  │  ├─ search.pxd
   │     │  │  ├─ search.pyx
   │     │  │  ├─ tests
   │     │  │  │  ├─ c_test_search.pyx
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ __init__.pxd
   │     │  │  └─ __init__.py
   │     │  ├─ initializers.py
   │     │  ├─ layers
   │     │  │  ├─ add.py
   │     │  │  ├─ array_getitem.py
   │     │  │  ├─ bidirectional.py
   │     │  │  ├─ cauchysimilarity.py
   │     │  │  ├─ chain.py
   │     │  │  ├─ clipped_linear.py
   │     │  │  ├─ clone.py
   │     │  │  ├─ concatenate.py
   │     │  │  ├─ dish.py
   │     │  │  ├─ dropout.py
   │     │  │  ├─ embed.py
   │     │  │  ├─ expand_window.py
   │     │  │  ├─ gelu.py
   │     │  │  ├─ hard_swish.py
   │     │  │  ├─ hard_swish_mobilenet.py
   │     │  │  ├─ hashembed.py
   │     │  │  ├─ layernorm.py
   │     │  │  ├─ linear.py
   │     │  │  ├─ list2array.py
   │     │  │  ├─ list2padded.py
   │     │  │  ├─ list2ragged.py
   │     │  │  ├─ logistic.py
   │     │  │  ├─ lstm.py
   │     │  │  ├─ map_list.py
   │     │  │  ├─ maxout.py
   │     │  │  ├─ mish.py
   │     │  │  ├─ multisoftmax.py
   │     │  │  ├─ mxnetwrapper.py
   │     │  │  ├─ noop.py
   │     │  │  ├─ padded2list.py
   │     │  │  ├─ parametricattention.py
   │     │  │  ├─ parametricattention_v2.py
   │     │  │  ├─ premap_ids.cp311-win_amd64.pyd
   │     │  │  ├─ premap_ids.cpp
   │     │  │  ├─ premap_ids.pyx
   │     │  │  ├─ pytorchwrapper.py
   │     │  │  ├─ ragged2list.py
   │     │  │  ├─ reduce_first.py
   │     │  │  ├─ reduce_last.py
   │     │  │  ├─ reduce_max.py
   │     │  │  ├─ reduce_mean.py
   │     │  │  ├─ reduce_sum.py
   │     │  │  ├─ relu.py
   │     │  │  ├─ remap_ids.py
   │     │  │  ├─ residual.py
   │     │  │  ├─ resizable.py
   │     │  │  ├─ siamese.py
   │     │  │  ├─ sigmoid.py
   │     │  │  ├─ sigmoid_activation.py
   │     │  │  ├─ softmax.py
   │     │  │  ├─ softmax_activation.py
   │     │  │  ├─ sparselinear.cp311-win_amd64.pyd
   │     │  │  ├─ sparselinear.cpp
   │     │  │  ├─ sparselinear.pyx
   │     │  │  ├─ strings2arrays.py
   │     │  │  ├─ swish.py
   │     │  │  ├─ tensorflowwrapper.py
   │     │  │  ├─ torchscriptwrapper.py
   │     │  │  ├─ tuplify.py
   │     │  │  ├─ uniqued.py
   │     │  │  ├─ with_array.py
   │     │  │  ├─ with_array2d.py
   │     │  │  ├─ with_cpu.py
   │     │  │  ├─ with_debug.py
   │     │  │  ├─ with_flatten.py
   │     │  │  ├─ with_flatten_v2.py
   │     │  │  ├─ with_getitem.py
   │     │  │  ├─ with_list.py
   │     │  │  ├─ with_nvtx_range.py
   │     │  │  ├─ with_padded.py
   │     │  │  ├─ with_ragged.py
   │     │  │  ├─ with_reshape.py
   │     │  │  ├─ with_signpost_interval.py
   │     │  │  └─ __init__.py
   │     │  ├─ loss.py
   │     │  ├─ model.py
   │     │  ├─ mypy.py
   │     │  ├─ optimizers.py
   │     │  ├─ py.typed
   │     │  ├─ schedules.py
   │     │  ├─ shims
   │     │  │  ├─ mxnet.py
   │     │  │  ├─ pytorch.py
   │     │  │  ├─ pytorch_grad_scaler.py
   │     │  │  ├─ shim.py
   │     │  │  ├─ tensorflow.py
   │     │  │  ├─ torchscript.py
   │     │  │  └─ __init__.py
   │     │  ├─ tests
   │     │  │  ├─ backends
   │     │  │  │  ├─ test_mem.py
   │     │  │  │  ├─ test_ops.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ conftest.py
   │     │  │  ├─ enable_mxnet.py
   │     │  │  ├─ enable_tensorflow.py
   │     │  │  ├─ extra
   │     │  │  │  ├─ test_beam_search.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ layers
   │     │  │  │  ├─ test_basic_tagger.py
   │     │  │  │  ├─ test_combinators.py
   │     │  │  │  ├─ test_feed_forward.py
   │     │  │  │  ├─ test_hash_embed.py
   │     │  │  │  ├─ test_layers_api.py
   │     │  │  │  ├─ test_linear.py
   │     │  │  │  ├─ test_lstm.py
   │     │  │  │  ├─ test_mappers.py
   │     │  │  │  ├─ test_mnist.py
   │     │  │  │  ├─ test_mxnet_wrapper.py
   │     │  │  │  ├─ test_parametric_attention_v2.py
   │     │  │  │  ├─ test_pytorch_wrapper.py
   │     │  │  │  ├─ test_reduce.py
   │     │  │  │  ├─ test_resizable.py
   │     │  │  │  ├─ test_shim.py
   │     │  │  │  ├─ test_softmax.py
   │     │  │  │  ├─ test_sparse_linear.py
   │     │  │  │  ├─ test_tensorflow_wrapper.py
   │     │  │  │  ├─ test_torchscriptwrapper.py
   │     │  │  │  ├─ test_transforms.py
   │     │  │  │  ├─ test_uniqued.py
   │     │  │  │  ├─ test_with_debug.py
   │     │  │  │  ├─ test_with_flatten.py
   │     │  │  │  ├─ test_with_transforms.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ model
   │     │  │  │  ├─ test_model.py
   │     │  │  │  ├─ test_validation.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ mypy
   │     │  │  │  ├─ configs
   │     │  │  │  │  ├─ mypy-default.ini
   │     │  │  │  │  └─ mypy-plugin.ini
   │     │  │  │  ├─ modules
   │     │  │  │  │  ├─ fail_no_plugin.py
   │     │  │  │  │  ├─ fail_plugin.py
   │     │  │  │  │  ├─ success_no_plugin.py
   │     │  │  │  │  ├─ success_plugin.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ outputs
   │     │  │  │  │  ├─ fail-no-plugin.txt
   │     │  │  │  │  ├─ fail-plugin.txt
   │     │  │  │  │  ├─ success-no-plugin.txt
   │     │  │  │  │  └─ success-plugin.txt
   │     │  │  │  ├─ test_mypy.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ regression
   │     │  │  │  ├─ issue519
   │     │  │  │  │  ├─ program.py
   │     │  │  │  │  ├─ test_issue519.py
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ test_issue208.py
   │     │  │  │  ├─ test_issue564.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ shims
   │     │  │  │  ├─ test_pytorch_grad_scaler.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ strategies.py
   │     │  │  ├─ test_config.py
   │     │  │  ├─ test_examples.py
   │     │  │  ├─ test_import__all__.py
   │     │  │  ├─ test_indexing.py
   │     │  │  ├─ test_initializers.py
   │     │  │  ├─ test_loss.py
   │     │  │  ├─ test_optimizers.py
   │     │  │  ├─ test_schedules.py
   │     │  │  ├─ test_serialize.py
   │     │  │  ├─ test_types.py
   │     │  │  ├─ test_util.py
   │     │  │  ├─ util.py
   │     │  │  └─ __init__.py
   │     │  ├─ types.py
   │     │  ├─ util.py
   │     │  ├─ __init__.pxd
   │     │  └─ __init__.py
   │     ├─ thinc-8.3.4.dist-info
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ threadpoolctl-3.6.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  └─ WHEEL
   │     ├─ threadpoolctl.py
   │     ├─ tqdm
   │     │  ├─ asyncio.py
   │     │  ├─ auto.py
   │     │  ├─ autonotebook.py
   │     │  ├─ cli.py
   │     │  ├─ completion.sh
   │     │  ├─ contrib
   │     │  │  ├─ bells.py
   │     │  │  ├─ concurrent.py
   │     │  │  ├─ discord.py
   │     │  │  ├─ itertools.py
   │     │  │  ├─ logging.py
   │     │  │  ├─ slack.py
   │     │  │  ├─ telegram.py
   │     │  │  ├─ utils_worker.py
   │     │  │  └─ __init__.py
   │     │  ├─ dask.py
   │     │  ├─ gui.py
   │     │  ├─ keras.py
   │     │  ├─ notebook.py
   │     │  ├─ rich.py
   │     │  ├─ std.py
   │     │  ├─ tk.py
   │     │  ├─ tqdm.1
   │     │  ├─ utils.py
   │     │  ├─ version.py
   │     │  ├─ _dist_ver.py
   │     │  ├─ _main.py
   │     │  ├─ _monitor.py
   │     │  ├─ _tqdm.py
   │     │  ├─ _tqdm_gui.py
   │     │  ├─ _tqdm_notebook.py
   │     │  ├─ _tqdm_pandas.py
   │     │  ├─ _utils.py
   │     │  ├─ __init__.py
   │     │  └─ __main__.py
   │     ├─ tqdm-4.67.1.dist-info
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ LICENCE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ trio
   │     │  ├─ abc.py
   │     │  ├─ from_thread.py
   │     │  ├─ lowlevel.py
   │     │  ├─ py.typed
   │     │  ├─ socket.py
   │     │  ├─ testing
   │     │  │  ├─ _checkpoints.py
   │     │  │  ├─ _check_streams.py
   │     │  │  ├─ _fake_net.py
   │     │  │  ├─ _memory_streams.py
   │     │  │  ├─ _network.py
   │     │  │  ├─ _raises_group.py
   │     │  │  ├─ _sequencer.py
   │     │  │  ├─ _trio_test.py
   │     │  │  └─ __init__.py
   │     │  ├─ to_thread.py
   │     │  ├─ _abc.py
   │     │  ├─ _channel.py
   │     │  ├─ _core
   │     │  │  ├─ _asyncgens.py
   │     │  │  ├─ _concat_tb.py
   │     │  │  ├─ _entry_queue.py
   │     │  │  ├─ _exceptions.py
   │     │  │  ├─ _generated_instrumentation.py
   │     │  │  ├─ _generated_io_epoll.py
   │     │  │  ├─ _generated_io_kqueue.py
   │     │  │  ├─ _generated_io_windows.py
   │     │  │  ├─ _generated_run.py
   │     │  │  ├─ _instrumentation.py
   │     │  │  ├─ _io_common.py
   │     │  │  ├─ _io_epoll.py
   │     │  │  ├─ _io_kqueue.py
   │     │  │  ├─ _io_windows.py
   │     │  │  ├─ _ki.py
   │     │  │  ├─ _local.py
   │     │  │  ├─ _mock_clock.py
   │     │  │  ├─ _parking_lot.py
   │     │  │  ├─ _run.py
   │     │  │  ├─ _run_context.py
   │     │  │  ├─ _tests
   │     │  │  │  ├─ test_asyncgen.py
   │     │  │  │  ├─ test_exceptiongroup_gc.py
   │     │  │  │  ├─ test_guest_mode.py
   │     │  │  │  ├─ test_instrumentation.py
   │     │  │  │  ├─ test_io.py
   │     │  │  │  ├─ test_ki.py
   │     │  │  │  ├─ test_local.py
   │     │  │  │  ├─ test_mock_clock.py
   │     │  │  │  ├─ test_parking_lot.py
   │     │  │  │  ├─ test_run.py
   │     │  │  │  ├─ test_thread_cache.py
   │     │  │  │  ├─ test_tutil.py
   │     │  │  │  ├─ test_unbounded_queue.py
   │     │  │  │  ├─ test_windows.py
   │     │  │  │  ├─ tutil.py
   │     │  │  │  ├─ type_tests
   │     │  │  │  │  ├─ nursery_start.py
   │     │  │  │  │  └─ run.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ _thread_cache.py
   │     │  │  ├─ _traps.py
   │     │  │  ├─ _unbounded_queue.py
   │     │  │  ├─ _wakeup_socketpair.py
   │     │  │  ├─ _windows_cffi.py
   │     │  │  └─ __init__.py
   │     │  ├─ _deprecate.py
   │     │  ├─ _dtls.py
   │     │  ├─ _file_io.py
   │     │  ├─ _highlevel_generic.py
   │     │  ├─ _highlevel_open_tcp_listeners.py
   │     │  ├─ _highlevel_open_tcp_stream.py
   │     │  ├─ _highlevel_open_unix_stream.py
   │     │  ├─ _highlevel_serve_listeners.py
   │     │  ├─ _highlevel_socket.py
   │     │  ├─ _highlevel_ssl_helpers.py
   │     │  ├─ _path.py
   │     │  ├─ _repl.py
   │     │  ├─ _signals.py
   │     │  ├─ _socket.py
   │     │  ├─ _ssl.py
   │     │  ├─ _subprocess.py
   │     │  ├─ _subprocess_platform
   │     │  │  ├─ kqueue.py
   │     │  │  ├─ waitid.py
   │     │  │  ├─ windows.py
   │     │  │  └─ __init__.py
   │     │  ├─ _sync.py
   │     │  ├─ _tests
   │     │  │  ├─ astrill-codesigning-cert.cer
   │     │  │  ├─ check_type_completeness.py
   │     │  │  ├─ module_with_deprecations.py
   │     │  │  ├─ pytest_plugin.py
   │     │  │  ├─ test_abc.py
   │     │  │  ├─ test_channel.py
   │     │  │  ├─ test_contextvars.py
   │     │  │  ├─ test_deprecate.py
   │     │  │  ├─ test_deprecate_strict_exception_groups_false.py
   │     │  │  ├─ test_dtls.py
   │     │  │  ├─ test_exports.py
   │     │  │  ├─ test_fakenet.py
   │     │  │  ├─ test_file_io.py
   │     │  │  ├─ test_highlevel_generic.py
   │     │  │  ├─ test_highlevel_open_tcp_listeners.py
   │     │  │  ├─ test_highlevel_open_tcp_stream.py
   │     │  │  ├─ test_highlevel_open_unix_stream.py
   │     │  │  ├─ test_highlevel_serve_listeners.py
   │     │  │  ├─ test_highlevel_socket.py
   │     │  │  ├─ test_highlevel_ssl_helpers.py
   │     │  │  ├─ test_path.py
   │     │  │  ├─ test_repl.py
   │     │  │  ├─ test_scheduler_determinism.py
   │     │  │  ├─ test_signals.py
   │     │  │  ├─ test_socket.py
   │     │  │  ├─ test_ssl.py
   │     │  │  ├─ test_subprocess.py
   │     │  │  ├─ test_sync.py
   │     │  │  ├─ test_testing.py
   │     │  │  ├─ test_testing_raisesgroup.py
   │     │  │  ├─ test_threads.py
   │     │  │  ├─ test_timeouts.py
   │     │  │  ├─ test_tracing.py
   │     │  │  ├─ test_trio.py
   │     │  │  ├─ test_unix_pipes.py
   │     │  │  ├─ test_util.py
   │     │  │  ├─ test_wait_for_object.py
   │     │  │  ├─ test_windows_pipes.py
   │     │  │  ├─ tools
   │     │  │  │  ├─ test_gen_exports.py
   │     │  │  │  ├─ test_mypy_annotate.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ type_tests
   │     │  │  │  ├─ check_wraps.py
   │     │  │  │  ├─ open_memory_channel.py
   │     │  │  │  ├─ path.py
   │     │  │  │  ├─ raisesgroup.py
   │     │  │  │  └─ task_status.py
   │     │  │  └─ __init__.py
   │     │  ├─ _threads.py
   │     │  ├─ _timeouts.py
   │     │  ├─ _tools
   │     │  │  ├─ gen_exports.py
   │     │  │  ├─ mypy_annotate.py
   │     │  │  └─ __init__.py
   │     │  ├─ _unix_pipes.py
   │     │  ├─ _util.py
   │     │  ├─ _version.py
   │     │  ├─ _wait_for_object.py
   │     │  ├─ _windows_pipes.py
   │     │  ├─ __init__.py
   │     │  └─ __main__.py
   │     ├─ trio-0.29.0.dist-info
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ LICENSE.APACHE2
   │     │  ├─ LICENSE.MIT
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ trio_websocket
   │     │  ├─ py.typed
   │     │  ├─ _impl.py
   │     │  ├─ _version.py
   │     │  └─ __init__.py
   │     ├─ trio_websocket-0.12.2.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ typer
   │     │  ├─ cli.py
   │     │  ├─ colors.py
   │     │  ├─ completion.py
   │     │  ├─ core.py
   │     │  ├─ main.py
   │     │  ├─ models.py
   │     │  ├─ params.py
   │     │  ├─ py.typed
   │     │  ├─ rich_utils.py
   │     │  ├─ testing.py
   │     │  ├─ utils.py
   │     │  ├─ _completion_classes.py
   │     │  ├─ _completion_shared.py
   │     │  ├─ _typing.py
   │     │  ├─ __init__.py
   │     │  └─ __main__.py
   │     ├─ typer-0.15.2.dist-info
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  └─ WHEEL
   │     ├─ typing_extensions-4.12.2.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  └─ WHEEL
   │     ├─ typing_extensions.py
   │     ├─ tzdata
   │     │  ├─ zoneinfo
   │     │  │  ├─ Africa
   │     │  │  │  ├─ Abidjan
   │     │  │  │  ├─ Accra
   │     │  │  │  ├─ Addis_Ababa
   │     │  │  │  ├─ Algiers
   │     │  │  │  ├─ Asmara
   │     │  │  │  ├─ Asmera
   │     │  │  │  ├─ Bamako
   │     │  │  │  ├─ Bangui
   │     │  │  │  ├─ Banjul
   │     │  │  │  ├─ Bissau
   │     │  │  │  ├─ Blantyre
   │     │  │  │  ├─ Brazzaville
   │     │  │  │  ├─ Bujumbura
   │     │  │  │  ├─ Cairo
   │     │  │  │  ├─ Casablanca
   │     │  │  │  ├─ Ceuta
   │     │  │  │  ├─ Conakry
   │     │  │  │  ├─ Dakar
   │     │  │  │  ├─ Dar_es_Salaam
   │     │  │  │  ├─ Djibouti
   │     │  │  │  ├─ Douala
   │     │  │  │  ├─ El_Aaiun
   │     │  │  │  ├─ Freetown
   │     │  │  │  ├─ Gaborone
   │     │  │  │  ├─ Harare
   │     │  │  │  ├─ Johannesburg
   │     │  │  │  ├─ Juba
   │     │  │  │  ├─ Kampala
   │     │  │  │  ├─ Khartoum
   │     │  │  │  ├─ Kigali
   │     │  │  │  ├─ Kinshasa
   │     │  │  │  ├─ Lagos
   │     │  │  │  ├─ Libreville
   │     │  │  │  ├─ Lome
   │     │  │  │  ├─ Luanda
   │     │  │  │  ├─ Lubumbashi
   │     │  │  │  ├─ Lusaka
   │     │  │  │  ├─ Malabo
   │     │  │  │  ├─ Maputo
   │     │  │  │  ├─ Maseru
   │     │  │  │  ├─ Mbabane
   │     │  │  │  ├─ Mogadishu
   │     │  │  │  ├─ Monrovia
   │     │  │  │  ├─ Nairobi
   │     │  │  │  ├─ Ndjamena
   │     │  │  │  ├─ Niamey
   │     │  │  │  ├─ Nouakchott
   │     │  │  │  ├─ Ouagadougou
   │     │  │  │  ├─ Porto-Novo
   │     │  │  │  ├─ Sao_Tome
   │     │  │  │  ├─ Timbuktu
   │     │  │  │  ├─ Tripoli
   │     │  │  │  ├─ Tunis
   │     │  │  │  ├─ Windhoek
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ America
   │     │  │  │  ├─ Adak
   │     │  │  │  ├─ Anchorage
   │     │  │  │  ├─ Anguilla
   │     │  │  │  ├─ Antigua
   │     │  │  │  ├─ Araguaina
   │     │  │  │  ├─ Argentina
   │     │  │  │  │  ├─ Buenos_Aires
   │     │  │  │  │  ├─ Catamarca
   │     │  │  │  │  ├─ ComodRivadavia
   │     │  │  │  │  ├─ Cordoba
   │     │  │  │  │  ├─ Jujuy
   │     │  │  │  │  ├─ La_Rioja
   │     │  │  │  │  ├─ Mendoza
   │     │  │  │  │  ├─ Rio_Gallegos
   │     │  │  │  │  ├─ Salta
   │     │  │  │  │  ├─ San_Juan
   │     │  │  │  │  ├─ San_Luis
   │     │  │  │  │  ├─ Tucuman
   │     │  │  │  │  ├─ Ushuaia
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ Aruba
   │     │  │  │  ├─ Asuncion
   │     │  │  │  ├─ Atikokan
   │     │  │  │  ├─ Atka
   │     │  │  │  ├─ Bahia
   │     │  │  │  ├─ Bahia_Banderas
   │     │  │  │  ├─ Barbados
   │     │  │  │  ├─ Belem
   │     │  │  │  ├─ Belize
   │     │  │  │  ├─ Blanc-Sablon
   │     │  │  │  ├─ Boa_Vista
   │     │  │  │  ├─ Bogota
   │     │  │  │  ├─ Boise
   │     │  │  │  ├─ Buenos_Aires
   │     │  │  │  ├─ Cambridge_Bay
   │     │  │  │  ├─ Campo_Grande
   │     │  │  │  ├─ Cancun
   │     │  │  │  ├─ Caracas
   │     │  │  │  ├─ Catamarca
   │     │  │  │  ├─ Cayenne
   │     │  │  │  ├─ Cayman
   │     │  │  │  ├─ Chicago
   │     │  │  │  ├─ Chihuahua
   │     │  │  │  ├─ Ciudad_Juarez
   │     │  │  │  ├─ Coral_Harbour
   │     │  │  │  ├─ Cordoba
   │     │  │  │  ├─ Costa_Rica
   │     │  │  │  ├─ Creston
   │     │  │  │  ├─ Cuiaba
   │     │  │  │  ├─ Curacao
   │     │  │  │  ├─ Danmarkshavn
   │     │  │  │  ├─ Dawson
   │     │  │  │  ├─ Dawson_Creek
   │     │  │  │  ├─ Denver
   │     │  │  │  ├─ Detroit
   │     │  │  │  ├─ Dominica
   │     │  │  │  ├─ Edmonton
   │     │  │  │  ├─ Eirunepe
   │     │  │  │  ├─ El_Salvador
   │     │  │  │  ├─ Ensenada
   │     │  │  │  ├─ Fortaleza
   │     │  │  │  ├─ Fort_Nelson
   │     │  │  │  ├─ Fort_Wayne
   │     │  │  │  ├─ Glace_Bay
   │     │  │  │  ├─ Godthab
   │     │  │  │  ├─ Goose_Bay
   │     │  │  │  ├─ Grand_Turk
   │     │  │  │  ├─ Grenada
   │     │  │  │  ├─ Guadeloupe
   │     │  │  │  ├─ Guatemala
   │     │  │  │  ├─ Guayaquil
   │     │  │  │  ├─ Guyana
   │     │  │  │  ├─ Halifax
   │     │  │  │  ├─ Havana
   │     │  │  │  ├─ Hermosillo
   │     │  │  │  ├─ Indiana
   │     │  │  │  │  ├─ Indianapolis
   │     │  │  │  │  ├─ Knox
   │     │  │  │  │  ├─ Marengo
   │     │  │  │  │  ├─ Petersburg
   │     │  │  │  │  ├─ Tell_City
   │     │  │  │  │  ├─ Vevay
   │     │  │  │  │  ├─ Vincennes
   │     │  │  │  │  ├─ Winamac
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ Indianapolis
   │     │  │  │  ├─ Inuvik
   │     │  │  │  ├─ Iqaluit
   │     │  │  │  ├─ Jamaica
   │     │  │  │  ├─ Jujuy
   │     │  │  │  ├─ Juneau
   │     │  │  │  ├─ Kentucky
   │     │  │  │  │  ├─ Louisville
   │     │  │  │  │  ├─ Monticello
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ Knox_IN
   │     │  │  │  ├─ Kralendijk
   │     │  │  │  ├─ La_Paz
   │     │  │  │  ├─ Lima
   │     │  │  │  ├─ Los_Angeles
   │     │  │  │  ├─ Louisville
   │     │  │  │  ├─ Lower_Princes
   │     │  │  │  ├─ Maceio
   │     │  │  │  ├─ Managua
   │     │  │  │  ├─ Manaus
   │     │  │  │  ├─ Marigot
   │     │  │  │  ├─ Martinique
   │     │  │  │  ├─ Matamoros
   │     │  │  │  ├─ Mazatlan
   │     │  │  │  ├─ Mendoza
   │     │  │  │  ├─ Menominee
   │     │  │  │  ├─ Merida
   │     │  │  │  ├─ Metlakatla
   │     │  │  │  ├─ Mexico_City
   │     │  │  │  ├─ Miquelon
   │     │  │  │  ├─ Moncton
   │     │  │  │  ├─ Monterrey
   │     │  │  │  ├─ Montevideo
   │     │  │  │  ├─ Montreal
   │     │  │  │  ├─ Montserrat
   │     │  │  │  ├─ Nassau
   │     │  │  │  ├─ New_York
   │     │  │  │  ├─ Nipigon
   │     │  │  │  ├─ Nome
   │     │  │  │  ├─ Noronha
   │     │  │  │  ├─ North_Dakota
   │     │  │  │  │  ├─ Beulah
   │     │  │  │  │  ├─ Center
   │     │  │  │  │  ├─ New_Salem
   │     │  │  │  │  └─ __init__.py
   │     │  │  │  ├─ Nuuk
   │     │  │  │  ├─ Ojinaga
   │     │  │  │  ├─ Panama
   │     │  │  │  ├─ Pangnirtung
   │     │  │  │  ├─ Paramaribo
   │     │  │  │  ├─ Phoenix
   │     │  │  │  ├─ Port-au-Prince
   │     │  │  │  ├─ Porto_Acre
   │     │  │  │  ├─ Porto_Velho
   │     │  │  │  ├─ Port_of_Spain
   │     │  │  │  ├─ Puerto_Rico
   │     │  │  │  ├─ Punta_Arenas
   │     │  │  │  ├─ Rainy_River
   │     │  │  │  ├─ Rankin_Inlet
   │     │  │  │  ├─ Recife
   │     │  │  │  ├─ Regina
   │     │  │  │  ├─ Resolute
   │     │  │  │  ├─ Rio_Branco
   │     │  │  │  ├─ Rosario
   │     │  │  │  ├─ Santarem
   │     │  │  │  ├─ Santa_Isabel
   │     │  │  │  ├─ Santiago
   │     │  │  │  ├─ Santo_Domingo
   │     │  │  │  ├─ Sao_Paulo
   │     │  │  │  ├─ Scoresbysund
   │     │  │  │  ├─ Shiprock
   │     │  │  │  ├─ Sitka
   │     │  │  │  ├─ St_Barthelemy
   │     │  │  │  ├─ St_Johns
   │     │  │  │  ├─ St_Kitts
   │     │  │  │  ├─ St_Lucia
   │     │  │  │  ├─ St_Thomas
   │     │  │  │  ├─ St_Vincent
   │     │  │  │  ├─ Swift_Current
   │     │  │  │  ├─ Tegucigalpa
   │     │  │  │  ├─ Thule
   │     │  │  │  ├─ Thunder_Bay
   │     │  │  │  ├─ Tijuana
   │     │  │  │  ├─ Toronto
   │     │  │  │  ├─ Tortola
   │     │  │  │  ├─ Vancouver
   │     │  │  │  ├─ Virgin
   │     │  │  │  ├─ Whitehorse
   │     │  │  │  ├─ Winnipeg
   │     │  │  │  ├─ Yakutat
   │     │  │  │  ├─ Yellowknife
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ Antarctica
   │     │  │  │  ├─ Casey
   │     │  │  │  ├─ Davis
   │     │  │  │  ├─ DumontDUrville
   │     │  │  │  ├─ Macquarie
   │     │  │  │  ├─ Mawson
   │     │  │  │  ├─ McMurdo
   │     │  │  │  ├─ Palmer
   │     │  │  │  ├─ Rothera
   │     │  │  │  ├─ South_Pole
   │     │  │  │  ├─ Syowa
   │     │  │  │  ├─ Troll
   │     │  │  │  ├─ Vostok
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ Arctic
   │     │  │  │  ├─ Longyearbyen
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ Asia
   │     │  │  │  ├─ Aden
   │     │  │  │  ├─ Almaty
   │     │  │  │  ├─ Amman
   │     │  │  │  ├─ Anadyr
   │     │  │  │  ├─ Aqtau
   │     │  │  │  ├─ Aqtobe
   │     │  │  │  ├─ Ashgabat
   │     │  │  │  ├─ Ashkhabad
   │     │  │  │  ├─ Atyrau
   │     │  │  │  ├─ Baghdad
   │     │  │  │  ├─ Bahrain
   │     │  │  │  ├─ Baku
   │     │  │  │  ├─ Bangkok
   │     │  │  │  ├─ Barnaul
   │     │  │  │  ├─ Beirut
   │     │  │  │  ├─ Bishkek
   │     │  │  │  ├─ Brunei
   │     │  │  │  ├─ Calcutta
   │     │  │  │  ├─ Chita
   │     │  │  │  ├─ Choibalsan
   │     │  │  │  ├─ Chongqing
   │     │  │  │  ├─ Chungking
   │     │  │  │  ├─ Colombo
   │     │  │  │  ├─ Dacca
   │     │  │  │  ├─ Damascus
   │     │  │  │  ├─ Dhaka
   │     │  │  │  ├─ Dili
   │     │  │  │  ├─ Dubai
   │     │  │  │  ├─ Dushanbe
   │     │  │  │  ├─ Famagusta
   │     │  │  │  ├─ Gaza
   │     │  │  │  ├─ Harbin
   │     │  │  │  ├─ Hebron
   │     │  │  │  ├─ Hong_Kong
   │     │  │  │  ├─ Hovd
   │     │  │  │  ├─ Ho_Chi_Minh
   │     │  │  │  ├─ Irkutsk
   │     │  │  │  ├─ Istanbul
   │     │  │  │  ├─ Jakarta
   │     │  │  │  ├─ Jayapura
   │     │  │  │  ├─ Jerusalem
   │     │  │  │  ├─ Kabul
   │     │  │  │  ├─ Kamchatka
   │     │  │  │  ├─ Karachi
   │     │  │  │  ├─ Kashgar
   │     │  │  │  ├─ Kathmandu
   │     │  │  │  ├─ Katmandu
   │     │  │  │  ├─ Khandyga
   │     │  │  │  ├─ Kolkata
   │     │  │  │  ├─ Krasnoyarsk
   │     │  │  │  ├─ Kuala_Lumpur
   │     │  │  │  ├─ Kuching
   │     │  │  │  ├─ Kuwait
   │     │  │  │  ├─ Macao
   │     │  │  │  ├─ Macau
   │     │  │  │  ├─ Magadan
   │     │  │  │  ├─ Makassar
   │     │  │  │  ├─ Manila
   │     │  │  │  ├─ Muscat
   │     │  │  │  ├─ Nicosia
   │     │  │  │  ├─ Novokuznetsk
   │     │  │  │  ├─ Novosibirsk
   │     │  │  │  ├─ Omsk
   │     │  │  │  ├─ Oral
   │     │  │  │  ├─ Phnom_Penh
   │     │  │  │  ├─ Pontianak
   │     │  │  │  ├─ Pyongyang
   │     │  │  │  ├─ Qatar
   │     │  │  │  ├─ Qostanay
   │     │  │  │  ├─ Qyzylorda
   │     │  │  │  ├─ Rangoon
   │     │  │  │  ├─ Riyadh
   │     │  │  │  ├─ Saigon
   │     │  │  │  ├─ Sakhalin
   │     │  │  │  ├─ Samarkand
   │     │  │  │  ├─ Seoul
   │     │  │  │  ├─ Shanghai
   │     │  │  │  ├─ Singapore
   │     │  │  │  ├─ Srednekolymsk
   │     │  │  │  ├─ Taipei
   │     │  │  │  ├─ Tashkent
   │     │  │  │  ├─ Tbilisi
   │     │  │  │  ├─ Tehran
   │     │  │  │  ├─ Tel_Aviv
   │     │  │  │  ├─ Thimbu
   │     │  │  │  ├─ Thimphu
   │     │  │  │  ├─ Tokyo
   │     │  │  │  ├─ Tomsk
   │     │  │  │  ├─ Ujung_Pandang
   │     │  │  │  ├─ Ulaanbaatar
   │     │  │  │  ├─ Ulan_Bator
   │     │  │  │  ├─ Urumqi
   │     │  │  │  ├─ Ust-Nera
   │     │  │  │  ├─ Vientiane
   │     │  │  │  ├─ Vladivostok
   │     │  │  │  ├─ Yakutsk
   │     │  │  │  ├─ Yangon
   │     │  │  │  ├─ Yekaterinburg
   │     │  │  │  ├─ Yerevan
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ Atlantic
   │     │  │  │  ├─ Azores
   │     │  │  │  ├─ Bermuda
   │     │  │  │  ├─ Canary
   │     │  │  │  ├─ Cape_Verde
   │     │  │  │  ├─ Faeroe
   │     │  │  │  ├─ Faroe
   │     │  │  │  ├─ Jan_Mayen
   │     │  │  │  ├─ Madeira
   │     │  │  │  ├─ Reykjavik
   │     │  │  │  ├─ South_Georgia
   │     │  │  │  ├─ Stanley
   │     │  │  │  ├─ St_Helena
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ Australia
   │     │  │  │  ├─ ACT
   │     │  │  │  ├─ Adelaide
   │     │  │  │  ├─ Brisbane
   │     │  │  │  ├─ Broken_Hill
   │     │  │  │  ├─ Canberra
   │     │  │  │  ├─ Currie
   │     │  │  │  ├─ Darwin
   │     │  │  │  ├─ Eucla
   │     │  │  │  ├─ Hobart
   │     │  │  │  ├─ LHI
   │     │  │  │  ├─ Lindeman
   │     │  │  │  ├─ Lord_Howe
   │     │  │  │  ├─ Melbourne
   │     │  │  │  ├─ North
   │     │  │  │  ├─ NSW
   │     │  │  │  ├─ Perth
   │     │  │  │  ├─ Queensland
   │     │  │  │  ├─ South
   │     │  │  │  ├─ Sydney
   │     │  │  │  ├─ Tasmania
   │     │  │  │  ├─ Victoria
   │     │  │  │  ├─ West
   │     │  │  │  ├─ Yancowinna
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ Brazil
   │     │  │  │  ├─ Acre
   │     │  │  │  ├─ DeNoronha
   │     │  │  │  ├─ East
   │     │  │  │  ├─ West
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ Canada
   │     │  │  │  ├─ Atlantic
   │     │  │  │  ├─ Central
   │     │  │  │  ├─ Eastern
   │     │  │  │  ├─ Mountain
   │     │  │  │  ├─ Newfoundland
   │     │  │  │  ├─ Pacific
   │     │  │  │  ├─ Saskatchewan
   │     │  │  │  ├─ Yukon
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ CET
   │     │  │  ├─ Chile
   │     │  │  │  ├─ Continental
   │     │  │  │  ├─ EasterIsland
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ CST6CDT
   │     │  │  ├─ Cuba
   │     │  │  ├─ EET
   │     │  │  ├─ Egypt
   │     │  │  ├─ Eire
   │     │  │  ├─ EST
   │     │  │  ├─ EST5EDT
   │     │  │  ├─ Etc
   │     │  │  │  ├─ GMT
   │     │  │  │  ├─ GMT+0
   │     │  │  │  ├─ GMT+1
   │     │  │  │  ├─ GMT+10
   │     │  │  │  ├─ GMT+11
   │     │  │  │  ├─ GMT+12
   │     │  │  │  ├─ GMT+2
   │     │  │  │  ├─ GMT+3
   │     │  │  │  ├─ GMT+4
   │     │  │  │  ├─ GMT+5
   │     │  │  │  ├─ GMT+6
   │     │  │  │  ├─ GMT+7
   │     │  │  │  ├─ GMT+8
   │     │  │  │  ├─ GMT+9
   │     │  │  │  ├─ GMT-0
   │     │  │  │  ├─ GMT-1
   │     │  │  │  ├─ GMT-10
   │     │  │  │  ├─ GMT-11
   │     │  │  │  ├─ GMT-12
   │     │  │  │  ├─ GMT-13
   │     │  │  │  ├─ GMT-14
   │     │  │  │  ├─ GMT-2
   │     │  │  │  ├─ GMT-3
   │     │  │  │  ├─ GMT-4
   │     │  │  │  ├─ GMT-5
   │     │  │  │  ├─ GMT-6
   │     │  │  │  ├─ GMT-7
   │     │  │  │  ├─ GMT-8
   │     │  │  │  ├─ GMT-9
   │     │  │  │  ├─ GMT0
   │     │  │  │  ├─ Greenwich
   │     │  │  │  ├─ UCT
   │     │  │  │  ├─ Universal
   │     │  │  │  ├─ UTC
   │     │  │  │  ├─ Zulu
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ Europe
   │     │  │  │  ├─ Amsterdam
   │     │  │  │  ├─ Andorra
   │     │  │  │  ├─ Astrakhan
   │     │  │  │  ├─ Athens
   │     │  │  │  ├─ Belfast
   │     │  │  │  ├─ Belgrade
   │     │  │  │  ├─ Berlin
   │     │  │  │  ├─ Bratislava
   │     │  │  │  ├─ Brussels
   │     │  │  │  ├─ Bucharest
   │     │  │  │  ├─ Budapest
   │     │  │  │  ├─ Busingen
   │     │  │  │  ├─ Chisinau
   │     │  │  │  ├─ Copenhagen
   │     │  │  │  ├─ Dublin
   │     │  │  │  ├─ Gibraltar
   │     │  │  │  ├─ Guernsey
   │     │  │  │  ├─ Helsinki
   │     │  │  │  ├─ Isle_of_Man
   │     │  │  │  ├─ Istanbul
   │     │  │  │  ├─ Jersey
   │     │  │  │  ├─ Kaliningrad
   │     │  │  │  ├─ Kiev
   │     │  │  │  ├─ Kirov
   │     │  │  │  ├─ Kyiv
   │     │  │  │  ├─ Lisbon
   │     │  │  │  ├─ Ljubljana
   │     │  │  │  ├─ London
   │     │  │  │  ├─ Luxembourg
   │     │  │  │  ├─ Madrid
   │     │  │  │  ├─ Malta
   │     │  │  │  ├─ Mariehamn
   │     │  │  │  ├─ Minsk
   │     │  │  │  ├─ Monaco
   │     │  │  │  ├─ Moscow
   │     │  │  │  ├─ Nicosia
   │     │  │  │  ├─ Oslo
   │     │  │  │  ├─ Paris
   │     │  │  │  ├─ Podgorica
   │     │  │  │  ├─ Prague
   │     │  │  │  ├─ Riga
   │     │  │  │  ├─ Rome
   │     │  │  │  ├─ Samara
   │     │  │  │  ├─ San_Marino
   │     │  │  │  ├─ Sarajevo
   │     │  │  │  ├─ Saratov
   │     │  │  │  ├─ Simferopol
   │     │  │  │  ├─ Skopje
   │     │  │  │  ├─ Sofia
   │     │  │  │  ├─ Stockholm
   │     │  │  │  ├─ Tallinn
   │     │  │  │  ├─ Tirane
   │     │  │  │  ├─ Tiraspol
   │     │  │  │  ├─ Ulyanovsk
   │     │  │  │  ├─ Uzhgorod
   │     │  │  │  ├─ Vaduz
   │     │  │  │  ├─ Vatican
   │     │  │  │  ├─ Vienna
   │     │  │  │  ├─ Vilnius
   │     │  │  │  ├─ Volgograd
   │     │  │  │  ├─ Warsaw
   │     │  │  │  ├─ Zagreb
   │     │  │  │  ├─ Zaporozhye
   │     │  │  │  ├─ Zurich
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ Factory
   │     │  │  ├─ GB
   │     │  │  ├─ GB-Eire
   │     │  │  ├─ GMT
   │     │  │  ├─ GMT+0
   │     │  │  ├─ GMT-0
   │     │  │  ├─ GMT0
   │     │  │  ├─ Greenwich
   │     │  │  ├─ Hongkong
   │     │  │  ├─ HST
   │     │  │  ├─ Iceland
   │     │  │  ├─ Indian
   │     │  │  │  ├─ Antananarivo
   │     │  │  │  ├─ Chagos
   │     │  │  │  ├─ Christmas
   │     │  │  │  ├─ Cocos
   │     │  │  │  ├─ Comoro
   │     │  │  │  ├─ Kerguelen
   │     │  │  │  ├─ Mahe
   │     │  │  │  ├─ Maldives
   │     │  │  │  ├─ Mauritius
   │     │  │  │  ├─ Mayotte
   │     │  │  │  ├─ Reunion
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ Iran
   │     │  │  ├─ iso3166.tab
   │     │  │  ├─ Israel
   │     │  │  ├─ Jamaica
   │     │  │  ├─ Japan
   │     │  │  ├─ Kwajalein
   │     │  │  ├─ leapseconds
   │     │  │  ├─ Libya
   │     │  │  ├─ MET
   │     │  │  ├─ Mexico
   │     │  │  │  ├─ BajaNorte
   │     │  │  │  ├─ BajaSur
   │     │  │  │  ├─ General
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ MST
   │     │  │  ├─ MST7MDT
   │     │  │  ├─ Navajo
   │     │  │  ├─ NZ
   │     │  │  ├─ NZ-CHAT
   │     │  │  ├─ Pacific
   │     │  │  │  ├─ Apia
   │     │  │  │  ├─ Auckland
   │     │  │  │  ├─ Bougainville
   │     │  │  │  ├─ Chatham
   │     │  │  │  ├─ Chuuk
   │     │  │  │  ├─ Easter
   │     │  │  │  ├─ Efate
   │     │  │  │  ├─ Enderbury
   │     │  │  │  ├─ Fakaofo
   │     │  │  │  ├─ Fiji
   │     │  │  │  ├─ Funafuti
   │     │  │  │  ├─ Galapagos
   │     │  │  │  ├─ Gambier
   │     │  │  │  ├─ Guadalcanal
   │     │  │  │  ├─ Guam
   │     │  │  │  ├─ Honolulu
   │     │  │  │  ├─ Johnston
   │     │  │  │  ├─ Kanton
   │     │  │  │  ├─ Kiritimati
   │     │  │  │  ├─ Kosrae
   │     │  │  │  ├─ Kwajalein
   │     │  │  │  ├─ Majuro
   │     │  │  │  ├─ Marquesas
   │     │  │  │  ├─ Midway
   │     │  │  │  ├─ Nauru
   │     │  │  │  ├─ Niue
   │     │  │  │  ├─ Norfolk
   │     │  │  │  ├─ Noumea
   │     │  │  │  ├─ Pago_Pago
   │     │  │  │  ├─ Palau
   │     │  │  │  ├─ Pitcairn
   │     │  │  │  ├─ Pohnpei
   │     │  │  │  ├─ Ponape
   │     │  │  │  ├─ Port_Moresby
   │     │  │  │  ├─ Rarotonga
   │     │  │  │  ├─ Saipan
   │     │  │  │  ├─ Samoa
   │     │  │  │  ├─ Tahiti
   │     │  │  │  ├─ Tarawa
   │     │  │  │  ├─ Tongatapu
   │     │  │  │  ├─ Truk
   │     │  │  │  ├─ Wake
   │     │  │  │  ├─ Wallis
   │     │  │  │  ├─ Yap
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ Poland
   │     │  │  ├─ Portugal
   │     │  │  ├─ PRC
   │     │  │  ├─ PST8PDT
   │     │  │  ├─ ROC
   │     │  │  ├─ ROK
   │     │  │  ├─ Singapore
   │     │  │  ├─ Turkey
   │     │  │  ├─ tzdata.zi
   │     │  │  ├─ UCT
   │     │  │  ├─ Universal
   │     │  │  ├─ US
   │     │  │  │  ├─ Alaska
   │     │  │  │  ├─ Aleutian
   │     │  │  │  ├─ Arizona
   │     │  │  │  ├─ Central
   │     │  │  │  ├─ East-Indiana
   │     │  │  │  ├─ Eastern
   │     │  │  │  ├─ Hawaii
   │     │  │  │  ├─ Indiana-Starke
   │     │  │  │  ├─ Michigan
   │     │  │  │  ├─ Mountain
   │     │  │  │  ├─ Pacific
   │     │  │  │  ├─ Samoa
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ UTC
   │     │  │  ├─ W-SU
   │     │  │  ├─ WET
   │     │  │  ├─ zone.tab
   │     │  │  ├─ zone1970.tab
   │     │  │  ├─ zonenow.tab
   │     │  │  ├─ Zulu
   │     │  │  └─ __init__.py
   │     │  ├─ zones
   │     │  └─ __init__.py
   │     ├─ tzdata-2025.1.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ LICENSE_APACHE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ uritemplate
   │     │  ├─ api.py
   │     │  ├─ orderedset.py
   │     │  ├─ py.typed
   │     │  ├─ template.py
   │     │  ├─ variable.py
   │     │  └─ __init__.py
   │     ├─ uritemplate-4.1.1.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ urllib3
   │     │  ├─ connection.py
   │     │  ├─ connectionpool.py
   │     │  ├─ contrib
   │     │  │  ├─ emscripten
   │     │  │  │  ├─ connection.py
   │     │  │  │  ├─ emscripten_fetch_worker.js
   │     │  │  │  ├─ fetch.py
   │     │  │  │  ├─ request.py
   │     │  │  │  ├─ response.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ pyopenssl.py
   │     │  │  ├─ socks.py
   │     │  │  └─ __init__.py
   │     │  ├─ exceptions.py
   │     │  ├─ fields.py
   │     │  ├─ filepost.py
   │     │  ├─ http2
   │     │  │  ├─ connection.py
   │     │  │  ├─ probe.py
   │     │  │  └─ __init__.py
   │     │  ├─ poolmanager.py
   │     │  ├─ py.typed
   │     │  ├─ response.py
   │     │  ├─ util
   │     │  │  ├─ connection.py
   │     │  │  ├─ proxy.py
   │     │  │  ├─ request.py
   │     │  │  ├─ response.py
   │     │  │  ├─ retry.py
   │     │  │  ├─ ssltransport.py
   │     │  │  ├─ ssl_.py
   │     │  │  ├─ ssl_match_hostname.py
   │     │  │  ├─ timeout.py
   │     │  │  ├─ url.py
   │     │  │  ├─ util.py
   │     │  │  ├─ wait.py
   │     │  │  └─ __init__.py
   │     │  ├─ _base_connection.py
   │     │  ├─ _collections.py
   │     │  ├─ _request_methods.py
   │     │  ├─ _version.py
   │     │  └─ __init__.py
   │     ├─ urllib3-2.3.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ licenses
   │     │  │  └─ LICENSE.txt
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  └─ WHEEL
   │     ├─ wasabi
   │     │  ├─ compat.py
   │     │  ├─ markdown.py
   │     │  ├─ printer.py
   │     │  ├─ py.typed
   │     │  ├─ tables.py
   │     │  ├─ tests
   │     │  │  ├─ test-data
   │     │  │  │  └─ wasabi-test-notebook.ipynb
   │     │  │  ├─ test_jupyter.py
   │     │  │  ├─ test_markdown.py
   │     │  │  ├─ test_printer.py
   │     │  │  ├─ test_tables.py
   │     │  │  ├─ test_traceback.py
   │     │  │  ├─ test_util.py
   │     │  │  └─ __init__.py
   │     │  ├─ traceback_printer.py
   │     │  ├─ util.py
   │     │  └─ __init__.py
   │     ├─ wasabi-1.1.3.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  ├─ WHEEL
   │     │  └─ zip-safe
   │     ├─ weasel
   │     │  ├─ about.py
   │     │  ├─ cli
   │     │  │  ├─ assets.py
   │     │  │  ├─ clone.py
   │     │  │  ├─ document.py
   │     │  │  ├─ dvc.py
   │     │  │  ├─ main.py
   │     │  │  ├─ pull.py
   │     │  │  ├─ push.py
   │     │  │  ├─ remote_storage.py
   │     │  │  ├─ run.py
   │     │  │  └─ __init__.py
   │     │  ├─ compat.py
   │     │  ├─ errors.py
   │     │  ├─ schemas.py
   │     │  ├─ tests
   │     │  │  ├─ cli
   │     │  │  │  ├─ test_cli.py
   │     │  │  │  ├─ test_cli_app.py
   │     │  │  │  ├─ test_document.py
   │     │  │  │  ├─ test_remote.py
   │     │  │  │  └─ __init__.py
   │     │  │  ├─ test_schemas.py
   │     │  │  ├─ test_validation.py
   │     │  │  ├─ util.py
   │     │  │  └─ __init__.py
   │     │  ├─ util
   │     │  │  ├─ commands.py
   │     │  │  ├─ config.py
   │     │  │  ├─ environment.py
   │     │  │  ├─ filesystem.py
   │     │  │  ├─ frozen.py
   │     │  │  ├─ git.py
   │     │  │  ├─ hashing.py
   │     │  │  ├─ logging.py
   │     │  │  ├─ modules.py
   │     │  │  ├─ remote.py
   │     │  │  ├─ validation.py
   │     │  │  ├─ versions.py
   │     │  │  └─ __init__.py
   │     │  ├─ __init__.py
   │     │  └─ __main__.py
   │     ├─ weasel-0.4.1.dist-info
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ webdriver_manager
   │     │  ├─ chrome.py
   │     │  ├─ core
   │     │  │  ├─ archive.py
   │     │  │  ├─ config.py
   │     │  │  ├─ constants.py
   │     │  │  ├─ download_manager.py
   │     │  │  ├─ driver.py
   │     │  │  ├─ driver_cache.py
   │     │  │  ├─ file_manager.py
   │     │  │  ├─ http.py
   │     │  │  ├─ logger.py
   │     │  │  ├─ manager.py
   │     │  │  ├─ os_manager.py
   │     │  │  ├─ utils.py
   │     │  │  └─ __init__.py
   │     │  ├─ drivers
   │     │  │  ├─ chrome.py
   │     │  │  ├─ edge.py
   │     │  │  ├─ firefox.py
   │     │  │  ├─ ie.py
   │     │  │  ├─ opera.py
   │     │  │  └─ __init__.py
   │     │  ├─ firefox.py
   │     │  ├─ microsoft.py
   │     │  ├─ opera.py
   │     │  ├─ py.typed
   │     │  └─ __init__.py
   │     ├─ webdriver_manager-4.0.2.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ REQUESTED
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ websocket
   │     │  ├─ py.typed
   │     │  ├─ tests
   │     │  │  ├─ data
   │     │  │  │  ├─ header01.txt
   │     │  │  │  ├─ header02.txt
   │     │  │  │  └─ header03.txt
   │     │  │  ├─ echo-server.py
   │     │  │  ├─ test_abnf.py
   │     │  │  ├─ test_app.py
   │     │  │  ├─ test_cookiejar.py
   │     │  │  ├─ test_http.py
   │     │  │  ├─ test_url.py
   │     │  │  ├─ test_websocket.py
   │     │  │  └─ __init__.py
   │     │  ├─ _abnf.py
   │     │  ├─ _app.py
   │     │  ├─ _cookiejar.py
   │     │  ├─ _core.py
   │     │  ├─ _exceptions.py
   │     │  ├─ _handshake.py
   │     │  ├─ _http.py
   │     │  ├─ _logging.py
   │     │  ├─ _socket.py
   │     │  ├─ _ssl_compat.py
   │     │  ├─ _url.py
   │     │  ├─ _utils.py
   │     │  ├─ _wsdump.py
   │     │  └─ __init__.py
   │     ├─ websocket_client-1.8.0.dist-info
   │     │  ├─ entry_points.txt
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ wrapt
   │     │  ├─ arguments.py
   │     │  ├─ decorators.py
   │     │  ├─ importer.py
   │     │  ├─ patches.py
   │     │  ├─ weakrefs.py
   │     │  ├─ wrappers.py
   │     │  ├─ _wrappers.cp311-win_amd64.pyd
   │     │  ├─ __init__.py
   │     │  └─ __wrapt__.py
   │     ├─ wrapt-1.17.2.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ wsproto
   │     │  ├─ connection.py
   │     │  ├─ events.py
   │     │  ├─ extensions.py
   │     │  ├─ frame_protocol.py
   │     │  ├─ handshake.py
   │     │  ├─ py.typed
   │     │  ├─ typing.py
   │     │  ├─ utilities.py
   │     │  └─ __init__.py
   │     ├─ wsproto-1.2.0.dist-info
   │     │  ├─ INSTALLER
   │     │  ├─ LICENSE
   │     │  ├─ METADATA
   │     │  ├─ RECORD
   │     │  ├─ top_level.txt
   │     │  └─ WHEEL
   │     ├─ _cffi_backend.cp311-win_amd64.pyd
   │     └─ _distutils_hack
   │        ├─ override.py
   │        └─ __init__.py
   ├─ pyvenv.cfg
   └─ Scripts
      ├─ activate
      ├─ activate.bat
      ├─ Activate.ps1
      ├─ deactivate.bat
      ├─ dotenv.exe
      ├─ f2py.exe
      ├─ google-oauthlib-tool.exe
      ├─ markdown-it.exe
      ├─ nltk.exe
      ├─ normalizer.exe
      ├─ numpy-config.exe
      ├─ pip.exe
      ├─ pip3.11.exe
      ├─ pip3.exe
      ├─ pygmentize.exe
      ├─ pymupdf.exe
      ├─ pyrsa-decrypt.exe
      ├─ pyrsa-encrypt.exe
      ├─ pyrsa-keygen.exe
      ├─ pyrsa-priv2pub.exe
      ├─ pyrsa-sign.exe
      ├─ pyrsa-verify.exe
      ├─ python.exe
      ├─ pythonw.exe
      ├─ spacy.exe
      ├─ tqdm.exe
      ├─ typer.exe
      ├─ weasel.exe
      └─ wsdump.exe

```