import argparse
import sys
import os
from . import ciphers
from . import utils

class Colors:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

BANNER = f"""{Colors.CYAN}
 $$$$$$\  $$\           $$\                                 $$$$$$$$\                  $$\ 
$$  __$$\ \__|          $$ |                                \__$$  __|                 $$ |
$$ /  \__|$$\  $$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\           $$ | $$$$$$\   $$$$$$\  $$ |
$$ |      $$ |$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\          $$ |$$  __$$\ $$  __$$\ $$ |
$$ |      $$ |$$ /  $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|         $$ |$$ /  $$ |$$ /  $$ |$$ |
$$ |  $$\ $$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |               $$ |$$ |  $$ |$$ |  $$ |$$ |
\$$$$$$  |$$ |$$$$$$$  |$$ |  $$ |\$$$$$$$\ $$ |               $$ |\$$$$$$  |\$$$$$$  |$$ |
 \______/ \__|$$  ____/ \__|  \__| \_______|\__|               \__| \______/  \______/ \__|
              $$ |                                                                         
              $$ |                                                  By: John Varghese (J0X)
              \__|                                                                         
{Colors.YELLOW}      >> Classical Encryption & Decryption Utility <<{Colors.RESET}
"""

def main():
    # Enable ANSI support on Windows
    if os.name == 'nt':
        os.system('')
        
    print(BANNER)
    
    parser = argparse.ArgumentParser(
        description=f"{Colors.GREEN}A compact tool by John Varghese (@Cyber__Trinity){Colors.RESET}",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    # Positional arguments
    parser.add_argument('mode', choices=['text', 'file'], help="Mode of operation: 'text' for direct input, 'file' for file I/O")
    parser.add_argument('operation', choices=['encrypt', 'decrypt'], help="Operation to perform")
    parser.add_argument('cipher', choices=['caesar', 'vigenere', 'xor'], help="Cipher algorithm to use")
    
    # Optional arguments
    parser.add_argument('--key', required=True, help="Key for the cipher (Integer for Caesar, String for Vigenère/XOR)")
    parser.add_argument('--input', required=True, help="Input text (in text mode) or input filename (in file mode)")
    parser.add_argument('--output', help="Output filename (required in file mode)")
    
    args = parser.parse_args()
    
    # Validate arguments
    if args.mode == 'file' and not args.output:
        parser.error("The --output argument is required in file mode.")
        
    try:
        # Validate and prepare key
        if args.cipher == 'caesar':
            key = utils.validate_shift_key(args.key)
        elif args.cipher == 'vigenere':
            key = utils.validate_keyword(args.key)
        elif args.cipher == 'xor':
            key = utils.validate_xor_key(args.key)
            
        # Process input
        if args.mode == 'text':
            input_data = args.input
            # For XOR text mode, we treat input as string
            if args.cipher == 'xor':
                # For text input with XOR, we might get non-printable chars on decrypt if we passed raw bytes string?
                # But CLI args are strings.
                pass
        else:
            # File mode
            binary_mode = (args.cipher == 'xor')
            input_data = utils.read_file(args.input, binary=binary_mode)
            
        # Perform operation
        if args.operation == 'encrypt':
            result = ciphers.encrypt(input_data, key, args.cipher)
            action_verb = "Encrypted"
        else:
            result = ciphers.decrypt(input_data, key, args.cipher)
            action_verb = "Decrypted"
            
        # Handle output
        if args.mode == 'text':
            print(f"\n{Colors.GREEN}Success! {action_verb} Output:{Colors.RESET}\n")
            print(f"{Colors.BOLD}{result}{Colors.RESET}")
        else:
            binary_mode = (args.cipher == 'xor')
            utils.write_file(args.output, result, binary=binary_mode)
            print(f"\n{Colors.GREEN}Success! {action_verb} file saved to: {Colors.BOLD}{args.output}{Colors.RESET}")
            
    except Exception as e:
        print(f"\n{Colors.RED}Error: {str(e)}{Colors.RESET}")
        sys.exit(1)

if __name__ == "__main__":
    main()
