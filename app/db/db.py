import flask

from flask_pymongo import PyMongo
from werkzeug.local import LocalProxy


def get_db():
    """
    Configuration method to return db instance
    """
    db = getattr(flask.g, "_database", None)

    if db is None:
        # The special variable object “g” is used here to define the PyMongo database in the global application context.
        db = flask.g._database = PyMongo(flask.current_app).db

    return db


# Use LocalProxy to read the global db instance with just `db`
ctx_db = LocalProxy(get_db)
