from numpy import datetime_as_string
import pandas as pd
import json
from elasticsearch import Elasticsearch
es = Elasticsearch()


"""
Program for the purpose of loading data into an Elasticsearch-Database (ES-Index),
searching for data inside this ES-Index and deleting this ES-Index.
"""


def readExcel(path_filename):
    """ Reads Excel and returns json """
    df = pd.read_excel(path_filename, index_col=None) # excel -> pandas dataframe
    print(df)
    data = df.to_dict(orient="records") # pandas dataframe -> dictionary

    data_print = json.dumps(data, indent=4, ensure_ascii=False).encode('utf8') # preperation for pretty-print: encoding with utf-8 for "ä, ö, etc."
    print(data_print.decode()) # pretty-print with indent level

    #return data


# def readCSV(filename):
#     with open(filename + ".csv") as csvFile:
#         reader = csv.DictReader(csvFile)
#         data = []
#         for row in reader:
#            # print(row)
#            data.append(row)
#     return data

#def transactToES(index, data):
#    """ Creates documents in ES-index with list like data """
#    data_print = json.dumps(data, indent=4, ensure_ascii=False).encode('utf8') # preperation for pretty-print: encoding with utf-8 for "ä, ö, etc."
#    print(data_print.decode()) # pretty-print with indent level
#    print("-" * 50)

#    for dat in data:
#        es.index(index=index, document=dat) # creates document in index


#def search(index, key, value, op):
#    """ 
#    Searches for data in ES-index

#    op: operator can be "and" (e.g. must match "Husten AND Fieber") or "or" (e.g. "Husten OR Fieber")
#    """

#    reqBody = {
#        "size": 5, # no. of hits that will be sent
#        "query": {
            # "match_all": {} # gives back all entries in ES-index
#            "match": {
#                key: { # key for example: "Name" oder "Symptome"
#                    "query": value, # value for example: "Fieber"
#                    "operator": op # op can be "and" or "or"
#                } 
#            }
#        }
#    }
#    res = es.search(index=index, body=reqBody)

#    data_print = json.dumps(res, indent=4, ensure_ascii=False).encode('utf8') # preperation for pretty-print: encoding with utf-8 for "ä, ö, etc."
#    print(data_print.decode()) # pretty-print with indent level


def mainFunction():
    #""" Execution of all relevant functions. Comment/Uncomment line to execute desired function. """
     data = readExcel('Dataset_Krankenheiten.xlsx') # extract data from excel-file and convert it to json
    # transactToES("krankheiten", data) # create document in index "krankheiten" in Elasticsearch
    # search("krankheiten", "Übertragen über", "Körperflüssigkeiten", "and") # search for entries in ES-index
    # es.indices.delete(index='krankheiten', ignore=[400, 404]) # deletes whole index with name "krankheiten"


mainFunction()