import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model, metrics

diabetes = datasets.load_diabetes()

# print(diabetes.keys())
# print(diabetes["DESCR"])
# print(diabetes.DESCR)

diabetes_X_train = diabetes.data
diabetes_X_test = diabetes.data

diabetes_Y_train = diabetes.target
diabetes_Y_test = diabetes.target

model = linear_model.LinearRegression()
model.fit(diabetes_X_train, diabetes_Y_train)
diabetes_Y_predict = model.predict(diabetes_X_test)

print("Mean squared error is: ", metrics.mean_squared_error(diabetes_Y_test, diabetes_Y_predict))
print("Weights/coefficients: ", model.coef_)
print("Intercept: ", model.intercept_)