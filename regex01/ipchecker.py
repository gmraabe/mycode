#!/usr/bin/env python3
# ipchecker.py
# Micah Raabe

# Lab 48 - Use RegEx ... IP Address

import urllib.request
import re
import netifaces as ni

## function to get public ip address
def get_external_ip():
    url = 'http://checkip.dyndns.org'
    requesty = urllib.request.urlopen(url).read().decode('utf-8')  # gets the public IP address
    externalIP = ''.join(re.findall('\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}', requesty))  # strips off the extra text and converts to a string
    return externalIP

print('Your public IP address is: ' + get_external_ip())
print('Your local IP address\' are: ')
## loop to get local ip address for every local interface
for local_interfaces in ni.interfaces():  # loops through local interfaces
    try:  # used to get and print the ip address for only interfaces that have an IPv4 address
        print('\t\t\t\t' + local_interfaces + ': ' + (ni.ifaddresses(local_interfaces)[ni.AF_INET][0]['addr']))
    except:  # skips interface if there is no IPv4 address
        pass
