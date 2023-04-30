from cropprediction import db,login_manager #login_manager # it will look from _init_ file by default in that it will look for db variable if it there it will import   
from datetime import date
from flask_login import UserMixin
from flask import url_for, redirect


@login_manager.user_loader
def load_user(user_id):
    return Farmers.query.get(user_id)


class Farmers(db.Model,UserMixin):
    id =db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(40),unique=False,nullable=False)
    phone=db.Column(db.BigInteger,unique=True,nullable=False)
    gender=db.Column(db.String(10),unique=False,nullable=False)
    district=db.Column(db.String(20),unique=False,nullable=False)
    farmerid=db.Column(db.String(20),unique=True,nullable=False)
    username=db.Column(db.String(20),unique=True,nullable=False)
    password=db.Column(db.String(255),nullable=False)

    def __repr__(self):
        return f'\nname :{self.name},\nphone : {self.phone},\ngender : {self.gender},\ndistrict : {self.district},\nfarmerid : {self.farmerid},\nusername : {self.username},\npassword : {self.password} \n'

class Farmers_Details(db.Model):
    id =db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(40),unique=False,nullable=False)
    phone=db.Column(db.BigInteger,unique=True,nullable=False)
    gender=db.Column(db.String(10),unique=False,nullable=False)
    district=db.Column(db.String(20),unique=False,nullable=False)
    farmerid=db.Column(db.String(20),unique=True,nullable=False)
    adharcard_no=db.Column(db.String(20),unique=True,nullable=False)
    address=db.Column(db.String(255),unique=False,nullable=False)
    pincode=db.Column(db.Integer,unique=False,nullable=False)
    bankaccount_no=db.Column(db.BigInteger,unique=True,nullable=False)
    bank_name=db.Column(db.String(40),unique=False,nullable=False)
    ifsc=db.Column(db.String(40),unique=False,nullable=False)

def __repr__(self):
    return f'\nname :{self.name},\nphone : {self.phone},\ngender : {self.gender},\ndistrict : {self.district},\nfarmerid : {self.farmerid}'

