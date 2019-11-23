'''
datasource.py

Code containing query object as well as methods that allow for queries

author: Tony Ngo, Ben Preiss, Cam Brown
date: 22 October 2019
Adapted some from code originally written by Jeff Ondich
'''

import psycopg2
import getpass
from CourseObj import*



class CourseQuery:
	'''
		object that when created will contain all criteria from a single user query
	'''

	def __init__(self, dept, number, name, term, requirements, period):
		
		self.courseDeptTag = dept
		self.courseNumber = number
		self.courseName = name
		self.courseTerm = term
		self.courseRequirements = requirements
		self.coursePeriod = period

		self.user = "ngot"
		self.password = "lamp792corn"
		self.connection = self.connect()

		self.QueryList =[self.getCourseByDeptTag(), self.getCourseByNumber(), self.getCourseByName(), self.getCourseByTerm(),
						 self.getCourseByRequirements(), self.getCourseByPeriod()]
		
	

	def createCourseList(self, courses):
		'''
		Helper method that takes in a list of courses in the form of tuples
		and creates a CourseObj for each course in the list

		PARAMETERS:
		courses - lists of tuples for courses

		Returns: 
		a new list of CourseObj objects
		'''
		courseList =[]
		for course in courses:
			courseObj = CourseObj(course)
			courseList.append(courseObj)
			
		return courseList
	
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
			exit()
		return connection

	def getCourseByDeptTag(self):
		'''
		Returns a query string for retrieving courses by department tag

		PARAMETERS:
			none

		RETURN:
			a query string for courses by department tag

		'''
		if self.courseDeptTag != None:
			query = "SELECT	* FROM classes WHERE UPPER(depttag) = UPPER('" + self.courseDeptTag + "') "
			return query
		else:
			return None


	def getCourseByNumber(self):
		'''
		Returns a query string for retrieving courses by course number

		PARAMETERS:
			none

		RETURN:
			a query string for courses by course number

		'''
		if self.courseNumber != None:
			self.courseNumber = int(self.courseNumber)
			if int(self.courseNumber) < 300:
				query = "SELECT	* FROM classes WHERE coursenum BETWEEN " + str(self.courseNumber) +  " AND " + str((self.courseNumber + 99)) 

			else:
				query = "SELECT	* FROM classes WHERE coursenum >= " + str(self.courseNumber)
			return query
		else:
			return None

	def getCourseByName(self):
		'''
		Returns a query string for retrieving courses by course name

		PARAMETERS:
			none

		RETURN:
			a query string for courses by course name

		'''

		if self.courseName != None:
			query = "SELECT	* FROM classes WHERE UPPER(coursename) LIKE UPPER('%" + self.courseName + "%') "
			return query
		else:
			return None


	def getCourseByTerm(self):
		'''
		Returns a combined query string for retrieving courses by course term  

		PARAMETERS:
			none

		RETURN:
			a query string for courses by course term(s)

		'''
		if self.courseTerm != None:
			self.courseTerm = self.courseTerm.split("&")
			query =  "SELECT * FROM classes WHERE UPPER(termsoffered) LIKE UPPER('%" + self.courseTerm[0] + "%') "
			query = self.getCourseByTermHelper(self.courseTerm[0])

			for termIndex in range(1, len(self.courseTerm)):
				query = query + " OR UPPER(termsoffered) LIKE UPPER('%" + self.courseTerm[termIndex] + "%') "
			return query
		else:
			return None


	def getCourseByRequirements(self):
		'''
		Returns a combined query string for retrieving courses by course requirements  

		PARAMETERS:
			none

		RETURN:
			a query string for courses by course requirement(s)

		'''

		if self.courseRequirements != None:
			self.courseRequirements = self.courseRequirements.split("&")
			query = "SELECT	* FROM classes WHERE UPPER(reqFilled) LIKE UPPER('%" + self.courseRequirements[0] + "%') "

			for reqIndex in range(1, len(self.courseRequirements)):
				query = query + " OR UPPER(reqFilled) LIKE UPPER('%" + self.courseRequirements[reqIndex] + "%') "
				
			return query
		else:
			return None


	def getCourseByPeriod(self):
		'''
		Returns a combined query string for retrieving courses by course period  

		PARAMETERS:
			none

		RETURN:
			a query string for courses by course periods(s)

		'''

		if self.coursePeriod != None:
			self.coursePeriod = self.coursePeriod.split("&")
			query = "SELECT	* FROM classes WHERE UPPER(classperiod) LIKE UPPER('%" + coursePeriod[0] + "%') "

			for periodIndex in range(1, len(self.coursePeriod)):
				query = query + " OR UPPER(classperiod) LIKE UPPER('%" + self.coursePeriod[periodIndex] + "%') "
			return query
		else:
			return None

	def masterQuery(self):
		'''
		Takes checks all query parameters from QueryList list and creates a query string 
		compiled of the intersects of all queries

		PARAMETERS:
			connection - connection to database

		RETURN:
			a list of course objects which satifies all criteria

		'''

		try:
			masterQuery = "Select * FROM classes"
			for queryItem in range(len(self.QueryList)):	
				if queryItem < (len(self.QueryList)-1):
					if self.QueryList[queryItem] != None:
						if queryItem == 0:
							masterQuery = self.QueryList[queryItem]
						else:	
							masterQuery = masterQuery + " INTERSECT " + self.QueryList[queryItem]
				else:
					if self.QueryList[queryItem] != None:
						
						masterQuery = masterQuery + " INTERSECT " + self.QueryList[queryItem]

			masterQuery = masterQuery + " ORDER BY coursenum ASC "

			cursor = self.connection.cursor()
			cursor.execute(masterQuery)
			courses = cursor.fetchall()
			courseList = self.createCourseList(courses)	
			return courseList

		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None


def main():
	'''
	order of items in query object
	(dept, number, name, term, requirements, period):

	# Initialize query object and test queries
	query = CourseQuery(None, None, "data", None, None, None)
	query = CourseQuery(None, 100, None, None, None, None)
	query = CourseQuery("AFST", 100, None, "Fall 2019", None,"2a&5a")
	query = CourseQuery(None, None, None, None, "FSR", None)

	results = query.masterQuery()

	if results is not None:
		print("Query results: ")
		for item in results:
			item.printCourseInfo()

	# Disconnect from database
	query.connection.close()
	
	'''
main()
