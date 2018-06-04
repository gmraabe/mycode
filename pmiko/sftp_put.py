#!/usr/bin/env python3
# sftp_put.py
# Micah Raabe

# Lab 66 - Paramiko and SFTP

import paramiko
source_filename = input('Enter the local source filename: ')
dest_filename = input('Enter the remote destination filename: ')
t = paramiko.Transport(('10.10.1.2', 22))
t.connect(username='john', password='alta3')
sftp = paramiko.SFTPClient.from_transport(t)
sftp.listdir()
sftp.put(source_filename, dest_filename)
sftp.close()
t.close()

