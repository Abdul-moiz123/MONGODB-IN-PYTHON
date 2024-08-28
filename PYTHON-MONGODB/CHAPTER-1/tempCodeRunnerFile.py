#CREATE DATABASE OF NAME DB1
import pymongo
my_client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = my_client["db1"] # db1 will not show in the list until its get some content to store