#!/usr/bin/env python3
# loopsnloops.py
# Micah Raabe

cisco_ios = {'device_type': 'cisco_ios_ssh', 'ip': '10.10.10.27', 'username': 'admin',
             'password': 'passwd', 'port': 22}

# Write a Python3 script with the following attributes:
#  - Iterate through the dictionary
#  - Dispay the PHRASE "CISCO LOGIN INFO - " beside each value. Example:
#     CISCO LOGIN INFO - cisco_ios_ssh
#	 CISCO LOGIN INFO - 10.10.10.27
#	 CISCO LOGIN INFO - admin
#	 CISCO LOGIN INFO - passwd
#	 CISCO LOGIN INFO - 22
#  - ** You may only write the phrase "CISCO LOGIN INFO" ONCE into your script

for x in cisco_ios.values():
    print("    CISCO LOGIN INFO - " + str(x))
