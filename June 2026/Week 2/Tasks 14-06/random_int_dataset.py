import numpy as np
import matplotlib.pyplot as plt

data = np.random.randint(1,100,11)
print(data)

plt.plot(range(1,11),data[:10])
plt.title("Random Graph")
plt.xlabel("Index")
plt.ylabel("Value")
plt.show()