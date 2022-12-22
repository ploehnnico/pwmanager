import sqlite3

class Entry:
	def __init__(self, id, name, password, description=None):
		self.id = id
		self.name = name
		self.password = password
		self.description = description

class DAL:
	def __init__(self, dbfile):
		self.dbfile = dbfile
		self.connection = None

	def connect(self):
		self.connection = sqlite3.connect(self.dbfile)
		self._createtables()

	def _createtables(self):
		cursor = self.connection.cursor() 
		cursor.execute("""CREATE TABLE IF NOT EXISTS passwords (
					   id integer PRIMARY KEY,
					   name text not NULL,
					   password text not NULL,
					   description text)""")

	def create_entry(self, name, password, description=""):
		cursor = self.connection.cursor()
		cursor.execute(""" INSERT INTO passwords 
					   (name, password, description) 
					   VALUES (?, ?, ?)""", (name, password, description))
		self.connection.commit()
	
	def get_entry(self, entry_id):
		cursor = self.connection.cursor()
		cursor.execute("SELECT * FROM passwords WHERE id =?", (entry_id,))
		row = cursor.fetchone()
		if row:
			return Entry(*row)
		else:
			return None

	def update_entry(self, entry_id, name, password, description):
		cursor = self.connection.cursor()
		cursor.execute("""UPDATE passwords SET name = ?, password = ?,
		description = ? WHERE id = ?""", (entry_id, name, password, description)
		)
		self.connection.commit()
	
	def delete_entry(self, entry_id):
		cursor = self.connection.cursor()
		cursor.execute("DELETE FROM passwords WHERE id = ?", (entry_id))
		self.connection.commit()
	
	def get_all_entries(self):
		cursor = self.connection.cursor()
		cursor.execute("SELECT * FROM passwords")
		rows = cursor.fetchall()
		entries = [Entry(*row) for row in entries]
		return entries
