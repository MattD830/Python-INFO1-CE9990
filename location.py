import json
import urllib.request as ur

class Location(object):
	def __init__(self,lat,lng):
		if lng > 180 or lng < -180:
			raise ValueError("Longitude must be between -180 and 180")
		if lat > 90 or lat < -90:
			raise ValueError("Latitude must be between -90 and 90")
		self.lat = self.setLatitude(lat)
		self.lng = self.setLongitude(lng)
		
	def __repr__(self):
		if self.lat >= 0:
			if self.lng >= 0:
				return self.getaddress()+' ('+self.north()+', '+self.east()+')'
			else:
				return self.getaddress()+' ('+self.north()+', '+self.west()+')'
		else:
			if self.lng >= 0:
				return self.getaddress()+' ('+self.south()+', '+self.east()+')'
			else:
				return self.getaddress()+' ('+self.south()+', '+self.west()+')'
		
	def getZipcode(self):
		self.mapf = self.getmap()
		if self.mapf['status'] == 'OK':
			for i in range(len(self.mapf['results'][0]['address_components'])):
				if self.mapf['results'][0]['address_components'][i]['types'][0] == 'postal_code':
					self.zip = int(self.mapf['results'][0]['address_components'][i]['long_name'])
					break
		else:
			self.zip = 0
		return self.zip
		
	def getmap(self):
		self.url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}'.format(self.lat,self.lng)
		self.mapf = json.loads(ur.urlopen(self.url).read())
		return self.mapf
		
	def getaddress(self):
		self.mapf = self.getmap()
		if self.mapf['status'] == 'OK':
			self.address = self.mapf['results'][0]['formatted_address']
		elif self.lat == 90:
			self.address = 'The North Pole'
		else:
			self.address = ''
		return self.address
		
	def north(self):
		return str(self.lat)+'°N'
	def south(self):
		return str(self.lat)+'°S'
		
	def east(self):
		return str(self.lng)+'°E'
	def west(self):
		return str(self.lng)+'°W'
		
	def getLatitude(self):
		return self.lat
	def getLongitude(self):
		return self.lng
		
	def setLatitude(self,lat):
		self.lat = lat
		return self.lat
	def setLongitude(self,lng):
		self.lng = lng
		return self.lng
	
	def setmap(self):
		None

if __name__ == "__main__":
	loc = Location(48.858222, 2.2945)
	print(loc.getaddress())
	loc.setLatitude(-90)
	print(loc.getLatitude())
	print(loc.getaddress())