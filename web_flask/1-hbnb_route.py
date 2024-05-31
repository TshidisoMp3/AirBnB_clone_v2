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

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
