#Password Generator Project

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator")

letters_input = int(input("How many letters would you like in your password\n"))
symbols_input = int(input("How many symbols would you like?\n"))
numbers_input = int(input("How many numbers would you like\n"))

password_list = []

for i  in range(1, letters_input + 1):
    password_list.append(random.choice(letters))
for i  in range(1, symbols_input + 1):
    password_list.append(random.choice(symbols))
for i  in range(1, numbers_input + 1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""
for i in password_list:
    password += i

print(f"Your generated password is: {password}")
      
# Second Variant

# letters_result = random.sample(letters, k = letters_input)
# symbols_result = random.sample(symbols, k = symbols_input)
# numbers_result = random.sample(numbers, k = numbers_input)

# total_result = letters_result + symbols_result + numbers_result
# random.shuffle(total_result)
# print(total_result)
# final_password = ''.join(total_result)
# print(f"Your generated password is: {final_password}")