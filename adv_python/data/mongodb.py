import pymongo
from pymongo import MongoClient
cl=MongoClient("mongodb+srv://josetellis2018:dHmjZHB5MZgPsH0f@cluster0.ghrj9wz.mongodb.net/?retryWrites=true&w=majority")
db=cl['test']
collection=db['traintest']
post={'id':100,'name':'jose'}
collection.insert_one(post)