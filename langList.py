#this script makes language.txt file out of CSV language-codes.csv file
import csv

languages = open("languages.txt","w")
with open('language-codes.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        languages.write("%s\n" %(row[1]))   
print('Ready')