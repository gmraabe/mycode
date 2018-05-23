#!/usr/bin/env python3
# forloop2.py
# Micah Raabe

vendors = ['cisco', 'juniper', 'big_ip', 'f5', 'arista', 'alta3', 'zach', 'stuart']
approved_vendors = ['cisco', 'juniper', 'big_ip']
for x in vendors:
    print("\nThe vendors is " + x, end="")
    if x not in approved_vendors:
        print(" - NOT AN APPROVED VENDOR!", end="")
print("\nOur loop has ended.")
