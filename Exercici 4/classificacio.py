import numpy as np
import sklearn
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

iris = pd.read_csv("Iris.csv")


iris.isnull().sum()
le = LabelEncoder()
iris['Species'] = le.fit_transform(iris['Species'])
X = iris.drop(columns = ['Species'])
y = iris['Species']


X_train, X_test, y_train, y_test = train_test_split(X,y,
                                                    test_size = 0.2)
model = LogisticRegression()
model.fit(X_train,y_train)
print("Resultados Logistic Regression:",model.score(X_test,y_test))

model2 = KNeighborsClassifier()
model2.fit(X_train,y_train)
print("Resultados KNeighbors", model2.score(X_test,y_test))