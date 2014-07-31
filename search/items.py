
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
    def __init__(self, issue, title, desc):
        self.issue = issue
        self.title = title
        self.desc = desc


class DailyPost:
    def __init__(self, title, src, pub_date):
        self.title = title
        self.src = src
        self.pub_date = pub_date

class Job:
    def __init__(self, issue, company, position):
        self.issue = issue
        self.company = company
        self.position = position