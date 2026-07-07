import seaborn as sns
import matplotlib.pyplot as plt

student=["Smaran","Rakhi","Mitesh","Swaham"]
marks=[80,75,65,89]

sns.barplot(x=student,y=marks)
plt.title("Student marks graph")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.show()