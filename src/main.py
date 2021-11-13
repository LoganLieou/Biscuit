import os
import pymongo
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

client = pymongo.MongoClient(os.getenv('MONGO_URI'))

try:
    db = client['hackathon']
    users = db['users']
except Exception:
    print("error connecting")

@app.route("/", methods=["POST", "GET"])
def hackathon():
    if (request.method == "POST"):
        doc = request.get_json()
        print(doc)
        users.insert_one(doc)
        return "what in the world are you doing?"
    return "why did you GET?"
