import csv, json
import pandas as pd

def readCSV(filename):
    with open(filename+"csv") as csvFile:
        reader = csv.DictReader(csvFile)
        data = []
        for row in reader:
            data.append
    return data

def writeJSON(filename,data):
    with open(filename+".json", "w") as jsonFile:
        json.dump(data,jsonFile,indent=4)
        
        

files = ["Krankheiten", "Symptome"]


for file in files:
    data = readCSV(file)

#Ordner = "C:\Users\kevin\Documents\kfandio\data.csv"
#filename = "data.csv"
#pd.read_csv(Ordner)