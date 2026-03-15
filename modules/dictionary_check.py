def load_dictionary(file_path):

    with open(file_path, "r", encoding="utf-8") as file:
        dictionary = set(line.strip().lower() for line in file)

    return dictionary


def check_dictionary(password, dictionary):

    password_lower = password.lower()

    # direct lookup (O(1))
    if password_lower in dictionary:
        return True

    # hybrid pattern check
    for word in dictionary:
        if word in password_lower:
            return True

    return False