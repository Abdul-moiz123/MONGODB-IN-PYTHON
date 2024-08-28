# PRINT THE LIMITED DOCUMENT FROM THE DOCUMENT
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
my = x.limit(3)
for x in my:
    print(x)