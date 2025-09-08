import csv
import argparse
from datetime import datetime
from datetime import timedelta
VERSION = '0.1.0'
VERSION_PRINT = 'NW-Scripter - version {}'.format(VERSION)
DAYS = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

parser = argparse.ArgumentParser()
parser.add_argument('-v','--version', action='store_true', help='Prints the current version of program')
parser.add_argument('-d','--date',type=str, help='The date to start adding from')
parser.add_argument('-f','--file', type=str, help='What file to use inside input folder')
parser.add_argument('-sat','--saturday', action='store_true', help='Sets weekend meeting to saturday, default is sunday')
args = parser.parse_args()


def run_program():
    rows: list[tuple[str, str, str, str]] = []

    mid_week_meeting_day:int = datetime.strptime(args.date, '%Y-%m-%d').date().weekday()
    weekend_meeting_day:int = 5 if args.saturday else 6
    meetings_diff = weekend_meeting_day - mid_week_meeting_day
    print('Running script for automated setup of dates with meeting-days:\n\n- {} \n- {}\n'.format(DAYS[mid_week_meeting_day], DAYS[weekend_meeting_day]))

    with open('./input/base_schedule.csv', mode='r', encoding='utf-8-sig') as file:
        csvFile = csv.DictReader(file)
        current_date = datetime.strptime(args.date, '%Y-%m-%d').date()

        for lines in csvFile:
            date_multiplier = int(lines['Date'])
            rows.append(
                (
                    str(current_date + timedelta(date_multiplier*7)),
                    lines['Person'],
                    lines['Type'],
                    lines['TypeName'],
                )
            )
            rows.append(
                (
                    str(current_date + timedelta((date_multiplier*7)+meetings_diff)),
                    lines['Person'],
                    lines['Type'],
                    lines['TypeName'],
                )
            )
    rows.sort()
    with open('./output/'+str(current_date)+'-output.csv', 'w', encoding='UTF-8') as f:
        f.write('Date, Person, Type, TypeName\n')
        for row in rows:
            f.write('%s,%s,%s,%s\n' % (row[0], row[1], row[2], row[3]))

        f.close()
    

if __name__ == '__main__':
    if args.version:
        print(VERSION_PRINT)
    else:
        run_program()
