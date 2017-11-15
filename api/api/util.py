'''API utilities'''
from hashlib import sha256
from uuid import uuid4

def salt_and_hash(value, salt=None):
    '''Salt and hash a value'''
    if salt is None:
        salt = sha256(uuid4().bytes).hexdigest()
    return salt + sha256(str.encode(salt + value)).hexdigest()
