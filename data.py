import items

class Connector:
	def __init__(self, connString):
		self.connString = connString

	def PushIssueToDatabase(self, issue):
		pass

	def PushPostToDatabase(self, post):
		pass

	def PushJobToDatabase(self, job):
		pass

	def HasIssuePushed(self, issue):
		pass