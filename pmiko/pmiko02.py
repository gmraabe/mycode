#!/usr/bin/env python3
# pmiko02.py
# Micah Raabe

# Lab 65 - Paramiko SSH to Remote Host

import paramiko
cmd = input('Enter a command: ')
client = paramiko.SSHClient()
#client.set_missing_host_key_policy(paramiko.WarningPolicy())
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('10.10.1.2', username="john", password="alta3")
stdin, stdout, stderr = client.exec_command(cmd)
print('john@10.10.1.2: ' + cmd)
for line in stdout:
    print(' ' + line.strip('\n'))
client.close()

client.connect('10.10.1.3', username="paul", password="alta3")
stdin, stdout, stderr = client.exec_command(cmd)
print('paul@10.10.1.3: ' + cmd)
for line in stdout:
    print(' ' + line.strip('\n'))
client.close()

client.connect('10.10.1.4', username="george", password="alta3")
stdin, stdout, stderr = client.exec_command(cmd)
print('george@10.10.1.4 ' + cmd)
for line in stdout:
    print(' ' + line.strip('\n'))
client.close()

