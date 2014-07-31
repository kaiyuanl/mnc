from spiders import *
from helper import *

curr_date = get_current_date()
last_update_date = get_daily_last_update_date()
dates = get_days_between_dates(last_update_date, curr_date)

#'get daily content'
for date_ in dates:
    year = date_.year
    month = date_.month
    day = date_.day

    daily_url = gen_daily_url(year, month, day)
    if(test_url_valid(daily_url)):
        spider = DailyContentSpider(daily_url, date_)
        spider.fill_items()
        posts = spider.get_posts()
        for post in posts:
            push_daily_post(post)


#'get issue content'
last_issue = get_last_issue()
begin_issue = last_issue + 1
for new_issue in range(begin_issue, begin_issue + 10):
    weekly_url = gen_weekly_url(new_issue)
    if(test_url_valid(weekly_url)):

        spider = IssueContentSpider(weekly_url, new_issue)
        spider.fill_items()
        posts = spider.get_posts()
        jobs = spider.get_jobs()
        pub_date = spider.get_date()
        push_new_issue(new_issue, pub_date)

        for post in posts:
            push_weekly_post(post)
            pass

        for job in jobs:
            push_job(job)
            pass