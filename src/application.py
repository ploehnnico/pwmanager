import crypto
import data 
import os

class Manager:
	def __init__(self, filepath=None):
		self.dal = None 
		self.key = None
		self.filepath = None

	def connect(self, path):
		self.dal = data.DAL(path)
		pass

	def new_key_file(self, password, name):
		key, salt = crypto.new_key(password)
		self.key = key
		with open(f'./db/.{name}_salt', 'w') as f:
			f.writelines(str(salt))
		path= f'./keyfiles/{name}.key'
		self.dal.connect(path)
		crypto.decrypt_file(self.key, path)
		return path

	def get_entries(self):
		crypto.decrypt_file(self.key, self.filepath)
		self.dal.connect()
		entries = self.dal.get_all_entries()
		crypto.encrypt_file(self.key, self.filepath)
		pass
	
	def new_entry(self, name, password, description=""):
		crypto.decrypt_file(self.key, self.filepath)
		self.dal.connect()
		self.dal.create_entry(name, password, description)
		crypto.encrypt_file(self.key, self.filepath)
		pass

	def get_key_files(self):
		files = [x.split('.')[0] for x in os.listdir('./keyfiles')]
		return files


	
