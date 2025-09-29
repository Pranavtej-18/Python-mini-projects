import string
import random

def gen_password(length):

    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    all_chars = letters + digits + symbols

    password = ''.join(random.choice(all_chars) for _ in range(length))

    return password

print("Generated password:",gen_password(12))