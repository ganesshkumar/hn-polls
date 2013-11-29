#! /usr/bin/python
import os
from pymongo import MongoClient, errors

class HNMongoClient:
    def __init__(self):
        self.client = MongoClient('mongodb://heroku:heroku123@paulo.mongohq.com:10049/app19833727')
        self.db = self.client.app19833727
        self.polls = self.db.polls


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

