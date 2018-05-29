#!/usr/bin/env python3
# myconfig.py
# Micah Raabe

# Lab - NAPALM Changes, Validation, and Rollback

# import code from NAPALM
from napalm import get_network_driver

# Tell NAPALM to speak "eos" commands to our switches (very cisco-like)
driver = get_network_driver('eos')

# Hard-code the switch credentials
device = driver('172.16.2.10', 'admin', 'alta3')

#Equates to: ssh into the switch, login, and enable
device.open()

# Print STARTUP, RUNNING, and CANDIDATE configs
print(device.get_config())
