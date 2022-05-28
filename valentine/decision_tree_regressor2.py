# importing the libraries
import pandas as pd
import numpy as np
# Reading the dataset using pandas librarie
dataset = pd.read_csv('../Julien/logicimmo - Copie.csv')


# shape of the dataset
print("les nombre de lignes x colonnes : \n", dataset.shape)
# Type of the dataset
print('type de chaque colonne:\n',dataset.dtypes)


# checking for the null value
print('nombre de valleur nulle dans chaque colonne:\n',dataset.isna().sum())
# Counting the number of null values
print('nombre de valeur nulle :', dataset.isna().sum().sum())


# encoder les variables (sert si on a des variables qui ne sont pas des entiers ou des nombres)
dataset = pd.get_dummies(dataset)


# independent variables
X = dataset.iloc[:, [True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True]].values
print('Mes variables test :\n', X[:5, :])

# dependent variable
y = dataset.iloc[:, [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False]].values
print('Ma variable test :\n', y[:5, :])

# je divise ma dataset :
# X_train : les variables (sauf prix) qui vont servir a entrainer le modele (20% du tableau)
# X_test : les 80% sur lequel on va tester le modele
# Y_train : 20% du tableau (le prix uniquement) qui va etre comparer a ce que le modele dit lors du test
# Y_test : 80% dont on ne se sert que si on veut calculer le taux d'accuracy.


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test  = train_test_split(X, y, test_size=0.2, random_state = 0)


# using feature scaling sert a normaliser les variables indépendantes
from sklearn.preprocessing import StandardScaler
X_sc = StandardScaler()
X_train = X_sc.fit_transform(X_train)


# training the dataset
from sklearn.tree import DecisionTreeRegressor
regrassor = DecisionTreeRegressor(random_state = 0)
regrassor.fit(X_train, y_train) # je creer mon modele et je l'entraine


# je predis les prix avec le reste du tableau (80%)
pred = regrassor.predict(X_sc.transform(X_test))


# Accuracy of the algorithm
from sklearn.metrics import accuracy_score
print(accuracy_score(pred, y_test))

# l'accuracy compare si le resultat du test et la valeur reel correspondent
# c'est un pourcentage
# ici il vaut 2% (pas terrible) mais peut etre que c'est pcq
# si le prix prédit et le vrai prix sont pas les memes ca compte faux

