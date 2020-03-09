from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired, Length

class AddForm(FlaskForm):
	fullName = StringField('Full Name',validators=[DataRequired(), Length(min = 8, max = 30)])
	Course = StringField('Course',validators=[DataRequired(), Length(min = 4, max = 4)])
	idNumber = StringField('ID Number',validators=[DataRequired(), Length(min = 9, max = 9)])

	submit = SubmitField('Add Students')
	edit = SubmitField ('Edit')

class searchForm(FlaskForm):
	ID = StringField('ID Number',validators=[DataRequired(), Length(min = 0, max = 9)])

	SubmitField = SubmitField('Search')