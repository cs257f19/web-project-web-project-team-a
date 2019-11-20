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

	def __init__(self, dept, number, name, term, requirements, period, professor,):
		
		self.courseDeptTag = dept
		self.courseNumber = number
		self.courseName = name
		self.courseTerm = term
		self.courseRequirements = requirements
		self.coursePeriod = period
		self.courseProfessor = professor

		self.user = "ngot"
		self.password = "lamp792corn"
		self.connection = self.connect()

		self.QueryList =[self.getCourseByDeptTag(), self.getCourseByNumber(), self.getCourseByName(), self.getCourseByTerm(), self.getCourseByRequirements(), self.getCourseByPeriod(), self.getCourseByProfessor()]
		
	

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
		Returns a list of all of the coursees within the specified subject.

		PARAMETERS:
			connection - connection to database

		RETURN:
			a list of course objects within the department

		'''
		if self.courseDeptTag != None:
			query = "SELECT	* FROM classes WHERE UPPER(depttag) LIKE UPPER('%" + self.courseDeptTag + "%') "
			return query
		else:
			return None

		'''	
		try:
			cursor = self.connection.cursor()
			
			cursor.execute(query)
			courses = cursor.fetchall()
			courseResults = self.createCourse(courses)
			return courseResults

		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None
		'''

	def getCourseByNumber(self):
		'''
		Returns a list of all coursees with the specified course number.

		PARAMETERS:
			connection - connection to database

		RETURN:
			a list of course objects with the specified course number.

		'''
		if self.courseNumber != None:
			if self.courseNumber < 300:
				query = "SELECT	* FROM classes WHERE coursenum BETWEEN " + str(self.courseNumber) +  " AND " + str((self.courseNumber + 99)) 

			else:
				query = "SELECT	* FROM classes WHERE coursenum >= " + str(self.courseNumber)
			return query
		else:
			return None

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
		'''

	def getCourseByName(self):
		'''
			Returns a list of all of the coursees the contain the course name from user input.

			PARAMETERS:
				connection - connection to database

			RETURN:
				a list of course objects that contain that string

			'''

		if self.courseName != None:
			query = "SELECT	* FROM classes WHERE UPPER(coursename) LIKE UPPER('%" + self.courseName + "%') "
			return query
		else:
			return None

		'''
		try:
			cursor = self.connection.cursor()
			query = "SELECT	* FROM classes WHERE UPPER(coursename) LIKE UPPER('%" + self.courseName + "%') ORDER BY coursename DESC"
			cursor.execute(query)
			courses = cursor.fetchall()
			courseResults = self.createCourse(courses)
			return courseResults


		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None
		
		'''

	def getCourseByTerm(self):
		#if the length of list is longer than 1
		#call helper that union category
		if self.courseTerm != None:
			self.courseTerm = self.courseTerm.split("&")
			query = self.courseTerm[0]
			if len(self.courseTerm) > 1:
				for termIndex in range(1, len(self.courseTerm)):
					query = query + " UNION "+ self.getCourseByTermHelper(self.course[termIndex])
			return query
		else:
			return None

	def getCourseByTermHelper(self, term):
		'''
		Returns a list of all coursees within the specified term.

		PARAMETERS:
			connection - connection to database

		RETURN:
			a list of course objects within the specified term.

		'''

		query = "SELECT	* FROM classes WHERE UPPER(termsoffered) LIKE UPPER('%" + term + "%') "
		return query
		

		'''
		try:
			cursor = self.connection.cursor()
			query = "SELECT	* FROM classes WHERE UPPER(termsoffered) LIKE UPPER('%" + self.courseTerm + "%') ORDER BY coursename DESC"
			cursor.execute(query)
			courses = cursor.fetchall()
			courseResults = self.createCourse(courses)
			return courseResults

		except Exception as e:
			print("Something went wrong when executing the query: ", e)
			return None
		''' 

	def getCourseByRequirements(self):

		if self.courseRequirements != None:
			self.courseRequirements = self.courseRequirements.split("&")
			query = self.courseRequirements[0]
			if len(self.courseRequirements) > 1:
				for reqIndex in range(1, len(self.courseRequirements)):
					query = query + " UNION "+ self.getCourseByRequirementsHelper(self.courseRequirements[reqIndex])
			return query
		else:
			return None

	def getCourseByRequirementsHelper(self, requirements):
		'''
			Returns a list of all of the coursees during the specified course period.

			PARAMETERS:
				connection - connection to database

			RETURN:
				a list of course objects that fulfill the requirements

		'''
		#if self.courseRequirements != None:
		query = "SELECT	* FROM classes WHERE UPPER(reqsFilled) LIKE UPPER('%" + requirements + "%') "
		return query
		#else:
		#	return None

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
		'''
	def getCourseByPeriod(self):

		if self.coursePeriod != None:
			self.coursePeriod = self.coursePeriod.split("&")
			query = self.coursePeriod[0]
			if len(self.coursePeriod) > 1:
				for periodIndex in range(1, len(self.coursePeriod)):
					query = query + " UNION "+ self.getCourseByPeriodHelper(self.coursePeriod[periodIndex])
			return query
		else:
			return None

	def getCourseByPeriodHelper(self, period):
		'''
		Returns a list of all of the coursees during the specified course period.

		PARAMETERS:
			connection - connection to database

		RETURN:
			a list of course objects during the period

		'''
		#if self.coursePeriod != None:
		query = "SELECT	* FROM classes WHERE classperiod LIKE '%" + str(period) + "%' "
		return query
		#else:
		#	return None

	def getCourseByProfessor(self):
		'''
			Returns a list of all of the courses that is taught by a specific professor.

			PARAMETERS:
				connection - connection to database

			RETURN:
				a list of course objects that contain that specific professor

			'''
		if self.courseProfessor != None:
			query = "SELECT	* FROM classes WHERE UPPER(professor) LIKE UPPER('%" + self.courseProfessor + "%') "
			return query
		else:
			return None

		'''
		try:
			cursor = self.connection.cursor()
			query = "SELECT	* FROM classes WHERE UPPER(professor) LIKE UPPER('%" + self.courseProfessor + "%') ORDER BY coursename DESC"
			cursor.execute(query)
			courses = cursor.fetchall()
			courseResults = self.createCourse(courses)
			return courseResults


		except Exception as e:
			print ("Something went wrong when executing the query: ", e)
			return None
		'''

	def masterQuery(self):
		
		'''
		Takes checks all query parameters and creates a query compiled of the intersects of all th queries

		PARAMETERS:
			connection - connection to database

		RETURN:
			a list of course objects which satifies all criteria

		'''

		try:

			masterQuery = "SELECT	* FROM classes "

			for i in range(len(self.QueryList)):

				if i < (len(self.QueryList)-1):
					if self.QueryList[i] != None:
						masterQuery = masterQuery + " INTERSECT " + self.QueryList[i]
				else:
					if self.QueryList[i] != None:
						masterQuery = masterQuery + " INTERSECT " + self.QueryList[i]

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
	
	# (dept, number, name, term, requirements, period, professor, description):
	# Initialize query object and test queries
	#query = CourseQuery("AFST", None, None, None, None, None, None)
	query = CourseQuery("AFST", 100, None, "Fall 2019&Winter 2020", None, None, None)
	#query = CourseQuery("AFST", 100, None, "Winter 2020", None, None, None)
	#query = CourseQuery(None, None, None, None, "FSR", None, None)

	#test queries
	#results = query.getCourseByName()
	#results = query.getCourseByDeptTag()
	#results = query.getCourseByTerm()
	#results = query.getCourseByNumber()
	results = query.masterQuery()

	if results is not None:
		print("Query results: ")
		for item in results:
			item.printCourseInfo()

	# Disconnect from database
	query.connection.close()

	
main()
