from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods = ['POST'])
def display():
    name = request.form['name']
    location = request.form['location']
    language = request.form['favorite_language']
    comments = request.form['comments']
    return render_template('results.html', name = name, location = location, favorite_language = language, comments = comments)
    # return redirect('/results')
app.run(debug = True)
