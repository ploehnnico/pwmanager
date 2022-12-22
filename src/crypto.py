import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def new_key(pw):
	salt = os.urandom(16)
	key = get_key(pw, salt)
	return key, salt

def get_key(pw, salt):
	kdf = PBKDF2HMAC(
		algorithm=hashes.SHA384(),
		length=32,
		salt=salt,
		iterations=480000
	)
	key = base64.urlsafe_b64encode(kdf.derive(pw.encode()))
	return key

def encrypt_file(key, path):
	with open(path, 'rb') as b:
		data = b.read()
	f = Fernet(key)
	token = f.encrypt(data)
	with open(path, 'wb') as  b:
		b.write(token)
	pass

def decrypt_file(key, path):
	with open(path, 'rb') as b:
		token = b.read()
	f = Fernet(key)
	token = f.decrypt(token)
	with open(path, 'wb') as  b:
		b.write(token)