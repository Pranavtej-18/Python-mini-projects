import random
import string

def gen_pass(length):

    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    all_chars = letters + digits + symbols

    password = ''.join(random.choice(all_chars) for _ in range(length))

    return password

n = int(input("Enter the length to be your password: ")) 
passw = gen_pass(n)
print(passw)