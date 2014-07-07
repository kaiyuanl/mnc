import helper
import items
import re

class IssueSpider:
	def __init__(self, url):
		self.url = url
		self.patternDiv = b'\<div class=\"issue\">[\s\S]+?\</div>'
		self.patternUrl = b'\<a href=\"(.*)\"\>'
		self.patternIssueNumber = b'issues/(\d+)'
		self.patternTitle = b'\<p>(.+)\</p\>'

	def GetIssues(self):
		html = helper.GetHtmlText(self.url)
		issueDivs = re.findall(self.patternDiv, html)

		for issueDiv in issueDivs:
			url = re.search(self.patternUrl, issueDiv).group(1)
			issueNumber = re.search(self.patternIssueNumber, url).group(1)
			title = re.search(self.patternTitle, issueDiv).group(1)
			issue = items.Issue(issueNumber, title, url)
			#print(title.encode('utf-8'))
			#yield issue



class IssueContentSpider:
	def __init__(self, issue, url):
		self.url = url
		self.issue = issue

		self.patternDate = b''

		#Search job items
		self.patternJobItemDiv = b''
		self.patternJobCompany = b''
		self.patternJobTitle
		self.patternJobLink

		#Search post items
		self.patternPostItemDiv
		self.patternPostTitle
		self.patternPostLink
		self.patternPostSubmitter
		self.patternPostSubmitterLink
		self.patternPostDescription

		#Get html text 
		html = helper.GetHtmlText(self.url)

	def GetDate(self):
		pass

	def GetPosts(self):
		postDivs = re.findall(self.patternItemDiv, self.html)
		for postDiv in postDivs:
			title = re.search(self.patternPostTitle, postDiv)
			link = re.search(self.patternPostLink, postDiv)
			submitter = re.search(self.patternPostSubmitter, postDiv)
			submitterLink = re.search(self.patternPostSubmitterLink, postDiv)
			description = re.search(self.patternPostDescription, postDiv)
			

	def GetJobs(self):
		pass
