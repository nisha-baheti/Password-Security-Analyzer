import hashlib

def hash_password(password):
    return hashlib.sha1(password.encode()).hexdigest()

def check_breach(password):

    dataset = "datasets/common_pw.txt"

    password_hash = hash_password(password)

    with open(dataset, "r", encoding="utf-8") as file:
        for line in file:
            if password_hash == line.strip():
                return True

    return False