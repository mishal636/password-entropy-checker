import re
import math
import string

def calculate_charset_size(password):
    charset = 0
    if re.search(r'[a-z]', password):
        charset += 26
    if re.search(r'[A-Z]', password):
        charset += 26
    if re.search(r'\d', password):
        charset += 10
    if re.search(rf"[{re.escape(string.punctuation)}]", password):
        charset += len(string.punctuation)
    return charset

def calculate_entropy(password):
    charset_size = calculate_charset_size(password)
    length = len(password)
    if charset_size == 0 or length == 0:
        return 0.0
    return length * math.log2(charset_size)

def display_suggestions(password):
    print("\n[!] Warning: Your password has low entropy.")
    print("Consider these improvements:")
    if len(password) < 12:
        print("- Increase password length.")
    if not re.search(r'[A-Z]', password):
        print("- Add uppercase letters.")
    if not re.search(r'[a-z]', password):
        print("- Add lowercase letters.")
    if not re.search(r'\d', password):
        print("- Add digits.")
    if not re.search(rf"[{re.escape(string.punctuation)}]", password):
        print("- Include symbols.")

def main():
    print("Password Entropy Checker")
    password = input("Enter password: ").strip()
    if not password:
        print("[!] No input detected.")
        return
    entropy_value = calculate_entropy(password)
    print(f"\nEntropy: {entropy_value:.2f} bits")
    if entropy_value < 30:
        display_suggestions(password)
    else:
        print("✅ Strong password detected.")

if __name__ == "__main__":
    main()

