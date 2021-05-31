
#CSV file imports
import csv

with open ('file name.csv') as csv file:
        csv reader = csv.reader(csv_file)
        lin_count = 0
        for row in csv_reader:
            if lin_count == 0:
                print(f'column Name are {",".join(row)')