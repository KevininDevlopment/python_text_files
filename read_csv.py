### CSV reader

import csv

with open('name_of_file.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


with open('name_of_file.csv', 'r') as file:
    reader = csv.reader(file)
    # reading a specific year in the file
    year = dict()
    for row in reader:
        year[row[0]] = row[1]
    print(year)


    max_num = max(year.values())

    for k,v in year.items():
        if max_num == v:
            print('Busiest month is {k}, time:{v.strip()}')