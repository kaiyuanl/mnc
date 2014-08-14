from urllib import urlopen
import sys
import ConfigParser
import io
import datetime
import httplib
import urlparse
import data

config = ConfigParser.ConfigParser(allow_no_value = True)
config.read('.config')

user = config.get('dbconnstr', 'User')
pwd = config.get('dbconnstr', 'Password')
host = config.get('dbconnstr', 'Host')
db = config.get('dbconnstr', 'Database')

conn = data.DBConn(user, pwd, host, db)

def get_html_content(url):
    response = urlopen(url)
    html = response.read()
    return html

def get_main_page_url():
    return config.get('targeturl','MainPageUrl')

def get_database_connection_string():
    pass

def is_item_job(item_div):
    return 'job.manong.io' in item_div

def is_item_post(item_div):
    return True

def display_posts(posts):
    for post in posts:
        print '-------------'
        print post.title

def display_jobs(jobs):
    for job in jobs:
        print '-------------'
        print job.company
        print job.position

def get_current_date():
    return datetime.date.today()

def get_daily_last_update_date():
    #return a test date value
    return conn.get_daily_last_update_date()

def get_days_between_dates(start_date, end_date):
    diff = end_date - start_date
    print diff
    for i in range(diff.days + 1):
        yield start_date + datetime.timedelta(i)

def gen_daily_url(year, month, day):
    return "http://daily.manong.io/%04d-%02d-%02d"%(year, month, day)

def gen_weekly_url(issue):
    return "http://weekly.manong.io/issues/%s"%(issue)

def test_url_valid(url):
    result = None
    host, path = urlparse.urlparse(url)[1:3]
    try:
        httpconn = httplib.HTTPConnection(host)
        httpconn.request('HEAD', path)
        result = httpconn.getresponse().status
    except StandardError:
        pass

    good_codes = [httplib.OK, httplib.FOUND, httplib.MOVED_PERMANENTLY]
    return result in good_codes

def get_last_issue():
    return conn.get_last_issue()

def push_daily_post(post):
    conn.push_daily_post(post)

def push_weekly_post(post):
    conn.push_weekly_post(post)

def push_job(job):
    conn.push_job(job)

def push_new_issue(issue, title, pub_date):
    conn.push_new_issue(issue, title, pub_date)
