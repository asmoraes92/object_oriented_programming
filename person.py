from datetime import datetime

class Person:

	current_year = int(datetime.strftime(datetime.now(), '%Y'))

	def __init__(self,name,age,gender,eating=False,talking=False):
		self.name = name
		self.age = age
		self.gender = gender
		self.eating = eating
		self.talking = talking

		if self.gender == 'male':
			self.subject_pronoun = 'he'
			self.object_pronoun = 'him'
			self.possessive_adjective = 'his'
			self.possessive_pronoun = 'his'
		elif self.gender == 'female':
			self.subject_pronoun = 'she'
			self.object_pronoun = 'her'
			self.possessive_adjective = 'her'
			self.possessive_pronoun = 'hers'
		else:
			raise AttributeError('This is only a simple test, therefore, gender must be "male" or "female".')

	def talk(self,subject):
		if self.eating:
			print(f"{self.name} can't talk because {self.subject_pronoun} is eating.")
		elif self.talking:
			print(f"{self.name} is already talking.")
		else:
			print(f'{self.name} is talking about {subject}.')
			self.talking = True

	def stop_talking(self):
		self.talking = False

	def eat(self,food):
		if self.talking:
			print(f"{self.name} can't eat because {self.subject_pronoun} is talking.")
		elif self.eating:
			print(f"{self.name} is already eating.")
		else:
			print(f'{self.name} is eating {food}.')
			self.eating = True

	def stop_eating(self):
		self.eating = False

	def was_born_in(self):
		return self.current_year - self.age