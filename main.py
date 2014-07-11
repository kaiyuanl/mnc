import spiders
import data
import helper
from globalvs import *

manongUrl = ''
issueSpider = spiders.IssueSpider(manongUrl)
issues = issueSpider.GetNewIssues()

connString = helper.GetDatabaseConnectionString()
conn = data.Connector(connString)

for issue in issues:
	conn.PushIssueToDatabase(issue)

