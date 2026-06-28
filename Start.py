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