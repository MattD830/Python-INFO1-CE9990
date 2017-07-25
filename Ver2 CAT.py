import sys

try:
	cat_age = int(input("How old is your cat? (Type 0 if you don't have a cat) "))
except:
	print("You have failed")
	sys.exit(1)
	
age = {
	1 : 15,
	2 : 24,
}

if cat_age == 0:
	print("Goodbye!")
	sys.exit(0)

try:
	print('If your cat was a human it would be about',age[cat_age],'years old')
except KeyError:
	if cat_age < 26:
		print('If your cat was a human it would be about', cat_age * 4 + 16, 'years old')
		sys.exit(0)
	print("Your cat is dead. Sorry.")
	sys.exit(0)

print("How did you get here?")
sys.exit(0)
