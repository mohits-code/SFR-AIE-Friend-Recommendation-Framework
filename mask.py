import hashlib

# Hash user data using sha256
def hash_user_data(user_data):
    hash_object = hashlib.sha256(user_data.encode())
    hashed_data = hash_object.hexdigest()
    return hashed_data
