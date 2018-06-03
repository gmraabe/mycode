#!/usr/bin/env python3

from simplecrypt import encrypt, decrypt
from os.path import exists
from os import unlink
import getpass

## Encrypt config file
def encrypt_file(filename, password):
    with open(filename, 'rb') as input:
        plaintext = input.read()
    with open(filename, 'wb') as output:
        ciphertext = encrypt(password, plaintext)
        output.write(ciphertext)

filename = input('Filename: ')
password = getpass.getpass(' password: ')
encrypt_file(filename, password)
print('Done')
