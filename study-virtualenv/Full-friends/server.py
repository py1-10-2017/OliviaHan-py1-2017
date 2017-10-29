from flask import Flask, request, redirect, render_template, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
# import the Connector function
from mysqlconnection import MySQLConnector
from datetime import datetime
app = Flask(__name__)
app.secret_key = "123"
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'friends')

@app.route('/')
def index():
    query = mysql.query_db ("SELECT * FROM friends")
    return render_template('index.html', friend_list = query)

@app.route('/friends', methods = ['POST'])
def create():

    query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) \
    VALUES (:new_first, :new_last, :new_email, NOW(), NOW())"
    data = {"new_first": request.form['first_name'],
            "new_last": request.form['last_name'],
            "new_email": request.form['email']
    }
    mysql.query_db(query,data)
    return redirect('/')




@app.route('/friends/<id>/edit')
def edit(id):

    query = "SELECT * FROM friends WHERE id = :id"
    data = {'id':id}

    one_friend = mysql.query_db(query,data)
    return render_template('edit.html', one_friend = one_friend)

@app.route('/friends/<id>', methods = ['POST'])
def update(id):
    query = "UPDATE friends SET first_name = :updated_first_name, last_name = :updated_last_name, \
    email = :updated_email, updated_at = now() WHERE id = :id "

    data = {"updated_first_name": request.form['first_name'],
            "updated_last_name": request.form['last_name'],
            "updated_email": request.form['email'],
            "id": id
    }

    mysql.query_db(query,data)
    return redirect('/')

@app.route('/friends/<id>/delete', methods = ['POST'])
def delete(id):
    query = 'DELETE FROM friends WHERE id = :id '
    data = {'id': id}
    mysql.query_db(query,data)
    return redirect('/')

app.run(debug=True)
