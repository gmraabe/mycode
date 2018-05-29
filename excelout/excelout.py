#!/usr/bin/env python3
# excelout.py
# Micah Raabe

# Lab 42 - Making Excel Sheets

## sudo apt install python3-pip

## python3 -m pip install pyexcel
## python3 -m pip install pyexcel-xls

import pyexcel

# Request data from user
def get_ip_data():
    input_ip = input("\nWhat is the IP address? ")
    input_driver = input("What is the driver associated with this device? ")
    input_user = input("What is the user name? ")
    input_pw = input("What is the password? ")
    d = {"IP": input_ip, "driver": input_driver, "user": input_user, "password": input_pw}
    return d

## This code is left turned off, but might help visualize how pyexcel works with data sets.
## IP is the first column, whereas driver is the second column.
## mylistdict = [ {"IP": "172.16.2.10", "driver": "arista_eos"}, {"IP": "172.16.2.20", "driver": "arista_eos"} ]
## pyexcel.save_as(records=mylistdict, dest_file_name="ip_list.xls")


# Runtime
mylistdict = []  # this will be our list we turn into a *.xls file

print("Hello! This program will make you a *.xls file")

while(True):
    mylistdict.append(get_ip_data()) # add an item to the list returned by get_ip_data() {"IP": value, "driver": value}
    keep_going = input("\nWould you like to add another value? Enter to continue, or enter 'q' to quit: ")
    if (keep_going.lower() == 'q'):
        break

filename = input("\nWhat is the name of the *.xls file? ")

pyexcel.save_as(records=mylistdict, dest_file_name="ip_list.xls")

print("The file " + filename + ".xls should be in your local directory")
