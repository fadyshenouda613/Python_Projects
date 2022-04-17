import random
import string

# declarations
letters = list(string.ascii_letters)
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
# Input
nr_letter = int(input("How many letters would you like in your password? \n"))
nr_number = int(input("How many numbers would you like in your password? \n"))
nr_symbols = int(input("How many symbols would you like in your password \n"))
password_list = []
# for loops to generate random password
for char in range(1, nr_letter + 1):
    password_list.append(random.choice(letters))
for char in range(1, nr_number + 1):
    password_list.append(random.choice(numbers))
for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))
# shuffles the password list
random.shuffle(password_list)
password = ""
# transforms the password_list into a string
for char in password_list:
    password += char
print(f"Your generated password:{password}")
