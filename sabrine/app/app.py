from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

import pandas as pd

def get_db_connection():
    df = pd.read_csv('.../Julien/logicimmo.csv')
    return df

app = Flask(__name__)
app.config['SECRET_KEY'] = 'projet2022'

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        area = int(request.form.get('area'))
        surface = int(request.form.get('surface'))
        rooms = int(request.form.get('rooms'))
        bedrooms = int(request.form.get('bedrooms'))
        energy = int(request.form.get('energy'))
        parking = request.form.get('parking')
        box = request.form.get('box')

        if not area:
            flash('Area is required!')
        else:
            print(area)
            print(surface)
            print(rooms)
            print(bedrooms)
            print(energy)
            print(parking)
            print(box)
    return render_template('index.html')



X = df.drop('Prix (Euros)', axis = 1)
y = df['Prix (Euros)']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

model_lin_reg = LinearRegression()
model_lin_reg.fit(X_train,y_train)
score_lin_reg = model_lin_reg.score(X_test,y_test)
score_list.append(score_lin_reg)
score_lin_reg

linear_selector = SelectFromModel(LinearRegression(),threshold='mean')
linear_selector.fit_transform(X,y)
linear_selector.get_support()

y_pred = model_lin_reg.predict(X_test)




















"""import matplotlib.pyplot as plt
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

from sklearn.linear_model import BayesianRidge
from sklearn.feature_selection import SelectFromModel
from sklearn.metrics import *

df = pd.read_csv('.../Julien/logicimmo - Copie.csv')
X = df.drop('Prix (Euros)', axis = 1)
y = df['Prix (Euros)']

df.sort_values(by=['Prix (Euros)'], ascending=False).head(15)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

MAE_list = []
RMSE_list = []
median_abs_err_list = []
model_list = []
score_list = []
mean_error_list = []
r2_list = []
max_error_list = []
variance_list = []
percentage_error_list = []

model_bayesian = BayesianRidge()
model_bayesian.fit(X_train, y_train)
score_bayesian = model_bayesian.score(X_test, y_test)
score_list.append(score_bayesian)
score_bayesian

cross_val_score(model_bayesian, X, y, cv=3)

selector_bayesian = SelectFromModel(BayesianRidge(),threshold='mean')
selector_bayesian.fit_transform(X,y)
selector_bayesian.get_support()

y_pred = model_bayesian.predict(X_test)
print('MAE : ', mean_absolute_error(y_test,y_pred))
print('RMSE : ', np.sqrt(mean_squared_error(y_test, y_pred)))
print('median absolut error : ', median_absolute_error(y_test, y_pred))
print('R2 score : ', r2_score(y_test, y_pred))
print('Max error : ', max_error(y_test, y_pred))
print('Explained variance : ', explained_variance_score(y_test, y_pred))
print('mean abs percentage error : ', mean_absolute_percentage_error(y_test, y_pred))

MAE_list.append(mean_absolute_error(y_test,y_pred))
RMSE_list.append(np.sqrt(mean_squared_error(y_test, y_pred)))
median_abs_err_list.append(median_absolute_error(y_test, y_pred))
r2_list.append(r2_score(y_test, y_pred))
max_error_list.append(max_error(y_test, y_pred))
variance_list.append(explained_variance_score(y_test, y_pred))
percentage_error_list.append(mean_absolute_percentage_error(y_test, y_pred))
model_list.append("Bayesian \nRidge")

error_hist = np.abs(y_test - y_pred)
mean_error_list.append(error_hist.mean())
plt.hist(error_hist, bins=50)
plt.show

def prediction():
    return 'cc'"""