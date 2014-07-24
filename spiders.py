from helper import *
from items import *
from filters import *
import re
import datetime

class IssueSpider:
	_pattern_div = b'\<div class=\"issue\">[\s\S]+?\</div>'
	_pattern_url = b'\<a href=\"(.*)\"\>'
	_pattern_issue_number = b'issues/(\d+)'
	_pattern_title = b'\<p>(.+)\</p\>'

	def __init__(self, url):
		self.url = url
		

	def get_new_issues(self):
		html = get_html_content(self.url)
		issue_divs = re.findall(self._pattern_div, html)

		all_issues = []

		for issue_div in issue_divs:
			url = re.search(self._pattern_url, issue_div).group(1)
			issue_number = re.search(self._pattern_issue_number, url).group(1)
			title = re.search(self._pattern_title, issue_div).group(1)
			all_issues.append(Issue(issue_number, title, url))

		new_issues = new_issues_filter(all_issues)

		return new_issues

	def get_issues(self):
		return self.get_new_issues()


class IssueContentSpider:
	_posts = []
	_jobs = []

	_pattern_issue_date = b'\<body class="issue"\>[\s\S]*?\<h2\>.+(\d{4})-(\d{2})-(\d{2})'
	_pattern_item_div = b'<h4>[\s\S]*?</h4>[\s\S]*?<p>[\s\S]*?</p>'
	_pattern_company = b'<h4>.+?>(.+)</a>'
	_pattern_positions_div = b'<p>(.+)</p>'
	_pattern_positions = b'<a.+?>(.+?)</a>'
	_pattern_title = b'<h4><a.+?>(.+?)</a>'
	_pattern_desc = b'<p>(.*)</p>'


	def __init__(self, issue, url):
		self.url = url
		self.issue = issue
		self.html = get_html_content(self.url)


	def get_items(self):
		items_div = re.findall(self._pattern_item_div, self.html)

		for item_div in items_div:
			if(is_item_job(item_div)):
				company = re.search(self._pattern_company, item_div).group(1)
				positions = re.findall(self._pattern_positions, re.search(self._pattern_positions_div))
				for position in positions:
					title = position.group(1)
					job = Job(company, title)
					self._jobs.append(job)

			elif(is_item_post(item_div)):
				title = re.search(self._pattern_title, item_div).group(1)
				desc = re.search(self._pattern_desc, item_div).group(1)
				post = Post(title, desc)
				self._posts.append(post)

			else:
				pass



			

	def get_posts(self):
		return None

	def get_jobs(self):
		pass

	def get_date(self):
		match = re.search(self._pattern_issue_date, self.html)
		year = int(match.group(1))
		month = int(match.group(2))
		day = int(match.group(3))
		return datetime.date(year, month, day)

