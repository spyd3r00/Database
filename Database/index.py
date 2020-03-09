from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

class button(FlaskForm):
	search = SubmitField('Search')
