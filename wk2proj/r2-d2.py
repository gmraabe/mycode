#!/usr/bin/env python3
# r2-d2.py
# Micah Raabe

# Week 2 Project

'''
This is a multifunction python 3 script.
It uses netmiko and has the ability to:
     - Create an xls document containing router info
     - Use an xls document to bootstrap devices
     - Restore a switch with a backup config file
     - Create a backup config file
     - Encrypt a file
     - Decrypt a file
'''

## Import Statements
## required modules for this program to execute:
  # python3 -m pip install pyexcel
  # python3 -m pip install pyexcel-xls
  # python3 -m pip install netmiko
  # python3 -m pip install napalm
  # python3 -m pip install pprint
  # python3 -m pip install pycrypto
  # python3 -m pip install simple-crypt
import os
import sys
import pprint as pp
import pyexcel # import code for working with xls files
from napalm import get_network_driver # import code from NAPALM
from netmiko import ConnectHandler # import code from Netmiko
from simplecrypt import encrypt, decrypt # import cryptography functions
import getpass # import code for password input
from blessings import Terminal
t = Terminal()

## Create excel file
def get_ip_data():   # Request data from user
    input_ip = input("\nWhat is the IP address? ")
    input_driver = input("What is the driver associated with this device? ")
    input_user = input("What is the user name? ")
    input_pw = getpass.getpass("What is the password? ")
    d = {"IP": input_ip, "driver": input_driver, "username": input_user, "password": input_pw}
    return d

def create_excel_file():
    mylistdict = []  # this will be our list we turn into a *.xls file
    print("\nHello! We are going to make you a *.xls file")
    while(True):
        mylistdict.append(get_ip_data()) # add an item to the list returned by get_ip_data() {"IP": value, "driver": value}
        keep_going = input("\nWould you like to add another value? Enter to continue, or enter 'q' to quit: ")
        if (keep_going.lower() == 'q'):
            break
    filename = input("\nWhat would you like to name the file? ")  # get filename from user
    pyexcel.save_as(records=mylistdict, dest_file_name=filename)  # create the xls file
    print("The file " + filename + ".xls should be in your local directory")

## Bootstrapper Function
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

## Create a backup of a running config with date in filename, and log backup in excel file
def create_backup_config():
    input_ip = input("\nWhat is the IP address? ")
    input_driver = input("What is the driver associated with this device? ")
    input_user = input("What is the user name? ")
    input_pw = getpass.getpass("What is the password? ")
    input_config = input("New Config File Name: ")

    driver = get_network_driver(input_driver)
    device = driver(hostname=input_ip, username=input_user, password=input_pw)

    device.open()
    device.get_facts()
    pp.pprint(device.get_interfaces())
    config = device.get_config()
    running_config = config['running']
    config_file = open(input_config, 'w')
    config_file.write(running_config)
    config_file.close()
    print('\nConfig File ' + input_config + ' successfully saved.')
    input('\n  Press enter to continue: ')

## Restore a switch with a backup config file
def restore_config():
    input_ip = input("\nWhat is the IP address? ")
    input_driver = input("What is the driver associated with this device? ")
    input_user = input("What is the user name? ")
    input_pw = getpass.getpass("What is the password? ")
    input_config = input("Config File: ")

    while not os.path.isfile(input_config):
        print("SORRY ", input_config, " is not a file ")
        input_config = input("What is the full path to the config file you want to use? ")

    driver = get_network_driver(input_driver)
    device = driver(hostname=input_ip, username=input_user, password=input_pw)
    print('Opening to ', input_ip)
    device.open()
    print('Loading replacement candidate ', input_config)
    # Prepare to diff by loading candidate
    device.load_replace_candidate(filename=input_config)
    # the configuration you can check the changes:
    print('\nDiff: ')
    print(device.compare_config())
    # You can commit or discard the candidate changes.
    choice = input("\nWould you like to commit these changes? [yN]: ")
    if choice == 'y':
        print('Committing ...')
        device.commit_config()
    else:
        print('Discarding ...')
        device.discard_config()
    # close the session with the device.
    device.close()
    print('\nDone.')
    input('  Press enter to continue: ')

## Encrypt config file
def encrypt_file(filename, password):
    with open(filename, 'rb') as input:
        plaintext = input.read()
    with open(filename, 'wb') as output:
        ciphertext = encrypt(password, plaintext)
        output.write(ciphertext)

## Decrypt config file
def decrypt_file(filename, password):
    with open(filename, 'rb') as input:
        ciphertext = input.read()
        plaintext = decrypt(password, ciphertext)
    with open(filename, 'wb') as output:
        output.write(plaintext)

## retrieve data set from excel
def retv_excel(par):
    d = {}
    records = pyexcel.iget_records(file_name=par) # create a record object that is an open excel sheet
    for record in records:
        d.update( { record['IP'] : [ record['driver'], record['username'], record['password'] ] } ) # adds a new IP and driver key:value pair to our dictionary
    return d # return the completed dictionary

