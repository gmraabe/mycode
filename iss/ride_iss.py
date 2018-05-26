#!/usr/bin/env python3
# ride_iss.py
# Micah Raabe

# Lab 36 - Space API's the Final Frontier

import urllib.request
import json
## Trace the ISS
#majortom = 'http://api.open-notify.org/astros.json'

## Call the webservice
#groundctrl = urllib.request.urlopen(majortom)
groundctrl = urllib.request.urlopen('http://api.open-notify.org/astros.json')
helmet = groundctrl.read()

## json 2 python data structure
#helmetson = json.load(groundctrl.read())
helmetson = json.loads(helmet.decode('utf-8'))

## display our pythonic data
print("Converted python data")
print(helmetson)

print("\n\nPeople in Space: ", helmetson['number'])  # print the number of people in space
people = helmetson['people']
#print(people)

for num_of_people in range(len(people)):             # loop through the list and print the name and craft
    print(people[num_of_people]['name'] + ' on the ' + people[num_of_people]['craft'])
