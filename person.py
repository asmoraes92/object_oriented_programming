from datetime import datetime

class Person:

	current_year = int(datetime.strftime(datetime.now(), '%Y'))

	def __init__(self,name,age,eating=False,talking=False):
		self.name = name
		self.age = age
		self.eating = eating
		self.talking = talking

	def talk(self,subject):
		if self.eating:
			print(f"{self.name} can't talk while eating.")
		elif self.talking:
			print(f"{self.name} is already talking.")
		else:
			print(f'{self.name} is talking about {subject}.')
			self.talking = True

	def stop_talking(self):
		self.talking = False

	def eat(self,food):
		if self.talking:
			print(f"{self.name} can't eat while talking.")
		elif self.eating:
			print(f"{self.name} is already eating.")
		else:
			print(f'{self.name} is eating {food}.')
			self.eating = True

	def stop_eating(self):
		self.eating = False

	def was_born_in(self):
		return self.current_year - self.age