from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["school"]

teachers = db["teachers"]
students = db["students"]
courses = db["courses"]
