from urllib import urlopen
import sys
import ConfigParser
import io
import datetime
import httplib
import urlparse

config = ConfigParser.ConfigParser(allow_no_value = True)
config.read('.config')

def get_html_content(url):
	response = urlopen(url)
	return response.read()

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
		print post.desc

def display_jobs(jobs):
	for job in jobs:
		print '-------------'
		print job.company
		print job.position

def get_current_date():
	return datetime.date.today()

def get_daily_last_update_date():
	#return a test date value
	return datetime.date(2014, 7, 1)

def get_days_between_dates(start_date, end_date):
	diff = end_date - start_date
	for i in range(diff.days + 1):
		yield start_date + datetime.timedelta(i)

def gen_daily_url(year, month, day):
	return "http://daily.manong.io/%04d-%02d-%02d"%(year, month, day)

def gen_weekly_url(issue):
	return "http://weekly.manong.io/issue/%s"%(issue)

def test_url_valid(url):
	result = None
	host, path = urlparse.urlparse(url)[1:3]
    try:
        conn = httplib.HTTPConnection(host)
        conn.request('HEAD', path)
        result = conn.getresponse().status
    except StandardError:
        pass

    good_codes = [httplib.OK, httplib.FOUND, httplib.MOVED_PERMANENTLY]
    return result in good_codes

def get_last_issue():
	return 38

