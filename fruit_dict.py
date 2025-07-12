#!/usr/bin/env python3

#Import the CSV Module
import csv

#Create a dictionary with random items
dict = {'Banana':1, 'Mango': 2, 'Apples': 3}

#opens a csv file with data in it
with open('fruits.csv', mode='r') as file:
    #put csv data into a dictionary reader
    csv_writer = csv.DictReader(file, delimiter=",")

    #Iterate through each lines
    for line in csv_writer:
        #If the csv reader line doesn't exist in the dictionary, add it with the given amount
        if line['Name'] not in dict.keys():
            dict[line['Name']] = int(line['Amount'])
        else:
            #if it does exist then add the amount from the line to the amount in the dictionary
            dict[line['Name']] += int(line['Amount'])

#Print the dictionary
print(dict)
    