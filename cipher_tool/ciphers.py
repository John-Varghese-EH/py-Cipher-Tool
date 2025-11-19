def caesar_cipher(text, shift, decrypt=False):
    """
    Encrypts or decrypts text using the Caesar cipher.
    
    Args:
        text (str): The input text.
        shift (int): The shift value.
        decrypt (bool): If True, decrypts the text.
        
    Returns:
        str: The processed text.
    """
    if decrypt:
        shift = -shift
        
    result = []
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            # (char_code - start + shift) % 26 + start
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result.append(new_char)
        else:
            result.append(char)
            
    return "".join(result)

def vigenere_cipher(text, key, decrypt=False):
    """
    Encrypts or decrypts text using the Vigenère cipher.
    
    Args:
        text (str): The input text.
        key (str): The keyword.
        decrypt (bool): If True, decrypts the text.
        
    Returns:
        str: The processed text.
    """
    result = []
    key_index = 0
    key = key.upper()
    
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            if decrypt:
                shift = -shift
                
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result.append(new_char)
            key_index += 1
        else:
            result.append(char)
            
    return "".join(result)

def xor_cipher(data, key):
    """
    Encrypts or decrypts data using XOR cipher. 
    Since XOR is symmetric, encryption and decryption are the same.
    
    Args:
        data (str or bytes): The input data.
        key (str or bytes): The key.
        
    Returns:
        str or bytes: The processed data (same type as input).
    """
    is_binary = isinstance(data, bytes)
    
    # Convert inputs to bytes for processing
    if isinstance(data, str):
        data_bytes = data.encode('utf-8')
    else:
        data_bytes = data
        
    if isinstance(key, str):
        key_bytes = key.encode('utf-8')
    else:
        key_bytes = key
        
    # Perform XOR
    result_bytes = bytearray()
    for i in range(len(data_bytes)):
        result_bytes.append(data_bytes[i] ^ key_bytes[i % len(key_bytes)])
        
    # Return in original format
    if is_binary:
        return bytes(result_bytes)
    else:
        # Attempt to decode back to string, might fail if result is not valid utf-8
        try:
            return result_bytes.decode('utf-8')
        except UnicodeDecodeError:
            # Fallback to latin-1 to preserve data in string format if strictly needed,
            return result_bytes.decode('latin-1')

def encrypt(text, key, cipher_type):
    if cipher_type == 'caesar':
        return caesar_cipher(text, int(key))
    elif cipher_type == 'vigenere':
        return vigenere_cipher(text, key)
    elif cipher_type == 'xor':
        return xor_cipher(text, key)
    else:
        raise ValueError(f"Unknown cipher type: {cipher_type}")

def decrypt(text, key, cipher_type):
    if cipher_type == 'caesar':
        return caesar_cipher(text, int(key), decrypt=True)
    elif cipher_type == 'vigenere':
        return vigenere_cipher(text, key, decrypt=True)
    elif cipher_type == 'xor':
        return xor_cipher(text, key) # XOR is symmetric
    else:
        raise ValueError(f"Unknown cipher type: {cipher_type}")
