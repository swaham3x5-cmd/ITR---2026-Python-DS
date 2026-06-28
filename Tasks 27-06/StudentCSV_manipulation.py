import pandas as pd
import numpy as np
import csv

df = pd.read_csv("student_dataset.csv")

# Missing Values
print(df.isnull().sum())

# Duplicate Values
print("Duplicate Values")
duplicates = df[df.duplicated()]
print(duplicates)

# Age mean
print("Age Mean")
print(df.fillna(df["Age"].mean()))

# City Unknown
print("City Unknown")
print(df.fillna("Unknown")["City"])

# Sort Student_ID
print("Sort Student_ID")
print(df.sort_values("Student_ID"))

# Uppercase Name
print("Uppercased Names")
df["Name"]= df["Name"].str.upper()
print(df)

# Date time conversion
df["DateTime"] = pd.to_datetime(df["DateTime"])
print(df)
