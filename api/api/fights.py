'''The fights module contains the following:
    register: registers a blueprint for fight operations to a Flask app
'''
from flask import Blueprint


def get_fights():
    '''Get multiple fights'''
    return 'Not implemented'


def register(app, prefix):
    '''Register a blueprint for fight operations to a Flask app'''
    blueprint = Blueprint('fights', __name__)
    blueprint.route('/fights')(get_fights)
    app.register_blueprint(blueprint, url_prefix=prefix)
