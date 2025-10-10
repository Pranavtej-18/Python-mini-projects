import random
import string
import argparse

def gen_password(length,use_digits,use_symbols):

    letters = string.ascii_letters
    digits = string.digits if use_digits else ''
    symbols = string.punctuation if use_symbols else ''

    all_chars = letters + digits + symbols

    if not all_chars:
        raise ValueError("No characters available for password generation")

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

parser = argparse.ArgumentParser(description="Password Generator")
parser.add_argument("-l", "--length", type=int,default=12,help="passowrd length")
parser.add_argument("-d", "--digits",action = "store_true",help="include digits")
parser.add_argument("-r", "--symbols",action = "store_true", help="passowrd length")