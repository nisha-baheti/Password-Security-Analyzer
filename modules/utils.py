def calculate_score(password, entropy, patterns, dictionary_flag):
    score = 0

    # length score
    if len(password) >= 12:
        score += 30
    elif len(password) >= 8:
        score += 20
    else:
        score += 10

    # entropy score
    if entropy > 60:
        score += 25
    elif entropy > 40:
        score += 15
    else:
        score += 5

    # pattern penalty
    if patterns:
        score -= 15

    # dictionary penalty
    if dictionary_flag:
        score -= 15

    return max(score, 0)


def classify_password(score):
    if score <= 30:
        return "Weak"
    elif score <= 60:
        return "Moderate"
    elif score <= 80:
        return "Strong"
    else:
        return "Very Strong"