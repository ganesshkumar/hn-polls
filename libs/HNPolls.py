#! /usr/bin/python

from flask import render_template, url_for, jsonify

from HNSoup import HNSoup
from HNMongo import HNMongoClient
from HNConstants import HNConstants

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

    def list_polls(self, request, page_index):
        client = HNMongoClient()
        collection = client.get_collection()
        # ToDo: Get polls_per_page and next_page_url from HNConstants
        polls_per_page = 20
        starting_index = (page_index - 1) * polls_per_page
        cursor = collection.find().sort("_id", -1)[starting_index:(starting_index+polls_per_page)]
        polls = []
        for poll in cursor:
            polls.append(poll)
        no_more_polls = False if len(polls) is polls_per_page else True
        return render_template("index.html", polls=polls , request=request, 
                next_page_url="/?page=" + str(page_index + 1), no_more_polls=no_more_polls)

