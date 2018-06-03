#!/usr/bin/env python3

from simplecrypt import encrypt, decrypt
from os.path import exists
from os import unlink
import getpass

## Decrypt config file
def decrypt_file(filename, password):
    with open(filename, 'rb') as input:
        ciphertext = input.read()
        plaintext = decrypt(password, ciphertext)
    with open(filename, 'wb') as output:
        output.write(plaintext)

filename = input('Filename: ')
password = getpass.getpass(' Password: ')
decrypt_file(filename, password)
print('Done')
