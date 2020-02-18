from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.rental
person = db.person

post = person.find_one({'name': 'Janet Jones'})
print(post)
