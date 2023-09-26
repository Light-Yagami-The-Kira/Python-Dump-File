from sklearn import datasets, linear_model, metrics
breast = datasets.load_breast_cancer()
x = breast.data
y = breast.target

model = linear_model.LinearRegression()
model.fit(x,y)
predicted_y = model.predict(x)
print("Mean absolute error: ", metrics.mean_absolute_error(predicted_y, y))
print("Mean absolute error: ", metrics.mean_absolute_error(y, predicted_y))

print("Mean Squared Error: ", metrics.mean_absolute_error(predicted_y, y))
print("Mean Squared Error: ", metrics.mean_absolute_error(y, predicted_y))

print("Mean Absolute Error: ", metrics.mean_absolute_error(y, predicted_y))
print("Absolute Percentage Error", metrics.mean_absolute_percentage_error(predicted_y, y))