MyList = ["New york","London","Paris","New delhi"]
Myfile = open('output.txt', 'w')
for element in MyList:
    Myfile.write(element)
    Myfile.write('\n')
Myfile.close()