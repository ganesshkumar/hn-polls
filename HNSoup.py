#! /usr/bin/python

import datetime
from bs4 import BeautifulSoup

from HNCurl import HNCurl
from HNConstants import HNConstants

class HNSoup:

    def __init__(self, post_id):
        self.post_id = post_id
        page_source = HNCurl.get_page_source(HNConstants.hn_post_url + post_id)
        self.parsed_html = BeautifulSoup(page_source)

    def get_title(self):
        return self.parsed_html.body.find('a', attrs={'href':'item?id='+self.post_id}).text.split(':')[1]

    def get_graph_labels(self):
        return [x.div.font.text if len(x.div.font.text) < 31 else x.div.font.text[:30] for x in self.parsed_html.find_all('td', attrs={'class':'comment'})]

    def get_post_votes(self):
        return self.parsed_html.find('td', attrs={'class':'subtext'}).span.text.split(' ')[0]

    def get_graph_votes(self):
        value = [int(x.span.span.text.split(' ')[0]) if x.span.span is not None else '' for x in self.parsed_html.find_all('td', attrs={'class':'default'})]
        return filter(None, value)

    def get_mongo_data(self):
        data = { "_id": int(self.post_id),
                 "votes": self.get_post_votes(),
                 "title": self.get_title(),
                 "date_added": datetime.datetime.utcnow()
               }
        return data
