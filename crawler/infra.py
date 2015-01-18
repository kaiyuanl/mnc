import os, platform, logging
import urllib
import urllib2
import httplib
import urlparse
import sys

#Logging relevant code
if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'),
                                os.getenv('HOMEPATH'),
                                'test.log')
else:
    logging_file = os.path.join(os.getenv('HOME'),
                                'test.log')
logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s : %(message)s',
    filename = logging_file,
    filemode = 'w', #'a' opens the file for appending
)

logger = logging.getLogger('test_logger')

def print_u(str):
    print str.encode('utf-8', 'ignore')

def gen_weekly_url(issue):
    return "http://weekly.manong.io/issues/%s"%(issue)

def get_html_content(url):
    '''return unicode'''
    response = urllib.urlopen(url)
    html = response.read().decode('utf-8')
    return html

def is_item_job(item_content):
    return 'job.manong.io' in item_content

def test_url_valid(url):
    result = None
    host, path = urlparse.urlparse(url)[1:3]
    try:
        httpconn = httplib.HTTPConnection(host)
        httpconn.request('HEAD', path)
        result = httpconn.getresponse().status
    except StandardError:
        pass

    good_codes = [httplib.OK, httplib.FOUND, httplib.MOVED_PERMANENTLY]
    return result in good_codes

def get_redir_url(url):
    req = urllib2.Request(url)
    opr = urllib2.build_opener()
    f = opr.open(req)
    return url


if __name__ == '__main__':
    url = 'http://weekly.manong.io/issues/58'
    html = get_html_content(url)
    print html.encode('ascii', 'ignore')
