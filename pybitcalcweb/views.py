from flask import render_template, redirect, url_for, request
from pybitcalcweb import app


@app.route('/')
def site_root():
    return redirect(url_for('calculator'))


@app.route('/calculator')
def calculator():
    return render_template('calculator.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    if request.method == 'POST':
        return redirect(url_for('calculator'))
    else:
        return redirect(url_for('calculator'))
