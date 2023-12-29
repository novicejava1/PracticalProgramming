#!/usr/bin/env python

class firstclass:
	def setData(self, value):
		self.data = value
	def display(self):
		print(self.data)

x = firstclass()
y = firstclass()

x.setData("Hello...")
y.setData("Python......")

x.display()
y.display()