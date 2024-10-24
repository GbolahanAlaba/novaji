from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import os
import base64

# AES 256 CBC encryption and decryption
def encrypt(text, key, iv):
    # Padding the text
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_text = padder.update(text.encode()) + padder.finalize()

    # Encrypt the padded text
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_text = encryptor.update(padded_text) + encryptor.finalize()

    # Return the encrypted text in base64 for readability
    return base64.b64encode(encrypted_text).decode()

def decrypt(encrypted_text, key, iv):
    # Decode base64 and decrypt
    encrypted_text_bytes = base64.b64decode(encrypted_text)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_padded_text = decryptor.update(encrypted_text_bytes) + decryptor.finalize()

    # Unpadding the text
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    decrypted_text = unpadder.update(decrypted_padded_text) + unpadder.finalize()

    return decrypted_text.decode()

# Generate random 32-byte key for AES-256 and a random 16-byte IV
key = os.urandom(32)  # 256-bit key for AES-256
iv = os.urandom(16)   # 128-bit IV for AES-CBC

# Text to encrypt and decrypt
text = "Welcome to Lagos"

# Encrypt the text
encrypted_text = encrypt(text, key, iv)
print(f"Encrypted: {encrypted_text}")

# Decrypt the text
decrypted_text = decrypt(encrypted_text, key, iv)
print(f"Decrypted: {decrypted_text}")
