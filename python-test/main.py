import csv
import argparse
from datetime import datetime
from datetime import timedelta

FROMTHURSTOSUN = 3
FROMSUNTOTHURS = 4
TIMEDELTAWEEK = timedelta(7)
rows: list[tuple[str, str, str, str]] = []

parser = argparse.ArgumentParser()
parser.add_argument('-d','--date',type=str)
args = parser.parse_args()

currentDate = datetime.strptime(args.date, "%Y-%m-%d").date()
# currentDate +=FROMTHURSTOSUN
# print(currentDate)
# currentDate +=FROMSUNTOTHURS
# print(currentDate)

with open("../input/mikrofoner.csv", mode='r', encoding="utf-8-sig") as file:
    csvFile = csv.DictReader(file)

    for lines in csvFile:
        # print(lines)
        date_multiplier = int(lines["Date"])
        # print(currentDate + timedelta(date_multiplier*7))
        rows.append(
            (
                str(currentDate + timedelta(date_multiplier*7)),
                lines["Person"],
                lines["Type"],
                lines["TypeName"],
            )
        )
        rows.append(
            (
                str(currentDate + timedelta((date_multiplier*7)+FROMTHURSTOSUN)),
                lines["Person"],
                lines["Type"],
                lines["TypeName"],
            )
        )
        # print(currentDate + timedelta((date_multiplier*7)+FROMTHURSTOSUN))
rows.sort()
for row in rows:
    print(row)
        # lines["Date"] = str(date + FROMTHURSTOSUN)
    