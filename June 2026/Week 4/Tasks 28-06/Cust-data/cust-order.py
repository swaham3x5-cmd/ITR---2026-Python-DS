import pandas as pd

customers = pd.read_csv("customer_table.csv")
orders = pd.read_csv("orders_table.csv")

# Tables
print("Customer Table")
print(customers)
print("Orders Table")
print(orders)

# Left Join
L_join = pd.merge(customers, orders, on = "CustomerID", how = "left")
print("Left Join")
print(L_join)

# Inner Join
I_join = pd.merge(customers, orders, on = "CustomerID", how = "inner")
print("Inner Join")
print(I_join)

# Right Join
R_join = pd.merge(customers, orders, on = "CustomerID", how = "right")
print("Right Join")
print(R_join)

# Outer join
O_join = pd.merge(customers, orders, on = "CustomerID", how = "outer")
print("Outer Join")
print(O_join)