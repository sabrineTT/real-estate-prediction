from flask import Flask, render_template, request

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

def predict_price(area, surface, rooms, bedrooms, energy, parking, box, elevator, floor, balcony):
    df = pd.read_csv('projet/scraping/logicimmo.csv')
    df = df[['Superficie (m2)', 'Nombre Pieces', 'Nombre Chambres', 'Code Postal',
             'Classe Energetique', 'Etage', 'Terrasse', 'Parking', 'Ascenseur', 'Box',
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
    X_test['Ascenseur'] = elevator
    X_test['Etage'] = floor
    X_test['Terrasse'] = balcony

    model_lin_reg = LinearRegression()
    model_lin_reg.fit(X_train, y_train)

    y_pred = model_lin_reg.predict(X_test)
    print(y_pred)
    return round(y_pred[0])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predicted.html', methods=['POST'])
def predicted():
    if request.method == 'POST':
        area = [int(request.form.get('area'))]
        surface = [int(request.form.get('surface'))]
        rooms = [int(request.form.get('rooms'))]
        bedrooms = [int(request.form.get('bedrooms'))]
        energy = [int(request.form.get('energy'))]
        parking = request.form.get('parking')
        box = request.form.get('box')
        elevator = request.form.get('elevator')
        floor = request.form.get('floor')
        balcony = request.form.get('balcony')

        if box == None:
            box = [-1]
        else:
            box = [1]

        if parking == None:
            parking = [-1]
        else:
            parking = [1]

        if elevator == None:
            elevator = [-1]
        else:
            elevator = [1]

        if balcony == None:
            balcony = [-1]
        else:
            balcony = [1]

        prediction = predict_price(area, surface, rooms, bedrooms, energy, parking, box, elevator, floor, balcony)
    return render_template('predicted.html', prediction=prediction)

@app.route('/about.html')
def about():
    return render_template('about.html')