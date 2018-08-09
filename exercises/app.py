from databases import *
from flask import Flask, render_template, url_for, request
app = Flask(__name__)



# add_student("Ariel" , 2000, False)

@app.route('/')
def home():
    return render_template('home.html', students=query_all())

@app.route('/student/<int:student_id>')
def display_student(student_id):
    return render_template('student.html', student=query_by_id(student_id))

@app.route('/add', methods=['GET', 'POST'])
def add_student_route():
	if request.method == 'GET':
		return render_template("add.html")
	else:
		name = request.form["name"]
		year = request.form["Year"]
		lab_t = request.form["lab"]
		if lab_t=="True": 
			add_student(name , year, True)
		else:
			add_student(name, year, False)

	return render_template("add.html" , b = "POST request recived")
		
		


if (__name__=='__main__'):
	app.run(debug=True)