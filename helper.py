from urllib.request import urlopen

def GetHtmlText(url):
	response = urlopen(url)
	#encoding = response.headers['content-type'].split('charset=')[1]
	#print(response.read().decode(encoding))
	return response.read()