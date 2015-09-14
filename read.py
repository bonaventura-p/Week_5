# this script opens the files and prints it out

with open('lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
	for line in inputFile:
		print line	