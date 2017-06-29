import sys
import urllib.request

def d(sym):
	"""
	downloads dataframe from google
	"""
	url = 'http://www.google.com/finance/historical?q=NASDAQ%3A{0}&ei=LL5UWaHxONaXeembtLgG&output=csv'.format(sym)
	try:
		r = urllib.request.urlopen(url)
	except Exception as e:
		print("URL failed: Try inputting an actual stock")
		sys.exit(2)
	f = r.readlines()
	r.close()
	return f[:11]

stock = input("What stock are you going to buy? ")
spam = d(stock)

i = 1
x = []
while i < 11:
	x.append(float(spam[i].decode('utf-8').replace('\n','').split(',')[4]))
	i += 1

if sum(x)/10 >= 5:
	print("Your stock is not a penny stock")
	sys.exit(0)
elif sum(x)/10 < 5:
	print("Your stock is a penny stock, it's best not to invest")
	sys.exit(0)
else:
	print("Something went wrong")
	sys.exit(1)
	
	
