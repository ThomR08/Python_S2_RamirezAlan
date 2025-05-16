# Class Day 9
#
from functionsGGDD import *

# Perform CRUD operations on jsonLime.json

artistList = openJSON()
LogsArtistList = openLogsJSON()

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
        print("")
        diccionaryEmpty={
            "Artist name": str(input("Enter the Artist name: ")),
            "Country": str(input("Enter the Country of artist: ")),
            "Active years": str(input("Enter the Active years of artist: ")),
            "Release year of first charted record": int(input("Enter the Release year of first charted record of artist: ")),
            "Genre": str(input("Enter the Genre of artist: ")),
            "Total certified units": str(input("Enter the Total certified units of artist: ")),
            "Claimed sales": str(input("Enter the Claimed sales of artist: "))
        }
        print("")
        artistList.append(diccionaryEmpty)
        saveJSON(artistList)
        artistList = openJSON()

    elif userOption==2:
        print("-----------------------------")
        print("--- Show All Artists ---")
        print("-----------------------------")
        print("")
        for i in range(len(artistList)):
            print("-----------------------------")
            print("--- Artist #",i+1," ---")
            print("-----------------------------")
            print("")
            print("Artist name:", artistList[i]["Artist name"])
            print("Country:", artistList[i]["Country"])
            print("Active years:", artistList[i]["Active years"])
            print("Release year of first charted record", artistList[i]["Release year of first charted record"])
            print("Genre:", artistList[i]["Genre"])
            print("Total certified units:", artistList[i]["Total certified units"])
            print("Claimed sales:", artistList[i]["Claimed sales"])
            print("")
    elif userOption==3:
        print("-----------------------------")
        print("--- Show a Single Artist ---")
        print("-----------------------------")
        print("")
        searchArtist=int(input("Enter the number of artist for Show: "))
        print("")
        if searchArtist<=len(artistList):
            searchArtist-=1
            print("-----------------------------")
            print("--- Artist #",searchArtist+1," ---")
            print("-----------------------------")
            print("")
            print("Artist name:", artistList[searchArtist]["Artist name"])
            print("Country:", artistList[searchArtist]["Country"])
            print("Active years:", artistList[searchArtist]["Active years"])
            print("Release year of first charted record", artistList[searchArtist]["Release year of first charted record"])
            print("Genre:", artistList[searchArtist]["Genre"])
            print("Total certified units:", artistList[searchArtist]["Total certified units"])
            print("Claimed sales:", artistList[searchArtist]["Claimed sales"])
            print("")
        else:
            print("Artist not found")
            print("")
    elif userOption==4:
        print("-----------------------------")
        print("--- Update a Specific Artist ---")
        print("-----------------------------")
        print("")
        searchArtist=int(input("Enter the number of artist for Update: "))
        print("")
        if searchArtist<=len(artistList):
            searchArtist-=1
            print("--- Past data: ---")
            print("")
            print("-----------------------------")
            print("--- Artist #",searchArtist+1," ---")
            print("-----------------------------")
            print("")
            print("Artist name:", artistList[searchArtist]["Artist name"])
            print("Country:", artistList[searchArtist]["Country"])
            print("Active years:", artistList[searchArtist]["Active years"])
            print("Release year of first charted record", artistList[searchArtist]["Release year of first charted record"])
            print("Genre:", artistList[searchArtist]["Genre"])
            print("Total certified units:", artistList[searchArtist]["Total certified units"])
            print("Claimed sales:", artistList[searchArtist]["Claimed sales"])
            print("")
            print("--- New data: ---")
            print("")
            print("-----------------------------")
            print("--- Artist #",searchArtist+1," ---")
            print("-----------------------------")
            artistList[searchArtist]["Artist name"]=str(input("Enter the Artist name: ")),
            artistList[searchArtist]["Country"]=str(input("Enter the Country of artist: ")),
            artistList[searchArtist]["Active years"]=str(input("Enter the Active years of artist: ")),
            artistList[searchArtist]["Release year of first charted record"]=int(input("Enter the Release year of first charted record of artist: ")),
            artistList[searchArtist]["Genre"]=str(input("Enter the Genre of artist: ")),
            artistList[searchArtist]["Total certified units"]=str(input("Enter the Total certified units of artist: ")),
            artistList[searchArtist]["Claimed sales"]=str(input("Enter the Claimed sales of artist: "))
            print("")
            saveJSON(artistList)
            artistList = openJSON()
            print("The artist has been successfully update")
            print("")
        else:
            print("Artist not found")
            print("")
    elif userOption==5:
        print("-----------------------------")
        print("--- Delete a Specific Artist ---")
        print("-----------------------------")
        print("")
        searchArtist=int(input("Enter the number of artist for Delete: "))
        print("")
        if searchArtist<=len(artistList):
            searchArtist-=1
            eliminateArtist=artistList.pop(searchArtist)
            LogsArtistList.append(eliminateArtist)
            saveLogsJSON(LogsArtistList)
            LogsArtistList=openLogsJSON()
            saveJSON(artistList)
            artistList=openJSON()
            print("The artist has been successfully removed")
            print("")
        else:
            print("Artist not found")
            print("")
    elif userOption==6:
        print("Bye bye")
        keepRunning=False
    else:
        print("It is not a valid option")
        print("")

# Developed by: Alan Ramirez - ID 1096702159