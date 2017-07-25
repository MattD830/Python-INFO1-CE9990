'''
This script provides the lyrics to the children's rhyme, "There was an old lady who swallowed a fly"

a is for animal and v is for verse and i is for indent.
'''

import sys

a1 = [ 'fly', 'spider', 'bird', 'cat', 'dog', 'goat', 'cow', 'horse' ]
a2 = []
i1 = 3 * ' '

v1 = 'There was an old lady who swallowed a '
v2 = [ 
"But I don't know why she swallowed the fly - perhaps she'll die!",
"That wriggled and wiggled and tickled inside her!",
"How absurd to swallow a bird!",
"Fancy that to swallow a cat!","What a hog, to swallow a dog!",
"She just opened her throat and swallowed a goat!",
"I don't know how she swallowed a cow!",
"...She's dead, of course!"
]

v3 = "She swallowed the {} to catch the {}"

for i in range(len(a1)):
	print(v1 + a1[i])
	if i == len(v2)-1:
		print(i1 + "...She's dead, of course!")
		break
	if i > 0:
		print(i1 + v2[i])
		print()
		
		a2 += [a1[i]]
		for j in range(len(a2) - 1, 0, -1):
			print(v3.format(a2[j], a2[j-1]))
      
	print(i1 + v2[0])
	print()

sys.exit(0)
