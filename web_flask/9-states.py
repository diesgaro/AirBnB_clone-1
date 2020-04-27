#!/usr/bin/python3
"""
    Script that starts a flask web application
"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask("web_flask")


@app.route('/states', strict_slashes=False)
def states():
    """
    states function that returns all the states
    """
    option = 'all_states'
    h1_content = 'States'
    data = storage.all(State).values()

    return render_template(
        '9-states.html', **locals()
    )


@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    """
    states_by_id function that returns the state and his cities
    """
    option = 'states_by_id'
    h1_content = 'State:'
    h3_content = 'Cities:'
    data = None

    for value in storage.all(State).values():
        if (value.id == id):
            data = value
            h1_content = 'State: {}'.format(data.name)

    return render_template(
        '9-states.html', **locals()
    )


@app.teardown_appcontext
def teardown_storage(response):
    """ After each request, remove the current SQLAlchemy Session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
