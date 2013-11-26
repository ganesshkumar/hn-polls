#! /usr/bin/python

import urllib2

class Curl:
    @staticmethod
    def get_page_source(url):
        response = urllib2.urlopen(url)
        return response.read()
