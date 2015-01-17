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

    def __str__(self):
        print '********'
        print 'weekly title: %s issue: %d'%(self.title, self.issue)

    def get_content(self):
        '''Return tuple (issue, title, pub_date, items)'''
        html = infra.get_html_content(self.url)
        soup = BeautifulSoup(html)

        self.title = soup.title.name

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
            #infra.print_u(head)
            link = raw_item.a['href']
            #infra.print_u(link)
            if infra.is_item_job(link):
                continue

            origin = None
            matched_origin = self._re_origin.search(head)
            if matched_origin:
                origin = matched_origin.group(1)
                #infra.print_u(origin)

            #get item's desc
            desc = raw_item.next_sibling.next_sibling.next_element
            #infra.print_u(desc)

            new_item = item.WeeklyItem(head,
                origin,
                link,
                desc)

            v = new_item.get_head()
            infra.print_u(v)
            self.items.append(item)

    def get_items(self):
        return self.items

    def get_title(self):
        return self.title

    def get_pub_date(self):
        return self.pub_date

if __name__ == '__main__':
    spider = WeeklySpider(58, 'http://weekly.manong.io/issues/58')
    spider.get_content()
    items = spider.get_content()
    for i in items:
        infra.print_u(i.head)




