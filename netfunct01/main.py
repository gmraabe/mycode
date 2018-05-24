#!/usr/bin/env python3
# main.py
# Micah Raabe

# function to push commands
def commandpush(devicecmd): # devicecmd==list
    for coffeetime in devicecmd.keys():
        print('Handshaking. .. ... connecting with ' + coffeetime )
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[coffeetime]:
            print('Attempting to sending command --> ' + mycmds )
            # we'll learn to write code that sends cmds to device here
        print()  # print a newline to clean up the output (1st customization request)

# function to reboot a list of IP's
def devicereboot(ip_list):
    for rbtip in ip_list.keys():
        print('Connecting to...' + str(rbtip))
        # code that connects to ip here
        print('    REBOOTING NOW!')
        # code that sends the reboot command here
        print() # print newline

### Start our script
work2do = {"10.1.0.1":["interface eth1/2", "no shut"], "10.2.0.1":["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]} # data that replaces data stored in file

print("Welcome to the network device command pusher") # welcome message

## get data set
print("\nData set found\n") # replace with function call that reads in data from file

## run
commandpush(work2do) # call function to push commands to devices
devicereboot(work2do) # call function to reboot devices
