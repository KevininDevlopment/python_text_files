import csv

# Change delimiter in csv file

with open('/path/to/file', 'r') as f:
    reader = csv.reader(f, delimiter=':', lineterminator='\n')
    for row in reader:
        print(row)

# Process a complete file with with a list csv module not used

with open('path/to/file') as f:
    devices = f.read().splitlines()

mylist = list()
for item in devices:
    tmp = item.split(':')
    mylist.append(tmp)

print(mylist)

# Csv module used to print items

#import csv
with open('/path/to/file') as f:
    reader = csv.reader(f, delimiter=':')
    for row in reader:
        print(row)