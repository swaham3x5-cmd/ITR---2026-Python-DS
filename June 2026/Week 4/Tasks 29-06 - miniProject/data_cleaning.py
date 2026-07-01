import pandas as pd

# Load dataset
df = pd.read_csv("shop_data.csv")

Original_rows = len(df)

# Display Dataset
print("=== Original Dataset ===")
print(f"Shape: {df.shape}")
print("\nHead of dataset:\n", df.head())
print("\nInfo:\n")
print(df.info())
print("\nDescription:\n", df.describe())

# Check missing values
C_null = df.isnull().sum().sum()

if C_null > 0:
    # Filling missing values
    df['quantity'] = df['quantity'].fillna(0)
    df['price'] = df['price'].fillna(df['price'].median())
    
    C_null = df.isnull().sum().sum()

# Calculating missing values
nonNULL_count = Original_rows - C_null
Total_nullRemoved = Original_rows - nonNULL_count

# Removing missing values
df.dropna()

# Remove duplicates
print("\n=== Duplicates ===")
duplicates = df[df.duplicated()]
No_duplicates = len(duplicates)
if No_duplicates > 0:
    df = df.drop_duplicates()
    print("Duplicates removed.")

# Remove Outliers
df = df.sort_values("quantity")
Q1 = df["quantity"].quantile(0.25)
Q3 = df["quantity"].quantile(0.75)
IQR = Q3 - Q1

outliers = df[
    (df["quantity"] < (Q1 - 1.5 * IQR)) |
    (df["quantity"] > (Q3 + 1.5 * IQR))
]
No_outliers = len(outliers)

df = df.drop(outliers.index)

# Total Cleaned Rows 
cleaned_rows = Original_rows - Total_nullRemoved - No_outliers - No_duplicates

# Final Report
print("\n----- DATA CLEANING REPORT -----")
print(f"\nOriginal Rows = {Original_rows}")
print(f"\nMissing Values Removed = {Total_nullRemoved}")
print(f"\nDuplicate Rows Removed = {No_duplicates}")
print(f"\nOutliers Removed = {No_outliers}")
print(f"\nFinal Cleaned Rows = {cleaned_rows}")

print("Data cleaned successfully!")

# Save the cleaned dataset
def saveCSV():
    df.to_csv('cleaned_shop_data.csv', index=False)
    print("\nCleaned dataset saved as 'cleaned_shop_data.csv'")
    
saveCSV()