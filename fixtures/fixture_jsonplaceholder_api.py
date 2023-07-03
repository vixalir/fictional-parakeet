from api.jsonplaceholder_api import JSONPlaceholderAPI
import pytest
import os

API_URL = os.environ.get("API_URL", "https://jsonplaceholder.typicode.com")


@pytest.fixture(scope="session")
def json_placeholder_api():
    return JSONPlaceholderAPI(API_URL)
