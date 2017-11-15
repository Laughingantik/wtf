# pylint: disable=missing-docstring,invalid-name
from mock import patch
from api.accounts import Account, AccountRepository


TEST_EMAIL = 'foobar@gmail.com'
TEST_PASSWORD_PLAIN = 'foobar123'
TEST_PASSWORD_HASH = (
    '67d765888ea8f71875dfe27334786bffdca070705ee97bd17bec85f8580f7f01'
    + '012eab80b72cbfe663429219e920aee8cd17ba8893e302844682104ee88d3145'
)
TEST_USERNAME = 'foobar'


@patch('api.accounts.uuid4')
def test_account_defaults(mock_uuid4):
    # stub out uuid4 to return the same uuid for testing purposes
    uuid = '048e8cf5-bf6f-4b39-ac97-6f9851f61b16'
    mock_uuid4.return_value = uuid
    account = Account()
    assert account.uuid == uuid
    assert account.email is None
    assert account.password is None
    assert account.username is None


def test_account_construction():
    uuid = 'eebcacc8-b2d4-11e7-abc4-cec278b6b50a'
    account = Account(
        uuid=uuid,
        email=TEST_EMAIL,
        password=TEST_PASSWORD_HASH,
        username=TEST_USERNAME
    )
    assert account.uuid == uuid
    assert account.email == TEST_EMAIL
    assert account.password == TEST_PASSWORD_HASH
    assert account.username == TEST_USERNAME


@patch('api.accounts.salt_and_hash')
def test_account_setters(mock_salt_and_hash):
    # stub out salt_and_hash to return the same hashes for testing purposes
    uuid = '60d0d4a4-3159-467d-a972-cd8a386931c4'
    mock_salt_and_hash.return_value = TEST_PASSWORD_HASH
    account = Account()
    account.uuid = uuid
    assert account.uuid == uuid
    account.email = TEST_EMAIL
    assert account.email == TEST_EMAIL
    account.password = TEST_PASSWORD_PLAIN
    assert account.password == TEST_PASSWORD_HASH
    account.username = TEST_USERNAME
    assert account.username == TEST_USERNAME


def test_account_equality():
    assert Account() != Account()


def test_account_equality_uuid():
    account1 = Account(uuid='test')
    account2 = Account(uuid='test')
    assert account1 == account2
    account2.uuid = 'asdf'
    assert account1 != account2


def test_account_equality_email():
    account1 = Account(uuid='test', password='test')
    account2 = Account(uuid='test', password='test')
    assert account1 == account2
    account2.password = 'asdf'
    assert account1 != account2
    # the same password will always be different after salting and hashing:
    account1 = Account(uuid='test')
    account1.password = 'test'
    account2 = Account(uuid='test')
    account2.password = 'test'
    assert account1 != account2


def test_account_equality_password():
    account1 = Account(uuid='test', email='test')
    account2 = Account(uuid='test', email='test')
    assert account1 == account2
    account2.email = 'asdf'
    assert account1 != account2


def test_account_equality_username():
    account1 = Account(uuid='test', username='test')
    account2 = Account(uuid='test', username='test')
    assert account1 == account2
    account2.username = 'asdf'
    assert account1 != account2


def test_account_equality_misc():
    assert Account() != 'asdf'
    assert Account() != 123
    assert Account() != {}
    assert Account() != ()
    assert Account() != None


def test_find_account_by_uuid():
    account = Account(username=TEST_USERNAME)
    repo = AccountRepository()
    repo.save(account)
    # todo: weak equality check
    assert repo.find_by_uuid(account.uuid) == account
    assert repo.find_by_uuid('asdf') is None


def test_find_account_by_email():
    account = Account(email=TEST_EMAIL)
    repo = AccountRepository()
    repo.save(account)
    # todo: weak equality check
    assert repo.find_by_email(TEST_EMAIL) == account
    assert repo.find_by_email('asdf') is None


def test_find_account_by_username():
    account = Account(username=TEST_USERNAME)
    repo = AccountRepository()
    repo.save(account)
    # todo: weak equality check
    assert repo.find_by_username(TEST_USERNAME) == account
    assert repo.find_by_username('asdf') is None


def test_find_account_by_email_password():
    expected = Account(email=TEST_EMAIL)
    # salt and hash the password:
    expected.password = TEST_PASSWORD_PLAIN
    repo = AccountRepository()
    repo.save(expected)
    actual = repo.find_by_email_password(TEST_EMAIL, TEST_PASSWORD_PLAIN)
    assert actual == expected


def test_find_account_by_email_password_incorrect_password():
    repo = AccountRepository()
    repo.save(Account(email=TEST_EMAIL, password=TEST_PASSWORD_HASH))
    assert repo.find_by_email_password(TEST_EMAIL, 'asdf42') is None


def test_find_account_by_email_password_not_found():
    repo = AccountRepository()
    assert repo.find_by_email_password(TEST_EMAIL, TEST_PASSWORD_PLAIN) is None


def test_persist_accounts_across_repo_instances():
    account = Account(email=TEST_EMAIL, username=TEST_USERNAME)
    repo1 = AccountRepository()
    repo1.save(account)
    assert repo1.find_by_uuid(account.uuid) == account
    assert repo1.find_by_email(account.email) == account
    assert repo1.find_by_username(account.username) == account
    repo2 = AccountRepository()
    assert repo2.find_by_uuid(account.uuid) == account
    assert repo2.find_by_email(account.email) == account
    assert repo2.find_by_username(account.username) == account
