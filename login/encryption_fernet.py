from cryptography.fernet import Fernet 
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os
import base64
password = b"gully@boy"
salt = os.urandom(16)
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=480000,
)
key = base64.urlsafe_b64encode(kdf.derive(password))
# key = Fernet.generate_key()
f = Fernet(key)

# encrypt
name = f.encrypt(b"Radha")
print(name)

# decrypt
data = f.decrypt(name)
print(data)