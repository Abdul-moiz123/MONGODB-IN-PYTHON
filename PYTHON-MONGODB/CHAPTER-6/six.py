# SORT THE RECORD IN THE ASCENDING ORDER WHICH IS SET BY DEFAULT IN THE MONGODB
import pymongo
my_client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = my_client["db1"]
my_table = mydb["customers"] # ITS WILL NOT CREATED UNTIL ITS GET SOME CONTENT TO STORED
x  = my_table.sort("name",1)
for a in x:
    print(a)


# SORT THE RECORD IN THE DESCENDING ORDER 
import pymongo
my_client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = my_client["db1"]
my_table = mydb["customers"] # ITS WILL NOT CREATED UNTIL ITS GET SOME CONTENT TO STORED
x  = my_table.sort("name",-1)
for a in x:
    print(a)
