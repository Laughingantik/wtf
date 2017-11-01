# pylint: disable=missing-docstring,invalid-name
from mock import patch, Mock
from api.accounts import Account, AccountRepository


@patch('api.accounts.uuid4')
def test_account_defaults(mock_uuid4):
    # stub out uuid4 to return the same uuid for testing purposes
    mock_uuid4.return_value = '048e8cf5-bf6f-4b39-ac97-6f9851f61b16'
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
def test_account_setters(mock_sha256):
    # stub out sha256 to return the same hashes for testing purposes
    hash1 = Mock()
    hash1.hexdigest = Mock(
        return_value=(
            '67d765888ea8f71875dfe27334786bffdca070705ee97bd17bec85f8580f7f01'
        )
    )
    hash2 = Mock()
    hash2.hexdigest = Mock(
        return_value=(
            '012eab80b72cbfe663429219e920aee8cd17ba8893e302844682104ee88d3145'
        )
    )
    mock_sha256.side_effect = [hash1, hash2]
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


def test_find_account_by_uuid():
    account = Account()
    account.username = 'foobar'
    repo = AccountRepository()
    repo.save(account)
    assert repo.find_by_uuid(account.uuid).username == 'foobar'
    assert repo.find_by_uuid('asdf') is None


def test_find_account_by_email():
    account = Account()
    account.email = 'foobar@gmail.com'
    repo = AccountRepository()
    repo.save(account)
    assert repo.find_by_email(account.email).uuid == account.uuid
    assert repo.find_by_email('asdf') is None


def test_find_account_by_username():
    account = Account()
    account.username = 'foobar'
    repo = AccountRepository()
    repo.save(account)
    assert repo.find_by_username(account.username).uuid == account.uuid
    assert repo.find_by_username('asdf') is None


def test_account_authentication():
    account = Account()
    account.email = 'foobar@gmail.com'
    account.password = 'foobar123'
    repo = AccountRepository()
    repo.save(account)
    assert repo.authenticate('foobar@gmail.com', 'foobar123')


def test_account_authentication_password_mismatch():
    account = Account()
    account.email = 'foobar@gmail.com'
    account.password = 'foobar123'
    repo = AccountRepository()
    repo.save(account)
    assert not repo.authenticate('foobar@gmail.com', 'asdf42')


def test_account_authentication_account_not_found():
    repo = AccountRepository()
    assert not repo.authenticate('foobar@gmail.com', 'foobar123')
