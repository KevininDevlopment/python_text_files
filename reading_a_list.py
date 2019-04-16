### Reading a file into a list

with open("name_of_file") as file:
    myList = file.read().splitlines()
    print(myList)

with open("name_of_file") as file:
    myList = file.readlines()
    print(myList)

with open("name_of_file") as file:
    for line in file:
        print(line, end='')

### Writing into a file
with open("name_of_file", 'r+') as file:
    file.write("We are writing text into a file")
    file.seek(200)
    file.write("We are now writing into the file after 200")
    file.read()
