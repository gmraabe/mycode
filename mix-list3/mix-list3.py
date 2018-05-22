#!/usr/bin/env python3
# mix-list3.py
# Micah Raabe

# Lab 10 - Lists of Lists
list1 = ['cisco_nxos', 'arista_eos', 'cisco_ios']
print(list1)
list1.extend(['juniper'])
print(list1)
list1.append(['10.1.0.1', '10.2.0.1', '10.3.0.1'])
print(list1)
print(list1[4])
print(list1[4][0])
