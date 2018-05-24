#!/usr/bin/env python3
# openstack.py
# Micah Raabe

outfile = open('admin.rc', 'a')

print('What is the OS_AUTH_URL?')
osAUTH = input()
print('export OS_AUTH_URL=' + osAUTH, file=outfile)
print('export OS_IDENTITY_API_VERSION=3', file=outfile)

print('What is the OS_PROJECT_NAME?')
osPROJ = input()
print('export OS_PROJECT_NAME=' + osPROJ, file=outfile)

print('What is the OS_PROJECT_DOMAIN_NAME?')
osPROJDOM = input()
print('export OS_PROJECT_DOMAIN_NAME=' + osPROJDOM, file=outfile)

print('What is the OS_USERNAME?')
osUSER = input()
print('export OS_USERNAME=' + osUSER, file=outfile)

print('What is the OS_USER_DOMAIN_NAME?')
osUSERDOM = input()
print('export OS_USER_DOMAIN_NAME=' + osUSERDOM, file=outfile)

print('What is the OS_PASSWORD?')
osPASS = input()
print('export OS_PASSWORD=' + osPASS, file=outfile)

outfile.close()
