import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ============================
# 1. LOAD DATASET
# ============================
df = pd.read_csv('ECOMMERS SALES.csv')
print(f"Shape: {df.shape}")

# ============================
# 2. CLEAN DATA
# ============================
len_df = len(df)
missing_values = df.isnull().sum().sum()

print(f"Total Missing Values Found = {missing_values}")

if missing_values > 0:
    df = df.dropna()
    print(f"✅ Missing Values Cleared! Rows removed = {len_df - len(df)}")
else:
    print("✅ No missing values found. Dataset is already clean.")

print(f"Dataset shape after cleaning: {df.shape}")
print("-" * 50)

# ============================
# 3. CALCULATIONS FOR REPORT
# ============================
total_sales = df["Total_Sales"].sum()

best_product = df.groupby('Product_Name')['Quantity'].sum().idxmax()

highest_rev_category = df.groupby('Category')['Total_Sales'].sum().idxmax()

avg_rev_per_category = df.groupby('Category')['Total_Sales'].mean().round(2)

best_customer_segment = df.groupby('Customer_Type')['Quantity'].sum().idxmax()

# ============================
# 4. PRINT REPORT
# ============================
print("\n" + "="*65)
print("----- E-COMMERCE SALES ANALYSIS REPORT -----")
print("="*65)
print(f"Total Sales = {total_sales}")
print(f"Best Selling Product = {best_product}")
print(f"Highest Revenue Category = {highest_rev_category}")
print(f"Average revenue from each category =\n{avg_rev_per_category}")
print(f"Customer Segment with Highest Purchases = {best_customer_segment}")
print("="*65)

# ============================
# 5. PLOTTINGS
# ============================

# 1. Sales Trend Line Chart - Region, Total Sales
plt.figure(figsize=(10, 6))
region_sales = df.groupby('Region')['Total_Sales'].sum().sort_values(ascending=False)
plt.plot(region_sales.index, region_sales.values, color='skyblue')
plt.title('Sales by Region (Total Sales)')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)

plt.show()

# 2. Product Sales Bar Chart - Category, Total Sales
plt.figure(figsize=(10, 6))
category_sales = df.groupby('Category')['Total_Sales'].sum().sort_values(ascending=False)
sns.barplot(x=category_sales.index, y=category_sales.values)
plt.title('Product Sales by Category')
plt.xlabel('Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)

plt.show()

# 3. Revenue Heatmap
plt.figure(figsize=(12, 7))
sns.heatmap(
    df[["Total_Sales", "Quantity"]].corr(),
    annot = True
)
plt.title('Revenue Heatmap by Category and Region')

plt.show()

# 4. Customer Segmentation Chart - Pie Chart
plt.figure(figsize=(8, 8))
customer_sales = df.groupby('Customer_Type')['Total_Sales'].sum()

plt.pie(customer_sales.values, 
        labels=customer_sales.index, 
        colors=["yellow", "blue", "red", "green"],
        )

plt.title('Customer Segmentation by Revenue', fontsize=14)
plt.legend(customer_sales.index, title="Customer Type", loc="best")
plt.axis('equal')
plt.show()

# 5. Profit Distribution Boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x='Category', y='Total_Sales', data=df)
plt.title('Sales Distribution by Category (Boxplot)')
plt.xlabel('Category')
plt.ylabel('Total Sales')

plt.show()