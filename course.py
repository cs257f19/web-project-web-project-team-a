class CourseObj:
	def init(self,course):
		
		self.courseDeptTag = dept course[0]
		self.courseNumber = number course[1]
		self.courseName = name course[2]
		self.coursePrerequisites = name course[3]
		self.courseRequirements = requirements course[4]
		self.courseTerm = term course[5]
		# not created yet in course database self.coursePeriod = period 

	def getCourseTerm(self):
		return self.courseTerm

	def getCourseNumber(self):
		return self.courseNumber

	def getCourseName(self):
		return self.courseName

	def getCourseDeptTag(self):
		return self.courseDeptTag

	def getCourseRequirements(self):
		return self.courseRequirements

	def getCoursePeriod(self):
		return self.coursePeriod

