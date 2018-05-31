#!/usr/bin/env python3
# nasapictofday.py
# Micah Raabe

# Lab 53 - Interaction with APIs - NASA 01

import urllib.request
import json
import webbrowser
from blessings import Terminal
t = Terminal()

## Define APOD
apodurl = 'https://api.nasa.gov/planetary/apod?'
mykey = 'api_key=oitOi7PWVAC5KvsR6mVbxTtQkgbTQx2tbDlkARYH'    ## your key goes in place of DEMO_KEY

while True:
    print(t.clear())
    print('\nNASA Picture of the Day 1.0\n')

    print('Instructions:  Enter the date of the picture you wish to view.')
    print('               Just press enter for today\'s picture.')

    print('Enter quit to exit')

    usr_date = str(input('\nEnter the date: (YYYY-MM-DD) : '))

    if usr_date.lower() == 'quit':  # exit program if user enters quit
        print('Thanks for playing')
        break

    ## Future code to error check input of usr_date

    usr_hd = input('Do you wish to view high resolution (HD)? yes/no : ')

    ## Determine user inputs and build the url to get the desired data
    if usr_date == '' and usr_hd.lower() == 'no':
        apodfullurl = apodurl + mykey
    elif usr_date == '' and usr_hd.lower() == 'yes':
        apodfullurl = apodurl + 'hd=True&' + mykey
    elif usr_hd.lower() == 'no' or usr_hd == '':
        apodfullurl = apodurl + 'date=' + usr_date + '&' + mykey
    elif usr_hd.lower() == 'yes':
        apodfullurl = apodurl + 'date=' + usr_date + '&hd=True&' + mykey
    else:
        print('Invalid input.  Defaulting to today\'s date and standard resolution.')
        apodfullurl = apodurl + mykey

    ## Call the webservice
    apodurlobj = urllib.request.urlopen(apodfullurl)

    ## read the file-like object
    apodread = apodurlobj.read()

    ## decode json to python data structure
    decodeapod = json.loads(apodread.decode('utf-8'))

    ## display our pythonic data
    #print("\n\nConverted python data")
    #print(decodeapod)

    print('\nTitle = ' + decodeapod['title'])
    print('Date = ' + decodeapod['date'])
    print('\nDescription = ' + decodeapod['explanation'])

    usr_open = str(input('\nDo you wish to open the NASA Picture of the Day in Firefox? : '))
    if usr_open.lower() == 'yes' or usr_open.lower() == 'y':
        ## use firefox to open the HTTPS URL
        #input('\nPress Enter to open NASA Picture of the Day in Firefox')
        webbrowser.open(decodeapod['url'])
