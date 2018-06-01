#!/usr/bin/env python3
# nasa02.py
# Micah Raabe

# Lab 54 - Interaction with API's - NASA 02

import urllib.request
import json
import webbrowser

def moon_len(missdistance):
    return float(missdistance) / 238900

def tracked_neo(decoded_neo):
    return decoded_neo['element_count']

start = str(input('Enter the start date (YYYY-MM-DD) : '))

## Define APOD
neourl = 'https://api.nasa.gov/neo/rest/v1/feed?'
startdate = 'start_date=' + start
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
#print("\n\nConverted python data")
#print(decodeneo)

print('\nTotal number of tracked NEO\'s = ' + str(tracked_neo(decodeneo)))
closest_neo = 93000000  # initialize variable for the closest distance of a neo (initial value set at 1 AU, or the distance from the earth to the sun)
closest_neoname = ''  # initialize variable for the name of the closest neo

for neodate in decodeneo['near_earth_objects']:   # loop through the dates
    x = 0  # initialize/set variable for the while loop to iteriate through the list
    while x < decodeneo['near_earth_objects'][neodate].__len__():   # loop through range of list
        print('Name = ' + decodeneo['near_earth_objects'][neodate][x]['name'], end='')
        print('  Miles = ' + decodeneo['near_earth_objects'][neodate][x]['close_approach_data'][0]['miss_distance']['miles'], end='')
        print('  Moon Lengths = ' + str(round(moon_len(decodeneo['near_earth_objects'][neodate][x]['close_approach_data'][0]['miss_distance']['miles']), 2)))

        ## check for and determine the closest neo
        if float(decodeneo['near_earth_objects'][neodate][x]['close_approach_data'][0]['miss_distance']['miles']) < float(closest_neo):
            closest_neo = decodeneo['near_earth_objects'][neodate][x]['close_approach_data'][0]['miss_distance']['miles']
            closest_neoname = decodeneo['near_earth_objects'][neodate][x]['name']
            
        x = x + 1  # add 1 to the while loop variable to continue to iteriate through the list

print('\nClosest NEO to Earth = ' + closest_neoname)
print('  With a distance of ' + str(closest_neo) + ' miles and ' + str(round(moon_len(closest_neo), 2)) + ' moon lengths')
