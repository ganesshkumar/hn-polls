#! /usr/bin/python
import os
from pymongo import MongoClient, errors

class HNMongoClient:
    def __init__(self):
        MONGO_URL = os.environ.get('MONGOHQ_URL')
        if MONGO_URL:
            self.client = MongoClient(MONGO_URL)
        else:
            self.client = MongoClient('mongodb://heroku:b69e0bd8ac101ac482568a762693ce42@paulo.mongohq.com:10049/app19833727')
        self.db = self.client['hn-polls']
        self.polls = self.db['polls']


    def get_collection(self):
        return self.polls

    def save(self, data):
        self.polls.save(data)

    def insert(self, data):
        try:
            self.polls.insert(data)
            return "Post added successfully"
        except errors.DuplicateKeyError:
            return  "Post already added"
