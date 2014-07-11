import helper
import items
import re
import datetime
import filters

class IssueSpider:
	patternDiv = b'\<div class=\"issue\">[\s\S]+?\</div>'
	patternUrl = b'\<a href=\"(.*)\"\>'
	patternIssueNumber = b'issues/(\d+)'
	patternTitle = b'\<p>(.+)\</p\>'

	def __init__(self, url):
		self.url = url
		

	def GetNewIssues(self):
		html = helper.GetHtmlText(self.url)
		issueDivs = re.findall(self.patternDiv, html)
		print(type(re.findall(self.patternDiv, html)))
		allIssues = []

		for issueDiv in issueDivs:
			url = re.search(self.patternUrl, issueDiv).group(1)
			print(type(re.search(self.patternUrl, issueDiv)))
			issueNumber = re.search(self.patternIssueNumber, url).group(1)
			title = re.search(self.patternTitle, issueDiv).group(1)
			allIssues.append(items.Issue(issueNumber, title, url))

		newIssues = filters.NewIssuesFilter(allIssues)

		for issue in newIssues:
			spider = IssueContentSpider(issue.url)
			issue.posts = spider.GetPosts()
			issue.jobs = spider.GetJobs()
			issue.date = spider.GetDate()

		return newIssues

	def GetIssues(self):
		return self.GetNewIssues()


class IssueContentSpider:
	patternIssueDate = b'\<body class="issue"\>[\s\S]*?\<h2\>.+(\d{4})-(\d{2})-(\d{2})'

	patternCategory = b'<h3>(.+?)</h3>'

	#Search job items
	patternJobItemDiv = b''
	patternJobCompany = b''
	patternJobTitle = b''
	patternJobLink = b''

	#Search post items
	patternPostItemDiv = b'<h3>(.+?)</h3>[\s\S]+?<h3'
	patternPostTitle = b''
	patternPostLink = b''
	patternPostSubmitter = b''
	patternPostSubmitterLink = b''
	patternPostDescription = b''	

	def __init__(self, issue, url):
		self.url = url
		self.issue = issue

		

		#Get html text 
		self.html = helper.GetHtmlText(self.url)


	def GetPosts(self):
		'''
		postDivs = re.findall(self.patternPostItemDiv, self.html)
		for postDiv in postDivs:
			print(postDiv)
			title = re.search(self.patternPostTitle, postDiv)
			link = re.search(self.patternPostLink, postDiv)
			submitter = re.search(self.patternPostSubmitter, postDiv)
			submitterLink = re.search(self.patternPostSubmitterLink, postDiv)
			description = re.search(self.patternPostDescription, postDiv)
			'''
		categories = re.findall(self.patternCategory, self.html)
		print(len(categories))
		print(type(categories[0]))
		i = 0
		while (i < len(categories) and i + 1 < len(categories)):
			patternCommon = categories[i] + b'[\s\S]*?' + categories[i+1]
			print(patternCommon)
			i = i + 1


			

	def GetJobs(self):
		return None

	def GetDate(self):
		match = re.search(self.patternIssueDate, self.html)
		year = int(match.group(1))
		month = int(match.group(2))
		day = int(match.group(3))
		return datetime.date(year, month, day)

