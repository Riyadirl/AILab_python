import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split


# Load iris dataset
iris = pd.read_csv('iris.csv')

# Convert labels to 0s and 1s
iris['species'] = (iris['species'] == 'versicolor').astype(int)

# Split dataset into features and labels
X = iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].values
y = iris['species'].values

# Shuffle X and y together
idx = np.random.permutation(len(X))
X, y = X[idx], y[idx]

# Split into train and test sets
split_idx = int(0.8 * len(X))
X_train, y_train = X[:split_idx], y[:split_idx]
X_test, y_test = X[split_idx:], y[split_idx:]

# K-Nearest Neighbors algorithm
k = 5

y_test_predicted = np.zeros(len(X_test))

for i in range(len(X_test)):
    x_test = X_test[i]
    dist = np.linalg.norm(X_train - x_test, axis=1)
    min_dist_indices = np.argsort(dist)[:k]
    y_neighbor = y_train[min_dist_indices]
    y_test_predicted[i] = np.bincount(y_neighbor).argmax()

# Calculate accuracy
accuracy = np.mean(y_test_predicted == y_test)

print(f"Test accuracy: {accuracy:.2f}")
