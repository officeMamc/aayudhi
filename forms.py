from flask_wtf import FlaskForm
from wtforms import StringField

class Login(FlaskForm):
    username = StringField('Username')
    
