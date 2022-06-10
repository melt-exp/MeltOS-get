import os

file = input("File to programify: ")
options = input(f"Options to add to {file}: ")
os.system(f"chmod {options} {file}")
print(f"{file} is now programified!")
