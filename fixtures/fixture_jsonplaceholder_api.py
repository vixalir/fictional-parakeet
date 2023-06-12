from api.jsonplaceholder_api import JSONPlaceholderAPI
import pytest


@pytest.fixture
def json_placeholder_api():
    return JSONPlaceholderAPI()
