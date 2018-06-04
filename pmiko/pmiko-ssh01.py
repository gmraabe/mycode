#!/usr/bin/env python3
# pmiko-ssh01.py
# Micah Raabe

# Lab 64 - Introducing Paramiko

import paramiko
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.WarningPolicy())
client.connect('localhost', username='student', password='alta3')
cmd = input('Enter a command: ')
stdin, stdout, stderr = client.exec_command(cmd)
print('result ' + cmd)
for line in stdout:
    print(' ' + line.strip('\n'))
client.close()

