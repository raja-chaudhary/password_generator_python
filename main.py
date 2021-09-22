import random
from characters import letters, numbers, symbols

print("Welcome to the PyPassword Generator!\n\n")

# taking inputs from user
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

total_characters = nr_letters + nr_symbols + nr_numbers

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# pulling out the letters randomly from the letters list and appending them in an empty list of characters
characters = []
for i in range(1, nr_letters+1):
    characters.append(letters[random.randint(0, 51)])
pass1 = "".join(characters)

# pulling out the letters randomly from the symbols list and appending them in an empty list of signs
signs = []
for i in range(1, nr_symbols+1):
    signs.append(symbols[random.randint(1, len(symbols)-1)])
pass2 = "".join(signs)


# pulling out the letters randomly from the numbers list and appending them in an empty list of nums
nums = []
for i in range(1, nr_numbers+1):
    nums.append(numbers[random.randint(1, len(numbers)-1)])
pass3 = "".join(nums)

print(f"Easy Password: {pass1}{pass2}{pass3}")

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_easy = pass1 + pass2 + pass3

# create a list of characters from the easy password
pass_list = list(password_easy)
# shuffle the items in the pass_list list
random.shuffle(pass_list)
pass_hard = ("".join(pass_list))
print(f"Hard Password: {pass_hard}")
