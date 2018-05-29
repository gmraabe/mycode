#!/usr/bin/env python3
# iss_tracking.py
# Micah Raabe

# Lab 41 - More APIs ... Vast

import urllib.request
import json
import turtle
import time

def issloc():
    ## Trace the ISS - earth-orbital space station
    eoss = 'http://api.open-notify.org/iss-now.json'
    ## Call the webserv
    trackiss = urllib.request.urlopen(eoss)
    ## put into file object
    ztrack = trackiss.read()
    ## json 2 python data structure
    result = json.loads(ztrack.decode('utf-8'))
    ## display our pythonic data
    #print("\n\nConverted python data")
    #print(result)
    #input('\nISS data retrieved & converted. Press enter to continue')
    return result

def isslon(result_lon):
    location = result_lon['iss_position']
    return location['longitude']

def isslat(result_lat):
    location = result_lat['iss_position']
    return location['latitude']

def isspass(userlat, userlon):
    passiss = 'http://api.open-notify.org/iss-pass.json'
    passiss = passiss + '?lat=' + str(userlat) + '&lon=' + str(userlon)
    response = urllib.request.urlopen(passiss)
    result = json.loads(response.read())
    # print(result) ## uncomment to see the downloaded result

    over = result['response'][0]['risetime']

    style = ('Arial', 6, 'bold')
    mylocation.write(time.ctime(over), font=style)

    print('The next five passes over ' + str(yellowlat) + ' ' + str(yellowlon))
    print('Pass 1 = ' + time.ctime(result['response'][0]['risetime']))
    print('Pass 2 = ' + time.ctime(result['response'][1]['risetime']))
    print('Pass 3 = ' + time.ctime(result['response'][2]['risetime']))
    print('Pass 4 = ' + time.ctime(result['response'][3]['risetime']))
    print('Pass 5 = ' + time.ctime(result['response'][4]['risetime']))



## Get user location
yellowlat = float(input('Enter your latitude location in decimal degrees (ex 47.6): '))
yellowlon = float(input('Enter your longitude location in decimal degrees (ex -122.3): '))

## Initialize the map window
screen = turtle.Screen() # Create a screen object
screen.setup(720, 360) # set the resolution
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic('iss_map.gif')
screen.register_shape('spriteiss.gif')

## Initialize the ISS sprite
iss = turtle.Turtle()
iss.shape('spriteiss.gif')
iss.setheading(90)

## Initialize the user location and place on map
mylocation = turtle.Turtle()
mylocation.penup()
mylocation.color('yellow')
mylocation.goto(yellowlon, yellowlat)
mylocation.dot(5)
mylocation.hideturtle()

while True:
    iss_location = issloc()  # Get the current location of the ISS

    ## Print the location of the ISS
    print('\nLatitude: ', isslat(iss_location))
    print('Longitude: ', isslon(iss_location))

    ## Convert ISS location to a float and round the number
    roundedlon = round(float(isslon(iss_location)))
    roundedlat = round(float(isslat(iss_location)))

    ## Place the ISS sprite on the map
    iss.penup()
    iss.goto(roundedlon, roundedlat)

    ## Get the next five passes and place the next one on the map
    isspass(yellowlat, yellowlon)
    test = input('Press enter to refresh / q to quit (Do not close the map window)')
    if test == 'q':
        break

print('Thanks for playing!')
#turtle.mainloop()
