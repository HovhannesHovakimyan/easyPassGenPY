#!/usr/local/bin/python3.6

# Importing a few standard Python 3 modules
# random string sequence
import random

# string library functionality
import string

def rand_pass(size):

    # Setting the necessary variables
    first_letter = ''
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numeric = string.digits
    symbolic = string.punctuation

    # Choosing uppercase or lowercase letter
    # randomly to be the first character
    # of the password
    first_letter = random.choice(lowercase + uppercase)

    # Concatinating everything in one string
    generate_pass = first_letter + ''.join([random.choice(
                        lowercase + uppercase + numeric + symbolic)
                        for n in range(size)])

    return generate_pass

# Generating 8-character password
password = rand_pass(7)

print(password)
