import helper
import spiders
import datetime
import data
import ConfigParser
import items

def test_get_main_page_url():
    url = helper.get_main_page_url()
    return url == 'http://weekly.manong.io/issues/'

def test_issue_content_spider():
	issue = spiders.IssueContentSpider('http://weekly.manong.io/issues/36', 36)
	issue.fill_items()
	posts = issue.get_posts()
	jobs = issue.get_jobs()
	helper.display_posts(posts)
	helper.display_jobs(jobs)
	print issue.get_title()

def test_gen_daily_url():
	curr_date = helper.get_current_date()
	last_update_date = helper.get_daily_last_update_date()
	dates = helper.get_days_between_dates(last_update_date, curr_date)
	for date_ in dates:
		print helper.gen_daily_url(date_.year, date_.month, date_.day)

def test_daily_content_spider():
	spider = spiders.DailyContentSpider('http://daily.manong.io/2014-07-29')
	spider.fill_items()
	posts = spider.get_posts()
	helper.display_posts(posts)

def test_db_connect():
	config = ConfigParser.ConfigParser(allow_no_value = True)
	config.read('.config')

	user = config.get('dbconnstr', 'User')
	pwd = config.get('dbconnstr', 'Password')
	host = config.get('dbconnstr', 'Host')
	db = config.get('dbconnstr', 'Database')

	conn = data.DBConn(user, pwd, host, db)
	return conn

def test_get_last_issue():
	conn = test_db_connect()
	print conn.get_last_issue()

def test_get_daily_last_update_date():
	conn = test_db_connect()
	print conn.get_daily_last_update_date()

def test_push_new_issue():
	conn = test_db_connect()
	conn.push_new_issue(-1, 'test title', datetime.date(1900, 2, 1))

def test_push_weekly_post():
	conn = test_db_connect()
	conn.push_weekly_post(items.Post(1, 'test title', 'test desc'))

def test_push_daily_post():
	conn = test_db_connect()
	conn.push_daily_post(items.DailyPost('test daily', '@author', datetime.date(1900, 2, 2)))

def test_push_job():
	conn = test_db_connect()
	conn.push_job(items.Job(1, 'MSFT', 'SDET'))

#test_get_main_page_url()

#test_issue_content_spider()

test_gen_daily_url()

#test_daily_content_spider()

#test_db_connect()

#test_get_last_issue()

#test_get_daily_last_update_date()

#test_push_new_issue()

#test_push_weekly_post()

#test_push_daily_post()

#test_push_job()