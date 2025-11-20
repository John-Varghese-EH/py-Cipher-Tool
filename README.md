# Cipher Tool

A compact, modular Python project, which allows encrypting and decrypting texts and files using classical ciphers through a simple and clean Command Line Interface (CLI).

<p align="center">
  <img src="/screenshort/cipher-tool-1.png" alt="Screenshort preview of Cipher tool" width="500" style="max-width: 100%; height: auto;">
</p>

## Features

- The supported ciphers are as follows:
  - **Caesar Cipher:** A basic substitution cipher, which shifts the characters by a defined amount.
  - **Vigenère Cipher:** A polyalphabetic substitution cipher that encrypts text based on a keyword.
  - **XOR Cipher:** A bitwise operation-based cipher available for the encryption of both text and binary files.

- Modes:
  - There are two possible modes to pick from: Text Mode and File Mode.
  - Text Mode: Encrypt/Decrypt text on-the-fly while using the command line.
  - File Mode: Encrypt/Decrypt text files (Caesar/Vigenère) or any binary file to the use of XOR.

- Educational Focus:
  - Clean and modular code structure.
  - Without external dependencies (The Standard Library was used only).
  - Promotes the separation of concerns (CLI, Logic, Utilities).
## Installation

1. Cloning the repository is relatively easy:
```bash
git clone https://github.com/John-Varghese-EH/py-Cipher-Tool.git
```
2. Navigate to the project directory:
```bash
cd py-Cipher-Tool
```

## Usage

### Display Help
```bash
python run.py -h
```

### Text Mode Examples

**Caesar Cipher:**
```bash
# Encrypt
python run.py text encrypt caesar --key 3 --input "Hello World"

# Decrypt
python run.py text decrypt caesar --key 3 --input "Khoor Zruog"
```

**Vigenère Cipher:**
```bash
# Encrypt
python run.py text encrypt vigenere --key SECRET --input "ATTACK AT DAWN"

# Decrypt
python run.py text decrypt vigenere --key SECRET --input "SXVRGD SX HMGR"
```

**XOR Cipher:**
```bash
# Encrypt/Decrypt (symmetric)
python run.py text encrypt xor --key MyKey --input "Secret Message"
```

### File Mode Examples

**Encrypt a text file:**
```bash
python run.py file encrypt caesar --key 5 --input message.txt --output encrypted.txt
```

**Decrypt a text file:**
```bash
python run.py file decrypt caesar --key 5 --input encrypted.txt --output decrypted.txt
```

**Encrypt a binary file (XOR):**
```bash
python run.py file encrypt xor --key SecretKey --input image.png --output encrypted.bin
```

## Testing

Run the test suite to verify all ciphers work correctly:
```bash
python tests.py
```

## Adding New Ciphers

To extend the tool with additional ciphers:

1. Implement the cipher logic in `cipher_tool/ciphers.py`
2. Add validation in `cipher_tool/utils.py` if necessary
3. Update `cipher_tool/main.py` to include argparse choices and dispatch logic
4. Add corresponding tests in `tests.py`

## Disclaimer

This tool is solely meant for **educational purposes**. The ciphers available (Caesar, Vigenère, simple XOR) are **NOT secure** for protecting sensitive data in real-world applications.
---

<a href="https://github.com/John-Varghese-EH/py-Cipher-Tool">Cipher Tool</a> © 2025 by <a href="https://www.linkedin.com/in/john--varghese/">John Varghese (@Cyber_Trinity) J0X</a>
