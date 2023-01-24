with open('customer.txt') as inFile:
    linesOfInputFile = inFile.readlines()
    inFile.close()

print(linesOfInputFile[0])
print(linesOfInputFile[1])

dashes = linesOfInputFile[1].split()
lenDashes = [len(dashes[0])]

for i in range (1, len(dashes),):
    lenDashes.append(lenDashes[i-1] + len(dashes) + 1)

print(lenDashes)

lCustomers = []

for i in range (2, len(linesOfInputFile), ):
    line =linesOfInputFile[i]

    print(line)
    lCustomers.append(dict(uname=line[0], passwd=line[1], lname=line[2], 
        fname=line[3], addr=line[4], zone=line[5], sex=line[6], age=line[7], 
        limit=line[8], balance=line[9], creditcard=line[10], email=line[11], 
        active=line[12]))

print(lCustomers)