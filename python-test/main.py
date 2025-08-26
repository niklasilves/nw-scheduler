import csv
import argparse
from datetime import datetime
from datetime import timedelta

FROMTHURSTOSUN = timedelta(3)
FROMSUNTOTHURS = timedelta(4)
rows = []

parser = argparse.ArgumentParser()
parser.add_argument('-d','--date',type=str)
args = parser.parse_args()

currentDate = datetime.strptime(args.date, "%Y-%m-%d").date()
currentDate +=FROMTHURSTOSUN
print(currentDate)
currentDate +=FROMSUNTOTHURS
print(currentDate)

with open("testfile.csv", mode='r', encoding="utf-8-sig") as file:
    csvFile = csv.DictReader(file)

    parseTest = datetime    
    for lines in csvFile:
        print(lines)
        date = datetime.strptime(lines["Date"], "%Y-%m-%d").date()
        lines["Date"] = str(date + FROMTHURSTOSUN)
        print(lines)
    