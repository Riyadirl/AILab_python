import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# Load iris dataset
iris_df = pd.read_csv('iris.csv')

# Create X and y numpy arrays
X = iris_df[['sepal.length', 'sepal.width',
             'petal.length', 'petal.width']].values
y = np.where(iris_df['variety'] == 'Setosa', 0, 1)

# Shuffle X and y together
np.random.seed(42)
shuffle_indices = np.random.permutation(len(X))
X, y = X[shuffle_indices], y[shuffle_indices]

# Split into train and test sets
train_size = int(0.8 * len(X))
X_train, X_test = X[:train_size], X[train_size:]
y_train, y_test = y[:train_size], y[train_size:]

# Define k-NN algorithm for predicting test set labels


def predict_labels(X_train, y_train, X_test, k):
    y_test_predicted = np.zeros(X_test.shape[0])
    for i in range(X_test.shape[0]):
        distances = np.sqrt(np.sum((X_train - X_test[i])**2, axis=1))
        nearest_indices = np.argsort(distances)[:k]
        nearest_labels = y_train[nearest_indices]
        y_test_predicted[i] = np.bincount(nearest_labels).argmax()
    return y_test_predicted


# Predict test set labels using k-NN with k=5
y_test_predicted = predict_labels(X_train, y_train, X_test, k=5)

# Calculate accuracy of predictions
accuracy = np.mean(y_test_predicted == y_test)
print("Test Accuracy: {:.2f}%".format(accuracy*100))
