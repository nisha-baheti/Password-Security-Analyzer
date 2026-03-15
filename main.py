import argparse

from modules.entropy import calculate_entropy
from modules.dictionary_check import load_dictionary, check_dictionary
from modules.pattern_detection import detect_patterns
from modules.crack_time import estimate_crack_time
from modules.breach_check import check_breach
from modules.utils import calculate_score, classify_password
from modules.attack_simulation import simulate_attacks
from modules.report import print_report
from modules.logger import log_analysis


def analyze(password):

    # Load dataset
    dictionary = load_dictionary("datasets/common_pw.txt")

    # Core analysis
    entropy = calculate_entropy(password)

    patterns = detect_patterns(password)

    dictionary_flag = check_dictionary(password, dictionary)

    crack_times = estimate_crack_time(entropy)

    # Attack simulation (FIX)
    attack_results = simulate_attacks(password, dictionary)

    # Breach check (optional but good)
    breach_flag = check_breach(password)

    # Score calculation
    score = calculate_score(password, entropy, patterns, dictionary_flag)

    strength = classify_password(score)

    # Print report
    print_report(entropy, score, strength, crack_times, attack_results)

    # Log result
    log_analysis(password, score, strength)


def main():

    parser = argparse.ArgumentParser(description="Password Security Analyzer")

    parser.add_argument(
        "--password",
        help="Password to analyze"
    )

    args = parser.parse_args()

    if args.password:
        analyze(args.password)
    else:
        password = input("Enter password: ")
        analyze(password)


if __name__ == "__main__":
    main()