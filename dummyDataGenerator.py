#!/usr/bin/python
# -*- coding: iso-8859-10 -*-

import random
import linecache
from geopy.geocoders import Nominatim


def generatePrice():
    return random.randint(5, 40)
    
def getExtra():
    return linecache.getline("extra.txt", random.randint(1, 8))
        
def getCoordinates(l):
    geolocator = Nominatim()
    location = geolocator.geocode(l, timeout=20)
    
    coord = "{latitude: %s , longitude: %s }" %(location.latitude,location.longitude)
    print coord
    return coord
    
    
def getImage():
    return  linecache.getline("images.txt", random.randint(1, 13))

def getLocation(): #city is more likely to be Helsinki or Malmö
    r = random.randint(1,8)
    if r<7:    
        l = linecache.getline("cities.txt", random.randint(1,156))#getting random location from the list
    elif r==7:
        l = ("Helsinki, Finland")
    else:
        l = ("Malmö, Sweden")
        
        
    print (l)
    return l
    
def getLanguagePair(): # first language of a pair is more likely to be Swedish, English or Finnish
    r = random.randint(1,8)
    if r<3:
        a = linecache.getline("languages.txt", random.randint(1, 185))
    elif r<5:
        a = ("Finnish")
    elif r<7:
        a = ("Swedish")
    else:
        a = ("English")                   
    b = linecache.getline("languages.txt", random.randint(1, 185))
    languagePair = '"%s , %s"' %(a.rstrip('\n'),b.rstrip('\n'))
    return languagePair                 

file=open("output.txt","w") 


for i in range(9,150): # it starts from 9 because ids 1-8 already exist in the code...
    
    n = linecache.getline("names.txt", random.randint(1, 5042)) #getting random name from the list
    sn = linecache.getline("names.txt", random.randint(1, 5042))#getting random surname from the list
    l = getLocation()
    s = linecache.getline("skills.txt", random.randint(1, 339))#getting random skill from the list
    c = getCoordinates(l) #get coordinated based on location
    lang= getLanguagePair() 
    p = generatePrice()
    e = getExtra()
    im = getImage()
    
    file.write("{\n")
    file.write("id: %d, \n" %(i))
    file.write('name: "%s %s",\n' %(n.rstrip('\n'), sn.rstrip('\n')))
    file.write("language: %s, \n" %(lang))
    file.write('location: "%s",\n' %(l.rstrip('\n')))
    file.write("coordinates: %s, \n" %(c))
    file.write("price: %d, \n" %(p))
    file.write('occupation: "%s",\n' %(s.rstrip('\n')))
    file.write('image: "%s",\n' %(im.rstrip('\n')))
    file.write('extra: %s, \n' %(e.rstrip('\n')))
    file.write("swiped:false,\n")
    file.write("},\n")
    
file.close()
print ("Success")
