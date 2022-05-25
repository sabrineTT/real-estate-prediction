from flask import Flask, render_template, request, url_for, flash, redirect

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

app = Flask(__name__)
app.config['SECRET_KEY'] = 'projet2022'

def predicted_price(area, surface, rooms, bedrooms, energy, parking, box):
    df = pd.read_csv('../logicimmo.csv')
    # df = df[['Superficie (m2)', 'Nombre Pieces', 'Nombre Chambres',
    #         'Code Postal', 'Classe Energetique', 'Terrasse',
    #         'Parking', 'Cave', 'Ascenseur', 'Box', 'Prix (Euros)']]
    df = df[['Superficie (m2)', 'Nombre Pieces', 'Nombre Chambres',
             'Code Postal', 'Classe Energetique', 'Parking', 'Box',
             'Prix (Euros)']]

    X = df.drop('Prix (Euros)', axis=1)
    y = df['Prix (Euros)']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1)

    X_test['Code Postal'] = area
    X_test['Superficie (m2)'] = surface
    X_test['Nombre Pieces'] = rooms
    X_test['Nombre Chambres'] = bedrooms
    X_test['Classe Energetique'] = energy
    X_test['Parking'] = parking
    X_test['Box'] = box

    model_lin_reg = LinearRegression()
    model_lin_reg.fit(X_train, y_train)

    y_pred = model_lin_reg.predict(X_test)
    print(y_pred)
    return render_template('index.html')

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        area = [int(request.form.get('area'))]
        surface = [int(request.form.get('surface'))]
        rooms = [int(request.form.get('rooms'))]
        bedrooms = [int(request.form.get('bedrooms'))]
        energy = [int(request.form.get('energy'))]
        parking = request.form.get('parking')
        box = request.form.get('box')

        if box == None:
            box = [-1]
        else:
            box = [1]

        if parking == None:
            parking = [-1]
        else:
            parking = [1]

        predicted_price(area, surface, rooms, bedrooms, energy, parking, box)
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')