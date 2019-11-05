
class CourseObj:
	'''
		object that contains all info of a single course
	'''
	def __init__(self,course):
		
		self.courseDeptTag = course[0]
		self.courseNumber = course[1]
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
	'''
	def getCoursePeriod(self):
		return self.coursePeriod
	'''
