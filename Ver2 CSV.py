"""
This script tell you where not to eat
"""

import sys
import urllib.request as ur
import re

url = 'https://data.cityofnewyork.us/api/views/xx67-kt59/rows.tsv?accessType=DOWNLOAD'
br = []

try:
	f = ur.urlopen(url)
except Exception as e:
	print("Something went wrong")
	print(e)
	sys.exit(1)
	
try:
	z = int(input("What is your zip code? "))
except:
	print("That's not a zipcode")
	sys.exit(1)
if z > 11697 or z < 10001:
	print("That zip is not in NYC")
	sys.exit(1)
	
print("\nPlease be patient while file is processing...\n")
	
for l in f:
	s = l.decode('utf-8').split('\t')
	if str(s[0]) == 'CAMIS' or str(s[5]) == 'N/A':
		continue
	try:
		score = int(s[13])
	except ValueError:
		score = 0
	zc = int(s[5])
	if z == zc:
		if score >= 30 and \
			bool(re.search("rat|roach|mice|flies", s[11])):
			br.append(s[1])

if br == []:
	print("That zip code has no restaurants or does not exist")
	sys.exit(0)

print("I would avoid the following restaurants:\n")
for i in br:
	print(i)
