from werkzeug.security import safe_str_cmp
from resources.user import UserModel

def authenticate(username, password):
    # user = username_mapping.get(username, None)
    user = UserModel.findByUsername(username)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    print(payload)
    user_id = payload['identity']
    return UserModel.findByUserId(user_id)
    # return userid_mapping.get(user_id, None)