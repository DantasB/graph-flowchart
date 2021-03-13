from utils.dotenv_utils import initialize_parameters
from utils.arango_utils import create_vertexes, create_edges, create_graph, create_database

parameters = initialize_parameters()

db = create_database(parameters["username"], parameters["password"], parameters["database_name"])

create_vertexes(db, parameters["collection_name"], parameters["classes_path"])
create_edges(db, parameters["edge_name"], parameters["requirements_path"])
create_graph(db, parameters["graph_name"])