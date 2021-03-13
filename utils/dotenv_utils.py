import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def initialize_parameters():
    return {"username": os.environ.get("ARANGO_USER"),
            "password": os.environ.get("ARANGO_PASSWORD"),
            "classes_path": os.environ.get("CLASSES_PATH"),
            "requirements_path": os.environ.get("REQUIREMENTS_PATH"),
            "database_name": os.environ.get("DATABASE_NAME"),
            "collection_name": os.environ.get("COLLECTION_NAME"),
            "graph_name": os.environ.get("GRAPH_NAME"),
            "edge_name": os.environ.get("EDGE_NAME")}