#!/usr/bin/python3
"""
    Script that starts a flask web application
"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask("web_flask")


@app.route('/states_list', strict_slashes=False)
def list_of_states():
    """
    list_of_states function that returns all the states in template
    """
    all_states = storage.all(State).values()

    return render_template(
        '7-states_list.html', states=all_states
    )


@app.teardown_appcontext
def teardown_storage(response):
    """ After each request, remove the current SQLAlchemy Session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
