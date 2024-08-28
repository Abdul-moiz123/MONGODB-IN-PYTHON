# INSERT DOCUMENT IN THE COLLECTION
import pymongo
my_client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = my_client["db1"]
my_table = mydb["customers"] # ITS WILL NOT CREATED UNTIL ITS GET SOME CONTENT TO STORED
my_value = {"name":"moiz","age":20,"address":"karachi"}
x = my_table.insert_one(my_value)

# RETURN THE ID OF THE DOCUMENT WHICH DECLARE BY DEFAULT IF YOU FORGET TO ASSIGN 
import pymongo
my_client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = my_client["db1"]
my_table = mydb["customers"] # ITS WILL NOT CREATED UNTIL ITS GET SOME CONTENT TO STORED
my_value = {"name":"moiz","age":20,"address":"karachi"}
x = my_table.insert_one(my_value)
print(x.inserted_id)

# INSERT MULTIPLE DOUCUMENT AT A TIME
import pymongo
my_client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = my_client["db1"]
my_table = mydb["customers"] # ITS WILL NOT CREATED UNTIL ITS GET SOME CONTENT TO STORED
my_value = [
    {"name":"rafay","age":30,"address":"lahore"},
    {"name":"haseeb","age":40,"address":"pindi"},
    {"name":"anas","age":50,"address":"karachi"},
    {"name":"momo","age":60,"address":"islamabad"}
    ]
x = my_table.insert_many(my_value)


# RETURN THE IDs OF THE DOCUMENT WHICH DECLARE BY DEFAULT IF YOU FORGET TO ASSIGN
import pymongo
my_client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = my_client["db1"]
my_table = mydb["customers"] # ITS WILL NOT CREATED UNTIL ITS GET SOME CONTENT TO STORED
my_value = [
    {"name":"rafay","age":30,"address":"lahore"},
    {"name":"haseeb","age":40,"address":"pindi"},
    {"name":"anas","age":50,"address":"karachi"},
    {"name":"momo","age":60,"address":"islamabad"}
    ]
x = my_table.insert_many(my_value)
my_ids = x.inserted_ids()
for ids in my_ids:
    print(ids)
