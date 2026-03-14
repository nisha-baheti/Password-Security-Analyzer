# Password Security Analyzer

A Python-based cybersecurity tool that evaluates password strength using entropy analysis, dictionary attack detection, and weak pattern identification. The tool generates a detailed password security report and provides recommendations for improving password robustness.

---

## Features

- Entropy-based password strength evaluation
- Detection of weak password patterns (repeated characters, sequential patterns)
- Dictionary attack simulation using common password datasets
- Security scoring system with strength classification
- Detailed command-line password security report
- Actionable suggestions for improving password strength

---

## Project Structure

password-security-analyzer
│
├── main.py                # Main program that runs the analyzer
├── entropy.py             # Calculates password entropy
├── dictionary_check.py    # Checks passwords against common password lists
├── pattern_detection.py   # Detects weak patterns in passwords
├── utils.py               # Scoring system and strength classification
├── password_dataset.txt   # Common password dataset for dictionary checks
└── README.md              # Project documentation

---

## Installation

1. Clone the repository

git clone https://github.com/nisha-baheti/password-security-analyzer.git

2. Navigate to the project directory

cd password-security-analyzer

3. Run the program

python main.py

---

## Usage

Run the analyzer and enter a password when prompted.

Example:

Enter password to analyze: password123

Output:

Password Security Report
------------------------
Entropy: 36.4 bits
Score: 35 / 100
Strength: Moderate

Warning: Password contains common dictionary words

Suggestions:
- Increase password length
- Add uppercase letters
- Add special characters

---

## Security Analysis Metrics

The analyzer evaluates password strength using:

- **Entropy Calculation**  
  Estimates password randomness using character set size and password length.

- **Dictionary Attack Detection**  
  Checks whether the password appears in a dataset of commonly used passwords.

- **Pattern Detection**  
  Detects weak patterns such as repeated characters or sequential keyboard patterns.

- **Strength Scoring System**  
  Generates a score out of 100 based on multiple security factors.

---

## Future Improvements

Possible enhancements for future versions:

- Integration with large leaked password datasets
- GUI-based password analyzer
- Password breach detection using online APIs
- Machine learning-based password strength prediction
- Integration with password manager tools

---

## Author

**Nisha Baheti**  
B.E. Computer Science & Engineering  
University College of Engineering, Osmania University

---

## License

This project is for educational and research purposes.
