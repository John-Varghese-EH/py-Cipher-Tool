import unittest
import os
from cipher_tool import ciphers, utils

class TestCiphers(unittest.TestCase):
    
    def test_caesar(self):
        text = "Hello World"
        shift = 3
        encrypted = ciphers.encrypt(text, shift, 'caesar')
        self.assertEqual(encrypted, "Khoor Zruog")
        decrypted = ciphers.decrypt(encrypted, shift, 'caesar')
        self.assertEqual(decrypted, text)
        
    def test_vigenere(self):
        text = "HELLO"
        key = "KEY"
        encrypted = ciphers.encrypt(text, key, 'vigenere')
        # H(7)+K(10)=R(17), E(4)+E(4)=I(8), L(11)+Y(24)=J(9), L(11)+K(10)=V(21), O(14)+E(4)=S(18)
        self.assertEqual(encrypted, "RIJVS")
        decrypted = ciphers.decrypt(encrypted, key, 'vigenere')
        self.assertEqual(decrypted, text)
        
    def test_xor_text(self):
        text = "Secret"
        key = "Key"
        encrypted = ciphers.encrypt(text, key, 'xor')
        decrypted = ciphers.decrypt(encrypted, key, 'xor')
        self.assertEqual(decrypted, text)
        
    def test_xor_binary(self):
        data = b'\x00\x01\x02'
        key = b'\xFF'
        encrypted = ciphers.encrypt(data, key, 'xor')
        self.assertEqual(encrypted, b'\xff\xfe\xfd')
        decrypted = ciphers.decrypt(encrypted, key, 'xor')
        self.assertEqual(decrypted, data)

class TestUtils(unittest.TestCase):
    def setUp(self):
        import tempfile
        self.temp_dir = tempfile.TemporaryDirectory()
        self.test_file = os.path.join(self.temp_dir.name, "test_utils_file.txt")
        with open(self.test_file, "w") as f:
            f.write("Test Content")
            
    def tearDown(self):
        self.temp_dir.cleanup()
            
    def test_read_write(self):
        content = utils.read_file(self.test_file)
        self.assertEqual(content, "Test Content")
        
        new_file = os.path.join(self.temp_dir.name, "test_utils_write.txt")
        utils.write_file(new_file, "New Content")
        self.assertEqual(utils.read_file(new_file), "New Content")

if __name__ == '__main__':
    unittest.main()
