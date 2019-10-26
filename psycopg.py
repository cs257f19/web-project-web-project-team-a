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

def getCoursePeriod(connection, coursePeriod):
	'''
	Returns a list of all of the coursees during the specified course period.

	PARAMETERS:
		period - the time period the user wants to find a course during

	RETURN:
		a list of all coursees during the period

	'''

def getCourseRequirements(connection, courseRequirements):
	'''
		Returns a list of all of the coursees during the specified course period.

		PARAMETERS:
			requirements - the requirement(s) the user wants the course to fulfill

		RETURN:
			a list of all coursees that fulfill the requirements

		'''

def getCourseTerm(connection, courseTerm):
	'''
	Returns a list of all coursees within the specified term.

	PARAMETERS:
		term - the term which the course is available

	RETURN:
		a list of all coursees within the specified term.

	'''
	try:
		cursor = connection.cursor()
		query = "SELECT	* FROM courses WHERE termsoffered LIKE '%" + courseTerm + "%' ORDER BY coursename DESC"
		cursor.execute(query)
		return cursor.fetchall()

	except Exception as e:
		print ("Something went wrong when executing the query: ", e)
		return None

def getCourseName(connection, courseName):
	'''
		Returns a list of all of the coursees the contain the course name from user input.

		PARAMETERS:
			name - course name that user inputed

		RETURN:
			a list of all coursees that contain that string

		'''
	try:
		cursor = connection.cursor()
		query = "SELECT	* FROM courses WHERE coursename LIKE '%" + courseName + "%' ORDER BY coursename DESC"
		cursor.execute(query)
		return cursor.fetchall()

	except Exception as e:
		print ("Something went wrong when executing the query: ", e)
		return None


def getCourseDeptTag(connection, courseDeptTag):
	'''
	Returns a list of all of the coursees within the specified subject.

	PARAMETERS:
		subject - the department the user wants to find a course in

	RETURN:
		a list of all coursees within the department

	'''
	try:
		cursor = connection.cursor()
		query = "SELECT	* FROM classes WHERE depttag LIKE '%" + courseDeptTag + "%'' ORDER BY coursename DESC"
		cursor.execute(query)
		return cursor.fetchall()

	except Exception as e:
		print ("Something went wrong when executing the query: ", e)
		return None


def getCourseNumber(connection, courseNumber):
	'''
	Returns a list of all coursees with the specified course number.

	PARAMETERS:
		courseNumber - the course number in which a course has

	RETURN:
		a list of all coursees withthe specified course number.

	'''
	try:
		cursor = connection.cursor()
		query = "SELECT	* FROM classes WHERE coursenum = " + str(courseNumber) + " ORDER BY coursename DESC"
		cursor.execute(query)
		return cursor.fetchall()

	except Exception as e:
		print ("Something went wrong when executing the query: ", e)
		return None


def main():
	user = 'ngot'
	password = getpass.getpass()

	# Connect to the database
	connection = connect(user, password)

	# Execute a simple query: What coursees are during the 2a block?
	
	#test queries 
	#results = getCourseNumber(connection, 250)
	#results = getCourseNumber(connection, 250)
	#results = getCourseDeptTag(connection, "ENGL")
	#results = getCourseTerm(connection, "Winter 2020")
	results = getCourseName(connection, "Data Structures")
	if results is not None:
		print("Query results: ")
		for item in results:
			print(item)

	# Disconnect from database
	connection.close()

main()
