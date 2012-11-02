from flask import Flask, render_template, redirect, request
import model

app = Flask(__name__)

@app.route("/")
def index():
	user_list = model.session.query(model.User).all()
	return render_template("user_list.html", users = user_list)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/sign_up")
def login():
    return render_template("signup.html")

@app.route("/authenticate", methods=["POST"])
def authenticate():
    email = request.form['email']
    password = request.form['password']
    user_id = model.authenticate(self, email, password)
    
    if user_id != None:
    	session['user_id'] = user_id
    	return render_template("ratings.html")
    else:
    	return redirect("/login")


@app.route("/new_user", methods=["POST"])
def add_new_user():
	email = request.form['email']
	password = request.form['password']
	age = request.form['age']
	zipcode = request.form['zipcode']
	user_id = model.new_user(self, email, password, age, zipcode)

	if user_id != None:
		session['user_id'] = user_id
		return render_template("ratings.html")
	else:
		return redirect("/sign_up")

if __name__ == "__main__":
	app.run(debug = True)