import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv

df = pd.read_csv("Employee.csv")

def Disp_empDetails():
    print(f"Details of all Employees: \n{df}")

def Disp_avgSalary():
    return df["Monthly_Salary"].mean()

def Disp_Hsalary():
    return df["Monthly_Salary"].max()

def Disp_Lsalary():
    return df["Monthly_Salary"].min()

def Disp_dept_salary_analysis():
    return df.groupby("Department")["Monthly_Salary"].mean()
    
def handle_missing_values():
    df.isnull()
    df.fillna(0,inplace = True)[["Age","Experience_Years","Monthly_Salary"]]
    df.fillna("Unknown")[["Name","Department","Education_Level","Gender","City"]]

def sort_salary():
    return df.sort_values("Monthly_Salary")