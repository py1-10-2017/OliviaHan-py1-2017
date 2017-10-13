from flask import Flask, render_template, request, session,redirect
app = Flask(__name__)
app.secret_key = 'count secret'

@app.route('/')
def counter():
    try:
        session['count'] += 1
        session['count2'] += 2

    except:
        session['count'] = 1
        session['count2'] = 2
    return render_template('index.html')

@app.route('/reset', methods = ['POST'])
def reset():
    session ['count'] =1
    session ['count2'] =2
    return redirect('/')

app.run(debug = True)
