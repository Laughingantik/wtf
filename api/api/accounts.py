'''The accounts module contains the following:
    Account: a model of an account in War Torn Faith
    AccountRepository: provides the ability to store and retrieve accounts
    register: registers a blueprint for account operations to a Flask app
'''
from uuid import uuid4
from flask import Blueprint
from .util import salt_and_hash


IN_MEMORY_ACCOUNTS = {
    'by_uuid': {},
    'by_email': {},
    'by_username': {}
}


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

    def __eq__(self, other):
        '''Compare this account with another account'''
        return (
            isinstance(other, Account)
            and self.uuid == other.uuid
            and self.email == other.email
            and self.password == other.password
            and self.username == other.username
        )

    def __ne__(self, other):
        return not self.__eq__(other)


class AccountRepository(object):
    '''The AccountRepository provides the ability to store and retrieve accounts

    `save()` persists an account - it creates a new account if one does not
        already exist, or updates an existing one.

    `find_by_uuid()`, `find_by_email()`, and `find_by_username()` retrieves an
        account by one of the three uniquely identifying fields: uuid, email, or
        username, respectively.

    `find_by_email_password()` retrieves an account by an email address and
        password combination. This function is intended to be used with account
        authentication - it will return `None` if the supplied email and
        password combination is incorrect. Note that the password is the
        account's plaintext password.
    '''

    def __init__(self):
        '''Initialize an account repository'''
        self.by_uuid = IN_MEMORY_ACCOUNTS.get('by_uuid')
        self.by_email = IN_MEMORY_ACCOUNTS.get('by_email')
        self.by_username = IN_MEMORY_ACCOUNTS.get('by_username')

    def save(self, account):
        '''Save an account'''
        self.by_uuid[account.uuid] = account
        self.by_email[account.email] = account
        self.by_username[account.username] = account

    def find_by_uuid(self, uuid):
        '''Find an account with the given UUID'''
        return self.by_uuid.get(uuid)

    def find_by_email(self, email):
        '''Find an account with the given email address'''
        return self.by_email.get(email)

    def find_by_username(self, username):
        '''Find an account with the given username'''
        return self.by_username.get(username)

    def find_by_email_password(self, email, password):
        '''Find an account with the given email address and password'''
        account = self.find_by_email(email)
        if account is not None:
            # the salt is the first 64 characters of the password
            salt = account.password[:64]
            if salt_and_hash(password, salt) != account.password:
                account = None
        return account


def register(app, prefix):
    '''Register a blueprint for account operations to a Flask app'''
    blueprint = Blueprint('accounts', __name__)
    blueprint.route('/accounts')(lambda: 'Not implemented')
    app.register_blueprint(blueprint, url_prefix=prefix)
