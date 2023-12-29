#!/usr/bin/env python

class firstclass:
	def setData(self, value):
		self.data = value
	def display(self):
		print(self.data)

class secondclass(firstclass):
	def display(self):
		print(str(self.data) + "_override")

x = secondclass()
y = secondclass()

x.setData("Python")
x.display()
y.setData(43)
y.display()