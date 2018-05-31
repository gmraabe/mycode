#!/usr/bin/env python3
# eim.py
# Micah Raabe

# Lab 52 - Construct a SimpleHTTPServer ande HTTP Client

import http.client

conn = http.client.HTTPConnection("localhost", 9021)

print('\nMake a selection to test')
print('    1 - Send HTTP HEAD')
print('    2 - Perform a GET and dump to file')

usr_input = int(input(': '))

if usr_input == 1:
    conn.request('HEAD', '/')
    res = conn.getresponse()
    print(res.status, res.reason)

elif usr_input == 2:
    conn.request('GET', '/')
    res = conn.getresponse()
    print(res.status, res.reason)
    page_data = res.read()
    print(page_data)
    ## dump the data to a file named 'http_readin.txt'
    with open('http_readin.txt', 'w') as dumpfile:
        dumpfile.write(str(page_data))
else:
    print('Invalid input')

print('Thanks for playing')
