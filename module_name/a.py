# dummy code to test my own tests integration and IDE
# delete this file

import hashlib

secrets_db = """john,a51dda7c7ff50b61eaea0444371f4a6a9301e501
alice,522b276a356bdf39013dfabea2cd43e141ecc9e8
maclane,33b501a5f87749b22562d3a7d38f8db6ccb80fe9
ghost,d01593a7b3919244b959c893a0db44f8d82f92b7
cloud,ece8f46bf734ca267a2b6e0f7c3b471a5c964428
toy,d01593a7b3919244b959c893a0db44f8d82f92b7
deus,21298df8a3277357ee55b01df9530b535cf08ec1
wild,0ce0cb683d02f030f1ddf06d763bdcfea5c76a59"""

def get_user_password(username):
    for line in secrets_db.split('\n'):
        stored_username,stored_password = line.split(',')
        if username == stored_username.strip():
            return stored_password.strip()

def sha1(password):
    try:
        return hashlib.sha1(password).hexdigest()
    except Exception:
        pass

def is_valid_login(username, password):
    return sha1(password) == get_user_password(username)
