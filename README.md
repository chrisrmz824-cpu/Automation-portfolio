# QualRecruit API Robot 🤖

This script automates the batch update of **Join Links** and **System Check Links** for participants within the QualRecruit platform using its official API.

## 🚀 Key Features
* **Batch Processing:** Updates dozens of participants in seconds, replacing manual entry.
* **Smart Filtering:** Automatically targets only "Spanish" language entries to maintain regional data integrity.
* **Validation Logic:** Validates ID length (min. 7 chars) and automatically skips empty link fields.
* **Execution Summary:** Provides a real-time log and a final report on successes, errors, and missing records.

## 🛠️ Requirements
* Python 3.7+
* Dependencies: `requests`, `pandas`, `openpyxl`

```bash
pip install requests pandas openpyxl
