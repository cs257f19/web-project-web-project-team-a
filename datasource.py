'''
datasource.py

Code containing query object as well as methods that allow for queries

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


	def getCourseNumber(self, connection):
		'''
		Returns a list of all coursees with the specified course number.

		PARAMETERS:
			connection - connection to database

		RETURN:
			a list of all courses withthe specified course number.

		'''
		try:
			cursor = connection.cursor()
			query = "SELECT	* FROM classes WHERE coursenum = " + str(self.courseNumber) + " ORDER BY coursename DESC"
			cursor.execute(query)
			return cursor.fetchall()

		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None

	

	def getCourseDeptTag(self, connection):
		'''
		Returns a list of all of the coursees within the specified subject.

		PARAMETERS:
			connection - connection to database

		RETURN:
			a list of all courses within the department

		'''
		try:
			cursor = connection.cursor()
			query = "SELECT	* FROM classes WHERE depttag LIKE '%" + self.courseDeptTag + "%' ORDER BY coursename DESC"
			cursor.execute(query)
			return cursor.fetchall()

		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None

	def getCourseName(self, connection):
		'''
			Returns a list of all of the coursees the contain the course name from user input.

			PARAMETERS:
				connection - connection to database

			RETURN:
				a list of all courses that contain that string

			'''
		try:
			cursor = connection.cursor()
			query = "SELECT	* FROM classes WHERE coursename LIKE '%" + self.courseName + "%' ORDER BY coursename DESC"
			cursor.execute(query)
			return cursor.fetchall()

		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None

	def getCourseNumber(self, connection):
		'''
		Returns a list of all coursees with the specified course number.

		PPARAMETERS:
			connection - connection to database

		RETURN:
			a list of all courses withthe specified course number.

		'''
		try:
			cursor = connection.cursor()
			query = "SELECT	* FROM classes WHERE coursenum = " + str(self.courseNumber) + " ORDER BY coursename DESC"
			cursor.execute(query)
			return cursor.fetchall()

		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None

	def getCoursePeriod(self, connection):
		'''
		Returns a list of all of the coursees during the specified course period.

		PARAMETERS:
			connection - connection to database

		RETURN:
			a list of all courses during the period

		'''

	def getCourseRequirements(self, connection):
		'''
			Returns a list of all of the coursees during the specified course period.

			PARAMETERS:
				connection - connection to database

			RETURN:
				a list of all courses that fulfill the requirements

			'''

	def getCourseTerm(self, connection):
		'''
		Returns a list of all coursees within the specified term.

		PARAMETERS:
			connection - connection to database

		RETURN:
			a list of all courses within the specified term.

		'''
		try:
			cursor = connection.cursor()
			query = "SELECT	* FROM classes WHERE termsoffered LIKE '%" + self.courseTerm + "%' ORDER BY coursename DESC"
			cursor.execute(query)
			return cursor.fetchall()

		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None
	def masterQuery(self,connection):
		'''
		Takes checks all query parameters and creates a query compiled of the intersects of all th queries

		PARAMETERS:
			connection - connection to database

		RETURN:
			a list of all course which satifies all criteria

		'''

def main():
	user = 'ngot'
	password = getpass.getpass()
	 
	# Connect to the database
	connection = connect(user, password)

	# Initialize query object and test queries
	query = courseQuery("ENGL", 251, "Data Structures", "Winter 2020", None, None)

	results = query.getCourseName(connection)
	#results = query.getCourseDeptTag(connection)
	#results = query.getCourseTerm(connection)
	#results = query.getCourseNumber(connection)

	if results is not None:
		print("Query results: ")
		for item in results:
			print(item)

	# Disconnect from database
	connection.close()

main()
