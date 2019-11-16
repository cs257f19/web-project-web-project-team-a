
class CourseObj:
	'''
		object that contains all info of a single course
		Takes in a course in the form of a tuple
		
		Formatting of tuple: 
		(courseDeptTag, courseNumber ,courseName, coursePrerequisites, courseRequirements, courseTerm)

	'''
	def __init__(self,course):
		self.course = course;
		self.courseDeptTag = course[0]
		self.courseNumber = str(course[1])
		self.courseName = course[2]
		self.coursePrerequisites = course[3]
		self.courseRequirements = course[4]
		self.courseTerm = course[5]

		#once period is implemented into database
		#self.coursePeriod = course[6] 

	def getCourseTerm(self):
		'''
		returns term(s) course is available
		'''
		return self.courseTerm

	def getCourseNumber(self):
		'''
		returns course number
		'''
		return self.courseNumber

	def getCourseName(self):
		'''
		returns course name
		'''
		return self.courseName

	def getCourseDeptTag(self):
		'''
		returns course department tag
		'''
		return self.courseDeptTag

	def getCourseRequirements(self):
		'''
		returns course requirements
		'''
		return self.courseRequirements

	def getCoursePrerequisites(self):
		'''
		returns course Prerequisites
		'''
		return self.coursePrerequisites
	'''
	Method will be implemented once database has course period

	def getCoursePeriod(self):
		return self.coursePeriod
	'''

	def printCourseInfo(self):
		'''
		prints out the contents of the course object 
		'''
		for i in range(0, 5):
			if(i !=4 ):
				print(self.course[i], end = ', ')
			else:
				print(self.course[i], end ='')
		print()
				








