#!/usr/bin/env python3
# pmiko03.py
# Micah Raabe

# Lab 66 - Paramiko and SFTP

import paramiko
t = paramiko.Transport(('10.10.1.2', 22))
t.connect(username='john', password='alta3')
sftp = paramiko.SFTPClient.from_transport(t)
sftp.listdir()
sftp.put("test.txt", "new_test.txt")
sftp.close()
t.close()

