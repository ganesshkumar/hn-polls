#! /usr/bin/python

from HNSoup import HNSoup
from HNMongo import HNMongoClient

from flask import Flask, render_template, url_for, request, jsonify

app = Flask(__name__)
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

@app.route("/add-post/<post_id>")
def add_post(post_id):
    data = HNSoup(post_id).get_mongo_data()
    status = HNMongoClient().insert(data)
    return render_template("add-post.html", status=status)

@app.route("/poll-detail", methods=['POST', 'GET'])
def poll_detail():
    post_id = request.args.get('poll_id', '', type=str)
    soup = HNSoup(post_id)
    result = dict(zip(soup.get_graph_labels(), soup.get_graph_votes()))
    return jsonify(result=result)

@app.route("/")
def hello():
    client = HNMongoClient()
    collection = client.get_collection()
    cursor = collection.find().limit(10)
    polls = []
    for poll in cursor:
        polls.append(poll)
    return render_template("index.html", polls=polls , request=request)

#if __name__ == "__main__":
#    app.run()