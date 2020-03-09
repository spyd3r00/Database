from flask import Flask, render_template, url_for,flash, redirect
from flask_sqlalchemy import SQLAlchemy
from form import AddForm, searchForm



app = Flask(__name__)
app.config['SECRET_KEY'] = 'random trext'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class Students(db.Model): 
	id = db.Column(db.Integer, primary_key =True)
	fullName = db.Column(db.String(20), unique = True, nullable = False)
	Course = db.Column(db.String(4), nullable = False)
	idNumber = db.Column(db.String(9), unique = True, nullable = False)

	def __repr__(self):
		return f"('{self.fullName}','{self.Course}','{self.idNumber}')"


@app.route('/')
def home():
	return render_template('home.html',title='Home')

@app.route('/Register', methods=['GET','POST'])
def Register():
	form = AddForm()
	if form.validate_on_submit():
		try:
			students_1 = Students(fullName=form.fullName.data, Course=form.Course.data, idNumber=form.idNumber.data)
			db.session.add(students_1)
			db.session.commit()
			flash('Registered Successfully!')
		except:
			flash('Information Already Exist!')
		return redirect(url_for('home'))
	return render_template('register.html',title='Register', form=form)

@app.route('/Search', methods = ['GET','POST'])
def Search():
	form = searchForm()
	if form.validate_on_submit():
		try:
			var = Students.query.filter_by(idNumber=form.ID.data).all()
			if var:
				flash('Search Successfully!')
			else:
				flash('No Data Existed!')
		except:
			flash('Query Error!')
		return render_template('search.html', title='Search', form= form, var = var)
	return render_template('search.html',title='Search', form= form)


@app.route('/View', methods = ['GET'])
def View():
	var = Students.query.all()

	return render_template('view.html', title= 'View' , var = var)

@app.route('/Delete/<string:id_number>', methods = ['GET'])
def Delete(id_number):
	var = Students.query.filter_by(idNumber=id_number).first()
	db.session.delete(var)
	db.session.commit()

	return redirect(url_for('View'))

@app.route('/Edit/<string:id_number>', methods = ['GET','POST'])
def Edit(id_number):
	form = AddForm()
	var = Students.query.filter_by(idNumber=id_number).first()
	if form.validate_on_submit():
		var.idNumber = form.idNumber.data
		var.fullName = form.fullName.data
		var.Course = form.Course.data
		db.session.commit()

		return redirect(url_for('View'))
	return render_template('edit.html',title='Edit', var = var, form = form)


if __name__ == '__main__':
	app.run(debug=True)