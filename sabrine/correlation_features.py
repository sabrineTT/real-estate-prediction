import warnings
warnings.filterwarnings('ignore')

#on lit la bdd
import pandas as pd
paris_housing = pd.read_csv("../Julien/logicimmo.csv")
print(paris_housing, "\n")

corr_paris_housing = paris_housing.corr()
print("The correlation DataFrame is:")
print(corr_paris_housing, "\n")
corr_paris_housing.to_csv('matrice_correlation_paris_housing.csv')