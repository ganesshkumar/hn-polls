#! /usr/bin/python

from flask import render_template, url_for, jsonify

from HNSoup import HNSoup
from HNMongo import HNMongoClient

class HNPolls:
    def __init__(self):
        pass

    def add_poll(self, poll_id):
        data = HNSoup(poll_id).get_mongo_data()
        status = HNMongoClient().insert(data)
        return render_template("add-post.html", status=status)

    def poll_detail(self, poll_id):
        soup = HNSoup(poll_id)

        graph_votes, graph_labels = zip(*sorted(zip(soup.get_graph_votes(), soup.get_graph_labels()), reverse=True))
        data = {
               "title" : soup.get_title(),
               "labels" : graph_labels,
               "votes" : graph_votes
        }

        # Updating the entry in datastore
        mongodb_data = soup.get_mongo_data()
        HNMongoClient().save(mongodb_data)

        return jsonify(result=data)

    def list_polls(self, request):
    	print "ther"
        client = HNMongoClient()
        collection = client.get_collection()
        cursor = collection.find().limit(10)
        polls = []
        for poll in cursor:
            polls.append(poll)
            print "ready to render "
        return render_template("index.html", polls=polls , request=request)

