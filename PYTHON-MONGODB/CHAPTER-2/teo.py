# CREATE COLLECTION IN THE DB1
import pymongo
my_client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = my_client["db1"]
my_table = mydb["customers"] # ITS WILL NOT CREATED UNTIL ITS GET SOME CONTENT TO STORED


# CHECK IF THE COLLECTION OR TABLE EXIST IN THE DB1 OR NOT
import pymongo
my_client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = my_client["db1"]
my_table = mydb["customers"] # ITS WILL NOT CREATED UNTIL ITS GET SOME CONTENT TO STORED
colections = mydb.list_collection_names()
for collection in colections:
    print(collection)

# YOU CAN ALSO CHECK PARTIULAR DATABASE
import pymongo
my_client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = my_client["db1"]
my_table = mydb["customers"] # ITS WILL NOT CREATED UNTIL ITS GET SOME CONTENT TO STORED
colections = mydb.list_collection_names()
if "db1" in colections:
    print("found")
else:
    print("Not found")    