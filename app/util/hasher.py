import hashlib

salt = "SaltIsSalty"


# function to hash password with salt
def hash_password(password: str):
    """
    generates hashed password with salted password string
    :param password: password string
    :return: SHA256 result string
    """
    # concatenate the password and salt
    salted_password = password + salt

    # hash the salted password
    hashed_password = hashlib.sha256(salted_password.encode('utf-8')).hexdigest()

    return hashed_password


def check_password_hash(hash_pass, password):
    """
    Matches plain password with SHA256 password
    :param hash_pass: SHA256 hashed string with salt
    :param password: plain password
    :return: True if matching else False
    """
    if hash_pass == hash_password(password):
        return True
    return False
