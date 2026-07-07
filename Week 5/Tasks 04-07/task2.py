import matplotlib.pyplot as plt

student=["Smaran","Rakhi","Mitesh","Swaham"]
marks=[80,75,65,89]

plt.bar(student,marks,
       color="Orange",
       edgecolor="DarkBlue",
       linewidth=2)

plt.title("Students Marks graph")
plt.xlabel("Student")
plt.ylabel("Marks")

plt.show()