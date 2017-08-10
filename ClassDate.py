"""
classDate.py

Create a class named Date and call one of its class methods (monthsInYear).
Then create an object named d of class Date and call its instance methods.
"""

import sys

class Date(object):
	"""
	Class Date demonstrates class and instance attributes, class and instance methods.
	It is a simple date class, containing year, month, and day integers.
	"""

	lengths = [
		None,
		31, #January
		28, #February
		31, #March
		30, #April
		31, #May
		30, #June
		31, #July
		31, #August
		30, #September
		31, #October
		30, #November
		31	#December
	]
	
	january = 1
	february = 2
	march = 3
	april = 4
	may = 5
	june = 6
	july = 7
	august = 8
	september = 9
	october = 10
	november = 11
	december = 12

	def __init__(self, month, day, year):
		assert isinstance(year, int)
		assert isinstance(month, int) and 1 <= month and month <= Date.monthsInYear()
		assert isinstance(day, int) and 1 <= day and day <= Date.lengths[month]
		self.year = year
		self.month = month
		self.day = day

	#These three methods are getters.

	def getYear(self):
		"Return my year."
		return self.year

	def getMonth(self):
		"Return the number of my month (1 to 12 inclusive)."
		return self.month

	def getDay(self):
		"Return the number of my day (1 to the length of my month, inclusive)."
		return self.day

	def __str__(self):
		"Return a string that looks like the contents of myself."
		return "{:02}/{:02}/{:04}".format(self.month, self.day, self.year)

	def dayOfYear(self):
		"Return my day of the year: a number in the range 1 to 365 inclusive."
		return sum(Date.lengths[1:self.month]) + self.day

	def nextDay(self):
		"Move myself one day into the future."
		if self.day < Date.lengths[self.month]:
			self.day += 1
		else:
			self.day = 1	   #Go to the first day of the next month.
			if self.month < Date.monthsinyear:
				self.month += 1
			else:
				self.month = 1 #Go to the first month of the next year.
				self.year += 1

	def nextDays(self, n):
		"Move myself n days into the future."
		assert isinstance(n, int) and n >= 0
		for i in range(n):
			self.nextDay()	   #Call the instance method in line 62.
			
	def prevDay(self):
		"""We're going back in time, Marty"""
		if self.day > 0:
			self.day -= 1
		else:
			self.day = Date.lengths[self.month]
			if self.month > Date.january:
				self.month -= 1
			else:
				self.month = Date.december
				self.year -= 1
	def prevDays(self, n):
		assert isinstance(n, int) and n >= 0
		for i in range(n):
			self.prevDay()
			
	def __sub__(self, other):
		"""
		Return the distance in days between the two Date objects.
		The return value is positive is self is later than other,
		negative if self is earlier than other, and zero if they're the same Date.
		"""
		iself  = 365 *	self.year +	 self.dayOfYear()
		iother = 365 * other.year + other.dayOfYear()
		return iself - iother
		
	def __lt__(self, other):
		"Return True if self is earlier than the other Date, False otherwise."
		return self.dayOfYear() - other.dayOfYear() > 0  
    
	@staticmethod
	def monthsInYear():
		"Return the number of months in a year.	 This function is selfless."
		return len(Date.lengths) - 1;
	
	@staticmethod
	def daysInYear():
		"""Returns the days in year"""
		return	sum (Date.lengths[1:])

	#The definition of class Date ends here.

d = Date(Date.january, 6, 2017)		  #Call the instance method in line 32.
d2 = Date(Date.november, 11, 2017)
print("months in year =", d.monthsInYear())
print("Days in year:",d.daysInYear())
print("type(d) =", type(d))
print()
#These three statements do the same thing:
print("d =", d)
print("d =", str(d))
print("d =", d.__str__())	   #Call the instance method in line 54.

print("month =", d.getMonth()) #Call the instance method in line 46.
print("day =", d.getDay())	   #Call the instance method in line 50.
print("year =", d.getYear())   #Call the instance method in line 42.
print()

print("{} is day number {} of the year {}.".format(d, d.dayOfYear(), d.getYear()))
d.nextDay()					   #Call the instance method in line 62.
print(d, "is the next day.")
d.nextDays(7)				   #Call the instance method in line 74.
print(d, "is a week after that.")
d.prevDays(8)
d.prevDay()
print(d, "was yesterday")
d.prevDays(7)
print(d, "was a week ago.")
if d > d2:
	print(d,"comes after",d2)
else:
	print(d,"comes before",d2)
print(d2 - d)
sys.exit(0)
