# Under construction
# variable g accorgint to height 
# show variable velocity per millisecond as the person is falling from a given height
import time
from scipy import constants

class Planet:
	def get_g(self):
		return self.g

class Earth(Planet):
	name = "Earth"
	g = 9.8
	R = constants.G

class Person():
	planet = Earth()
	def __init__(self,name,age,weight):
		self.name = name
		self.age = age
		self.weight = weight

	def _get_weight(self):
		return self.weight

	def get_mass(self):
		return self.planet.g * self.weight		


import pdb;pdb.set_trace()

# def get_g():
# 	pass




# for i in range(101):
# 	b = "Loading {} %".format(i)
	
	# print(b,end='\r')
	# time.sleep(0.02)