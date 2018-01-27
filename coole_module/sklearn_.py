import pandas as pd
import numpy as np

from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split


data = pd.read_csv('iris.data.csv',header=None)


x = data[[0,1,2,3]]
y = data[4]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.33)


cls = KNeighborsClassifier(n_neighbors=3)
cls.fit(x_train,y_train)



print(cls.score(x_test,y_test))