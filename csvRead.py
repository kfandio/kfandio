import csv, json
from elasticsearch import Elasticsearch
import pandas as pd

es = Elasticsearch()

def readCSV(filename):
    with open(filename + ".csv") as csvFile:
        reader = csv.DictReader(csvFile)
        data = []
        for row in reader:
           # print(row)
           data.append(row)
    return data

def dataToEs(index, data):
    for element in data:
        es.index(index=index, id =element["Name"], body =json.dumps(element))


def writeJSON(filename, data):
    with open(filename + ".json", "w") as jsonFile:
        json.dump(data, jsonFile, indent=4)

def search(index):
    requestBody = {
        "query":{
            "match_all":{}
        }
    }
    response = es.search(index=index, body=requestBody)
    print(response["hits"]["hits"])

files = ["Krankheiten"]
#for file in files:
#    data = readCSV(file)
#    dataToEs("kranheiten-data",data)
#    #writeJSON(file,data)

search("kranheiten-data")