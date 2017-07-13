'''
This script provides the lyrics to the children's rhyme, "There was an old lady who swallowed a fly"
'''

import sys

a = [ 'fly','spider','bird','cat','dog','goat','cow','horse' ];a1 = []

v1 = 'There was an old lady who swallowed a '
v2 = [ "But I don't know why she swallowed the fly - perhaps she'll die!","That wriggled and wiggled and tickled inside her!","How absurd to swallow a bird!","Fancy that to swallow a cat!","What a hog, to swallow a dog!","She just opened her throat and swallowed a goat!","I don't know how she swallowed a cow!","...She's dead, of course!"]
v3 = "She swallowed the {} to catch the {}"

for i in range(len(a)):
	a1 += [a[i]]
	print(v1+a[i]+'\n'+'   '+v2[i]+'\n')
	if i == 0: continue
	elif i == 7: break
	else:
		for j in sorted(range(len(a1)),reverse=True):
			if j == 0: continue
			print('   '+v3.format(a1[j],a1[j-1]))
	print('   '+v2[0]+'\n')

sys.exit(0)
