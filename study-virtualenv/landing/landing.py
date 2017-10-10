from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/ninjas')
def hello_ninjas():
    return render_template('ninjas.html')

@app.route('/dojos/new')
def action():
    return render_template('dojos.html', action = 'new')

app.run(debug=True)
