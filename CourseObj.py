
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
		self.courseTerm = course[3]
		self.courseRequirements = course[4]
		self.coursePeriod = course[5]
		self.courseProfessor = course[6]
		self.courseDescription = course[7]
		#self.coursePrerequisites = course[3]
		
		
		#once period is implemented into database
		#self.coursePeriod = course[6] 
	def getCourseDeptTag(self):
		'''
		returns course department tag
		'''
		return self.courseDeptTag	

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

	def getCourseTerm(self):
		'''
		returns term(s) course is available
		'''
		return self.courseTerm

	def getCourseRequirements(self):
		'''
		returns course requirements
		'''
		return self.courseRequirements

	def getCoursePeriod(self):
		'''
		returns course requirements
		'''
		return self.coursePeriod

	def getCourseProfessor(self):
		'''
		returns course requirements
		'''
		return self.courseProfessor

	def getCourseDescription(self):
		'''
		returns course requirements
		'''
		return self.courseDescription

	def getCoursePrerequisites(self):
		'''
		returns course prerequisites
		'''
		return self.coursePrerequisites

	def getCoursePeriod(self):
		'''
		returns course period
		'''
		return self.coursePeriod

	def printCourseInfo(self):
		'''
		prints out the contents of the course object 
		'''
		for i in range(0, 7):
			if(i != 7 ):
				print(self.course[i], end = ', ')
			else:
				print(self.course[i], end ='')

		print()
		print()
				








