import json

def openJSON():
    dicFinal={}
    with open("./jsonLime.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def saveJSON(dic):
    with open("./jsonLime.json",'w') as outFile:
        json.dump(dic,outFile)

def openLogsJSON():
    dicFinal={}
    with open("./jsonLimeLogs.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def saveLogsJSON(dic):
    with open("./jsonLimeLogs.json",'w') as outFile:
        json.dump(dic,outFile)