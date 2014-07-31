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
        return 36

    def get_daily_last_update_date(self):
        return datetime.date(2014, 7, 29)

    def push_new_issue(self, issue, pub_date):
        print 'push new issue', issue, pub_date

    def __display_daily_post(self, post):
        print 'diplay daily post ->', post.title, '|||', post.src, '|||', post.pub_date

    def __display_weekly_post(self, post):
        print 'display weekly post ->', post.title, '|||', post.desc, '|||', post.issue

    def __display_job(self, job):
        print 'display job->', job.company, '|||', job.position, '|||', job.issue
