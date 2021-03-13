from pyArango.collection import Collection, Field, Edges
from pyArango.graph import Graph, EdgeDefinition

class Classes(Collection):
    _fields = {
        "course": Field(),
        "name": Field(),
        "credits": Field(),
        "code": Field(),
        "semester": Field()
    }

class Requirements(Edges): 
    _fields = {
        "label": Field()
    }

class Flowchart(Graph) :
    _edgeDefinitions = [EdgeDefinition("Requirements", fromCollections=["Classes"], toCollections=["Classes"])]
    _orphanedCollections = []
