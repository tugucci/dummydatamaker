import random
import linecache
from geopy.geocoders import Nominatim

file=open("output.txt","w") 

def generatePrice():
    return random.randint(5, 40)
    
def getExtra():
    return linecache.getline("extra.txt", random.randint(1, 8))
        
def getCoordinates(l):
    geolocator = Nominatim()
    location = geolocator.geocode(l)
    
    coord = "{latitude: %s , longitude: %s }" %(location.latitude,location.longitude)
    print coord
    return coord
    
    
def getImage():
    return  linecache.getline("images.txt", random.randint(1, 12))

    
def getLanguagePair():
    
    a = linecache.getline("languages.txt", random.randint(1, 185))
    b = linecache.getline("languages.txt", random.randint(1, 185))
    languagePair = '"%s , %s"' %(a.rstrip('\n'),b.rstrip('\n'))
    return languagePair                 


for i in range(9,150):
    
    n = linecache.getline("names.txt", random.randint(1, 5042)) #getting random name from the list
    sn = linecache.getline("names.txt", random.randint(1, 5042))#getting random surname from the list
    l = linecache.getline("cities.txt", random.randint(1,156))#getting random location from the list
    print (l)
    s = linecache.getline("skills.txt", random.randint(1, 339))#getting random skill from the list
    c = getCoordinates(l) #get coordinated based on location
    lang= getLanguagePair() 
    p = generatePrice()
    e = getExtra()
    im = getImage()
    
    file.write("{\n")
    file.write("id: %d, \n" %(i))
    file.write('name: "%s %s",\n' %(n.rstrip('\n'), sn.rstrip('\n')))
    file.write("languages: %s, \n" %(lang))
    file.write('location: "%s",\n' %(l.rstrip('\n')))
    file.write("coordinates: %s, \n" %(c))
    file.write("price: %d, \n" %(p))
    file.write('occupation: "%s",\n' %(s.rstrip('\n')))
    file.write('image: "%s",\n' %(im.rstrip('\n')))
    file.write('extra: %s, \n' %(e.rstrip('\n')))
    file.write("},\n")
    
file.close()

