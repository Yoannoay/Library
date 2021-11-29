from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
import os, getenv

app = Flask(__name__) # Declare Flask object

app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI=sqlite:///data.db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) 


if __name__=='__main__':
    app.run(debug==True, host='0.0.0.0')