from flask import Flask, request, redirect, render_template, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
LETTERS_ONLY = re.compile(r'^[a-zA-Z]*$')
# import the Connector function
from mysqlconnection import MySQLConnector
from datetime import datetime
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key = "123"
bcrypt = Bcrypt(app)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'users')

# create a users database to have first name, last name, email, password, confirm password
# having an index html with the registration and login form
# having a registration route to validate the information submitted through registration

@app.route('/')
def landing():
    return render_template('index.html')

@app.route('/register', methods = ['POST'])
def register():
    errors = []
# first name validation
    if len(request.form['first_name']) < 2:
        errors.append('invalid first name')
    if not LETTERS_ONLY.match(request.form['first_name']):
        errors.append('first name need to be letter only')
# last name validation
    if len(request.form['last_name']) < 2:
        errors.append('invalid last name')
    if not LETTERS_ONLY.match(request.form['last_name']):
        errors.append('last name need to be letter only')
# password validation
    if len(request.form['password']) < 8:
        errors.append('password should be at least 8 characters')
# password confirmation validation
    if request.form['password'] != request.form['confirm_password']:
        errors.append('password does not match')
# email already existed validation
    query = 'SELECT id FROM users WHERE email = :enter_email'
    data = {'enter_email': request.form['email']}
    if mysql.query_db(query,data):
        errors.append('this email has been registered')

    if errors:
        for e in errors:
            flash(e)
        return redirect ('/')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])

    query = "INSERT INTO users (first_name,last_name,email,password, created_at, updated_at) \
    VALUES (:new_first, :new_last,:new_email, :pwd, NOW(), NOW())"
    data = {'new_first': request.form['first_name'],
            'new_last': request.form['last_name'],
            'new_email': request.form['email'],
            'pwd': pw_hash
            }
    mysql.query_db(query,data)

    flash('successful registered')
    return render_template('success.html')

@app.route('/login', methods = ['POST'])
def login():
    errors = []
# check DB for email address
    query = 'SELECT id, password FROM users WHERE email = :enter_email'
    data = {'enter_email': request.form['email']}
    user = mysql.query_db(query, data)[0]
    print user
    if not user:
        errors.append('user name/password does not match')
    else:
        if not bcrypt.check_password_hash(user['password'],request.form['password']):
            errors.append('password/user name does not match')
    if errors:
        for e in errors:
            flash(e)
        return redirect('/')
    session['id'] = user['id']
    return render_template('success.html')

@app.route('/logout', methods = ['POST'])
def logout():
    session.clear()
    return redirect('/')


app.run(debug=True)
