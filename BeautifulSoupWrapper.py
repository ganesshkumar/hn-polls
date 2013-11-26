#! /usr/bin/python

from bs4 import BeautifulSoup

class BeautifulSoupWrapper:

    def __init__(self, page_source):
        self.parsed_html = BeautifulSoup(page_source)

    def get_title(self):
        return self.parsed_html.body.find('a', attrs={'href':'item?id=6801294'}).text.split(':')[1]

    def get_graph_data(self):
        return [x.div.font.text for x in self.parsed_html.find_all('td', attrs={'class':'comment'})]

    def get_graph_value(self):
        value = [x.span.span.text.split(' ')[0] if x.span.span is not None else '' for x in self.parsed_html.find_all('td', attrs={'class':'default'})]
        filter(None, value)