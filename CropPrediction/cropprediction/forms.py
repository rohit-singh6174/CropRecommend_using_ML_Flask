from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,SelectField,DateField,TextAreaField,FileField
from wtforms.validators import DataRequired,Length,EqualTo,Email
from flask_wtf.file import FileField, FileRequired,FileAllowed
from fileinput import filename


district=[('Ahmednaga','Ahmednaga'),
('Akola','Akola'),
('Aurangabad','Aurangabad'),
('Bhandara','Bhandara'),
('Buldhana','Buldhana'),
('Chandrapur','Chandrapur'),
('Mumbai City','Mumbai City'),
('Mumbai Suburban','Mumbai Suburban')
]  

gender=[
        ('MALE','MALE'),
        ('FEMALE','FEMALE'),
        ('OTHER','OTHER')
        ]


class FarmerRegForm(FlaskForm):
    name = StringField('name',validators=[DataRequired(),Length(min=3,max=20)])
    phone= StringField('phone',validators=[DataRequired(),Length(min=10,max=10)])
    gender=SelectField('district',choices=gender)
    district=SelectField('district',choices=district)
    farmerid = StringField('farmerid',validators=[DataRequired(),Length(min=10,max=20)])
    username = StringField('Username',validators=[DataRequired(),Length(min=3,max=20)])
    password=PasswordField('Password',validators=[DataRequired(),Length(min=6,max=20)])
    confirm_password= PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField(label='Sign Up')

class FarmerLogForm(FlaskForm):
     username = StringField('Username',validators=[DataRequired(),Length(min=3,max=20)])
     password=PasswordField('Password',validators=[DataRequired(),Length(min=6,max=20)])
     submit=SubmitField(label='Sign in')


class FarmerAccountUpdate(FlaskForm):
    name = StringField('name',validators=[DataRequired(),Length(min=3,max=20)])
    phone= StringField('phone',validators=[DataRequired(),Length(min=10,max=10)])
    gender=SelectField('district',choices=gender)
    district=SelectField('district',choices=district)
    farmerid = StringField('farmerid',validators=[DataRequired(),Length(min=10,max=20)])
    username = StringField('Username',validators=[DataRequired(),Length(min=3,max=20)])
    submit=SubmitField(label='Sign Up')
     