import os

from pyArango.connection import *
from dotenv import load_dotenv, find_dotenv
from csv import reader

load_dotenv(find_dotenv())

username        = os.environ.get("ARANGO_USER")
password        = os.environ.get("ARANGO_PASSWORD")
classes_path    = os.environ.get("CLASSES_PATH")
database_name   = os.environ.get("DATABASE_NAME")
collection_name = os.environ.get("COLLECTION_NAME")

conn = Connection(username=username, password=password)
if not conn.hasDatabase(database_name):
    conn.createDatabase(name=database_name)

db = conn["ufrj"]
if not db.hasCollection(collection_name):
    db.createCollection(name=collection_name)

collection = db["Flowchart"]

# open file in read mode
with open(classes_path, 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    next(csv_reader)
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        document = collection.createDocument()
        document["name"]     = row[0]
        document["credits"]  = row[1]
        document["semester"] = row[3]
        document._key        = row[2]

        try:
            document.save()
        except:
            print(f"[Warning] Key {row[2]} already in the collection")