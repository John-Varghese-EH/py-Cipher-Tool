# Cipher Tool

Compact, modular Python project, that encrypts and decrypts text and files using classical ciphers via a clean command-line user interface (CLI).

<p align="center">
  <img src="/screenshort/cipher-tool-1.png" alt="Screenshort Preview of Cipher Tool" width="500" style="max-width: 100%; height: auto;">
</p>

## Features

- Ciphers supported are:
  - **Caesar Cipher:** A basic substitution cipher that shifts the characters by some predefined amount.
  - **Vigenère Cipher:** A polyalphabetic substitution cipher, whereby text is encrypted based on a keyword.
  - **XOR Cipher:** A classical cipher based on bitwise operations for encrypting arbitrary text and binary files.

- Modes:
  Text Mode and File Mode are the two modes available for selection
  - Text Mode: Encrypt/Decrypt text on-the-fly via command line.
  - File Mode: Encrypt/Decrypt text files (using Caesar/Vigenère) or any file(binary) using XOR.

- Educational Focus:
  - Clean and modular code structure.
  - Without external dependencies (The Standard Library was used only).
  - Separation of Concerns (CLI, Logic, Utilities).
## Installation

1. To Clone the repository:
```bash
git clone https://github.com/John-Varghese-EH/py-Cipher-Tool.git
```
2. Navigate to the project directory:
```bash
cd py-Cipher-Tool
```

## Usage

### Display help
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

**To Encrypt a text file:**
```bash
python run.py file encrypt caesar --key 5 --input message.txt --output encrypted.txt
```

**To Decrypt a text file:**
```bash
python run.py file decrypt caesar --key 5 --input encrypted.txt --output decrypted.txt
```

**To Encrypt a binary file (XOR):**
```bash
python run.py file encrypt xor --key SecretKey --input image.png --output encrypted.bin
```

## Testing

Run the test suite to verify all cipher implementations work as expected.
```bash
python tests.py
```

## Adding New Ciphers

To add more ciphers to the tool:

1. Implement the cipher logic in `cipher_tool/ciphers.py`
2. Add validation in `cipher_tool/utils.py` wherever applicable
3. Modify `cipher_tool/main.py` to add the argparse choices and dispatch logic
4. Add corresponding tests in `tests.py`

## Disclaimer

This tool is for education only. The ciphers offered for (Caesar, Vigenère, simple XOR) are NOT secure for protecting sensitive data if applied in the real world.
---

<a href="https://github.com/John-Varghese-EH/py-Cipher-Tool">Cipher Tool</a> © 2025 by <a href="https://www.linkedin.com/in/john--varghese/">John Varghese (@Cyber_Trinity) J0X</a>
