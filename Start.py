import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#module 1: Data Loading
df=pd.read_csv("student_analysis_v2.csv")
print("First 5 records of the dataset:")
print(df.head(5))
print("\nLast 5 records of the dataset:")
print(df.tail(5))
print("\nShape of the dataset:", df.shape)
print("\nColumns in the dataset:")
print(df.dtypes)

#module 2: Data Inspection
print("\n MISSING VALUES IN THE DATASET:")
print(df.isnull().sum())
print("\n DUPLICATE RECORDS IN THE DATASET:")
print(df.duplicated().sum())
print("\n  DESCRIPTIVE STATISTICS OF THE DATASET:")
print(df.describe())
print("\n MEMORY USAGE OF THE DATASET:")
print(df.memory_usage())
print("\n SUMMARY INFORMATION OF THE DATASET:")
print(df.info())

#module 3: Data Cleaning
print("\n DATA CLEANING:")
#Removing duplicate records
df.drop_duplicates()

#Handle missing data
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())
df["StudyHours"] = df["StudyHours"].fillna(df["StudyHours"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df["Name"] = df["Name"].fillna("Unknown")

# Remove invalid entries (Blank Names)
df = df[df["Name"].str.strip() != ""]

# Validate Attendance (0 to 100)
df = df[(df["Attendance"] >= 0) & (df["Attendance"] <= 100)]

# Validate Study Hours (0 to 24)
df = df[(df["StudyHours"] >= 0) & (df["StudyHours"] <= 24)]

# Validate Marks (0 to 100)
df = df[(df["Marks"] >= 0) & (df["Marks"] <= 100)]

# Save the cleaned dataset
df.to_csv("cleaned_data.csv", index=False)

print("\nData cleaning completed successfully.")
print("Cleaned dataset saved as 'cleaned_data.csv'")
