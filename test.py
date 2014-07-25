import helper
import spiders
def test_get_main_page_url():
    url = helper.get_main_page_url()
    return url == 'http://weekly.manong.io/issues/'

def test_issue_content_spider():
	issue = spiders.IssueContentSpider(36, 'http://weekly.manong.io/issues/36')
	issue.get_items()
	posts = issue.get_posts()
	jobs = issue.get_jobs()
	helper.display_posts(posts)
	helper.display_jobs(jobs)

test_get_main_page_url()

test_issue_content_spider()
