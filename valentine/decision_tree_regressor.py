# importing the libraries
import pandas as pd
import numpy as np
# Reading the dataset using pandas librarie
dataset = pd.read_csv('winequality-red.csv')


# shape of the dataset
print("les nombre de lignes x colonnes : \n", dataset.shape)
# Type of the dataset
print('type de chaque colonne:\n',dataset.dtypes)


# checking for the null value
print('nombre de valleur nulle dans chaque colonne:\n',dataset.isna().sum())
# Counting the number of null values
print('nombre de valeur nulle :', dataset.isna().sum().sum())


# encoding the categorical data
dataset = pd.get_dummies(dataset)


# independent variables
X = dataset.iloc[:, :-1].values
# dependent variable
y = dataset.iloc[:, -1:].values


# spliting the dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test  = train_test_split(X, y, test_size=0.2, random_state = 0)


# using feature scaling
from sklearn.preprocessing import StandardScaler
X_sc = StandardScaler()
X_train = X_sc.fit_transform(X_train)


# training the dataset
from sklearn.tree import DecisionTreeRegressor
regrassor = DecisionTreeRegressor(random_state = 0)
regrassor.fit(X_train, y_train)


# predictzing the result
pred = regrassor.predict(X_sc.transform(X_test))


# Accuracy of the algorithm
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, pred))