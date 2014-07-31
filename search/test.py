import helper
import spiders
import datetime
def test_get_main_page_url():
    url = helper.get_main_page_url()
    return url == 'http://weekly.manong.io/issues/'

def test_issue_content_spider():
	issue = spiders.IssueContentSpider('http://weekly.manong.io/issues/36')
	issue.fill_items()
	posts = issue.get_posts()
	jobs = issue.get_jobs()
	helper.display_posts(posts)
	helper.display_jobs(jobs)

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

#test_get_main_page_url()

#test_issue_content_spider()

#test_gen_daily_url()

#test_daily_content_spider()
