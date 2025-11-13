# Customer Personality Analysis Data Cleaning Script
# -------------------------------------------------
# Author: Priyanshu Dubey
# Task: Data Analyst Internship - Task 1 (Data Cleaning and Preprocessing)

import pandas as pd

# Load dataset
df = pd.read_csv("marketing_campaign.csv", sep='\t', encoding='latin1')

# 1. Handle missing values
df['Income'] = df['Income'].fillna(df['Income'].median())

# 2. Remove duplicate records
df = df.drop_duplicates()

# 3. Standardize text columns
df['Education'] = df['Education'].str.lower().str.strip()
df['Marital_Status'] = df['Marital_Status'].str.lower().str.strip()

# 4. Convert date format and calculate Age
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], format='%d-%m-%Y', errors='coerce')
df['Age'] = 2025 - df['Year_Birth']
df = df.drop(columns=['Year_Birth'])

# 5. Combine children columns
df['TotalChildren'] = df['Kidhome'] + df['Teenhome']
df = df.drop(columns=['Kidhome', 'Teenhome'])

# 6. Calculate Total Spend
spend_cols = ['MntWines', 'MntFruits', 'MntMeatProducts', 'MntFishProducts', 'MntSweetProducts', 'MntGoldProds']
df['TotalSpend'] = df[spend_cols].sum(axis=1)

# 7. Drop unnecessary columns (constants)
df = df.drop(columns=['Z_CostContact', 'Z_Revenue'])

# 8. Rename columns to be clean and uniform
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Export cleaned dataset
df.to_csv("cleaned_customer_personality.csv", index=False)

print("✅ Data cleaning completed successfully! Cleaned dataset saved as 'cleaned_customer_personality.csv'.")
