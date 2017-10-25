from flask import Flask, render_template, request, redirect, flash, session
app = Flask(__name__)
app.secret_key = '123'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods = ['POST'])
def process():
    # errors = False
    if len(request.form['name']) == 0:
        flash('Name must not be blank')
        # errors = True
    if len(request.form['comment']) > 120:
        flash('Commment can not be over 120 characters')
        # error = True
    # if errors:
    #     return redirect('/')
    return redirect('/')

    # session['submitted_info'] = request.form
    # return redirect('/result')

@app.route('/results', methods = ['POST'])
def display():
    if len(request.form['name']) >0 and len(request.form['comment']) < 120:
        return render_template('result.html')

app.run(debug = True)
