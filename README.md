<div align="center">

<img src="entropy_banner.svg" alt="Entropy Checker Banner" width="100%">

<br>

**A lightweight Python CLI tool to calculate cryptographic password entropy and brute-force resilience.**

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](#)
[![Security](https://img.shields.io/badge/Security-Cryptography-16a34a?style=for-the-badge&logo=shield&logoColor=white)](#)
[![CLI](https://img.shields.io/badge/Interface-CLI-0f172a?style=for-the-badge&logo=gnome-terminal&logoColor=white)](#)

*Evaluating password unpredictability based on character set depth and string length.*

</div>

<br>

## 📋 Architectural Overview
This Python project evaluates the core strength of user passwords by calculating their **Shannon Entropy**. Password entropy is a definitive measure of unpredictability; a higher bit-value directly correlates to increased mathematical resistance against offline brute-force and dictionary attacks. 

Engineered for local, offline execution, it ensures sensitive strings are never transmitted over a network during analysis.

---

## ⚙️ Core Engine Features

* **Mathematical Analysis:** Dynamically calculates entropy bits based on character types and total length.
* **Pool Estimation:** Accurately determines the size of the utilized character set (Lowercase, Uppercase, Numeric Digits, Special Symbols).
* **Actionable Telemetry:** Provides specific, algorithmic suggestions to improve string strength when entropy falls below secure thresholds.
* **Zero-Dependency Architecture:** Built using only standard Python libraries (`re`, `math`, `string`) for maximum portability across Linux, macOS, and Windows environments.

---

## 🧮 The Mathematics

The engine calculates cryptographic strength using the standard entropy formula:

```text
E = L × log₂(R)

Where:
E = Total password entropy (in bits)
L = Length of the password
R = Size of the pool of unique characters used

```
## 🚀 Local Deployment Guide

To deploy the analyzer locally for testing or integration, follow these CLI commands:

**1. Clone the repository:**
```bash
git clone https://github.com/YOUR_USERNAME/password-entropy-checker.git
cd password-entropy-checker
```

**2. Execute the analyzer:**
*(Ensure Python 3.x is installed on your system)*
```bash
python password_entropy_checker.py
```

### Example Telemetry Output

**Secure Execution:**
```text
Password Entropy Checker
Enter password: > ************

Entropy: 72.40 bits
✅ Strong password detected.
```

**Vulnerable Execution:**
```text
Password Entropy Checker
Enter password: > pass

Entropy: 18.80 bits
[!] Warning: Critical vulnerability. Low entropy detected.

Recommended Mitigations:
- Increase overall string length.
- Inject uppercase alphabetic characters.
- Integrate non-alphanumeric symbols.
```

---

## 🗺️ V1.1 Engineering Roadmap

We are actively exploring expansions for the entropy engine to handle enterprise-scale auditing:

- [ ] **Pattern Recognition Engine:** Detect spatial keyboard patterns (e.g., `qwerty`), sequential characters (e.g., `1234`), and repetitive blocks that artificially inflate math-based entropy.
- [ ] **Dictionary Cross-Referencing:** Integrate against known breach compilations (e.g., HaveIBeenPwned API) to flag compromised hashes.
- [ ] **Batch Processing Mode:** Enable `.txt` or `.csv` ingestion to audit multiple passwords simultaneously for active directory environments.

---

## 📚 Security References
* **NIST Special Publication 800-63B:** Digital Identity Guidelines
* **OWASP:** Password Storage Cheat Sheet Series
* **Python Documentation:** [Regex HOWTO](https://docs.python.org/3/howto/regex.html)

⸻

Author: Mishal Mohammed
Date: 24-06-2025
