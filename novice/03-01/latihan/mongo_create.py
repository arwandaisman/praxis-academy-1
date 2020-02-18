from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.rental

person = db.person
post=([
   { 'id_member': 1, 'name': "Janet Jones", 'address': "First Street", 'salutation': 2 },
   { 'id_member': 2, 'name': "Robert Phill", 'address': "Street 34", 'salutation': 1 },
   { 'id_member': 3, 'name': "Phill Robinshon", 'address': "Avenue", 'salutation': 1 }
]);
result = person.insert_many(post)

movierent = db.movieRent
post=([
    {'id_member': 1, 'title': "Pirates of the Caribbean"},
    {'id_member': 1, 'title': "Clash of the Titans"},
    {'id_member': 2, 'title': "Pengabdi Setan"},
    {'id_member': 2, 'title': "Impetigore"},
    {'id_member': 3, 'title': "Clash if The Titans"}
]);
result = movierent.insert_many(post)
print('Multiple posts: {0}'.format(result.inserted_ids))
