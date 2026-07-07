import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("Visualize Sales Trends.csv")

print("MONTHLY SALES DATA")

plt.figure(facecolor = "purple")

plt.plot(
    data["Month"],
    data["Sales"],
    
    color = "pink",
    marker = "x",
    markeredgecolor = "black",
    markerfacecolor = "yellow",
    linewidth = 3
)

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.grid(axis = "x", linestyle = "--")

plt.show()