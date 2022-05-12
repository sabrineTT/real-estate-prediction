from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort
import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY'] = 'projet2022'

@app.route('/')
def index():
    return render_template('index.html')
