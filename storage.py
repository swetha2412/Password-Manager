import json
import os
from crypto import encrypt, decrypt

VAULT = "vault.json"

def load_vault(key):
    if not os.path.exists(VAULT):
        return {}
    with open(VAULT) as f:
        encrypted = f.read()
    return json.loads(decrypt(encrypted, key))

def save_vault(data, key):
    encrypted = encrypt(json.dumps(data), key)
    with open(VAULT, "w") as f:
        f.write(encrypted)
