import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


def generate_easy_password(nr_of_letters,nr_of_symbols,nr_of_numbers):
    password=""
    for i in range(1, nr_of_letters+1):
        password += random.choice(letters)
    for i in range(1, nr_of_symbols+1):
        password += random.choice(symbols)
    for i in range(1, nr_of_numbers+1):
        password += random.choice(numbers)
    return password

#print("easy PW: "+ generate_easy_password(nr_letters,nr_symbols,nr_numbers))

def generate_hard_password():
    password = generate_easy_password(nr_letters,nr_symbols,nr_numbers)
    print("Easy PW: " + password)
    shuffled_password = ''.join(random.sample(password,len(password)))
    return shuffled_password

print("hard PW: " + generate_hard_password())
