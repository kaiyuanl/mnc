import items
import datetime
import mysql.connector
from mysql.connector import errorcode

class DBConn:
    def __init__(self, user, password, host, database):
        try:
            self.conn = mysql.connector.connect(
                user = user,
                password = password,
                host = host,
                database = database,
                autocommit = True
                )
            self.cursor = self.conn.cursor()

        except mysql.connector.Error as err:
            print err
    
    def __del__(self):
        try:
            self.conn.close()
        except mysql.connector.Error as err:
            print err


    def push_new_issue(self, issue, title, pub_date):
        args = (issue, title, pub_date)
        try:
            result = self.cursor.callproc('PushNewIssue', args)
            print result
        except mysql.connector.Error as err:
            print err

    def push_daily_post(self, post):
        args = (post.title, post.src, post.pub_date)
        print args
        try:
            result = self.cursor.callproc('PushDailyPost', args)
        except mysql.connector.Error as err:
            print err

    def push_weekly_post(self, post):
        args = (post.issue, post.title, post.desc)
        try:
            result = self.cursor.callproc('PushWeeklyPost', args)
            print result
        except mysql.connector.Error as err:
            print err

    def push_job(self, job):
        args = (job.issue, job.company, job.position)
        try:
            result = self.cursor.callproc('PushJob', args)
        except mysql.connector.Error as err:
            print err

    def get_last_issue(self):
        args = (0,)
        result = self.cursor.callproc('GetLastIssue', args)
        if result[0] is None:
            return 0
        else:
            return result[0]

    def get_daily_last_update_date(self):
        args = (None,)
        result = self.cursor.callproc('GetDailyLastUpdateDate', args)
        if(result[0] is None):
            return datetime.date(2014, 6, 1)
        else:
            result_str = result[0].encode('ascii', 'replace')
            dt = datetime.datetime.strptime(result_str, '%Y-%m-%d')
            return datetime.date(dt.year, dt.month, dt.day)


    def __display_daily_post(self, post):
        print 'diplay daily post ->', post.title, '|||', post.src, '|||', post.pub_date

    def __display_weekly_post(self, post):
        print 'display weekly post ->', post.title, '|||', post.desc, '|||', post.issue

    def __display_job(self, job):
        print 'display job->', job.company, '|||', job.position, '|||', job.issue
