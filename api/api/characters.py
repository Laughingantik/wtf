'''The characters module contains the following:
    register: registers a blueprint for character operations to a Flask app
'''
from flask import Blueprint


def get_characters():
    '''Get multiple characters'''
    return 'Not implemented'


def register(app, prefix):
    '''Register a blueprint for character operations to a Flask app'''
    blueprint = Blueprint('characters', __name__)
    blueprint.route('/characters')(get_characters)
    app.register_blueprint(blueprint, url_prefix=prefix)
