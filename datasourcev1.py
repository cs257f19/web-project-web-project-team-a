#authors: Ben Preiss, Cam Brown, Tony Ngo
#date: 22 October 2019


import psycopg
import getpass


class DataSource:
	'''
	DataSource executes all of the queries on the database.
	It also formats the data to send back to the frontend, typically in a list
	or some other collection or object.
	'''

    def __init__(self, term, subject, credits, requirements, classPeriod):
		self.term = term;
		self.subject = subject;
		self.requirements = requirements;
		self.credits = credits;
		self.classPeriod = classPeriod


	def getClassTerm(self, term):
		'''
		Returns a list of all classes within the specified term.

		PARAMETERS:
			term - the term which the class is available

		RETURN:
			a list of all classes within the specified term.

		'''
		return[]

	def getClassSubject(self, subject):
		'''
		Returns a list of all of the classes within the specified subject.

		PARAMETERS:
			subject - the department the user wants to find a class in

		RETURN:
			a list of all classes within the department

		'''

		return[]

	def getClassCredits(self, term):
		'''
		Returns a list of all classes that have correct amount of credits.

		PARAMETERS:
			credits - the amount of credits that a class has

		RETURN:
			a list of all classes that have the correct amount of credits

		'''

		return []

	def getClassPeriod(self, period):
		'''
		Returns a list of all of the classes during the specified class period.

		PARAMETERS:
			period - the time period the user wants to find a class during

		RETURN:
			a list of all classes during the period

		'''
		return []

	def getClassRequirements(self, requirements):
		'''
		Returns a list of all of the classes during the specified class period.

		PARAMETERS:
			requirements - the requirement(s) the user wants the class to fulfill

		RETURN:
			a list of all classes that fulfill the specified requirement

		'''
		return []








	#returns all classes in department above this department level

	#returns all classes within a department within a class period

	#return all classes that meet a certain requirement

	#
