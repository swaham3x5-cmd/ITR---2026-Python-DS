import numpy as np
import matplotlib.pyplot as plt

sales = np.array([120, 160, 100, 80, 120])
brands = np.array(['iPhone', 'Vivo', 'Oppo', 'Lava', 'iQOO'])

# Total sales
total_sales = np.sum(sales)
print(f'Total sales: {total_sales}')

# Average sales
average_sales = np.mean(sales)
print(f'Estimated sales: {average_sales}')

# Standard deviation of sales
std_dev_sales = np.std(sales)
print(f'Standard deviation of sales: {std_dev_sales}')

# Plotting sales data
plt.bar(brands, sales)

plt.xlabel('Mobile Brands')
plt.ylabel('Sales')
plt.title('Mobile Sales Analysis ')

plt.show()