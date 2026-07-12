import seaborn as sns
import matplotlib.pyplot as plt

marks = [10,20,24,32,45,56,32]

sns.boxplot(data = marks)
plt.title("Marks")
plt.show()