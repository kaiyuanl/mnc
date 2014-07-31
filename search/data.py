import items
import datetime

class DBConn:
    def __init__(self, connString):
        self.connString = connString

    def push_daily_post(self, post):
        self.__display_daily_post(post)

    def push_weekly_post(self, post):
        self.__display_weekly_post(post)

    def push_job(self, job):
        self.__display_job(job)

    def get_last_issue(self):
        return 38

    def get_daily_last_update_date(self):
        return datetime.date(2014, 7, 29)

    def __display_post(self, post):
        print '__-------------'
        print post.title

    def __display_daily_post(self, post):
        print post.title, '|||', post.src

    def __display_weekly_post(self, post):
        print post.title, '|||', post.desc

    def __display_job(self, job):
        print job.company, '|||', job.position
