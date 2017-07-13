"""
Downloads lyrics and returns the complexity of the chosen song
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
		c = ur.urlopen(r).read()
	except:
		print("That song doesn't exist")
		continue
	k = 1
	
	try:
		v = c.split(b'<p id="songLyricsDiv"  class="songLyricsV14 iComment-text">')[1].split(b'</p>')[0].replace(b'<br />',b'')
	except IndexError:
		print("You have typed incorrectly.")
		continue

	if b'\r\n' in v:
		num_of_verses = v.replace(b'\r\n\r\n',b'\r\n').split(b'\r\n')
		vs = len(num_of_verses)
		v1 = v.replace(b'\r\n\r\n',b'\r\n').replace(b'\r\n',b'').replace(b' ',b'')
		for i in v.split(b'\r\n'):
			if i == b'':
				k += 1
	else:
		num_of_verses = v.replace(b'\n\n',b'\n').split(b'\n')
		vs = len(num_of_verses)
		v1 = v.replace(b'\n\n',b'\n').replace(b'\n',b'').replace(b' ',b'')
		for i in v.split(b'\n'):
			if i == b'':
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
