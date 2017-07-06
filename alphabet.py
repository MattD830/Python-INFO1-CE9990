import sys

c = 'bcdfghjklmnpqrstvwxyz'
v = 'aeiou'

for i in c:
	if i == 'n':
		sys.exit(0)
	elif i != 'l':
		for j in v:
			y = ''
			x = '-'+i
			if j == 'a':
				x += 'ay'
			elif j == 'e':
				x += 'ee'
			elif j == 'i':
				x += j+'cky'+'-'+i+j
			elif j == 'o':
				x = ' '+i+j
				y = ' '+i+'icky-'+i+'i'+' '+i+'o,'
			elif j == 'u':
				x = ' '+i+j		
			print(i.upper()+"-"+j.upper()+x+','+y,end=' ')
		print(i+'icky '+i+'i '+i+'o '+i+'u.')
	else:
		for j in v:
			y = ''
			x = '-'+i
			if j == 'a':
				x += 'ay'
			elif j == 'e':
				x += 'ee'
			elif j == 'i':
				x += j+'cky'+'-'+i+j
			elif j == 'o':
				x = ' '+i+j
				y = ' '+i+'icky-'+i+'i'+' '+i+'o,'
			elif j == 'u':
				x = ' '+i+j		
			print(i.upper()+"-"+j.upper()+x+','+y,end=' ')
		print('Curly\'s a dope.')
	
sys.exit(0)
