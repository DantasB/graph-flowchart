import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def initialize_parameters():
    print("[Debug] Loading dotenv parameters.")
    try:
        return {"username": os.environ.get("ARANGO_USER"),
                "password": os.environ.get("ARANGO_PASSWORD"),
                "classes_path": os.environ.get("CLASSES_PATH"),
                "requirements_path": os.environ.get("REQUIREMENTS_PATH"),
                "database_name": os.environ.get("DATABASE_NAME"),
                "collection_name": os.environ.get("COLLECTION_NAME"),
                "graph_name": os.environ.get("GRAPH_NAME"),
                "edge_name": os.environ.get("EDGE_NAME")}
    except:
        print("[Error] Incorrect .env parameters. Please check the README for more information.")
        return {"username": "",
                "password": "",
                "classes_path": "",
                "requirements_path": "",
                "database_name": "",
                "collection_name": "",
                "graph_name": "",
                "edge_name": ""}
