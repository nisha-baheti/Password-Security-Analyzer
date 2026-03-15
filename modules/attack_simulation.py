def simulate_attacks(password, dictionary):

    results = {}

    # Dictionary attack
    if password.lower() in dictionary:
        results["Dictionary Attack"] = "COMPROMISED"
    else:
        results["Dictionary Attack"] = "SAFE"

    # Hybrid attack
    hybrid_found = False
    for word in dictionary:
        if len(word) > 3 and word in password.lower():
            hybrid_found = True
            break

    if hybrid_found:
        results["Hybrid Attack"] = "LIKELY"
    else:
        results["Hybrid Attack"] = "SAFE"

    # Numeric brute-force weakness
    if password.isdigit():
        results["Numeric Attack"] = "HIGH RISK"
    else:
        results["Numeric Attack"] = "SAFE"

    return results