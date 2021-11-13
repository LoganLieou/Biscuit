import os
import pymongo

client = pymongo.MongoClient(os.getenv('MONGO_URI'))
try:
    db = client['hackathon']
    users = db['users']
    doc = {
        "name": "Joe"
    }
    ins_id = users.insert_one(doc).inserted_id
    print(ins_id)
except Exception:
    print("Error!")
