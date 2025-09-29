import random
import string

def gen_password(length,use_digits=True,use_symbols=True):

    letters = string.ascii_letters
    digits = string.digits if use_digits else ''
    symbols = string.punctuation if use_symbols else ''

    all_chars = letters + digits + symbols

    if not all_chars:
        raise ValueError("No Characters available for password generation")
    
    password = []
    password.append(random.choice(letters))
    if use_digits:
        password.append(random.choice(digits))
    if use_symbols:
        password.append(random.choice(symbols))

    while len(password) < length:
        password.append(random.choice(all_chars))

    random.shuffle(password)
    return ''.join(password)

n = int(input("Enter the password length:  "))
use_digits = input("Include digits? (y/n): ").lower()=='y';
use_symbols = input("Include symbols? (y/n): ").lower()=='y';

password = gen_password(n,use_digits,use_symbols)

save = input("Do you want to this password? (y/n): ").lower()
 
if save == 'y':
    with open("passwords.txt", "a") as f:
        f.write(password + "\n")
    print("Password saved to the passwords.txt")