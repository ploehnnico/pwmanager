import argparse
import application
import time
from getpass import getpass
import application


class CLI:
	def __init__(self):
		self.manager = application.Manager() 
		pass

	def new_file(self):
		name = input("Name:")
		_delete_lines(1)
		while(True):
			pw = getpass("Enter new password:")
			repeat = getpass("Repeat password")
			if pw == repeat:
				break
			print("Passwords dont match!")
			time.sleep(1)
			_delete_lines(4)
		path = self.manager.new_key_file(pw, name)
		self.manager.connect(path)
		print("Created new key file.")
		pass
	
	def select_option(self):
		print(("1 Create new keyfile \n"
			   "2 Choose from existing \n"
			   "3 Enter path\n"))
		choice = 0
		while choice not in ["1", "2", "3"]:
			choice = input("Select option:")
			_delete_lines(1)
		_delete_lines(7)
		return choice

	def select_file(self):
		files = self.manager.get_key_files()
		n = 0
		for i, f in enumerate(files):
			print(f"{i+1} {f} \n")
			n = i 
		#TODO: back to menu
		choice = 0
		while choice not in [str(x +1) for x in range(0, n)]:
			choice = input("Select existing key file:")
			_delete_lines(1)
		_delete_lines(i+1)
		path = files[choice -1]
		self.manager.connect(path)
		return choice

	def list_entries(self):
		pass
		
def main():
	cli = CLI()
	choice = cli.select_option()
	if choice == "1":
		cli.new_file()
		pass
	elif choice == "2":
		cli.select_file()
		pass
	elif choice == "3":
		pass
	pass

def _delete_lines(nlines):
	LINE_UP = '\033[1A'
	LINE_CLEAR = '\x1b[2K'
	for _ in range(nlines):
		print(LINE_UP, end=LINE_CLEAR)
	pass

if __name__ == "__main__":
	main()