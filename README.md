# Cipher Tool

A compact, modular Python project, which allows encrypting and decrypting texts and files using classical ciphers through a simple and clean Command Line Interface (CLI).

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
2. You may then proceed to the directory of the project with:
```bash
cd kay-Cipher-Tool
```
## Usage

The easiest way to run its parts as used below:

```bash
python run.py -h
```

Implement the logic in cipher_tool/ciphers.py.
- Validation should be included in cipher_tool/utils.py if necessary.
- Update cipher_tool/main.py to include argparse choices and dispatch logic for the new cipher. 

Disclaimer
This tool is solely meant for educational purposes. The ciphers available (Caesar, Vigenère, simple XOR) are in no way safe for securing sensitive data in real-world use.

Author
Name: John Varghese
GitHub: John-Varghese-EH
Instagram: Cyber__Trinity
