#CREATE DATABASE OF NAME DB1
import pymongo
my_client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = my_client["db1"] # db1 will not show in the list until its get some content to store
print("successfully cconnected")


# CHECK IF THE DB1 EXIST IN THE DATABASE LIST OR NOT
import pymongo
my_client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = my_client["db1"] # db1 will not show in the list until its get some content to store
print(my_client.list_database_names())


#  YOU CAN ALSO CHECK IF THE PARTICULAR DATABASE EXIST IN THE DATABASES OF YOUR NETWORK
import pymongo
my_client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = my_client["db1"] # db1 will not show in the list until its get some content to store
databases = my_client.list_database_names()
if "db1" in databases:
    print("exist")
else:
    print("Not exist")