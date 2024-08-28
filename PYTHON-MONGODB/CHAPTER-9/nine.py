# UPDATE THE SINGLE THE DOCUMENT FROM A COLLECTION
import pymongo
my_client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = my_client["db1"]
my_table = mydb["customers"] # ITS WILL NOT CREATED UNTIL ITS GET SOME CONTENT TO STORED
old_query = {"name":"moiz"}
new_query = {"$set":{"name":"rafay"}}
x = my_table.update_one(old_query,new_query)
for a in x:
    print(a)
print(x.modified_count)


# UPDATE THE MULTIPLE THE DOCUMENT FROM A COLLECTION
import pymongo
my_client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = my_client["db1"]
my_table = mydb["customers"] # ITS WILL NOT CREATED UNTIL ITS GET SOME CONTENT TO STORED
old_query = {"name":{"$regex":"^m"}}
new_query = {"$set":{"name":"rafay"}}
x = my_table.update_one(old_query,new_query)
print(x.modified_count)