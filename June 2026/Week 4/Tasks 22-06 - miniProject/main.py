import Employee_dataset_operation as ED

print("1.   HR Data Analysis Report")
print("2.   Sort Employee Salaries")
print("3.   Print all Employee details")
print("4.   Exit")

option = 0

while option != 4 :
    
    option = int(input("Enter your desired operation: "))
    
    try:
        ED.handle_missing_values()

        
        if option == 1:
            print(f"\n----- HR DATA ANALYSIS REPORT -----")
            print(f"\nTotal Employees = {ED.df["Empid"].count()}")
            print(f"\nAverage Salary = {ED.Disp_avgSalary()}")
            print(f"\nHighest Salary = {ED.Disp_Hsalary()}")
            print(f"\nLowest Salary = {ED.Disp_Lsalary()}")
            print(f"\nDepartment-wise Average Salary:\n{ED.Disp_dept_salary_analysis()}")
    
        elif option == 2:
            print(f"Sorted by salaries(ascending):\n",ED.sort_salary())
            
        elif option == 3:
            print(ED.Disp_empDetails())
            
        elif option == 4:
            break

    except ValueError:
        print("Enter valid option!")