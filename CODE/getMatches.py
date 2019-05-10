'''
	getMatches - Python script to get matches of each player
	input: accountIDs.txt - list of account IDs you wanna get the matches of
	output: feature.csv - FEATURE VECTOR

	Authors:
	DELOS SANTOS, Angelo Vincent
	DEL ROSARIO, Luis Gabriel
	MIRANDA, Edrene Bryze
'''

import time
import urllib.request
import json
from socket import timeout

# open the file
idFile = open('accountIDs.txt', 'r')

# store IDs in a list
accountIDs = []
for line in idFile:
	accountIDs.append(int(line))

idFile.close()

# open the output file feature vector)
o = open('feature.csv', 'w+')

# for all IDs
for aid in accountIDs:
	print('ID: %d' % aid)

	# Open URL of recent matches from OpenDota API
	#  - keep trying; catch TIMEOUT, URL and HTTP errors
	success = 0
	while(1):
		try:
			req = urllib.request.urlopen('https://api.opendota.com/api/players/%d/recentMatches' % aid, timeout=5).read()
			success = 1
			break
		except urllib.error.HTTPError: 
			print ("HTTP ERROR AT ACCOUNT ID %d" % aid)
			time.sleep(1.5)
		except urllib.error.URLError: 
			print ("URL ERROR AT ACCOUNT ID %d" % aid)
			time.sleep(1.5)
		except timeout:
		    print ('socket timed out.')
		    time.sleep(1.5)

	# If for some reason loop was broken, GET was unsuccessful
	if(success == 0): 
		print("UNSUCCESSFUL GET")
		o.write('%d\n' % (-1))
	else:
		# successful get
		req = req.decode('utf-8') # decode text to turn it into a string
		data = json.loads(req) # parse JSON
		isStart = 1 # for printing commas
		for i in data:
			# print comma if it's NOT the start
			if (isStart == 1): isStart = 0
			else: o.write(',')

			o.write('%d' % i['hero_id']) # write the hero ID

			# script for checking if the player won
			if (i['player_slot'] < 128 and i['radiant_win']):
				# They won!
				o.write(',%d' % 1)
			elif (i['player_slot'] >= 128 and not i['radiant_win']):
				# They won!
				o.write(',%d' % 1)
			else:
				# They lost.
				o.write(',%d' % 0)
		o.write('\n')
		time.sleep(1.1) # wait 1.1 seconds, since the API only allows 1 request per second

o.close()