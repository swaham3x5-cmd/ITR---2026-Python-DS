import pandas as pd

df = pd.read_csv("employee_salary_dataset.csv")
# print(df)

df = df.sort_values("Monthly_Salary")
print(df)

Q1 = df["Monthly_Salary"].quantile(0.25)
Q3 = df["Monthly_Salary"].quantile(0.75)

IQR = Q3 - Q1

outliers = df[
    (df["Monthly_Salary"] < (Q1 - 1.5 * IQR)) |
    (df["Monthly_Salary"] > (Q3 + 1.5 * IQR))
]

print(outliers)