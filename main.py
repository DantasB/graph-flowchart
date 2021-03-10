import os

from pyArango.connection import *
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

username = os.environ.get("ARANGO_USER")
password = os.environ.get("ARANGO_PASSWORD")

conn                = Connection(username=username, password=password)
db                  = conn.createDatabase(name="ufrj")
flowchartCollection = db.createCollection(name="Flowchart")
