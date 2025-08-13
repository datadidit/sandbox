from fastapi.testclient import TestClient
import pytest
from hello_api.my_app import app

@pytest.fixture(name="client")
def _client():
    return TestClient(app)

client = TestClient(app)

def test_hello():
    """
    Root URL greets the world
    """
    # print("Hello World")
    resp = client.get("/")
    
    assert 200 == resp.status_code

    assert {'message': 'Hello World'} == resp.json()