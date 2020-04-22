#!/usr/bin/python3
"""
    Script that starts a flask web application
"""

from flask import Flask
app = Flask("web_flask")


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'
