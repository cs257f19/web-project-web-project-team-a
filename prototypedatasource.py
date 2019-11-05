'''
prototypedatasrouce.py

Code containing query object as well as methods that allow for queries

author: Tony Ngo, Ben Preiss, Cam Brown
date: 22 October 2019
Adapted from code originally written by Jeff Ondich
'''

import psycopg2
import getpass
from CourseObj import*




class courseQuery:
	'''
		object that when created will contain all criteria from a single user query
	'''

	def __init__(self, dept, number, name, term, requirements, period):
		self.courseTerm = term
		self.courseNumber = number
		self.courseName = name
		self.courseDeptTag = dept
		self.courseRequirements = requirements
		self.coursePeriod = period
		self.user = "ngot"
		self.password = "lamp792corn"
		self.connection = self.connect()
		
	def create(self, courses):
		print("hit3")
		courseResults =[]
		print(courses)
		for course in courses:
			print("hit8")
			courseObj = CourseObj(course)
			courseResults.append(courseObj)
		return courseResults
	
	def connect(self):
		
		'''
		Establishes a connection to the database with the following credentials:
			user - username, which is also the name of the database
			password - the password for this database on perlman

		Returns: a database connection.

		Note: exits if a connection cannot be established.
		'''

		try:
			connection = psycopg2.connect(database= self.user, user=self.user, password=self.password)
		except Exception as e:
			print("Connection error: ", e)
			exit()
		return connection

	
	def getCourseNumber(self):
		'''
		Returns a list of all coursees with the specified course number.

		PARAMETERS:
			connection - connection to database

		RETURN:
			a list of all courses withthe specified course number.

		'''
		print("hit7")
		try:
			cursor = self.connection.cursor()
			print("hit6")
			query = "SELECT	* FROM classes WHERE coursenum = " + str(self.courseNumber) + " ORDER BY coursename DESC"
			cursor.execute(query)
			print("hit4")
			courses = cursor.fetchall()
			self.create(courses)
			print("hit5")
			return courseResults

		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None

	

	def getCourseDeptTag(self):
		'''
		Returns a list of all of the coursees within the specified subject.

		PARAMETERS:
			connection - connection to database

		RETURN:
			a list of all courses within the department

		'''
		try:
			cursor = self.connection.cursor()
			query = "SELECT	* FROM classes WHERE depttag LIKE '%" + self.courseDeptTag + "%' ORDER BY coursename DESC"
			cursor.execute(query)
			create(cursor.fetchall())
			return courseResults

		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None

	def getCourseName(self):
		'''
			Returns a list of all of the coursees the contain the course name from user input.

			PARAMETERS:
				connection - connection to database

			RETURN:
				a list of all courses that contain that string

			'''
		try:
			cursor = self.connection.cursor()
			query = "SELECT	* FROM classes WHERE coursename LIKE '%" + self.courseName + "%' ORDER BY coursename DESC"
			cursor.execute(query)
			create(cursor.fetchall())
			return courseResults


		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None

	def getCoursePeriod(self):
		'''
		Returns a list of all of the coursees during the specified course period.

		PARAMETERS:
			connection - connection to database

		RETURN:
			a list of all courses during the period

		'''

	def getCourseRequirements(self):
		'''
			Returns a list of all of the coursees during the specified course period.

			PARAMETERS:
				connection - connection to database

			RETURN:
				a list of all courses that fulfill the requirements

		'''
		try:
			cursor = self.connection.cursor()
			query = "SELECT	* FROM classes WHERE reqsFilled LIKE '%" + self.courseRequirements + "%' ORDER BY coursename DESC"
			cursor.execute(query)
			create(cursor.fetchall())
			return courseResults

		except Exception as e:
			print("Something went wrong when executing the query: ", e)
			return None

	def getCourseTerm(self):
		'''
		Returns a list of all coursees within the specified term.

		PARAMETERS:
			connection - connection to database

		RETURN:
			a list of all courses within the specified term.

		'''
		try:
			cursor = self.connection.cursor()
			query = "SELECT	* FROM classes WHERE termsoffered LIKE '%" + self.courseTerm + "%' ORDER BY coursename DESC"
			cursor.execute(query)
			create(cursor.fetchall())
			return courseResults

		except Exception as e:
			print("Something went wrong when executing the query: ", e)
			return None
	def masterQuery(self):
		'''
		Takes checks all query parameters and creates a query compiled of the intersects of all th queries

		PARAMETERS:
			connection - connection to database

		RETURN:
			a list of all course which satifies all criteria

		'''

def main():
	

	# Initialize query object and test queries
	query = courseQuery("ENGL", 251, "Data Structures", "Winter 2020", None, None)

	#results = query.getCourseName()
	#results = query.getCourseDeptTag(connection)
	#results = query.getCourseTerm(connection)
	print("hit1")
	results = query.getCourseNumber()
	print("hit2")
	if results is not None:
		print("Query results: ")
		for item in results:
			print(item)

	# Disconnect from database
	query.connection.close()

main()
