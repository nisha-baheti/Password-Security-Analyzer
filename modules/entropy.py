import math
import re

def calculate_entropy(password):
    charset = 0

    if re.search("[a-z]", password):
        charset += 26
    if re.search("[A-Z]", password):
        charset += 26
    if re.search("[0-9]", password):
        charset += 10
    if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        charset += 32

    if charset == 0:
        return 0

    entropy = len(password) * math.log2(charset)
    return round(entropy, 2)