## Ping router - returns True or False
def ping_router(hostname):
    response = os.system("ping -c 1 " + hostname)
    #and then check the response...
    if response == 0:
        return True
    else:
        return False

## Check interfaces - Issue "show ip init brief"
def interface_check(dev_type, dev_ip, dev_un, dev_pw):
    try:
        open_connection = ConnectHandler(device_type=dev_type, ip=dev_ip, username=dev_un, password=dev_pw)
        my_command = open_connection.send_command("show ip int brief")
    except:
        my_command = "** ISSUING COMMAND FAILED **"
    finally:
        return my_command

## Login to router - SSH Check with Netmiko class ConnectHandler
def login_router(dev_type, dev_ip, dev_un, dev_pw):
    try:
        open_connection = ConnectHandler(device_type=dev_type, ip=dev_ip, username=dev_un, password=dev_pw)
        return True
    except:
        return False

## Read hostname, IP address, username, and password from excel file and run initial config/bootstrap
def bootstrap_start():
    ## Determine where *.xls input is
    file_location = str(input("\nWhere is the file location? "))

    while not os.path.isfile(file_location): # check for valid file
        print("SORRY ", file_location, " is not a file ")
        file_location = input("What is the full path to the config file you want to use? ")
    
    ## Entry is now a local dictionary containing IP(key):driver(value)
    entry = retv_excel(file_location)

    ## Use a loop to check each device for SSH accessability
    print("\n***** BEGIN SSH CHECKING *****")
    for x in entry.keys():
        if login_router(str(entry[x][0]), x, str(entry[x][1]), str(entry[x][2])):
            print("\n\t**IP: - " + x + " - SSH connectivty UP\n")
        else:
            print("\n\t**IP: - " + x + " - SSH connectivty DOWN\n")

    ## Use a loop to check each device for ICMP responses
    print("\n***** BEGIN ICMP CHECKING *****")
    for x in entry.keys():
        if ping_router(x):
            print("\n\t**IP: - " + x + " - responding to ICMP\n")
        else:
            print("\n\t**IP: - " + x + " - NOT responding to ICMP\n")

    ## Use a loop to check each device for ICMP responses
    print("\n***** BEGIN SHOW IP INT BRIEF *****")
    for x in entry.keys():
        print("\n" + interface_check(str(entry[x][0]), x, str(entry[x][1]), str(entry[x][2])))

    ## Determine if new config should be applied && if so apply new config
    print("\n***** NEW BOOTSTRAPPING CHECK *****")
    ynchk = input("\nWould you like to apply a new configuration? y/N ")
    if (ynchk.lower() == "y") or (ynchk.lower() == "yes"):  # if user input yes or y
        conf_loc = str(input("\nWhere is the location of the new config file? "))
        conf_ip = str(input("\nWhat is the IP address of the device to be configured? "))

        if bootstrapper.bootstrapper(entry[conf_ip][0], conf_ip, entry[conf_ip][1], entry[conf_ip][2], conf_loc):
            print("\nNew configuration applied!")
        else:
            print("\nProblem in applying new configuration!")

##### Main Menu #####
while True:
    print(t.clear())
    print('\n     R2-D2 ver 1.0\n')
    print('Main Menu:\n')
    print(' 1 - Create an xls document for router config')
    print(' 2 - Use an xls document to bootstrap devices')
    print(' 3 - Restore a switch with a backup config file')
    print(' 4 - Create a backup config file')
    print(' 5 - Encrypt a file')
    print(' 6 - Decrypt a file')
    print(' q - Quit / Exit')

    usr_input = str(input('\nPick an option: '))

    if usr_input == '1': ## Option # 1
        create_excel_file()
    elif usr_input == '2': ## Option # 2
        bootstrap_start()
    elif usr_input == '3': ## Option # 3
        restore_config()
    elif usr_input == '4': ## Option # 4
        create_backup_config()
    elif usr_input == '5': ## Option # 5
        ## Encrypt
        filename = input('Filename: ')
        if os.path.isfile(filename) == True: # check for valid file
            password = getpass.getpass(' password: ')
            encrypt_file(filename, password)
            print('Done')
        else:
            print("SORRY ", filename, " is not a file ")
            input('  Press enter to continue: ')

    elif usr_input == '6': ## Option # 6
        ## Decrypt
        filename = input('Filename: ')
        if os.path.isfile(filename) == True: # check for valid file
            password = getpass.getpass(' Password: ')
            decrypt_file(filename, password)
            print('Done')
        else:
            print("SORRY ", filename, " is not a file ")
            input('  Press enter to continue: ')
    elif usr_input.lower() == 'q': ## Option # 6
        break
    else:
        input('Invalid section! Press Enter to continue...')
