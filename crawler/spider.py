from bs4 import BeautifulSoup
from datetime import date
import re
import infra
import item
import data
import sys

class WeeklySpider:
    _re_weekly_date = re.compile(\
        r'(\d{4})-(\d{2})-(\d{2})'
        )

    _re_origin = re.compile(\
        r'[(](.+)[)]'
        )

    def __init__(self, issue, url):
        self.issue = issue
        self.url = url

        self.items = []

    def gen_content(self):
        '''Return tuple (issue, title, pub_date, items)'''
        html = infra.get_html_content(self.url)
        soup = BeautifulSoup(html)

        self.title = unicode(soup.title.next_element)
        infra.print_u(self.title)
        #get publish date of weekly issue
        h2 = soup.h2.string
        matched_date = self._re_weekly_date.search(h2)
        self.pub_date = date(int(matched_date.group(1)),
            int(matched_date.group(2)),
            int(matched_date.group(3)))

        #get items' content
        raw_items = soup.find_all('h4')
        del raw_items[-1]
        del raw_items[-1]
        for raw_item in raw_items:
            #get item's  head, link, and origin if exists
            #print raw_item
            head = raw_item.next_element.next_element
            infra.print_u(head)
            link = raw_item.a['href']
            #infra.print_u(link)
            if infra.is_item_job(link):
                continue

            #infra.print_u(link)
            #link = infra.get_redir_url(link)
            #infra.print_u(link)

            origin = None
            matched_origin = self._re_origin.search(head)
            if matched_origin:
                origin = matched_origin.group(1)
                #infra.print_u(origin)

            new_item = item.WeeklyItem(unicode(head),
                unicode(origin),
                unicode(link))

            infra.print_u(new_item.head)

            self.items.append(new_item)

if __name__ == '__main__':
    spider = WeeklySpider(58, 'http://weekly.manong.io/issues/58')
    spider.gen_content()
    items = spider.items
    for i in items:
        infra.print_u(i.link)




