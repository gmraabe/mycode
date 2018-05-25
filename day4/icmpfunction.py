#!/usr/bin/env python3
# icmpfunction.py
# Micah Raabe

# Day 4 Afternoon Exercise  2018.05.24

import subprocess
# use subprocess.call("linux command here")

# user is askecd for a 'c' number and an ip address
# both values passed to function icmpsender(cnumber, ipaddress)
# function issues command ping -c cnumber ipaddress
#                     ex - ping -c 10 8.8.8.8

cnumber = input('How many icmp packets would you like to send? ')
ipaddress = input('What is the IP address? ')

subprocess.call(["ping", "-c", cnumber, ipaddress])
