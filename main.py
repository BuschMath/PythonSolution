with open('customer.txt') as inFile:
    linesOfInputFile = inFile.readlines()
    inFile.close()

dashes = linesOfInputFile[1].split()
lenDashes = [len(dashes[0])]

for i in range (1, len(dashes),):
    lenDashes.append(lenDashes[i-1] + len(dashes[i]) + 1)

lCustomers = []
line = []

for i in range (2, len(linesOfInputFile), ):
    line.clear()
    line.append(linesOfInputFile[i][0:lenDashes[0]])
    for j in range(1, len(lenDashes), ):
        line.append(linesOfInputFile[i][lenDashes[j-1]:lenDashes[j]])

    lCustomers.append(dict(uname=line[0].strip(), passwd=line[1].strip(), 
        lname=line[2].strip(), fname=line[3].strip(), addr=line[4].split(), 
        zone=line[5].strip(), sex=line[6].strip(), age=line[7].strip(), 
        limit=line[8].strip(), balance=line[9].strip(), creditcard=line[10].strip(), 
        email=line[11].strip(), active=line[12].strip()))

with open('zonecost.txt') as inFile:
    linesOfInputFile = inFile.readlines()
    inFile.close()

dashes = linesOfInputFile[1].split()
lenDashes = [len(dashes[0])]

for i in range (1, len(dashes),):
    lenDashes.append(lenDashes[i-1] + len(dashes[i]) + 1)

lZone = []
line = []

for i in range (2, len(linesOfInputFile), ):
    line.clear()
    line.append(linesOfInputFile[i][0:lenDashes[0]])
    for j in range(1, len(lenDashes), ):
        line.append(linesOfInputFile[i][lenDashes[j-1]:lenDashes[j]])

    lZone.append(dict(zoneid=line[0].strip(), zonedesc=line[1].strip(), 
        price=line[2].strip()))

print(lZone)