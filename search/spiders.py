from helper import *
from items import *
from filters import *
import re
import datetime

class IssueContentSpider:
	_posts = []
	_jobs = []

	_pattern_issue_date = r'\<body class="issue"\>[\s\S]*?\<h2\>.+(\d{4})-(\d{2})-(\d{2})'
	_pattern_item_div = r'<h4>[\s\S]*?</h4>[\s\S]*?<p>[\s\S]*?</p>'
	_pattern_company = r'<h4>.+?>(.+)</a>'
	_pattern_positions_div = r'<p>(.+)</p>'
	_pattern_positions = r'<a.+?>(.+?)</a>'
	_pattern_title = r'<h4><a.+?>(.+?)</a>'
	_pattern_desc = r'<p>(.*)</p>'


	def __init__(self, url):
		self.url = url
		self.html = get_html_content(self.url)


	def fill_items(self):
		items_div = re.findall(self._pattern_item_div, self.html)

		for item_div in items_div:
			if(is_item_job(item_div)):
				company = re.search(self._pattern_company, item_div).group(1)
				positions = re.findall(self._pattern_positions, re.search(self._pattern_positions_div, item_div).group(1))
				for position in positions:
					title = position
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
		return self._posts

	def get_jobs(self):
		return self._jobs

	def get_date(self):
		match = re.search(self._pattern_issue_date, self.html)
		year = int(match.group(1))
		month = int(match.group(2))
		day = int(match.group(3))
		return datetime.date(year, month, day)

class DailyContentSpider:
	_posts = []

	_pattern_post_div = r'<div class="post">([\s\S]+?)</div>'
	_pattern_posts = r'<li>[\s\S]+?</li>'
	_pattern_title = r'<a.+?>(.+)</a>'
	_pattern_src = r'\((.+)\)'

	def __init__(self, url):
		self.url = url
		self.html = get_html_content(self.url)

	def fill_items(self):
		posts_div = re.search(self._pattern_post_div, self.html).group(1)
		posts = re.findall(self._pattern_posts, posts_div)
		for post in posts:
			title = re.search(self._pattern_title, post).group(1)
			src = re.search(self._pattern_src, post).group(1)
			print title, src
			post = DailyPost(title, src)
			self._posts.append(post)

	def get_posts(self):
		return self._posts



