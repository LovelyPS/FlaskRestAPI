from datetime import timedelta
from flask import Flask
from flask_restful import Api
import os
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app=Flask(__name__)

basedir=os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'appdb.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

app.secret_key = "secret key"
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(minutes=10)

db=SQLAlchemy(app)
api=Api(app)
cors = CORS(app)
ma=Marshmallow(app)
          

UPLOAD_FOLDER=os.path.join(basedir,'media')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER