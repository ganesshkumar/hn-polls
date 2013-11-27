#! /usr/bin/python

from HNSoup import HNSoup
from HNMongo import HNMongoClient

from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)


@app.route("/add/<post_id>")
def add_post(post_id):
    data = HNSoup(post_id).get_mongo_data(post_id)
    status = HNMongoClient().insert(data)
    return render_template("add-post.html", status=status)

@app.route("/")
def hello():
    return render_template("graph.html")

