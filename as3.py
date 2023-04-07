import numpy as np
import panda as pd
# from sklearn.model_selection import train_test_split
################################
# Load iris dataset
iris_df = pd.read_csv('iris.csv')

# Create X and y numpy arrays
# X = iris_df[['sepal.length', 'sepal.width',
#    'petal.length', 'petal.width']].values
# y = np.where(iris_df['variety'] == 'Setosa', 0, 1)
