# encoding=utf-8
#Relevant item class crawled from site pages

class WeeklyItem:
    def __init__(self):
        pass

    def __init__(self,
        head,
        origin,
        origin_link,
        desc):

        self.head = head
        self.origin = origin
        self.origin_link = origin_link
        self.desc = desc

    def __str__(self):
        text = \
'''********
head : {}
origin : {}
origin_link : {}
desc : {}
********'''.format(
    self.head,
    self.origin,
    self.origin_link,
    self.desc
    )
        return text

#Testing for class Weekly
if __name__ == '__main__':
    weekly_item = WeeklyItem('head',
        'origin', 'origin_link', 'desc')
    print weekly_item
