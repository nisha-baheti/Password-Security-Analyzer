from entropy import calculate_entropy
from dictionary_check import load_dictionary, check_dictionary
from pattern_detection import detect_patterns
from crack_time import estimate_crack_time
from attack_simulation import simulate_attacks
from breach_check import check_breach
from utils import calculate_score, classify_password


def analyze_password(password):
    dictionary = load_dictionary("datasets/common_pw.txt")
    entropy = calculate_entropy(password)
    patterns = detect_patterns(password)
    dictionary_flag = check_dictionary(password, dictionary)
    crack_time = estimate_crack_time(entropy)
    attack_results = simulate_attacks(password, dictionary)
    breach_flag = check_breach(password)

    # Score calculation
    score = calculate_score(password, entropy, patterns, dictionary_flag)

    # Strength classification
    strength = classify_password(score)

    return {
        "entropy": entropy,
        "patterns": patterns,
        "dictionary_flag": dictionary_flag,
        "crack_time": crack_time,
        "attack_results": attack_results,
        "breach_flag": breach_flag,
        "score": score,
        "strength": strength
    }