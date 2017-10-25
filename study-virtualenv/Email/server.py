from flask import Flask, request, redirect, render_template, session, flash
# import the Connector function
from mysqlconnection import MySQLConnector
from datetime import datetime
app = Flask(__name__)
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'email')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods = ['POST'])
def add():
    query = "INSERT INTO emails (email, created_on, updated_on) \
    VALUES (:new_email, NOW(), NOW())"
    data = {"new_email": request.form['email']}
    mysql.query_db(query,data)
    return redirect('/success/{}'.format(request.form['email']))

@app.route('/success/<new_email>')
def display(new_email):
    query = mysql.query_db ("SELECT * FROM emails")

    return render_template('success.html', email_list = query, add_email = new_email)







app.run(debug=True)
