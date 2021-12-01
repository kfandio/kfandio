import csv, json
import pandas as pd

#filename = "Krankheiten.csv"
#pd.read_csv(filename)

with open("Krankheiten.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)