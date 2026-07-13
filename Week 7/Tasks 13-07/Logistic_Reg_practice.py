# Importing libraries
import numpy as np
from sklearn.linear_model import LogisticRegression

# Initialization Data
X = np.array([12,33,21,34,54,64,76]).reshape((-1,1))
y = np.array([0,0,0,0,1,1,1])

# Calling the Algorithm and creating fit model
logr = LogisticRegression().fit(X,y)

# Predict from custom input
predicted = logr.predict(np.array([20,31,42,79]).reshape(-1,1))

# Print the prediction
print(predicted)