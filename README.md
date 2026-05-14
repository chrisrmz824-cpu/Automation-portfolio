# QualRecruit API Robot

Batch updates respondent join links and system check links in QualRecruit projects via their official API.

## Requirements

- Python 3.7+
- `requests`, `pandas`, `openpyxl`

## Installation

```bash
pip install requests pandas openpyxl
Configuration
Edit these variables in robot.py:

python
PROJECT_ID = "your_project_id"
GROUP_IDS = ["group_id_1", "group_id_2", "group_id_3", "group_id_4"]
Excel File (DATA_FILE_CLEAN.xlsx)
Column	Description
Respondent ID	Unique identifier (min 7 chars)
Respondent Name	Display name
Language	Must contain "Spanish"
Respondent Join Link	Custom join link
Respondent System Check Link	Custom check link
Usage
bash
python robot.py
Paste your Bearer token when prompted (with or without "Bearer " prefix).

What It Does
Loads Spanish respondents from Excel

Fetches all respondents from your QualRecruit groups

Matches Respondent IDs to API records

Updates join links and check links

Shows success/failure summary

Output Example
text
[1/77] abc12345 (John Doe)
  [OK] Updated.

============================================================
FINAL SUMMARY
  Successful:      75
  Not found:       2
  Errors:          0
============================================================
Notes
Only Spanish language entries are processed

Respondent IDs are case-insensitive

IDs shorter than 7 characters are ignored

Empty links are skipped automatically
Batch updates respondent join links and system check links in QualRecruit projects.

How it works?

## Quick Start

1. Install dependencies:
```bash
pip install requests pandas openpyxl
Configure PROJECT_ID and GROUP_IDS in robot.py

Run:

bash
python robot.py
Paste your Bearer token when prompted

Excel Format (DATA_FILE_CLEAN.xlsx)
Column	Required
Respondent ID	Yes
Respondent Name	No
Language	Yes (filters "Spanish")
Respondent Join Link	No
Respondent System Check Link	No
Output
✅ Successfully updated

❌ Not found / Error

📊 Summary report at the end

Notes
Only processes Spanish entries

Respondent IDs matched case-insensitively (min 7 chars)?
Tienes razón. Aquí está corregido y completo:

markdown
# Automation-portfolio
# QualRecruit API Robot

Batch updates respondent join links and system check links in QualRecruit projects.

## Quick Start

1. Install dependencies:
```bash
pip install requests pandas openpyxl
Configure PROJECT_ID and GROUP_IDS in robot.py

Run:

bash
python robot.py
Paste your Bearer token when prompted

Excel Format (DATA_FILE_CLEAN.xlsx)
Column	Required
Respondent ID	Yes
Respondent Name	No
Language	Yes (filters "Spanish")
Respondent Join Link	No
Respondent System Check Link	No
Output
✅ Successfully updated

❌ Not found / Error

📊 Summary report at the end

Notes
Only processes Spanish entries

Respondent IDs matched case-insensitively (min 7 chars)

Empty links are skipped automatically

Only rows with Language = "Spanish" are processed
