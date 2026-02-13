
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://pandeymannu54:Manoj1pandey@cluster0.l1av4a1.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


## this is my database 
mydb = client["mydatabase"]

client.list_database_names()

#collection
mycol = mydb["myfirstcollection"]

#record
myfirstrecord = {"name": "manoj","lname": "pandey", "address": "haldwani"}

#insert record
x = mycol.insert_one(myfirstrecord)

mysecondrecord = {"movie": "avengers", "hero": "ironman", "director": "joss whedon"}

y = mycol.insert_one(mysecondrecord)

mythirdrecord = {"job": "developer", "company": "google", "location": "usa"}
z = mycol.insert_one(mythirdrecord)


multiplerecords = [{
"class":12, "section":"a", "rollno": 23} , 
{"class":11, "section":"b", "rollno": 24} , 
{"class":10, "section":"c", "rollno": 25},
{"class":9, "section":"d", "rollno": 26} , 
{"class":8, "section":"e", "rollno": 27} , 
{"class":7, "section":"f", "rollno": 28} , 
{"class":6, "section":"g", "rollno": 29} , 
{"class":5, "section":"h", "rollno": 30}]

a = mycol.insert_many(multiplerecords)