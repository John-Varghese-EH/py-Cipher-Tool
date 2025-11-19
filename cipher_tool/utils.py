import os

def read_file(filepath, binary=False):
    """
    Reads content from a file.
    
    Args:
        filepath (str): Path to the file.
        binary (bool): If True, read as binary bytes. Else read as text.
        
    Returns:
        str or bytes: The content of the file.
        
    Raises:
        FileNotFoundError: If the file does not exist.
        IOError: If there is an error reading the file.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
        
    mode = 'rb' if binary else 'r'
    encoding = None if binary else 'utf-8'
    
    try:
        with open(filepath, mode, encoding=encoding) as f:
            return f.read()
    except Exception as e:
        raise IOError(f"Error reading file {filepath}: {e}")

def write_file(filepath, content, binary=False):
    """
    Writes content to a file.
    
    Args:
        filepath (str): Path to the file.
        content (str or bytes): Content to write.
        binary (bool): If True, write as binary bytes. Else write as text.
        
    Raises:
        IOError: If there is an error writing to the file.
    """
    mode = 'wb' if binary else 'w'
    encoding = None if binary else 'utf-8'
    
    try:
        with open(filepath, mode, encoding=encoding) as f:
            f.write(content)
    except Exception as e:
        raise IOError(f"Error writing to file {filepath}: {e}")

def validate_shift_key(key):
    """
    Validates that the key is a valid integer for Caesar cipher.
    """
    try:
        k = int(key)
        return k
    except ValueError:
        raise ValueError("Key must be an integer for Caesar cipher.")

def validate_keyword(key):
    """
    Validates that the key is a valid string for Vigenère cipher.
    """
    if not key or not isinstance(key, str) or not key.isalpha():
        raise ValueError("Key must be a non-empty alphabetic string for Vigenère cipher.")
    return key

def validate_xor_key(key):
    """
    Validates the XOR key. It can be a string or bytes.
    """
    if not key:
        raise ValueError("Key must not be empty for XOR cipher.")
    return key
