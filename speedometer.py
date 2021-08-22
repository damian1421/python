#!/data/data/com.termux/files/usr/bin/python
import subprocess
import ast
import time
from os import system
from math import asin, cos, pi, sqrt
r = 6371 #earth radius in Kilometers
locationList = [] #store all the location data
def getLocation():
    location=subprocess.run("termux-location", stdout=subprocess.PIPE)
    current_time = time.time() #get the current time
    location=location.stdout.decode("utf-8")
    location=ast.literal_eval(location)
    locationList.insert(0, { "latitude": location["latitude"], "longitude": location["longitude"], "time" : current_time})
def calDistance(a, b): #takes two index values for List
    p = pi/180 #multiply this to convert Degrees to Radians
    lat1 = locationList[b]["latitude"]
    lon1 = locationList[b]["longitude"]
    lat2 = locationList[a]["latitude"]
    lon2 = locationList[a]["longitude"]
    
    return 2 * r * asin(sqrt(0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2))
def calSpeed(a, b):
    #For current speed a & b will be first & second values on list
    #For average speed it will be first & last values
    time = locationList[a]["time"] - locationList[b]["time"]
    distance = calDistance(a, b)
    return (distance*3600//time) #Multiplying by 3600 for Km/Hrs

print("Calculating Your Current Speed .. !")
try:
    while True:
        if len(locationList) < 1: #need at least 1 prev. location
            getLocation()
        else:
            getLocation()
            current_speed = calSpeed(0, 1) #first & second values
            system('clear')
            print("Your Current Speed Is : " + str(current_speed) + " Km/H")
except KeyboardInterrupt:
    print("\nGood Bye..!")
