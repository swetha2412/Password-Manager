import hashlib
import os

FILE = "master.key"

def hash_password(pw):
    return hashlib.sha256(pw.encode()).hexdigest()

def setup_master():
    pw = input("Set master password: ")
    with open(FILE, "w") as f:
        f.write(hash_password(pw))
    print("Master password created.")

def login():
    pw = input("Enter master password: ")
    with open(FILE) as f:
        stored = f.read()
    return hash_password(pw) == stored
