#!/usr/bin/env python3
# pmiko02.py
# Micah Raabe

# Lab 65 - Paramiko SSH to Remote Host

import paramiko
ustour = [ { 'ip' : '10.10.1.2', 'un' : 'john', 'pw' : 'alta3' }, 
           { 'ip' : '10.10.1.3', 'un' : 'paul', 'pw' : 'alta3' }, 
           { 'ip' : '10.10.1.4', 'un' : 'george', 'pw' : 'alta3' },
           { 'ip' : '10.10.1.5', 'un' : 'stuart', 'pw' : 'alta3' },
           { 'ip' : '10.10.1.6', 'un' : 'pete', 'pw' : 'alta3' },
           { 'ip' : '10.10.1.7', 'un' : 'ringo', 'pw' : 'alta3' } ]

cmd = input('Enter a command: ')
for x in ustour:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(x['ip'], username=x['un'], password=x['pw'])
    stdin, stdout, stderr = client.exec_command(cmd)
    print(x['un'] + '@' + x['ip'] + ': ' + cmd)
    for line in stdout:
        print(' ' + line.strip('\n'))
    client.close()


