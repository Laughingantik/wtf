# pylint: disable=missing-docstring,invalid-name
from mock import patch, Mock
from api import util

@patch('api.util.sha256')
def test_salt_and_hash_no_salt(mock_sha256):
    # stub out sha256 to return the same hashes for testing purposes
    hash1 = Mock()
    hash1.hexdigest = Mock(return_value='foo')
    hash2 = Mock()
    hash2.hexdigest = Mock(return_value='bar')
    mock_sha256.side_effect = [hash1, hash2]
    assert util.salt_and_hash('asdf') == 'foobar'
