from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'


@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method=='POST':
		user=request.form["name"]
		ag=request.form["age"]
		mes=request.form["message"]
		if name==user and age==ag message==mes:
			return redirect(url_for('home'))
	return render_template('login.html')

@app.route('/', ) # What methods are needed?
def home():
	
	return render_template('home.html')


@app.route('/error')
def error():

	return render_template('error.html')


@app.route('/display')
def display():

	return render_template('display.html', ) # What variables are needed?


@app.route('/thanks')
def thanks():

	return render_template('thanks.html')


if __name__ == '__main__':
	app.run(debug=True)