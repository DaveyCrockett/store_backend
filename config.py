import pymongo
import certifi

mongo_url = "mongodb+srv://dbUser:EditWeb22@cluster0.qydsr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = pymongo.MongoClient(mongo_url, tlsCAFile=certifi.where())

# get the specific database
db = client.get_database("ParedesDB")
