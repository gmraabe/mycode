#!/usr/bin/env python3
# pmiko02.py
# Micah Raabe

# Lab 65 - Paramiko SSH to Remote Host

import paramiko
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.WarningPolicy())
client.connect('10.10.1.2', username="john", password="alta3")
cmd = 'ls'
stdin, stdout, stderr = client.exec_command(cmd)
print('result ' + cmd)
for line in stdout:
    print(' ' + line.strip('\n'))

