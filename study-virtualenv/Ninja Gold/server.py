from flask import Flask, render_template, request, session, redirect
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = '123'


@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
    return render_template('index.html',gold = session['gold'])

@app.route('/process_money', methods = ['POST'])
def process():
    time =datetime.now()
    building = request.form['building']

    try: temp = session['activaties']
    except KeyError:
        temp =[]

    if building == 'farm':
        draw = random.randint(10,21)


    elif  building == 'cave':
        draw = random.randint(5,11)

    elif  building == 'house':
        draw = random.randint(2,6)

    elif  building == 'casino':
        draw = random.randint(-50,51)

    session['gold'] = int(session['gold']) + draw
    temp.append('You have earned {} at {} on {}'.format(draw,building,time))
    session['activaties'] = temp
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')





app.run(debug = True)
