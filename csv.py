"""
This script tells you where not to eat
"""

import sys
import os
import csv
import re

USERNAME = os.getlogin()

if sys.platform.startswith('win32'):
	p = 'C:/users/'+USERNAME+'/Desktop/'
elif sys.platform.startswith('darwin'):
	p = '/Volumes/MyDrive/Users/'+USERNAME+'/Desktop/'
else:
	print('Your Operating System is not Supported')
	sys.exit(1)

fn = p+'DOHMH_New_York_City_Restaurant_Inspection_Results.tsv'

try:
	f = open(fn)
except FileNotFoundError:
	print("Go to the following link > export > TSV for excel > and save the file to your desktop\n")
	print("https://data.cityofnewyork.us/Health/DOHMH-New-York-City-Restaurant-Inspection-Results/xx67-kt59")
	sys.exit(1)

count = 0
try:
	r = int(input("What is your zip code? "))
except:
	print("That's not a zipcode")
	sys.exit(1)
for i in str(r):
	count += 1

if count == 4:
	print("That zipcode is not in NYC")
	sys.exit(1)
elif count != 5:
	print("That is not a zip code")
	sys.exit(1)
if r >11697:
	print("That zipcode is not in NYC")
	sys.exit(0)
	
br = []

for l in f:
	s = l.split("\t")
	if l[0:5] == 'CAMIS' or str(s[5]) == 'N/A':
		continue
	if s[13] == '':
		s[13] = 0
	if r == int(s[5]):
		if int(s[13]) >= 30 and \
				bool(re.findall("rat|roach|mice|flies",str(s[11]))):
			br.append(s[1])
      
if br == []:
	print("That zipcode is not in NYC")
	sys.exit(1)
  
print("I would avoid these restaurants:")
for i in br:
	print(i)

sys.exit(0)
