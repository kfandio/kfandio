try:
    import os
    import sys

    import elasticsearch
    from elasticsearch import Elasticsearch
    import pandas as pd

    print("Import alle Module !")
except Exception as e:
    print("Some Modules are Missing {}".format(e))

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])
#es.ping()

#doc1 = {"city": "Jaunde", "country": "Kamerun", "datetime": "2018,01,01,10,20,00"} #datetime format: yyyy,MM,dd,hh,mm,ss
#doc2 = {"city": "London", "country": "England", "datetime": "2018,01,02,03,12,00"}
#doc3 = {"city": "Los Angeles", "country": "USA", "datetime": "2018,04,19,19,21,00"}

# Create index
#Documents to insert in the elasticsearch index "cities"
es.indices.create(index ='my-foo', ignore=400 )