
import datetime

class Issue:
	posts = []
	jobs = []

	def __init__(self, number, title, url):
		self.number = number
		self.title = title
		self.url = url

	def set_date(date):
		self.date = date

	def add_post(post):
		self.posts.append(post)

	def add_job(job):
		self.jobs.append(job)


class Post:
	def __init__(self, title, desc):
		self.title = title
		self.desc = desc

class Job:
	def __init__(self, company, position):
		self.company = company
		self.position = position