# this script opens the files and prints it out
import collections

population_dict = collections.defaultdict(int)

with open('lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
    header = next(inputFile)
    for line in inputFile:
        line = line.rstrip().split(',')
        line[5] = int(line[5])
        if line[1] == 'Total National Population':
            population_dict[line[0]] += line[5]


# see the result
print population_dict

with open('NationalPopulation.csv', 'w') as outputFile:
    outputFile.write('content,2010_population\n')
    for key, value in population_dict.iteritems():
        outputFile.write(key+','+str(value)+'\n')


#with the package csv
import csv

with open('lecz-urban-rural-population-land-area-estimates_codebook.csv', 'r') as inputFile:
    inputReader = csv.reader(inputFile)
    for line in inputReader:
        print line