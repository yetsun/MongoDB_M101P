from pymongo import MongoClient

conn  = MongoClient('localhost', 27017)

db = conn.test

names = db.names

name_list = names.find()


for one_name in name_list:
    print one_name['first_name']
    print one_name['last_name']
    print


