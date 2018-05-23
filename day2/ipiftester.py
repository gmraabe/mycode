#!/usr/bin/env python3
# ipiftester.py
# Micah Raabe

# Tuesday afternoon exercise
# Write a python3 script with the following attributes:
#    - Takes an IP address
#    - Determines IF it matches the gateway's IP address 10.10.3.1
#        - if true, tells user not to use this IP address
#    - else, if IP matches DNS server IP 10.20.5.2
#        - if true, tells user not to use this IP address
#    - Otherwise (else), place the IP address in a list

# Part 2
#    - Make the above question loop-- and keep adding IP addresses to the list.
#    - Program ends when IP address "Q" or 'q' is entered.

# Define variables
ip_addr = ''
ip_addr_list = []

while 'true':     # Start a while loop
    ip_addr = input("Please enter an IP address: ")    # Get user input

    if ip_addr == '10.10.3.1':   # Check to see if input equals gateway address
        print('This is the IP address for the gateway: Please do not use this IP address')
    elif ip_addr == '10.20.5.2':   # Check to see if input equals DNS address
        print('This is the IP address for the DNS server: Please do not use this IP address')
    elif ip_addr == 'q' or ip_addr == 'Q':   # Check to see if input equals 'q' or 'Q' 
        print(ip_addr_list)    # Print out the list of IP addresses
        exit()      # exit the script
    else:
        ip_addr_list.append(ip_addr)   # Add the IP address to the List
