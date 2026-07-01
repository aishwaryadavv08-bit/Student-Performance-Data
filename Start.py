import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns


#Module 1: Data Loading
df=pd.read_csv("student_analysis_v2.csv")
print("First 5 records of the dataset:")
print(df.head(5))
print("\nLast 5 records of the dataset:")
print(df.tail(5))
print("\nShape of the dataset:", df.shape)
print("\nColumns in the dataset:")
print(df.dtypes)

#Module 2: Data Inspection
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

#Module 3: Data Cleaning
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
print("\n SORTING: ")

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

print("\nSorted datasets are shown in the output.")

# Module 8 : Grouping
print("\n GROUPING: ")

# Average Marks by Grade
print("\nAverage Marks by Grade:")
avg_marks_grade = df.groupby("Grade")["Marks"].mean()
print(avg_marks_grade)

# Number of Students in Each Grade
print("\nNumber of Students in Each Grade:")
students_grade = df.groupby("Grade").size()
print(students_grade)

# Average Attendance by Grade
print("\nAverage Attendance by Grade:")
avg_attendance_grade = df.groupby("Grade")["Attendance"].mean()
print(avg_attendance_grade)
print("Grouping done successfully.")


# Module 9 : Statistical Analysis
print("\n STATISTICAL ANALYSIS:")

# Mean
print("\nMean:")
print(df[["Marks", "Attendance", "StudyHours"]].mean())

# Median
print("\nMedian:")
print(df[["Marks", "Attendance", "StudyHours"]].median())

# Mode
print("\nMode:")
print(df[["Marks", "Attendance", "StudyHours"]].mode())

# Standard Deviation
print("\nStandard Deviation:")
print(df[["Marks", "Attendance", "StudyHours"]].std())

# Variance ,It tells how spread out the values are from average.
print("\nVariance:")
print(df[["Marks", "Attendance", "StudyHours"]].var())

# Correlation Matrix, It shows the relationship between different variables in the dataset. The values range from -1 to 1, where 1 indicates a strong positive correlation, -1 indicates a strong negative correlation, and 0 indicates no correlation.
print("\nCorrelation Matrix:")
print(df[["Marks", "Attendance", "StudyHours"]].corr()) 

# Module 10 : Report Generation
print("\n REPORT GENERATION ")

report = {
    "Metric": [
        "Total Students",
        "Passed Students",
        "Failed Students",
        "Highest Marks",
        "Lowest Marks",
        "Average Marks",
        "Average Attendance"
    ],
    "Value": [
        len(df),
        (df["Result"] == "Pass").sum(),
        (df["Result"] == "Fail").sum(),
        df["Marks"].max(),
        df["Marks"].min(),
        round(df["Marks"].mean(), 2),
        round(df["Attendance"].mean(), 2)
    ]
}

# Grade-wise Distribution (Always show A, B, C, D, F)
grade_distribution = df["Grade"].value_counts().reindex(
    ["A", "B", "C", "D", "F"],
    fill_value=0
)

# Add grade distribution to report
for grade, count in grade_distribution.items():
    report["Metric"].append(f"Grade {grade}")
    report["Value"].append(count)

# Convert dictionary to DataFrame
report_df = pd.DataFrame(report)

# Display report
print("\nFinal Report:")
print(report_df)

# Save report as CSV
report_df.to_csv("report.csv", index=False)

print("\nReport generated successfully.")
print("Report saved as 'report.csv'")

# Module 11 : Export Data
print("\n EXPORT DATA TO CSV FILES ")

import os      #It let your program interact with the files and folder present in your computer. 
# Export cleaned dataset
df.to_csv("output/cleaned_data.csv", index=False)

# Export toppers dataset
topper.to_csv("output/topper.csv", index=False)

# Export failed students dataset
failed.to_csv("output/failed.csv", index=False)

# Export report
report_df.to_csv("output/report.csv", index=False)

print("\nAll files have been exported successfully!")

print("Generated Files:")
print("1. output/cleaned_data.csv")
print("2. output/topper.csv")
print("3. output/failed.csv")
print("4. output/report.csv")



print("\n DATA VISUALIZATION ")

# Visualization 12: Grade Distribution
#GRADE DISTRIBUTION BAR CHART
grade_counts = df["Grade"].value_counts().sort_index()

plt.figure(figsize=(6,4))
plt.bar(grade_counts.index, grade_counts.values, color=['green', 'blue', 'orange', 'red', 'purple'])
plt.title("Grade Distribution",fontsize=14,fontweight="bold")
plt.xlabel("Grades")
plt.ylabel("Number of Students")
plt.grid(axis="y")
plt.tight_layout()
plt.savefig("output/grade_distribution.png")
plt.show(block=True) 
plt.close()
 
#visual 2nd added
plt.figure(figsize=(8, 5))
plt.scatter(df["Attendance"], df["Marks"], alpha=0.4, color="darkorange")
plt.title("Attendance vs Marks")
plt.xlabel("Attendance (%)")
plt.ylabel("Marks")
print(" Saved chart_attendance_vs_marks.png")
plt.savefig("output/chart_attendance_vs_marks.png")
plt.show(block=True)
plt.close()


 


