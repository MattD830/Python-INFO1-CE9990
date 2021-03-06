"""
Downloads lyrics and returns the complexity of the chosen song

Decoded binary to string form
"""

import sys
import urllib.request as ur

while True:
	rl = 0
	s = str(input("\nPick a song(or type 0 to exit): "))
	if s == '0': 
		print("Goodbye!")
		sys.exit(0)
	else:
		s = s.replace(' ','-')+'-lyrics'
	a = input('Who sings it? ').replace(' ','-')
	url = 'http://www.songlyrics.com/'+a+'/'+s+'/'
	r = ur.Request(url,headers={'User-Agent':'Magic Browser'})
	try:
		c = ur.urlopen(r).read().decode('utf-8')
	except:
		print("That song doesn't exist")
		continue
	k = 1
	
	try:
		v = c.split('<p id="songLyricsDiv"  class="songLyricsV14 iComment-text">')[1].split('</p>')[0].replace('<br />','')
	except IndexError:
		print("You have typed incorrectly.")
		continue

	if '\r\n' in v:
		num_of_verses = v.replace('\r\n\r\n','\r\n').split('\r\n')
		vs = len(num_of_verses)
		v1 = v.replace('\r\n\r\n','\r\n').replace('\r\n','').replace(' ','')
		for i in v.split('\r\n'):
			if i == '':
				k += 1
	else:
		num_of_verses = v.replace('\n\n','\n').split('\n')
		vs = len(num_of_verses)
		v1 = v.replace('\n\n','\n').replace('\n','').replace(' ','')
		for i in v.split('\n'):
			if i == '':
				k += 1

	nr = [[verse,num_of_verses.count(verse)] for verse in set(num_of_verses)]
	for i in nr:
		if i[1] > 1:
			rl += i[1]

	avg_v = round(len(v1)/vs,2)

	cp = rl + ( avg_v * vs )

	print("\nComplexity: ",round(cp,2))

print("\nGoodbye!")
sys.exit(1)
