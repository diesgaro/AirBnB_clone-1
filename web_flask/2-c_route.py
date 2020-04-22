#!/usr/bin/python3
"""
    Script that starts a flask web application
"""

from flask import Flask


app = Flask("web_flask")


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    hello_hbnb function that returns a string
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    hbnb function that returns a string
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """
    c_is_fun function that returns a string
    """
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
