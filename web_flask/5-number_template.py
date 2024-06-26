#!/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hihi_hbnb():
    """Function to return Hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def Yelloz():
    """Function to show/return HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cfunc(text):
    """Function to show/return C + text"""
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythonCool_text(text='is cool'):
    """Function to show/return Python + text"""
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def numbz(n):
    """Function to show/return n is a number"""
    return '%d is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_templatezz(n):
    return render_template('5-number.html', numbzz=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
