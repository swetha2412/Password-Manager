from cryptography.fernet import Fernet
import base64
import hashlib

def derive_key(master_password: str):
    hash = hashlib.sha256(master_password.encode()).digest()
    return base64.urlsafe_b64encode(hash)

def encrypt(data: str, key: bytes):
    return Fernet(key).encrypt(data.encode()).decode()

def decrypt(data: str, key: bytes):
    return Fernet(key).decrypt(data.encode()).decode()
