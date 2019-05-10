'''
	makeLabels - scipt for making label vector
	input: list of players + their roles ('prettyProPlayers.txt')
	output: labels.csv

	Authors:
	DELOS SANTOS, Angelo Vincent
	DEL ROSARIO, Luis Gabriel
	MIRANDA, Edrene Bryze
'''


f = open('prettyProPlayers.txt','r')
o = open('labels.csv', 'w+')
for line in f:
	a = line.split(',')
	o.write(a[1])

f.close()
o.close()