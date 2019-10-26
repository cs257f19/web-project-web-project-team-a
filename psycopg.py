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

def getClassPeriod(connection, classPeriod):
	'''
	Returns a list of all of the classes during the specified class period.

	PARAMETERS:
		period - the time period the user wants to find a class during

	RETURN:
		a list of all classes during the period

	'''

def getClassTerm(connection, classTerm):
	'''
	Returns a list of all classes within the specified term.

	PARAMETERS:
		term - the term which the class is available

	RETURN:
		a list of all classes within the specified term.

	'''
	try:
		cursor = connection.cursor()
		query = "SELECT	* FROM classes WHERE term LIKE " + %classTerm% + " ORDER BY name DESC"
		cursor.execute(query)
		return cursor.fetchall()

	except Exception as e:
		print ("Something went wrong when executing the query: ", e)
		return None


def getClassSubject(connection, classSubject):
	'''
	Returns a list of all of the classes within the specified subject.

	PARAMETERS:
		subject - the department the user wants to find a class in

	RETURN:
		a list of all classes within the department

	'''
	try:
		cursor = connection.cursor()
		query = "SELECT	* FROM classes WHERE subject = " + classSubject + " ORDER BY name DESC"
		cursor.execute(query)
		return cursor.fetchall()

	except Exception as e:
		print ("Something went wrong when executing the query: ", e)
		return None



def getClassRequirements(connection, classRequirements):
	'''
		Returns a list of all of the classes during the specified class period.

		PARAMETERS:
			requirements - the requirement(s) the user wants the class to fulfill

		RETURN:
			a list of all classes that fulfill the requirements

		'''

def getClassName(connection, className):
	'''
		Returns a list of all of the classes the contain the class name from user input.

		PARAMETERS:
			name - class name that user inputed

		RETURN:
			a list of all classes that contain that string

		'''
	try:
		cursor = connection.cursor()
		query = "SELECT	* FROM classes WHERE name = " + className + " ORDER BY name DESC"
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

	# Execute a simple query: What classes are during the 2a block?
	#results = getClassPeriod(connection, 2)
	results = getClassTerm(connection, "Winter 2020")
	if results is not None:
		print("Query results: ")
		for item in results:
			print(item)

	# Disconnect from database
	connection.close()

main()
