# DELTEE A SINGLE DOCUMENT IN THE COLLECTION
import pymongo
my_client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = my_client["db1"]
my_table = mydb["customers"] # ITS WILL NOT CREATED UNTIL ITS GET SOME CONTENT TO STORED
my_query = {"name":"moiz"}
x = my_table.delete_one(my_query)
print(x.deleted_count)


# DELTEE A MULTIPLE DOCUMENT IN THE COLLECTION
import pymongo
my_client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = my_client["db1"]
my_table = mydb["customers"] # ITS WILL NOT CREATED UNTIL ITS GET SOME CONTENT TO STORED
my_query = [{"name":"moiz"},{"name":"rafay"},{"name":"anas"}]
my_table.delete_many(my_query)
print(x.deleted_count)


# DELETE ALL THE DOCUMENT FROM THE COLLECTION
import pymongo
my_client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = my_client["db1"]
my_table = mydb["customers"] # ITS WILL NOT CREATED UNTIL ITS GET SOME CONTENT TO STORED
my_table.delete_many({})
print(x.deleted_count)