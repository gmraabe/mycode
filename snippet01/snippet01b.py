#!/usr/bin/env python3
# snippet01a.py
# Micah Raabe

# Lab 32 - Snippet.split.join

def rmvdot(ip):                              # function to remove the dot from an IPv4 IP address and reserves a block of 10 addresses
    ip_list = ip.split(".")                       # remove the '.'
    oct4 = int(ip_list[3]) + 10                   # add 10
    if oct4 > 255:                                # check to see if ending IP address is valid
        return False
    else:                                         # sucess
        return True

print('This program reserves a block of 10 IP addresses.')
start_ip_address = input('Please enter the starting IP address: ')
worked = rmvdot(start_ip_address)                 # call the remove dot function and reserve 10 IP addresses
if worked:
    print('Reservation sucessful')
else:
    print('Reservation failed')
 
