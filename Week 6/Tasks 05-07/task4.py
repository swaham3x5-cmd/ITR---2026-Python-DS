import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({
    "Maths" : [12,23,34,45,56],
    "Science" : [23,34,54,54,65],
    "Python" : [98,87,76,65,54]
})

sns.heatmap(data.corr(), annot = True) # display numerical inside cell if True

plt.title("Coorelation Heatmap")
plt.show()