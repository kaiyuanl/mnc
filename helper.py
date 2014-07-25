from urllib import urlopen
import sys
import ConfigParser
import io
config = ConfigParser.ConfigParser(allow_no_value = True)
config.read('.config')

def get_html_content(url):
	response = urlopen(url)
	return response.read()

def get_main_page_url():
	return config.get('targeturl','MainPageUrl')

def get_database_connection_string():
	pass

def is_item_job(item_div):
	return 'job.manong.io' in item_div

def is_item_post(item_div):
	return True

def display_posts(posts):
	for post in posts:
		print '-------------'
		print post.title
		print post.desc

def display_jobs(jobs):
	for job in jobs:
		print '-------------'
		print job.company
		print job.position
