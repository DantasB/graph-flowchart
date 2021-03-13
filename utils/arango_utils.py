from csv import reader
from classes.graph import Flowchart
from pyArango.connection import *

def login_to_database(username, password):
    return Connection(username=username, password=password)

def create_database(username, password, database_name):
    connection = login_to_database(username, password)
    if not connection.hasDatabase(database_name):
        connection.createDatabase(name=database_name)
    
    return connection[database_name]

def safe_create_collection(db, collection_name, class_name):
    if not db.hasCollection(collection_name):
        db.createCollection(className=class_name, name=collection_name)

    return db[collection_name]

def create_vertexes(db, collection_name, vertex_path):
    collection = safe_create_collection(db, collection_name, "Collection")

    # open file in read mode
    with open(vertex_path, 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        next(csv_reader)
        # Iterate over each row in the csv using reader object
        for row in csv_reader:
            document = collection.createDocument()
            document["course"]   = row[0]
            document["name"]     = row[1]
            document["credits"]  = row[2]
            document["semester"] = row[4]
            document._key        = row[3].strip()

            try:
                document.save()
            except:
                print(f"[Warning] Key {row[3].strip()} already in the collection")

def create_edges(db, edge_name, edges_path):
    collection = safe_create_collection(db, edge_name, "Edges")

    with open(edges_path, 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        next(csv_reader)
        # Iterate over each row in the csv using reader object
        for row in csv_reader:
            document          = collection.createDocument()
            document._from    = row[0].strip()
            document._to      = row[1].strip()
            document._key     = row[0].strip().split('/')[1] + "TO" + row[1].strip().split('/')[1]
            document["label"] = row[2].strip()
            try:
                document.save()
            except:
                print(f"[Warning] Couldn't save {row[0].strip().split('/')[1]} to {row[1].strip().split('/')[1]} edge. Already in the collection")

def create_graph(db, graph_name):
    if not db.hasGraph(graph_name):
        theGraph = db.createGraph(graph_name)