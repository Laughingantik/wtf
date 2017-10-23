'''The War Torn Faith RESTful API is a Flask application that exposes the
backend logic of the game for clients to consume. While it is mostly designed to
be consumed by War Torn Faith's web app, third-party consumption is also a
possibility.
'''
from flask import Blueprint
from . import accounts
from . import characters
from . import fights


def register(app, prefix='/api'):
    '''Register the API's Flask Blueprints into a Flask application and under
    the specified url prefix ("/api" by default)
    '''
    accounts.register(app, prefix)
    characters.register(app, prefix)
    fights.register(app, prefix)
