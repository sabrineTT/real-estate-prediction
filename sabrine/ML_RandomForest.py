import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# ------ 1 : Data Pre-Processing ------

#on lit la bdd
import pandas as pd
paris_housing = pd.read_csv("../Julien/logicimmo.csv")
#paris_housing = df[["Superficie (m2)", "Nombre Pieces", "Nombre Chambres", "Box", "Prix (Euros)"]]

#Extracting Independent and dependent Variable
"""X = paris_housing.drop('Prix (Euros)', axis=1).values
y = paris_housing["Prix (Euros)"].values"""
# independent variables
X = paris_housing.iloc[:, [True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, True, True]].values

# dependent variable
y = paris_housing.iloc[:, [False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False]].values

# Splitting the dataset into training and test set.
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test  = train_test_split(X, y, test_size=0.2, random_state = 0)

#feature Scaling
from sklearn.preprocessing import StandardScaler
st_x = StandardScaler()
X_train = st_x.fit_transform(X_train)
X_test = st_x.transform(X_test)

# ------ 2 : Fitting the Random Forest algorithm to the training set ------

#Fitting Decision Tree classifier to the training set
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=10, random_state=0)
regressor.fit(X_train, y_train)

# ------ 3 : Predicting the Test Set result ------

#Predicting the test set result
y_pred = regressor.predict(X_test)

# ------ 4 : Performance metrics ------

from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test, y_pred)
rmse = mse**.5
print(mse)
print(rmse)

"""# ------ 4 : Creating the Confusion Matrix ------

#Creating the Confusion matrix
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
cm = confusion_matrix(y_test, y_pred)
print(cm)
#print(classification_report(y_test, y_pred))

# ------ 5 : VISUALIZING THE RANDOM FOREST REGRESSION RESULTS -----
X_grid = np.arange(min(X_test), max(X_test), 0.01)
X_grid = X_grid.reshape((len(X_grid), 1))

plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_grid, y_pred, color = 'blue')
plt.title('Random Forest Classification')
plt.xlabel('Features')
plt.ylabel('Price')
plt.show()"""
