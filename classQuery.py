  
class classQuery:

  def __init__(self, term, name, subject, credits, requirements, classPeriod):
		self.term = term;
		self.name = name;
		self.subject = subject;
		self.requirements = requirements;
		self.credits = credits;
		self.classPeriod = classPeriod

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
	query = "SELECT	* FROM classes WHERE termsoffered LIKE '%" + courseTerm + "%' ORDER BY coursename DESC"
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
		
def getClassPeriod(connection, classPeriod):
	'''
	Returns a list of all of the classes during the specified class period.

	PARAMETERS:
		period - the time period the user wants to find a class during

	RETURN:
		a list of all classes during the period

	'''
	try:
		cursor = connection.cursor()
		query = "SELECT	* FROM classes WHERE period = " + str(classPeriod) + " ORDER BY name DESC"
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
		query = "SELECT	* FROM classes WHERE subject = " + str(classSubject) + " ORDER BY name DESC"
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
	intersectQuery = "SELECT * FROM classes"

	for requirement in classRequirements:
		try:
			cursor = connection.cursor()
			intersectQuery =  intersectQuery + "INTERSECT" +  "SELECT	* FROM classes WHERE requirements LIKE " + requirement + " ORDER BY name DESC"

	try:
		cursor.execute(intersectQuery)
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
		query = "SELECT	* FROM classes WHERE coursename LIKE '%" + courseName + "%' ORDER BY coursename DESC"
		cursor.execute(query)
		return cursor.fetchall()

	except Exception as e:
		print ("Something went wrong when executing the query: ", e)
		return None

