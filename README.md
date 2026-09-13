# Work Order Automation

A Python-based automation pipeline for processing daily work-order reports, applying configurable business rules, classifying records and generating structured Excel reports.

This portfolio project demonstrates practical IT operations automation using **Python, Pandas and OpenPyXL**.

> \*\*Data disclaimer:\*\* The repository contains only synthetic sample data and generic business rules. No company-confidential information, real employee data, internal URLs, credentials or proprietary code is included.

## Problem

Daily work-order reports often require repetitive manual activities:

* Downloading and reading operational reports
* Cleaning unnecessary or inconsistent data
* Applying business rules to identify work-order categories
* Separating records for different operational teams
* Preparing Excel reports
* Distributing structured outputs

## Solution

The pipeline converts these steps into a repeatable workflow:

```text
Input Excel/CSV
      |
      v
Read \& Validate
      |
      v
Data Cleaning
      |
      v
Business-Rule Classification
      |
      v
Category Assignment
      |
      v
Excel Report Generation
      |
      v
Timestamped Outputs
```

The project is inspired by a real enterprise work-order automation workflow that handled approximately **700–750 records per day** and reduced manual processing from roughly **15–25 minutes to under 5 minutes**. The public repository itself uses a small synthetic dataset for demonstration.

## Features

* XLSX and CSV input support
* Input schema validation
* Duplicate and empty-row handling
* Text normalization
* Date normalization
* Deterministic rule-based classification
* Separate Excel report generation by category
* Timestamped output files
* Summary report
* Unit tests with pytest
* Modular project structure

## Classification Rules

The sample implementation demonstrates five operational categories:

|Category|Example signals|
|-|-|
|User Lifecycle|Leaver, user deletion, deactivation, joiner/mover|
|Identity Management|Identity, access, password, account, IDM|
|Application Support|Application, portal, software, app support|
|Service Request|Service request, standard request|
|Business as Usual|Fallback for routine operational work|

These are generic demonstration rules and can be replaced with organization-specific rules.

## Project Structure

```text
work-order-automation/
├── src/
│   ├── \_\_init\_\_.py
│   ├── config.py
│   ├── reader.py
│   ├── cleaner.py
│   ├── classifier.py
│   ├── report\_generator.py
│   └── pipeline.py
├── sample\_data/
│   └── work\_orders.xlsx
├── output/
│   └── .gitkeep
├── tests/
│   ├── test\_cleaner.py
│   └── test\_classifier.py
├── .env.example
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Installation

```bash
git clone https://github.com/Deek2o/work-order-automation.git
cd work-order-automation

python -m venv .venv
```

```cmd

.venv\\Scripts\\activate.bat

```

Linux/macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

Using the included synthetic Excel report:

```bash
python -m src.pipeline --input sample\_data/work\_orders.xlsx --output output
```

The pipeline will print the number of input records, records remaining after cleaning, and generated reports.

## Test

```bash
pytest -q
```

## Design Notes

The code is intentionally separated into small modules:

* `reader.py` handles input and schema validation.
* `cleaner.py` handles normalization and duplicate removal.
* `classifier.py` contains business-rule classification.
* `report\_generator.py` creates operational outputs.
* `pipeline.py` orchestrates the complete workflow.
* `config.py` keeps runtime configuration separate from business logic.

This structure makes the automation easier to test, maintain and extend.

## Future Improvements

Potential production-oriented extensions include:

* Outlook/Graph API input adapter
* Email-based report retrieval
* Configurable rules from YAML/JSON
* Structured logging
* Retry and exception handling
* Database persistence
* REST API trigger
* Scheduled execution
* Dashboard/metrics
* Docker deployment
* CI/CD with GitHub Actions

## Author

**Deekshith V**

Automation Engineer focused on Python automation, IT operations automation, REST APIs, ITSM workflows and enterprise automation.

