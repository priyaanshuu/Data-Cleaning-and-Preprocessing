# 🧹 Customer Personality Analysis – Data Cleaning & Preprocessing

### 🎯 **Objective**

To clean and preprocess the raw **Customer Personality Analysis** dataset by identifying and fixing missing values, duplicates, and inconsistent formats using **Python (Pandas)**.

---

###  **Overview**

This project is part of the **Data Analyst Internship – Task 1** focusing on **data cleaning and preprocessing**.
The dataset provides customer demographic and behavioral information for marketing analysis.

---

###   **Steps Performed**

1. **Handled Missing Values**

   * Filled missing `Income` values using the **median**.
2. **Removed Duplicates**

   * Checked and removed duplicate rows.
3. **Standardized Text Fields**

   * Lowercased and trimmed text in `Education` and `Marital_Status`.
4. **Fixed Date Formats**

   * Converted `Dt_Customer` to datetime (`dd-mm-yyyy`).
5. **Derived New Columns**

   * Added `Age` = 2025 – `Year_Birth`.
   * Added `TotalChildren` = `Kidhome` + `Teenhome`.
   * Added `TotalSpend` = sum of all product spend columns.
6. **Removed Unnecessary Columns**

   * Dropped constant columns `Z_CostContact` and `Z_Revenue`.
7. **Renamed Columns**

   * Made all column names lowercase with underscores for clarity.

---

### 📊 **Final Output**

| File                               | Description                        |
| ---------------------------------- | ---------------------------------- |
| `cleaned_customer_personality.csv` | Final cleaned dataset              |
| `README.md`                        | Summary of all cleaning steps      |
| `data_cleaning.py`                 | Python code used for data cleaning |

---

###  **Tech Stack**

* **Language:** Python 3.11
* **Libraries:** Pandas, NumPy
* **Environment:** Jupyter Notebook / VS Code

---

###  **Key Learnings**

* Data preprocessing fundamentals
* Handling missing and duplicate values
* Feature engineering and data standardization
* Real-world dataset cleaning using Pandas


