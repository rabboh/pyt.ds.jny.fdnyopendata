import csv

filename = 'Fire_Incident_Dispatch_Data.csv'

fields = []
rows = []
count = 0

categoryfields = [2, 5, 12, 13, 14, 15, 16, 22, 23]
fieldvalues = []
for i in range(29):
    fieldvalues.append([])

with open(filename, 'r') as csvinput:
	
    inputreader = csv.reader(csvinput)
    fields = next(inputreader)


    # List of fields, with indices
    for i, field in enumerate(fields):
        print(str(i) + ': ' + field)

    print()


    # Counting the number of rows and collecting distinct elements of category fields
    for row in inputreader:
        count = count + 1
        examplerow = row
        for categoryfieldid in categoryfields:
            val = row[categoryfieldid]
            if val not in fieldvalues[categoryfieldid]:
                fieldvalues[categoryfieldid].append(val)

    print("Total numbers of rows: %d\n"%(count))


    # Print the last row as an example
    for i, data in enumerate(examplerow):
        print(fields[i] + ': ' + examplerow[i])

    print()

    
    # Printing the distinct elements of category fields
    for categoryfieldid in categoryfields:
        print("Value set of " + fields[categoryfieldid] + ":")
        for val in fieldvalues[categoryfieldid]:
            print(' * ' +val)
        print()



