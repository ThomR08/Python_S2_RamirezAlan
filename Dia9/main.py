# Class Day 9
#
from functionsGGDD import *
from functions import *

# Perform CRUD operations on jsonLime.json

artistList = openJSON()

print("")
print("Welcome to the Artist Library")
print("")
keepRunning = True
while(keepRunning):
    print("-----------------------------")
    print("--- Artist Library ---")
    print("-----------------------------")
    print("")
    print("1. Create Artist")
    print("2. Show All Artists")
    print("3. Show a Single Artist")
    print("4. Update a Specific Artist")
    print("5. Delete a Specific Artist")
    print("6. Exit Program")
    userOption = int(input("Choose an option (Numeric): "))
    print("")
    
    if userOption==1:
        print("-----------------------------")
        print("--- Create Artist ---")
        print("-----------------------------")
        diccionaryEmpty={
            "Artist name": str(input("Enter the Artist name")),
            "Country": "United Kingdom",
            "Active years": "1960\\u20131970",
            "Release year of first charted record": 1962,
            "Genre": "Rock\\/pop",
            "Total certified units": "294.6 millionUS: 217.250 millionJPN: 4.950 millionGER: 8 millionUK: 34.355 millionFRA: 4.090 millionCAN: 14.455 millionAUS: 3.060 millionBRA: 580,000NLD: 345,000ITA: 640,000SPA: 1.250 millionSWE: 485,000NOR: 200,000DEN: 610,000SWI: 350,000ARG: 1.926 millionBEL: 440,000AUT: 500,000POL: 175,000FIN: 118,048NZ: 660,000POR: 135,000",
            "Claimed sales": "600 million500 million"
        }


# Developed by: Alan Ramirez - ID 1096702159