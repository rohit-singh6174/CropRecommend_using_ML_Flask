from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY']='croppredictions'
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:''@localhost/crop_prediction'
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False

db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager =LoginManager(app)

from cropprediction import routes