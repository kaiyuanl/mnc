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
        return u'weekly item\nhead: ' + self.head

    def get_head(self):
        return self.head

#Testing for class Weekly
if __name__ == '__main__':
    weekly_item = WeeklyItem('head',
        'origin', 'origin_link', 'desc')
    print weekly_item
