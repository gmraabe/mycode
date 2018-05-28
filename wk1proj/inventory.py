#!/usr/bin/env python3
# inventory.py
# Micah Raabe

# Lab 38 - Capstone01 (Week 1 Project)

## Inventory Tracker
##   Create a program that assumes inventory.txt will be local to where it was launched
##   Each line in inventory.txt contains a real world thing and the location of that real world thing (think room, or short description, or gps coordinates)
##   Create two functions callable by the user from a repeating menu:
##     1) create an new entry in inventory.txt
##     2) search inventory.txt for an entry, and if an entry is found, the user should be given the option of removing that entry from inventory.txt
##   Feel free to make your own additional features!

import json
from blessings import Terminal
t = Terminal()
myDict = {}              # initialize dictionary
filename = 'inventory.txt'            # file name to use to store inventory

def new_entry(new_item, new_loc):                # function for creating a new entry
    with open(filename, 'r') as myfile:            # open file with implied close (with)
        myDict = json.loads(myfile.read())           # read file into a dictionary
    myDict[new_item] = new_loc                     # append new item and location to dictionary
    with open(filename, 'w') as myfile:            # open file with implied close (with)
        myfile.write(json.dumps(myDict))             # write dictionary to file
    print(new_item + ' added to inventory')
    input('Press enter to continue')

def search_entry(search_str):    # function for searching inventory
    with open(filename, 'r') as myfile:            # open file with implied close (with)
        myDict = json.loads(myfile.read())           # read file into a dictionary
    print('The Location for ' + search_str + ' is: ' + myDict.get(search_str, "not found"))
    if type(myDict.get(search_str))() is None:     # check to see if no entry is found
        input('Press enter to continue')             # if no entry then only option is to return to Main Menu
    else:                                          # if an entry is found
        while True:                                  # loop until a valid selection is made
            print('Enter 1 to delete ' + search_str + ' or 2 to return to Main Menu')
            selection = input()                        # get input from user
            if selection == '1':                         # check if user wishes to delete the found search item
                myDict.pop(search_str)                     # remove search string from dictionary
                with open(filename, 'w') as myfile:        # open file with implied close (with)
                    myfile.write(json.dumps(myDict))         # write dictionary to file
                print(search_str + ' is deleted')          # print confirmation message
                input('Press enter to continue')           # wait for user before continuing
                break
            elif selection == '2':                     # if user wishes to exit to main menu
                break
            else:                                      # if anything else then loop
                print('Invalid selection')

def print_entrys():               # function for printing the inventory
    print('\nItem\t\tLocation')
    print('----\t\t--------')
    with open(filename, 'r') as myfile:            # open file with implied close (with)
        myDict = json.loads(myfile.read())           # read file into a dictionary
    for itm, loc in myDict.items():                # loop through dictionary
        print(itm + '\t\t' + loc)                    # print dictionary item
    input('\nPress enter to continue')             # wait for user before continuing

while True:
    print(t.clear())                               # clear screen
    print('\nInventory Tracker 1.0\n')

    print('Main Menu:\n')                          # print main menu
    print('  1 - Create or modify an entry')
    print('  2 - Search for an entry')
    print('  3 - Print inventory')
    print('  q - Quit')

    menu_selection = input('\nPlease enter a selection: ')  # get user input

    if menu_selection.lower() == 'q':              # if user enters 'q' then quit
        break
    elif menu_selection == '1':                    # if user wishes to add/modify an entry
        new_item = input('Please enter an item: ')
        new_location = input('Please enter the location: ')
        new_entry(new_item, new_location)            # call the new_entry function
    elif menu_selection == '2':                    # if user wishes to search for an entry
        search_input = input('Search for: ')         # get search input from user
        search_entry(search_input)                   # call the search_entry function
    elif menu_selection == '3':                    # if user wishes to print inventory
        print_entrys()                               # call the print_entrys function
    else:                                          # if anything else then loop
        print('Invalid selection - Press enter to continue')
        input()
