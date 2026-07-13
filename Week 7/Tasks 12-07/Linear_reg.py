# Importing libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Initializing Data
X = np.array([5,15,25,35,45,55]).reshape((-1,1))
y = np.array([5,20,14,32,22,38])

# Creating Fit Model
model = LinearRegression().fit(X,y)     # fit() = best fit straight line for data

# View Results
print("Intercept:", model.intercept_)
print("Slope:",model.coef_)             # y change for each unit change in X
print("R² score:", model.score(X,y))    # R² = variance in data / R=1 -> Perfect, R=0 -> No linear relation

# Predictions
y_pred = model.predict(X)
print("Predictions:", y_pred)

# Plot
plt.figure(figsize=(5,4))
plt.scatter(X, y, color='blue', 
            label = 'Actual Data')
plt.plot(X, y_pred, color = 'red', 
         linewidth = 2, label = 'Regression Line')

plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Linear Regression Example")

plt.legend()
plt.grid(True)
plt.show()