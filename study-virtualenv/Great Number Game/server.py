from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "dd"


@app.route('/')
def index():
    if 'target' not in session:
        session['target'] =random.randint(1,101)
    print session['target']
    return render_template('index.html')

@app.route('/type', methods =['POST'])
def input():
    if int(request.form['guess']) == session['target']:
        session['result'] = "Matched"
    elif int(request.form['guess']) > session['target']:
        session['result'] = 'Too High'
    elif int(request.form['guess']) < session['target']:
        session['result'] = 'Too Low'
    return redirect('/')

@app.route('/reset', methods = ['POST'])
def reset():
    session['target'] =random.randint(1,101)
    return redirect('/')



app.run(debug = 'True')
