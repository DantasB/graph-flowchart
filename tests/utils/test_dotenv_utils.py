import pytest
from src.utils.dotenv_utils import initialize_parameters

class TestDotenvUtils(object):
    def test_initialize_parameters(self):
        actual = initialize_parameters()

        not_expected = {"username": "",
                "password": "",
                "classes_path": "",
                "requirements_path": "",
                "database_name": "",
                "collection_name": "",
                "graph_name": "",
                "edge_name": ""}

        assert actual != not_expected
