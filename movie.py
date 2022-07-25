import pymongo;

movie=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=movie["film"]
mycol=mydb["movieCollection"] 
movieList=[
    {
        "title" : "Fight Club",
        "writer" : "Chunk Palanhniuk",
        "year" : 1999,
        "actors" : ["Brad Pitt", "Edward Norton"],
    },
    {
        "title" : "Pulp Fiction",
        "writer" : "Quentin Tarantino",
        "year" : 1994,
        "actors" : ["John Travolta", "Uma Thurman"],
    },
    {
        "title" : "Inglorious Basterds",
        "writer" : "Quentin Tarantino",
        "year" : 2009,
        "actors" : ["Brad Pitt", "Diane Kruger", "Eli Roth"],
    },
    {
        "title" : "The Hobbit: An Unexpected Journey",
        "writer" : "J.R.R. Tolkein",
        "year" : 2012,
        "franchise" : "The Hobbit",
    },
    {
        "title" : "The Hobbit: The Desolation of Smaug",
        "writer" : "J.R.R. Tolkein",
        "year" : 2013,
        "franchise" : "The Hobbit",
    },
    {
        "title" : "The Hobbit: The Battle of the Five Armies",
        "writer" : "J.R.R. Tolkein",
        "year" : 2012,
        "franchise" : "The Hobbit",
        "synopsis" : "Bilbo and Company are forced to engage in a war"
    },
    {
        "title" : "Pee Wee Herman's Big Adventure",
    },
    {
        "title" : "Avatar",
    },
]

writer=mycol.insert_many(movieList) 
print(writer.inserted_ids) 

filmWriter = mycol.find({"writer":"Quentin Tarantino"}) 
for f in filmWriter: 
    print(f) 
    print()

filmYear = mycol.find({"year": {"$lt":2000}} or {"year": {"$gt":2010}})
for y in filmYear:
    print(y)

updateActor = mycol.update_one({"title":"Pulp Fiction"}, {"$set": {"actors": ["Brad Pitt", "Edward Norton", "Samuel L. Jackson"]}})
print(updateActor.modified_count, "modified actor")
print()

writerName = mycol.find({"writer":{"$regex": "k$"}})
for n in writerName:
    print(n["writer"])
    print()
   