import string
import random

def gen_password(length,use_digits=True,use_symbols=True):

    letters = string.ascii_letters
    digits = string.digits if use_digits else ""
    symbols = string.punctuation if use_symbols else ""

    all_chars = letters + digits + symbols

    if not all_chars:
        raise ValueError("No characters available for password generation!!!")

    password = ''.join(random.choice(all_chars) for _ in range(length))

    return password

print("Generated password:",gen_password(16,use_digits=True,use_symbols=False))