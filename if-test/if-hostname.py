#!/usr/bin/env python3
# if-hostname.py
# Micah Raabe

# Lab 11 - Testing with if
hostname = input("Please enter a hostname: ")     # Get hostname from user
if hostname.lower() == 'mtg':                     # if hostname equals mtg
    print('The hostname was found to be mtg')        # print a confirmation
    print('hostname matches expected config')        # that it matches config
print('Exiting the script')
