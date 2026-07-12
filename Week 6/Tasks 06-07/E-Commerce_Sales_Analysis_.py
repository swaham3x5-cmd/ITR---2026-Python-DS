import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import csv

# Load the dataset
df = pd.read_csv('Tasks 06-07\ECOMMERS SALES.csv')

# Store original number of rows
len_df = len(df)

# Clean Data
missing_values = df.isnull().sum().sum()   # Total missing values in whole dataset

print(f"Total Missing Values Found = {missing_values}")

# Drop rows with missing values (only if there are any)
if missing_values > 0:
    df = df.dropna()
    print(f"✅ Missing Values Cleared! Rows removed = {len_df - len(df)}")
else:
    print("✅ No missing values found. Dataset is already clean.")

# Optional: Show current shape
print(f"Dataset shape after cleaning: {df.shape}")

print("-"*25)

# Analysis 
print(f"Description of dataset\n{df.describe()}")
print(f"Information of dataset\n")
print(df.info())

# Sales Trend
best_product = df.groupby('Product_Name')['Quantity'].sum().idxmax()

# Highest Revenue Category
high_rev = df.groupby('Category')['Total_Sales'].sum().idxmax()

# Average Revenue
avg_rev = df

# Report 

# print(f"---- E-Commerce Sales Analysis Report ----")

print(f"Total Sales ={df["Total_Sales"].sum()}") 
 
print(f"Best Selling Product = {best_product}") 

print(f"Highest Revenue from = {high_rev}") 

print(f"Average Revenue = {avg_rev}") 
 
# print(f"Highest Purchases Product ={}")
