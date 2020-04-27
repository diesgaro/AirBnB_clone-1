#!/usr/bin/python3
"""
    Script that starts a flask web application
"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask("web_flask")


@app.route('/hbnb_filters', strict_slashes=False)
def states():
    """
    states function that returns all the states
    """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()

    return render_template(
        '10-hbnb_filters.html', **locals()
    )


@app.teardown_appcontext
def teardown_storage(response):
    """ After each request, remove the current SQLAlchemy Session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
