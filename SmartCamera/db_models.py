from . import db
from flask_login import UserMixin

#can add alerts as a seperate class with 1:N realtionship
class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))