import os

while True:
	usr = os.getlogin()
	home = os.getcwd()

	cmd = input("(bash)" + usr + "@" + home + ": ")
	os.system(cmd)