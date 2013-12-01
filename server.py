#! /usr/bin/python

import sys
from flask import Flask, render_template, url_for, request, jsonify

sys.path.append('libs')
from HNPolls import HNPolls

app = Flask(__name__)
hn_polls = HNPolls()

@app.route("/add-poll/<poll_id>")
def add_polls(poll_id):
    return hn_polls.add_poll(poll_id)

@app.route("/poll-detail", methods=['POST', 'GET'])
def poll_detail():
    poll_id = request.args.get('poll_id', '', type=str)
    if poll_id is '':
        return "Invalid request"
    return hn_polls.poll_detail(poll_id)


@app.route("/", methods=['POST', 'GET'])
def index():
    index = request.args.get('page', 1, type=int)
    return hn_polls.list_polls(request, index)

#if __name__ == "__main__":
#    app.run()