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
df["Name"] = df["Name"].fillna("Unknown") #fillna is method of pandas that let u fill missing values

# Remove invalid entries (Blank Names) makes sure that data is relevant
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

# Module 4 : Data Transformation


print("\n  DATA TRANSFORMATION = ")

# Create Grade column
def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

df["Grade"] = df["Marks"].apply(grade)

# Create Result column
df["Result"] = df["Marks"].apply(lambda x: "Pass" if x >= 40 else "Fail")

# Create Performance Score
df["Performance_Score"] = (
    (df["Marks"] * 0.6) +
    (df["Attendance"] * 0.2) +
    (df["StudyHours"] * 2)
)

print(df.head())

# Module 5 : Data Filtering


print("\n DATA FILTERING ")

# Top-performing students (Grade A)
topper = df[df["Grade"] == "A"]

# Failed students(F grade)
failed = df[df["Grade"] == "F"]

# Students with attendance below 75%
low_attendance = df[df["Attendance"] < 75]

# Students studying more than 8 hours
more_study = df[df["StudyHours"] > 8]

# Save filtered datasets
topper.to_csv("topper.csv", index=False)
failed.to_csv("failed.csv", index=False)
low_attendance.to_csv("low_attendance.csv", index=False)
more_study.to_csv("more_than_8_hours.csv", index=False)

print("Topper dataset saved as topper.csv")
print("Failed dataset saved as failed.csv")
print("Low attendance dataset saved as low_attendance.csv")
print("More than 8 hours study dataset saved as more_than_8_hours.csv")

# Module 6 : Data Analysis
print("\n  DATA ANALYSIS= ")

# Average Marks
print("Average Marks:", df["Marks"].mean())

# Highest Marks
print("Highest Marks:", df["Marks"].max())

# Lowest Marks
print("Lowest Marks:", df["Marks"].min())

# Average Attendance
print("Average Attendance:", df["Attendance"].mean())

# Average Study Hours
print("Average Study Hours:", df["StudyHours"].mean())

# Pass Percentage
pass_percentage = (df["Result"] == "Pass").sum() / len(df) * 100
print("Pass Percentage:", round(pass_percentage, 2), "%")

# Fail Percentage
fail_percentage = (df["Result"] == "Fail").sum() / len(df) * 100
print("Fail Percentage:", round(fail_percentage, 2), "%")

# Grade Distribution
print("\nGrade Distribution:")
print(df["Grade"].value_counts())

#Module 7 : Data Sorting
print("\n===== SORTING =====")

# Sort by Marks (Highest to Lowest)
sorted_marks = df.sort_values(by="Marks", ascending=False)
print("\nStudents Sorted by Marks (Highest to Lowest):")
print(sorted_marks)

# Sort by Attendance (Highest to Lowest)
sorted_attendance = df.sort_values(by="Attendance", ascending=False)
print("\nStudents Sorted by Attendance (Highest to Lowest):")
print(sorted_attendance)

# Sort by Study Hours (Highest to Lowest)
sorted_study_hours = df.sort_values(by="StudyHours", ascending=False)
print("\nStudents Sorted by Study Hours (Highest to Lowest):")
print(sorted_study_hours)

print("\nSorted datasets saved successfully.")
