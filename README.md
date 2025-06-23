# Password Entropy Checker

## Overview
This Python project helps users evaluate the strength of their passwords by calculating password entropy. Password entropy is a measure of how unpredictable a password is, which correlates to how resistant it is to brute-force attacks.

## Features
- Calculates password entropy based on character types and length.
- Estimates the size of the character set used (lowercase, uppercase, digits, symbols).
- Provides suggestions to improve password strength when entropy is low.
- Simple command-line interface for ease of use.

## Installation
1. Make sure you have Python 3 installed on your system.
2. Clone or download this repository.
3. No additional dependencies required; uses Python standard libraries (`re`, `math`, `string`).

## Usage
Run the script via command line:
```bash
python password_entropy_checker.py
```

You will be prompted to enter a password, and the program will output the entropy value and suggestions if the password is weak.

How It Works
	•	The script checks which character sets are present in the password: lowercase letters, uppercase letters, digits, and symbols.
	•	It calculates the entropy using the formula:

```
entropy = length_of_password * log2(character_set_size)
```

•	If the entropy is below 30 bits, the tool recommends improvements such as increasing length or adding missing character types.

Example Output

```
Password Entropy Checker
Enter password: password123

Entropy: 47.60 bits
✅ Strong password detected.
```
```
Password Entropy Checker
Enter password: pass

Entropy: 18.80 bits

[!] Warning: Your password has low entropy.
Consider these improvements:
- Increase password length.
- Add uppercase letters.
- Include symbols.
```
Future Improvements
	•	Add a graphical user interface (GUI) for enhanced user experience.
	•	Integrate a dictionary check to avoid common or leaked passwords.
	•	Support batch processing for checking multiple passwords at once.
	•	Detect patterns like repeated or sequential characters to better estimate strength.

References
	•	NIST Special Publication 800-63B: Digital Identity Guidelines.
	•	OWASP Cheat Sheet Series: Password Storage.
	•	Python Documentation: https://docs.python.org/3/
	•	Regular Expressions HOWTO: https://docs.python.org/3/howto/regex.html

⸻

Author: Mishal Mohammed
Date: 24-06-2025
