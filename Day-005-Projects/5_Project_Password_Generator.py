import random
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

print("Welcome to Python Password Generator")
nr_letters = int(input("How many letters would you like in your password:\n"))
nr_numbers = int(input("How many numbers you want in your password:\n"))
nr_symbols = int(input("How many symbols you want in your password:\n"))

letter_pass = ""
for i in range(nr_letters):
    letter_pass += random.choice(letters)

print(letter_pass)

number_pass = ""
for i in range(nr_numbers):
    number_pass += random.choice(numbers)

print(number_pass)

symbol_pass = ""
for i in range(nr_symbols):
    symbol_pass += random.choice(symbols)

print(symbol_pass)

concatenate = letter_pass + number_pass + symbol_pass
combined_pass_list = concatenate
print(combined_pass_list)
total_characters = len(combined_pass_list)

final_password = ""
for i in range(total_characters):
    final_password += combined_pass_list[random.randint(0,total_characters-1)]

print(f"Your generated password is: {final_password}")

#or

#we can use random.shuffle()
