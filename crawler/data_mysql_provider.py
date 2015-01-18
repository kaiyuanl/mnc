import item
from datetime import date
import mysql.connector
from mysql.connector import errorcode

class MySql_Conn:
    def __init__(self, user, pwd, host, database):
        try:
            self.conn = mysql.connector.connect(
                user = user,
                password = pwd,
                host = host,
                database = database,
                autocommit = True)

            self.cursor = self.conn.cursor()

        except mysql.connector.Error as err:
            print err

    def __del__(self):
        try:
            self.conn.close()
        except mysql.connector.Error as err:
            print err

    def add_weekly(self, issue, title, pub_date):
        args = (issue, title, pub_date)
        try:
            result = self.cursor.callproc('PushNewIssue', args)
            print result
        except mysql.connector.Error as err:
            print err

    def add_weekly_item(self, issue, head, origin, link):
        args = (issue, head, origin, link)
        try:
            result = self.cursor.callproc('PushWeeklyPost', args)
        except mysql.connector.Error as err:
            print err

    def get_last_issue(self):
        args = (0,)
        result = self.cursor.callproc('GetLastIssue', args)
        if result[0] is None:
            return 0
        else:
            return result[0]
