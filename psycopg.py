'''
psycopg2-test.py

Sample code demonstrating how to use the psycopg2 Python library to connect
to a database and execute a query.

author: Tony Ngo, Ben Preiss, Cam Brown
date: 22 October 2019
Adapted from code originally written by Jeff Ondich
'''

import psycopg2
import getpass

def connect(user, password):
		'''
		Establishes a connection to the database with the following credentials:
			user - username, which is also the name of the database
			password - the password for this database on perlman

		Returns: a database connection.

		Note: exits if a connection cannot be established.
		'''
		try:
			connection = psycopg2.connect(database=user, user=user, password=password)
		except Exception as e:
			print("Connection error: ", e)
			exit()
		return connection


class courseQuery:
	'''
		object that when created will contain all criteria from a single user quiery
	'''

	def __init__(self, dept, number, name, term, requirements, period):
		self.courseTerm = term
		self.courseNumber = number
		self.courseName = name
		self.courseDeptTag = dept
		self.courseRequirements = requirements
		self.coursePeriod = period
		self.connect


	def getCourseNumber(self):
		'''
		Returns a list of all coursees with the specified course number.

		PARAMETERS:
			courseNumber - the course number in which a course has

		RETURN:
			a list of all coursees withthe specified course number.

		'''
		try:
			cursor = connection.cursor()
			query = "SELECT	* FROM classes WHERE coursenum = " + str(self.courseNumber) + " ORDER BY coursename DESC"
			cursor.execute(query)
			return cursor.fetchall()

		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None

	

	def getCourseDeptTag(self):
		'''
		Returns a list of all of the coursees within the specified subject.

		PARAMETERS:
			subject - the department the user wants to find a course in

		RETURN:
			a list of all coursees within the department

		'''
		try:
			cursor = connection.cursor()
			query = "SELECT	* FROM classes WHERE depttag LIKE '%" + self.courseDeptTag + "%'' ORDER BY coursename DESC"
			cursor.execute(query)
			return cursor.fetchall()

		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None

	def getCourseName(self):
		'''
			Returns a list of all of the coursees the contain the course name from user input.

			PARAMETERS:
				name - course name that user inputed

			RETURN:
				a list of all coursees that contain that string

			'''
		try:
			cursor = connection.cursor()
			query = "SELECT	* FROM classes WHERE coursename LIKE '%" + self.courseName + "%' ORDER BY coursename DESC"
			cursor.execute(query)
			return cursor.fetchall()

		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None

	def getCourseNumber(self):
		'''
		Returns a list of all coursees with the specified course number.

		PARAMETERS:
			courseNumber - the course number in which a course has

		RETURN:
			a list of all coursees withthe specified course number.

		'''
		try:
			cursor = connection.cursor()
			query = "SELECT	* FROM classes WHERE coursenum = " + str(self.courseNumber) + " ORDER BY coursename DESC"
			cursor.execute(query)
			return cursor.fetchall()

		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None

	def getCoursePeriod(self):
		'''
		Returns a list of all of the coursees during the specified course period.

		PARAMETERS:
			period - the time period the user wants to find a course during

		RETURN:
			a list of all coursees during the period

		'''

	def getCourseRequirements(self):
		'''
			Returns a list of all of the coursees during the specified course period.

			PARAMETERS:
				requirements - the requirement(s) the user wants the course to fulfill

			RETURN:
				a list of all coursees that fulfill the requirements

			'''

	def getCourseTerm(self):
		'''
		Returns a list of all coursees within the specified term.

		PARAMETERS:
			term - the term which the course is available

		RETURN:
			a list of all coursees within the specified term.

		'''
		try:
			cursor = connection.cursor()
			query = "SELECT	* FROM classes WHERE termsoffered LIKE '%" + self.courseTerm + "%' ORDER BY coursename DESC"
			cursor.execute(query)
			return cursor.fetchall()

		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None





def main():
	#user = 'ngot'
	#password = getpass.getpass()
	 
	# Connect to the database
	connection = connect(user, password)
	# Query object and test queries
	query = courseQuery(ENGL, 251, "Data Structures", "Winter 2020", None, None)
	#connection = query.connect()

	results = query.getCourseName()
	#results = query.getCourseDeptTag()
	#results = query.getCourseTerm()
	#results = query.getCourseNumber()

	if results is not None:
		print("Query results: ")
		for item in results:
			print(item)

	# Disconnect from database
	connetion.close()

main()
