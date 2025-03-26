Data Cleaning App

📌 Overview

This Data Cleaning Application is a Python-based script that automates the process of cleaning datasets stored in CSV or Excel format. It performs essential cleaning tasks such as:
✅ Detecting and removing duplicate records✅ Identifying and handling missing values✅ Exporting cleaned datasets for further analysis✅ Saving duplicate records separately for review✅ Adding random processing delays for a realistic experience 😉

🚀 Installation

🔹 Prerequisites

Make sure you have Python 3.x installed along with the following dependencies:

pip install pandas numpy openpyxl xlrd

🔧 Usage

🏃 Run the Script

Execute the script by running:

python data_cleaning_app.py

✏️ Input Parameters

When prompted, enter:
1️⃣ Dataset Path → Full path to the CSV or Excel file2️⃣ Dataset Name → A reference name for output files

📂 Output Files

After processing, the application will generate:
📌 <dataset_name>_Duplicate.csv → Contains duplicate records (if any)📌 <dataset_name>_Clean_data.csv → The cleaned dataset with duplicates removed and missing values handled

🔍 Example

User Input:

Please enter dataset path: data/wallmart.xlsx
Enter the dataset name: jan_sales

Generated Files:

jan_sales_Duplicate.csv
jan_sales_Clean_data.csv

🛠️ Data Cleaning Process

✔ Handling Duplicates:

Identifies and removes duplicate records

Saves duplicate records separately for review

✔ Handling Missing Values:

Numerical Columns: Replaces missing values with the mean of the column

Non-Numerical Columns: Drops rows containing missing values

✔ Error Handling:

Checks if the file path exists and prompts the user to re-enter if incorrect

Detects unsupported file formats and exits gracefully

🎯 Future Enhancements

🔹 Add support for JSON and Parquet files🔹 Provide custom missing value handling options🔹 Create a GUI version for easier interaction

✨ Author : ANIKET D MAHALLE

👨‍💻 Name📧 MAHALLEANIKET22@GMAIL.COM

📜 License

This project is licensed under the MIT License.


