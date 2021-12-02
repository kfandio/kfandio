import csv, json
import pandas as pd

#filename = "Krankheiten.csv"
#pd.read_csv(filename)

with open("Krankheiten.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        confirmed = int(row["confirmed"])
        recovered = int(row["recovered"])
        deaths    = int(row["deaths"])
        active    = confirmed - recovered - deaths
        print("active :", active)