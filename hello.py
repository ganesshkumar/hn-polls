#! /usr/bin/python

from curl import Curl
from BeautifulSoupWrapper import BeautifulSoupWrapper
from flask import Flask




app = Flask(__name__)

@app.route("/")
def hello():
    page_source = Curl.get_page_source("https://news.ycombinator.com/item?id=6801294")
    soup = BeautifulSoupWrapper(page_source)
    return "Hello World!" + soup.get_title()

