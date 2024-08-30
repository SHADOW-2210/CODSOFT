import random
import string

def easy_level_pass_numbers(n):
	print("Easy level password (only numbers): ", end="")
	for i in range(n):
		print(random.randint(0, 9), end="")
	print()

def easy_level_pass_letters(n):
	print("Easy level password (only letters): ", end="")
	for i in range(n):
		print(random.choice(string.ascii_letters), end="")
	print()

def mid_level_pass(n):
	print("Medium level password: ", end="")
	for i in range(n):
		print(random.choice(string.ascii_letters + string.digits), end="")
	print()

def strong_level_pass(n):
	print("Strong level password: ", end="")
	for i in range(n):		
		print(random.choice(string.ascii_letters + string.digits + string.punctuation), end="")
	print()

if __name__ == '__main__':
	n = int(input("Enter the Length of the Password:"))

	easy_level_pass_numbers(n)
	easy_level_pass_letters(n)
	mid_level_pass(n)
	strong_level_pass(n)


