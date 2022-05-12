import os

while True:
	usr = os.getlogin()
	home = os.getcwd()

	cmd = input(f"(bash) {usr}@{home}: ")
	os.system(cmd)
