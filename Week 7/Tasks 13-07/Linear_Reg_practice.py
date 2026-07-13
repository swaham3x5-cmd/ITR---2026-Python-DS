# Importing libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Initialization Data
X = np.array([12,33,21,34,54,64,76]).reshape((-1,1))
y = np.array([10,30,25,34,56,61,72])

# Creating fit model
model = LinearRegression().fit(X,y)

# Calculate R²
print("R² score:", model.score(X,y))

# Predictions
y_pred = model.predict(X)

# Plot
plt.scatter(X, y, color = 'Green',
            label = 'Actual Data')
plt.plot(X, y_pred, color = 'red',
         linewidth = 1,
         label = 'Regression Line')

plt.show()