import csv
import matplotlib.pyplot as plt

filename = 'Fire_Incident_Dispatch_Data.csv'

fields = []
rows = []
count = 0

INCIDENT_BOROUGH = 5

incidentsbyborough = {}
incidentsbyboroughper100000 = {}

population = {}
population['RICHMOND / STATEN ISLAND'] = 495747
population['BRONX'] = 1472654
population['BROOKLYN'] = 2736074
population['QUEENS'] = 2405464
population['MANHATTAN'] = 1694263

with open(filename, 'r') as csvinput:
	
    inputreader = csv.reader(csvinput)
    fields = next(inputreader)

    for row in inputreader:
        borough = row[INCIDENT_BOROUGH]
        if borough not in incidentsbyborough.keys():
            incidentsbyborough[borough] = 0
        incidentsbyborough[borough] += 1

    print("Number of incidents per boroughs:")
    for key in incidentsbyborough:
        print(key + ': ' + str(incidentsbyborough[key]))

    print()
    print("Number of incidents per 100000 inhabitants per boroughs:")
    for key in incidentsbyborough:
        incidentsbyboroughper100000[key] = int(incidentsbyborough[key])/population[key]*100000
        print(key + ': ' + str(incidentsbyboroughper100000[key]))

plt.bar(incidentsbyborough.keys(), incidentsbyborough.values())
plt.show()