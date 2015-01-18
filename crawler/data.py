import data_mysql_provider
from datetime import date
import ConfigParser

config = ConfigParser.ConfigParser(allow_no_value = True)
config.read('.config')

user = config.get('dbconnstr', 'User')
pwd = config.get('dbconnstr', 'Password')
host = config.get('dbconnstr', 'Host')
db = config.get('dbconnstr', 'Database')
conn = data_mysql_provider.MySql_Conn(user, pwd, host, db)

def get_latest_weekly_issue():
    return conn.get_last_issue()

def add_weekly(issue, title, pub_date):
    conn.add_weekly(issue, title, pub_date)


def add_weekly_item(issue, it):
    conn.add_weekly_item(issue, it.head, it.origin, it.link)
