import os
from dotenv import load_dotenv

import pymongo
from pprint import pprint

from flask import Flask, jsonify, request, Response
from flask_cors import CORS

import json
from bson import ObjectId

app = Flask(__name__)
CORS(app)

print('\n')

try:
    load_dotenv()
    MONGO_CLUSTER = os.environ['MONGO_URI']
    client = pymongo.MongoClient(MONGO_CLUSTER)
    # client = pymongo.MongoClient(MONGO_URI)

    db = client.hackathon
    users = db.users
except Exception:
    print("Error connecting...")



result = users.find_one().get('name')
print(result)

search = users.find_one({'name': 'Joe, but better'})
print(search)
print(search.get('name'))

@app.route("/", methods=["POST", "GET"])
def index():
    if (request.method == "POST"):
        doc = request.get_json()
        print(doc)
        users.insert_one(doc)
        return "what in the world are you doing?"
    else:
        return "Why did you GET?\nLet's GET this bread!"

@app.route("/query/<string:name>", methods=["GET"])
def get_mult(name):
    search = users.find_one({'name': name})
    return Response(json.dumps(search,default=str),mimetype="application/json")

