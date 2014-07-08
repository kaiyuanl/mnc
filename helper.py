from urllib.request import urlopen
import sys

def GetHtmlText(url):
	response = urlopen(url)
	page_encoding = response.headers['content-type'].split('charset=')[1]
	sys_encoding = sys.getfilesystemencoding()      # local encode format  
	#print(response.read().decode(page_encoding).encode(sys_encoding))  # convert encode format  
	return response.read().decode(page_encoding).encode(sys_encoding)


