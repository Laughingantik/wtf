# pylint: disable=missing-docstring
from mock import patch
from api.accounts import Account


@patch('api.accounts.uuid4')
def test_account_defaults(uuid4):
    # stub out uuid4 to return the same uuid for testing purposes
    uuid4.return_value = '048e8cf5-bf6f-4b39-ac97-6f9851f61b16'
    account = Account()
    assert account.uuid == '048e8cf5-bf6f-4b39-ac97-6f9851f61b16'
    assert account.email == ''
    assert account.password == ''
    assert account.username == ''


def test_account_construction():
    account = Account(
        uuid='eebcacc8-b2d4-11e7-abc4-cec278b6b50a',
        email='foobar@gmail.com',
        password='foobar123',
        username='foobar'
    )
    assert account.uuid == 'eebcacc8-b2d4-11e7-abc4-cec278b6b50a'
    assert account.email == 'foobar@gmail.com'
    assert account.password == 'foobar123'
    assert account.username == 'foobar'


def test_account_setters():
    account = Account()
    account.uuid = '60d0d4a4-3159-467d-a972-cd8a386931c4'
    assert account.uuid == '60d0d4a4-3159-467d-a972-cd8a386931c4'
    account.email = 'foobar@gmail.com'
    assert account.email == 'foobar@gmail.com'
    account.password = 'foobar123'
    assert account.password == 'foobar123'
    account.username = 'foobar'
    assert account.username == 'foobar'
