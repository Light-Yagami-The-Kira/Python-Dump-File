from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier  ## importing classifiers
iris = datasets.load_iris()
x = iris.data
y = iris.target
# print(x[0], y[0])
# print(iris.keys())
# print(iris.DESCR)

classifier = KNeighborsClassifier()
classifier.fit(x,y)                        
## classifier.predict uses double dimension arrays
value = (classifier.predict([[1,1,1,1]]))[0]   ## classifier.predict gives a list containing value of the flower so we use list slicing to get the number
dic = {0:"Setosa", 1:"Second Wala", 2:"Virginica"} ## this dictionary contains the outputs to be shown w.r.t the flower number
print(dic[value]) ## prints the output