# Password Strength Analyzer

A cybersecurity tool that evaluates password security using entropy analysis, dictionary attack simulation, pattern detection, and crack-time estimation.

## Features

- Entropy-based password strength calculation
- Dictionary attack detection
- Hybrid attack simulation
- Pattern detection (sequential characters, repeated characters)
- Password breach check using SHA-1 hashing
- Crack time estimation for CPU, GPU, and supercomputer attacks
- Security score classification
- Password analysis logging
- Rich CLI security report visualization

## Project Structure

password_strength_analyzer/
│
├── main.py
├── entropy.py
├── dictionary_check.py
├── pattern_detection.py
├── crack_time.py
├── attack_simulation.py
├── breach_check.py
├── utils.py
├── report.py
├── logger.py
│
├── datasets/
│   └── common_pw.txt
│
├── logs/
│   └── password_logs.txt
│
└── requirements.txt

## Installation

Clone the repository:

git clone https://github.com/nisha-baheti/password-strength-analyzer.git

Navigate to the project:

cd password-strength-analyzer

Install dependencies:

pip install -r requirements.txt

## Usage

Run the analyzer:

python main.py

Or analyze a password directly:

python main.py --password MyPassword123!

## Example Output

Password Security Report

Entropy: 58.99 bits  
Score: 20/100  
Strength: Weak  

Crack Time Estimates:
CPU: 18153 years  
GPU: 18 years  
Supercomputer: 0.018 years  

Attack Simulation:
Dictionary Attack: SAFE  
Hybrid Attack: LIKELY  
Numeric Attack: SAFE  

## Technologies Used

Python  
Regular Expressions  
Cryptographic Hashing (SHA-1)  
Entropy Calculations  
CLI Reporting with Rich  

## Future Improvements

- Integration with real breach databases
- Rule-based password attack simulation
- Machine learning password strength prediction
- Web interface for password analysis