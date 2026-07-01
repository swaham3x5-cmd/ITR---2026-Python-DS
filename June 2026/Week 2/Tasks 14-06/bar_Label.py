import numpy as np
import matplotlib.pyplot as plt

data = np.random.randint(1,100,10)
print(data)

bar = plt.bar(range(1,11), data)

plt.bar_label(bar)

plt.bar(range(1,11), data)
plt.title("Random Graph")
plt.xlabel("Index")
plt.ylabel("Value")
plt.grid()

plt.show()