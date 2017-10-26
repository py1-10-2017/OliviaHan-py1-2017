from flask import Flask, request, redirect, render_template, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
# import the Connector function
from mysqlconnection import MySQLConnector
from datetime import datetime
app = Flask(__name__)
app.secret_key = "123"
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'email')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods = ['POST'])
def add():
        if len(request.form['email']) < 1:
            flash('Email can not be blank')
            return redirect('/')

        elif not EMAIL_REGEX.match(request.form['email']):
            flash('Invalid Email Input')
            return redirect('/')
        else:

            flash( 'You entered valid email {}'.format(request.form['email']))
            query = "INSERT INTO emails (email, created_on, updated_on) \
            VALUES (:new_email, NOW(), NOW())"
            data = {"new_email": request.form['email']}
            mysql.query_db(query,data)

            return redirect('/success')


@app.route('/success')
def display():
    query = mysql.query_db ("SELECT * FROM emails")

    return render_template('success.html', email_list = query)

app.run(debug=True)
