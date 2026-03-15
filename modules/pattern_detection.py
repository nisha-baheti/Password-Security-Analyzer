import re

def detect_patterns(password):
    patterns = []

    if re.search(r"(.)\1{2,}", password):
        patterns.append("Repeated characters detected")

    if re.search(r"1234|abcd|qwerty", password.lower()):
        patterns.append("Sequential or keyboard pattern detected")

    if password.isnumeric():
        patterns.append("Password contains only numbers")

    return patterns