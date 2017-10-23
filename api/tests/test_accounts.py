from api.accounts import Account


class TestAccount(object):

    def test_defaults(self):
        account = Account()
        assert account.email == ''
        assert account.password == ''
        assert account.username == ''

    def test_setters(self):
        account = Account()
        account.email = 'foobar@gmail.com'
        assert account.email == 'foobar@gmail.com'
        account.password = 'foobar123'
        assert account.password == 'foobar123'
        account.username = 'foobar'
        assert account.username == 'foobar'
