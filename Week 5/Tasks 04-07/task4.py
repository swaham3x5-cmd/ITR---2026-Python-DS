import matplotlib.pyplot as plt

student=["Smaran","Rakhi","Mitesh","Swaham"]
marks=[80,75,95,89]

plt.figure(facecolor="skyblue")

plt.plot(   student,marks,
            color="Green",
            #marker= "x",
            marker= "o",
            markeredgecolor="black",
            markerfacecolor="Yellow",
            linewidth=5,
            markersize =5
            
)
plt.title("Student marks")
plt.xlabel("Student")
plt.ylabel("marks")
plt.grid(axis="y",linestyle="--")
plt.show()