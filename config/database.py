from pymongo.mongo_client import MongoClient

#client = MongoClient("mongodb+srv://sheikhd811:FfuzhsyUI2EvSWtH@cluster0.igk87kb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

client = MongoClient('mongodb://localhost:27017/')
db = client.blog_db
collection_name  = db["blog_collection"]