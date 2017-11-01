# pylint: disable=missing-docstring
from mock import patch
from api.accounts import Account


@patch('api.accounts.uuid4')
def test_account_defaults(uuid4):
    # stub out uuid4 to return the same uuid for testing purposes
    uuid4.return_value = '048e8cf5-bf6f-4b39-ac97-6f9851f61b16'
    account = Account()
    assert account.uuid == '048e8cf5-bf6f-4b39-ac97-6f9851f61b16'
    assert account.email is None
    assert account.password is None
    assert account.username is None


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


@patch('api.accounts.sha256')
def test_account_setters(sha256):
    # stub out sha256 to return the same hashes for testing purposes
    sha256.side_effect = [
        '67d765888ea8f71875dfe27334786bffdca070705ee97bd17bec85f8580f7f01',
        '012eab80b72cbfe663429219e920aee8cd17ba8893e302844682104ee88d3145'
    ]
    account = Account()
    account.uuid = '60d0d4a4-3159-467d-a972-cd8a386931c4'
    assert account.uuid == '60d0d4a4-3159-467d-a972-cd8a386931c4'
    account.email = 'foobar@gmail.com'
    assert account.email == 'foobar@gmail.com'
    account.password = 'foobar123'
    assert account.password == (
        '67d765888ea8f71875dfe27334786bffdca070705ee97bd17bec85f8580f7f01'
        + '012eab80b72cbfe663429219e920aee8cd17ba8893e302844682104ee88d3145'
    )
    account.username = 'foobar'
    assert account.username == 'foobar'
