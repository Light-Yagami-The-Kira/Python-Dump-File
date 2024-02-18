from sklearn import datasets
import numpy as np

iris = datasets.load_iris()
digits = datasets.load_digits()
# print(iris["data"])
iris_data = np.array(iris.data)
iris_target = np.array(iris.target)
print(iris_target)
print(iris_data)
