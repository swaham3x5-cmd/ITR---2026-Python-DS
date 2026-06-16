import numpy as np
import matplotlib.pyplot as plt

sales = np.array([100, 150, 200, 250, 300])

print("Sales mean:", np.mean(sales))
print("Sales median:", np.median(sales))
print("Sales standard deviation:", np.std(sales))

months = np.array(["Jan", "Feb", "Mar", "Apr", "May"])

plt.bar(months, sales)
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales")
plt.show()

np.save("sales_data.npy", sales)
loaded_sales = np.load("sales_data.npy")
print("Loaded sales data:", loaded_sales)