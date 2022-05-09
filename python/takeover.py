import os

while True:
	usr = os.getlogin()
	home = os.getcwd()

	try:
		cmd = input("(bash)" + usr + "@" + home + ": ")
		if(cmd == "exit"):
			exit()
		else:
			print(os.system(cmd))
	except KeyboardInterrupt:
		print("\n")