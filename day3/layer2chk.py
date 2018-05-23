#!/usr/bin/env python3
# layer2chk.py
# Micah Raabe

# Start the program with while(True)
# the program ends whtn they enter eth, fc, ifb, or otn
# if a L2 network protocol isn't recognized, the program loops

while('true'):
    netprot = input("Please enter a L2 network protocol: ")  # prompt the user for a L2 network protocol
    if netprot == 'eth':                    # Check for eth
        print("ethernet protocol allowed")
        break
    elif netprot == 'fc':                   # Check for fc
        print("fiber channel NOT allowed")
        break
    elif netprot == 'ifb':                  # Check for ifb 
        print("infiniband NOT allowed")
        break
    elif netprot == 'otn':                  # Check for otn
        print("optical network allowed")
        break
    else:                                   # Print error msg and loop
        print("No idea what that technology is")
