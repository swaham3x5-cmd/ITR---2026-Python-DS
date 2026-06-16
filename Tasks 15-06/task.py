import numpy as np
import matplotlib.pyplot as plt

data = np.random.randint(1, 50, 10)
print(data)

# Create color list for each bar
colors = []
for i in range(10):
    if data[i] >= 35:
        colors.append('red')
    elif data[i] >= 25:
        colors.append('green')
    elif data[i] >= 15:
        colors.append('blue')
    else:
        colors.append('black')

# Plot with color variation
bar = plt.bar(range(1, 11), data, color=colors)
plt.bar_label(bar)

plt.title("Random Graph")
plt.xlabel("Index")
plt.ylabel("Value")
plt.grid()

plt.show()