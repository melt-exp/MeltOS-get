import os

usr = os.getlogin()
home = os.getcwd()

while True:
		cmd = input("(shell)" + usr + "@" + home + ": ")
		if(cmd == "exit"):
			exit()
		else:
			print(os.system(cmd))