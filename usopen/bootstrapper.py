#!/usr/bin/env python3
# bootstrapper.py
# Micah Raabe

from netmiko import ConnectHandler
## Define our new function called bootstrapper and the expected arugments (all five)
def bootstrapper(dev_type, dev_ip, dev_un, dev_pw, config):
    try:
        config_file = open(config, 'r') # open the file object described by config argument
        config_lines = config_file.read().splitlines() # create a list of the file lines without \n
        config_file.close() # close the file object

        open_connection = ConnectHandler(device_type=dev_type, ip=dev_ip, username=dev_un, password=dev_pw)
        open_connection.enable() # this sets the connection in enable mode
        output = open_connection.send_config_set(config_lines) # pass the config to the send_config_set() method
        print(output) # print the config to the screen # output to the screen
        open_connection.send_command_expect('write memory') # write the memory (okay if this gets done twice)
        open_connection.disconnect() # close the open connection

        return True # Everything worked! - "Return TRUE when complete"
    except:
        return False # Something failed during the configuration process - "Return FALSE if fails"
