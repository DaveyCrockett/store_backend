import pymongo

mongo_url = "mongodb+srv://student:FullStack@cluster0.glkph.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

client = pymongo.MongoClient(mongo_url)

# get the specific database
db = client.get_database("Paredes")