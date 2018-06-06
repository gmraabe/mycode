#!/usr/bin/env python3
# sorted06.py
# Micah Raabe

# Lab 74 - list.sort() vs sorted()

vendors = ['cisco', 'juniper', 'big_ip', 'f5', 'arista', 'hp', 'dell']
print("Currently the value of the list vendors:", vendors)
print("\nThe results of sorted(vendors) are not permanent:", sorted(vendors))
print("\nThe sorted() function does not permantly alter the list: " + str(vendors))
print("\nThe results of vendors.sort() method are permanent. It is a method that alters the list. It returns None... see?", vendors.sort())
print("\nThe old list vendors has been reordered:", vendors)
