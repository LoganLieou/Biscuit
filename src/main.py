import os
from bson.json_util import dumps
import pymongo
from flask import Flask, request
from flask_cors import CORS

# CORS middleware
app = Flask(__name__)
CORS(app)

# get connection string
client = pymongo.MongoClient(os.getenv('MONGO_URI'))

# try and connect to the database
try:
    db = client['hackathon']
    users = db['users']
except Exception:
    print("error connecting")
    exit()

# login endpoint handle login requests
@app.route('/login', methods=["POST", "GET"])
def login():
    if (request.method == "POST"):
        data = request.get_json()
        print(data)
        res = users.find_one({"name": data['name']})
        print(res)

        # return information for user
        return {
            "name": res['name'],
            "trade_his": res['trade_hist'],
            "holdings": res['holdings']
        }
    return "you made a GET request failure"

