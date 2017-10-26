# pylint: disable=missing-docstring
from api.accounts import Account


def test_account_defaults():
    account = Account()
    assert account.email == ''
    assert account.password == ''
    assert account.username == ''


def test_account_setters():
    account = Account()
    account.email = 'foobar@gmail.com'
    assert account.email == 'foobar@gmail.com'
    account.password = 'foobar123'
    assert account.password == 'foobar123'
    account.username = 'foobar'
    assert account.username == 'foobar'
