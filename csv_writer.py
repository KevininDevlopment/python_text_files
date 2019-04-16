# csv file writer

import csv

with open('csv_file_name', 'a') as csvfile:
    writer = csv.writer(csvfile)
    csvdata = (5, 'Kevin', 'newinfo')
    writer.writerow(csvdata)

# for loop to write data to csv file

with open('name_of_csv_file', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['x', 'x**2', 'x**3', 'x**4'])
    for x in range(1, 101):
        writer.writerow([x, x**2, x**3, x**4])


# Change delimiter in csv file

with open('passwd', 'r') as f:
    reader = csv.reader(f, delimiter=':', lineterminator='\n')
    for row in reader:
        print(row)

# Process a complete file with with a list

with open('path/to/file') as f:
    devices = f.read().splitlines()

mylist = list()
for item in devices:
    tmp = item.split(':')
    mylist.append(tmp)

print(mylist)
