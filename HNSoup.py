#! /usr/bin/python

import datetime
from bs4 import BeautifulSoup

from curl import Curl
from constants import Constants

class HNSoup:

    def __init__(self, post_id):
        page_source = Curl.get_page_source(Constants.hn_post_url + post_id)
        self.parsed_html = BeautifulSoup(page_source)

    def get_title(self):
        return self.parsed_html.body.find('a', attrs={'href':'item?id=6801294'}).text.split(':')[1]

    def get_graph_data(self):
        return [x.div.font.text for x in self.parsed_html.find_all('td', attrs={'class':'comment'})]

    def get_post_votes(self):
        return self.parsed_html.find('td', attrs={'class':'subtext'}).span.text.split(' ')[0]

    def get_graph_value(self):
        value = [x.span.span.text.split(' ')[0] if x.span.span is not None else '' for x in self.parsed_html.find_all('td', attrs={'class':'default'})]
        filter(None, value)

    def get_mongo_data(self, post_id):
        data = { "_id": int(post_id),
                 "votes": self.get_post_votes(),
                 "title": self.get_title(),
                 "date_added": datetime.datetime.utcnow()
               }
        return data