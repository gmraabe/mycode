#!/usr/bin/env python3
# mix-list2.py
# Micah Raabe

# Lab 09 - Mix List 2
proto = ['ssh', 'http', 'https']
protoa = ['ssh', 'http', 'https']
print(proto)   # Print entire list
proto.append('dns')  # This line will add 'dns' to the end of our list
protoa.append('dns')  # This line will add 'dns' to the end of our list
print(proto)   # Print entire list again
proto2 = [ 22, 80, 443, 53 ] # list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)
proto.insert(1, 'ftp')
print(proto)
