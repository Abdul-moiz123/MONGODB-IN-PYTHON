# DROP THE COLLECTION FROM A DATABASE
import pymongo
my_client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = my_client["db1"]
my_table = mydb["customers"] # ITS WILL NOT CREATED UNTIL ITS GET SOME CONTENT TO STORED
my_table.drop()


# DROP THE DATABASE
import pymongo
my_client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = my_client["db1"]
my_client.drop_database("db1")