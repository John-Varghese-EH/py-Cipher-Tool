# Cipher Tool

A small, modular Python project for the course "Python Essentials". This allows enciphering and deciphering the text and files using classical ciphers through a clean Command Line Interface (CLI).

## Features

- **Ciphers Supported**:
  - **Caesar Cipher**: A substitution cipher that simply shifts characters by a certain amount.
  - **Vigenère Cipher**: A polyalphabetic substitution cipher using a keyword.
  - **XOR Cipher**: A bitwise operation cipher that can be applied to both text and binary files.

- **Modes**:
  - **Text Mode**: Encrypt/Decrypt inside command line.
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
2. Change directory to py-Cipher-Tool:
   ```bash
   cd py-Cipher-Tool
   ```

## Usage

The easiest way of running the tool is through `run.py` script.

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
Decrypt "RIJVS" using key "KEY":
```bash
python run.py text decrypt vigenere --key "KEY" --input "RIJVS"
```
*Output: HELLO*

**3. XOR Cipher (File Mode)**
Encrypt file `secret.txt` to `encrypted.bin`:
```bash
python run.py file encrypt xor --key "mysecretkey" --input secret.txt --output encrypted.bin
```

## Extending the Project

To add a new cipher:
1. Implement logic into `cipher_tool/ciphers.py`.
2. Enhance validation into `cipher_tool/utils.py`, if necessary.
3. Integrate the cipher into `argparse` choices and dispatch logic in `cipher_tool/main.py`.

## Disclaimer

The tool is for educational purposes only. The ciphers developed (Caesar, Vigenère, and simple XOR) aren't secure for sensitive data protection in real-life applications.

## Author

- **Name**: John Varghese
- **GitHub**: [John-Varghese-EH](https://github.com/John-Varghese-EH)
- **Instagram**: [Cyber__Trinity](https://instagram.com/Cyber__Trinity)