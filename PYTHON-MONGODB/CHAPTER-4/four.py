# FIND THE DOCUMENT IN THE COLLECTION OF PARTICULAR DATABASE
import pymongo
my_client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = my_client["db1"]
my_table = mydb["customers"] # ITS WILL NOT CREATED UNTIL ITS GET SOME CONTENT TO STORED
x = my_table.find_one() # return the every first docement of the collection
print(x)

# FIND ALL THE DOCUMENT IN THE COLLECTION OF PARTICULAR DATABASE
import pymongo
my_client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = my_client["db1"]
my_table = mydb["customers"] # ITS WILL NOT CREATED UNTIL ITS GET SOME CONTENT TO STORED
x = my_table.find() # return the every first docement of the collection
for a in x:
    print(a)


# FIND ONLY THE PARTICULAR DOCUMENT IN THE COLLECTION OF PARTICULAR DATABASE
import pymongo
my_client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = my_client["db1"]
my_table = mydb["customers"] # ITS WILL NOT CREATED UNTIL ITS GET SOME CONTENT TO STORED
x = my_table.find({} , {"name":0 , "age":1 ,"address":1})
for a in x:
    print(a)


# YOU ARE NOT ALLOW TO USED BOTH 1 AND 0
import pymongo
my_client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = my_client["db1"]
my_table = mydb["customers"] # ITS WILL NOT CREATED UNTIL ITS GET SOME CONTENT TO STORED
x = my_table.find({} , {"name":0})
print(x)


# THIS WILL RAISE AN ERROR
import pymongo
my_client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = my_client["db1"]
my_table = mydb["customers"] # ITS WILL NOT CREATED UNTIL ITS GET SOME CONTENT TO STORED
x = my_table.find({} , {"name":0 , "age":1})
print(x)