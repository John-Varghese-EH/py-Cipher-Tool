# Cipher Tool

A compact, modular Python project for the "Python Essentials" course. This tool allows users to encrypt and decrypt text and files using classical ciphers via a clean Command Line Interface (CLI).

## Features

- **Ciphers Supported**:
  - **Caesar Cipher**: A simple substitution cipher that shifts characters by a specified amount.
  - **Vigenère Cipher**: A polyalphabetic substitution cipher using a keyword.
  - **XOR Cipher**: A bitwise operation cipher suitable for both text and binary files.

- **Modes**:
  - **Text Mode**: Encrypt/Decrypt text directly from the command line.
  - **File Mode**: Encrypt/Decrypt text files (Caesar/Vigenère) or arbitrary binary files (XOR).

- **Educational Focus**:
  - Clean, modular code structure.
  - No external dependencies (Standard Library only).
  - clear separation of concerns (CLI, Logic, Utilities).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/John-Varghese-EH/py-Cipher-Tool.git
   ```
2. Navigate to the project directory:
   ```bash
   cd py-Cipher-Tool
   ```

## Usage

The easiest way to run the tool is using the `run.py` script:

```bash
python run.py -h
```

### Examples

**1. Caesar Cipher (Text Mode)**
Encrypt "Hello" with a shift of 3:
```bash
python run.py text encrypt caesar --key 3 --input "Hello"
```
*Output: Khoor*

**2. Vigenère Cipher (Text Mode)**
Decrypt "RIJVS" with key "KEY":
```bash
python run.py text decrypt vigenere --key "KEY" --input "RIJVS"
```
*Output: HELLO*

**3. XOR Cipher (File Mode)**
Encrypt a file `secret.txt` to `encrypted.bin`:
```bash
python run.py file encrypt xor --key "mysecretkey" --input secret.txt --output encrypted.bin
```

## Extending the Project

To add a new cipher:
1. Implement the logic in `cipher_tool/ciphers.py`.
2. Add validation in `cipher_tool/utils.py` if needed.
3. Update `cipher_tool/main.py` to include the new cipher in `argparse` choices and dispatch logic.

## Disclaimer

This tool is for **educational purposes only**. The implemented ciphers (Caesar, Vigenère, simple XOR) are **not secure** for protecting sensitive data in real-world scenarios.

## Author

- **Name**: John Varghese
- **GitHub**: [John-Varghese-EH](https://github.com/John-Varghese-EH)
- **Instagram**: [Cyber__Trinity](https://instagram.com/Cyber__Trinity)
