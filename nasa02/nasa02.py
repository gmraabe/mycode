#!/usr/bin/env python3
# nasa02.py
# Micah Raabe

# Lab 54 - Interaction with API's - NASA 02

import urllib.request
import json
import webbrowser

## Define APOD
neourl = 'https://api.nasa.gov/neo/rest/v1/feed?'
startdate = 'start_date=2018-06-01'
enddate = '&end_date=END_DATE'
mykey = '&api_key=oitOi7PWVAC5KvsR6mVbxTtQkgbTQx2tbDlkARYH'    ## your key goes in place of DEMO_KEY

neourl = neourl + startdate + mykey

## Call the webservice
neourlobj = urllib.request.urlopen(neourl)

## read the file-like object
neoread = neourlobj.read()

## decode json to python data structure
decodeneo = json.loads(neoread.decode('utf-8'))

## display our pythonic data
print("\n\nConverted python data")
print(decodeneo)
