'''The accounts module contains the following:
    Account: a model of an account in War Torn Faith
    AccountRepository: provides the ability to store and retrieve accounts
    register: registers a blueprint for account operations to a Flask app
'''
from hashlib import sha256
from uuid import uuid4
from flask import Blueprint


class Account(object):
    '''Accounts are created by the players of War Torn Faith

    Accounts have the following properties:
        uuid: a "universally unique identifier" for the account
        email: an email address that the player can be reached at
        password: the password used to authenticate as the account
        username: the player's public identity
    '''

    def __init__(self, uuid=None, email=None, password=None, username=None):
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
        self._password = salt_and_hash(value)

    @property
    def username(self):
        '''Get the account's username'''
        return self._username

    @username.setter
    def username(self, value):
        '''Set the account's username'''
        self._username = value


class AccountRepository(object):
    '''The AccountRepository provides the ability to store and retrieve accounts

    `save` persists an account - it creates a new account if one does not
        already exist, or updates an existing one.

    `find_by_uuid()`, `find_by_email()`, and `find_by_username()` retrieves an
        account by one of the three uniquely identifying fields: uuid, email, or
        username, respectively.

    `authenticate()` confirms the authenticity of an email and password
        combination that is presumably being supplied by a user in order to gain
        access to an account. It will return `True` if the combination matches
        an account on record and False otherwise.
    '''

    def __init__(self):
        '''Initialize an account repository'''
        self.by_uuid = {}
        self.by_email = {}
        self.by_username = {}

    def save(self, account):
        '''Save an account'''
        self.by_uuid[account.uuid] = account
        self.by_email[account.email] = account
        self.by_username[account.username] = account

    def find_by_uuid(self, uuid):
        '''Find an account by a UUID'''
        return self.by_uuid.get(uuid)

    def find_by_email(self, email):
        '''Find an account by an email address'''
        return self.by_email.get(email)

    def find_by_username(self, username):
        '''Find an account by a username'''
        return self.by_username.get(username)

    def authenticate(self, email, password):
        '''Perform an authentication check with an email and password'''
        account = self.find_by_email(email)
        authentic = False
        if account is not None:
            # the salt is the first 64 characters of the password
            salt = account.password[:64]
            authentic = salt_and_hash(password, salt) == account.password
        return authentic


def salt_and_hash(value, salt=None):
    '''Salt and hash a value'''
    if salt is None:
        salt = sha256(uuid4().bytes).hexdigest()
    return salt + sha256(str.encode(salt + value)).hexdigest()


def get_accounts():
    '''Get multiple accounts'''
    return 'Not implemented'


def register(app, prefix):
    '''Register a blueprint for account operations to a Flask app'''
    blueprint = Blueprint('accounts', __name__)
    blueprint.route('/accounts')(get_accounts)
    app.register_blueprint(blueprint, url_prefix=prefix)
