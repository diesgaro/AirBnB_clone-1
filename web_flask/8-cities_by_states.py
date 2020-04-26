#!/usr/bin/python3
"""
    Script that starts a flask web application
"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask("web_flask")


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    cities_by_states function that returns all the states with his cities
    """
    all_states = storage.all(State).values()

    return render_template(
        '8-cities_by_states.html', states=all_states
    )


@app.teardown_appcontext
def teardown_storage(response):
    """ After each request, remove the current SQLAlchemy Session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
