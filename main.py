with open('customer.txt') as inFile:
    linesOfInputFile = inFile.readlines()
    inFile.close()

print(linesOfInputFile[0])
print(linesOfInputFile[1])

dashes = linesOfInputFile[1].split()
lenDashes = [len(dashes[0])]

for i in range (1, len(dashes),):
    lenDashes.append(lenDashes[i-1] + len(dashes[i]) + 1)

print(lenDashes)

lCustomers = []
line = []

for i in range (2, len(linesOfInputFile), ):
    line.clear()
    line.append(linesOfInputFile[i][0:lenDashes[0]])
    for j in range(1, len(lenDashes), ):
        line.append(linesOfInputFile[i][lenDashes[j-1]:lenDashes[j]])

    print(line)
    lCustomers.append(dict(uname=line[0], passwd=line[1], lname=line[2], 
        fname=line[3], addr=line[4], zone=line[5], sex=line[6], age=line[7], 
        limit=line[8], balance=line[9], creditcard=line[10], email=line[11], 
        active=line[12]))

print(lCustomers)