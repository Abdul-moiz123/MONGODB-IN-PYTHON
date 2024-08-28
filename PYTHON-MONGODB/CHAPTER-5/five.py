# FILTER THE RESULT IN THE PARTICULAR TABLE OF PARTICULAR DATABASE 
import pymongo
my_client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = my_client["db1"]
my_table = mydb["customers"] # ITS WILL NOT CREATED UNTIL ITS GET SOME CONTENT TO STORED
my_query = {"address":"karachi"}
x = my_table.find(my_query)
for a in x:
    print(a)


# FILTER THE RESULT IN THE ADVANCE WAY IN THE PARTICULAR TABLE OF PARTICULAR DATABASE 
import pymongo
my_client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = my_client["db1"]
my_table = mydb["customers"] # ITS WILL NOT CREATED UNTIL ITS GET SOME CONTENT TO STORED
my_query = {"address":{"$gt":"k"}}
x  = my_table.find(my_query)
for a in x:
    print(a)


# YOU CAN ALSO FILTER THE RESULT BY USING REGUKAR EXPREESION    
import pymongo
my_client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = my_client["db1"]
my_table = mydb["customers"] # ITS WILL NOT CREATED UNTIL ITS GET SOME CONTENT TO STORED
my_query = {"address":{"$regex":"k"}}
x  = my_table.find(my_query)
for a in x:
    print(a)

  
    