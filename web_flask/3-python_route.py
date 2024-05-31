#!/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask
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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
