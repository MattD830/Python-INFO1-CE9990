"""
This program scrapes latitude and longitude from the web and returns information about it
"""

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
		"""
		Returns basic information
		"""
		if self.lat >= 0:
			if self.lng >= 0:
				return ('+self.north()+', '+self.east()+')'
			else:
				return ('+self.north()+', '+self.west()+')'
		else:
			if self.lng >= 0:
				return ('+self.south()+', '+self.east()+')'
			else:
				return ('+self.south()+', '+self.west()+')'
		
	def getZipcode(self):
		"""
		Returns the zip code
		"""
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
		"""
		Scrapes the required data from the web
		"""
		self.url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}'.format(self.lat,self.lng)
		self.mapf = json.loads(ur.urlopen(self.url).read())
		return self.mapf
		
	def north(self):
		"""
		Appends directional notion
		"""
		return str(self.lat)+'°N'
	def south(self):
                """
                Appends directional notion
                """
		return str(self.lat)+'°S'
		
	def east(self):
                """
                Appends directional notion
                """
		return str(self.lng)+'°E'
	def west(self):
                """
                Appends directional notion
                """
		return str(self.lng)+'°W'
		
	def getLatitude(self):
		"""
		Returns the latitude of the object
		"""
		return self.lat
	def getLongitude(self):
		"""
		Returns the longitude of the object
		"""
		return self.lng
		
	def setLatitude(self,lat):
		"""
		Converts the input into the latitude object
		"""
		self.lat = lat
		return self.lat
	def setLongitude(self,lng):
		"""
		Converts the input into the longitude object
		"""
		self.lng = lng
		return self.lng
	
	def setmap(self):
		"""
		This does nothing
		"""
		None

if __name__ == "__main__":
	loc = Location(48.858222, 2.2945)
	print(loc)
	loc.setLatitude(-90)
	print(loc.getLatitude())
