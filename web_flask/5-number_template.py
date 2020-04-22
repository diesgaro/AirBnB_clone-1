#!/usr/bin/python3
"""
    Script that starts a flask web application
"""

from flask import Flask
from flask import render_template


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


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text):
    """
    python_is_cool function that returns a string
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def is_a_number(n):
    """
    is_a_number function that returns a int
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    number_template function that returns a int in template
    """
    number = 'Number: {}'.format(n)
    return render_template('5-number.html', number=number)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
