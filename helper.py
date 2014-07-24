from urllib.request import urlopen
import sys
import configparser

config = configparser.ConfigParser()
config.read('.config')

def get_html_content(url):
	response = urlopen(url)
	return response.read()

def get_main_page_url():
	return config['targeturl']['MainPageUrl']

def get_database_connection_string():
	pass

def is_item_job(item_div):
	return 'job.manong.io' in item_div

def is_item_post():
	return True