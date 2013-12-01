#! /usr/bin/python

import urllib2

class HNCurl:
    @staticmethod
    def get_page_source(url):
        response = urllib2.urlopen(url)
        return response.read()
