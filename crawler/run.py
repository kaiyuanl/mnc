import spider
import infra
import item
import data

if __name__ == '__main__':
    latest_weekly_issue = data.get_latest_weekly_issue()
    print latest_weekly_issue

    for issue in range(latest_weekly_issue + 1, latest_weekly_issue + 10):
        print issue
        weekly_url = infra.gen_weekly_url(issue)
        print weekly_url, 'test'
        if infra.test_url_valid(weekly_url) == False:
            continue

        weekly_spider = spider.WeeklySpider(issue, weekly_url)
        weekly_spider.gen_content()
        title = weekly_spider.title
        pub_date = weekly_spider.pub_date
        items = weekly_spider.items

        data.add_weekly(issue, title, pub_date)

        for it in items:
            data.add_weekly_item(issue, it)




