QualRecruit API Robot 🤖This script automates the batch update of Join Links and System Check Links for participants within the QualRecruit platform using its official API.🚀 Key FeaturesBatch Processing: Updates dozens of participants in seconds, replacing manual entry.Smart Filtering: Automatically targets only "Spanish" language entries to maintain regional data integrity.Validation Logic: Validates ID length (min. 7 chars) and automatically skips empty link fields.Execution Summary: Provides a real-time log and a final report on successes, errors, and missing records.🛠️ RequirementsPython 3.7+Dependencies: requests, pandas, openpyxlBashpip install requests pandas openpyxl

⚙️ ConfigurationBefore running the script, update the following constants in robot.py:
PythonPROJECT_ID = "your_project_id_here"
GROUP_IDS  = ["group_id_1", "group_id_2"]

📊 Excel Format (DATA_FILE_CLEAN.xlsx)The input file must contain the following columns:ColumnRequiredDescriptionRespondent IDYesUnique identifier (minimum 7 characters).LanguageYesThe script filters rows specifically containing "Spanish".Respondent Join LinkNoCustom participation link.Respondent System Check LinkNoCustom system check link.💻 UsageRun the script via terminal:Bashpython robot.py

Paste your Bearer Token when prompted (the script automatically handles the "Bearer " prefix if included).Monitor the real-time progress and review the final summary report.📝 Technical NotesCase-Insensitive: Respondent IDs are matched regardless of casing.Security-First: The API token is never hardcoded; it is requested via secure console input during runtime.Optimized Stack: Leverages pandas for high-performance data handling and requests for robust API interaction.
