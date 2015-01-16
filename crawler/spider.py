import re
import infra
import item
import data

class WeeklySpider:
    _re_title = re.compile(
        r'(?<=<title>).+?(?=</title>)'
        )

    _re_publish_date = re.compile(
        r'<body class="issue">[\s\S]*?<h2>.+(\d{4})-(\d{2})-(\d{2})'
        )

    _re_raw_item = re.compile(
        r'<h4>[\s\S]*?</h4>[\s\S]*?<p>[\s\S]*?</p>'
        )

    _re_item_title = re.compile(
        r'<h4><a.+?>(.+?)</a>'
        )

    _re_item_origin = re.compile(
        r''
        )

    _re_item_link = re.compile(
        r''
        )

    _re_item_desc = re.compile(
        r''
        )

    def __init__(self, url):
        pass

    def __str__(self):
        return 'weekly_spider'

    def content(self):
        '''Return tuple (title, issue, items)'''
        return None

