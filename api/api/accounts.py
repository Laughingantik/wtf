'''The accounts module contains the following:
    Account: a model of an account in War Torn Faith
    register: registers a blueprint for account operations to a Flask app
'''
from uuid import uuid4
from flask import Blueprint


class Account(object):
    '''Accounts are created by the players of War Torn Faith

    Accounts have the following properties:
        email: an email address that the player can be reached at
        password: the password used to authenticate as the account
        username: the player's public identity
    '''

    def __init__(self, uuid=None, email='', password='', username=''):
        '''Initialize an account'''
        self._uuid = uuid or uuid4()
        self._email = email
        self._password = password
        self._username = username

    @property
    def uuid(self):
        '''Get the account's UUID'''
        return self._uuid

    @uuid.setter
    def uuid(self, value):
        '''Set the account's UUID'''
        self._uuid = value

    @property
    def email(self):
        '''Get the account's email address'''
        return self._email

    @email.setter
    def email(self, value):
        '''Set the account's email address'''
        self._email = value

    @property
    def password(self):
        '''Get the account's password'''
        return self._password

    @password.setter
    def password(self, value):
        '''Set the account's password'''
        self._password = value

    @property
    def username(self):
        '''Get the account's username'''
        return self._username

    @username.setter
    def username(self, value):
        '''Set the account's username'''
        self._username = value


def get_accounts():
    '''Get multiple accounts'''
    return 'Not implemented'


def register(app, prefix):
    '''Register a blueprint for account operations to a Flask app'''
    blueprint = Blueprint('accounts', __name__)
    blueprint.route('/accounts')(get_accounts)
    app.register_blueprint(blueprint, url_prefix=prefix)
