import items
import datetime

class DBConn:
    def __init__(self, connString):
        self.connString = connString

    def push_daily_post(self, post):
        self.__display_post(post)

    def push_weekly_post(self, post):
        self.__display_post(post)

    def push_job(job):
        self.__display_job(job)

    def get_last_issue(self):
        return 38

    def get_daily_last_update_date(self):
        return datetime.date(2014, 7, 1)

    def __display_post(post):
        print '-------------'
        print post.title

    def __display_job(job):
        print '-------------'
        print job.company
        print job.position
