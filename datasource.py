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




class CourseQuery:
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
		
	def createCourse(self, courses):
		'''
		Helper method that takes in a list of courses in the form of tuples
		and creates a CourseObj for each course in the list

		PARAMETERS:
			courses - lists of tuples for courses

		Returns: 
			a new list of CourseObj objects
		'''
		courseResults =[]
		for course in courses:
			courseObj = CourseObj(course)
			courseResults.append(courseObj)
		return courseResults
	
	def connect(self):	
		'''
		Establishes a connection to the database with the following credentials:
			user - username, which is also the name of the database
			password - the password for this database on perlman

		Returns: 
			a database connection.

		Note: exits if a connection cannot be established.
		'''

		try:
			connection = psycopg2.connect(database= self.user, user=self.user, password=self.password)
		except Exception as e:
			print("Connection error: ", e)
			exit()result = ds[0]
		return connection

	
	def getCourseByNumber(self):
		'''
		Returns a list of all coursees with the specified course number.

		PARAMETERS:
			connection - connection to database

		RETURN:
			a list of course objects with the specified course number.

		'''
		try:
			cursor = self.connection.cursor()
			query = "SELECT	* FROM classes WHERE coursenum = " + str(self.courseNumber) + " ORDER BY coursename DESC"
			cursor.execute(query)
			courses = cursor.fetchall()
			courseResults = self.createCourse(courses)
			return courseResults

		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None

	

	def getCourseByDeptTag(self):
		'''
		Returns a list of all of the coursees within the specified subject.

		PARAMETERS:
			connection - connection to database

		RETURN:
			a list of course objects within the department

		'''
		try:
			cursor = self.connection.cursor()
			query = "SELECT	* FROM classes WHERE depttag LIKE '%" + self.courseDeptTag + "%' ORDER BY coursename DESC"
			cursor.execute(query)
			courses = cursor.fetchall()
			courseResults = self.createCourse(courses)
			return courseResults

		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None

	def getCourseByName(self):
		'''
			Returns a list of all of the coursees the contain the course name from user input.

			PARAMETERS:
				connection - connection to database

			RETURN:
				a list of course objects that contain that string

			'''
		try:
			cursor = self.connection.cursor()
			query = "SELECT	* FROM classes WHERE coursename LIKE '%" + self.courseName + "%' ORDER BY coursename DESC"
			cursor.execute(query)
			courses = cursor.fetchall()
			courseResults = self.createCourse(courses)
			return courseResults


		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None

	def getCourseByPeriod(self):
		'''
		Returns a list of all of the coursees during the specified course period.

		PARAMETERS:
			connection - connection to database

		RETURN:
			a list of course objects during the period

		'''

	def getCourseByRequirements(self):
		'''
			Returns a list of all of the coursees during the specified course period.

			PARAMETERS:
				connection - connection to database

			RETURN:
				a list of course objects that fulfill the requirements

		'''
		try:
			cursor = self.connection.cursor()
			query = "SELECT	* FROM classes WHERE reqsFilled LIKE '%" + self.courseRequirements + "%' ORDER BY coursename DESC"
			cursor.execute(query)
			courses = cursor.fetchall()
			courseResults = self.createCourse(courses)
			return courseResults

		except Exception as e:
			print("Something went wrong when executing the query: ", e)
			return None

	def getCourseByTerm(self):
		'''
		Returns a list of all coursees within the specified term.

		PARAMETERS:
			connection - connection to database

		RETURN:
			a list of course objects within the specified term.

		'''
		try:
			cursor = self.connection.cursor()
			query = "SELECT	* FROM classes WHERE termsoffered LIKE '%" + self.courseTerm + "%' ORDER BY coursename DESC"
			cursor.execute(query)
			courses = cursor.fetchall()
			courseResults = self.createCourse(courses)
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
			a list of course objects which satifies all criteria

		'''

def main():
	

	# Initialize query object and test queries
	#query = CourseQuery("ENGL", 251, "Data Structures", "Winter 2020", None, None)

	#test queries
	#results = query.getCourseByName()
	#results = query.getCourseByDeptTag()
	#results = query.getCourseByTerm()
	'''
	results = query.getCourseByNumber()

	if results is not None:
		print("Query results: ")
		for item in results:
			item.printCourseInfo()

	# Disconnect from database
	query.connection.close()
	'''
main()
