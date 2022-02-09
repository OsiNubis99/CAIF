# importing module
from env import db_url, db_name
from pymongo import MongoClient
# connect to MongoDB
try:
    print(db_url)
    client = MongoClient(db_url)
    db = client[db_name]
    print(db.develop.count_documents({}))
    print("Connected successfully!!!")
except:
    print("Could not connect to MongoDB")

# Access database
