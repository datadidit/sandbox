"""
Test issue using non aware datetimes and polyfactory
"""
import logging as log
import json
import pytest
from polyfactory.factories.pydantic_factory import ModelFactory

from python_examples.pydantic.awaredatetime.user import User, UserAwareDateTime
from fastapi.testclient import TestClient
from python_examples.pydantic.awaredatetime.user_router import app

class UserFactory(ModelFactory[User]):
    """
    User factory.
    """
    pass

class UserFactoryAwareDatetime(ModelFactory[UserAwareDateTime]):
    pass


@pytest.fixture
def user() -> User:
    """Simple user fixture."""
    return UserFactory.build()

@pytest.fixture
def user_aware_datetime():
    """Simple user w/ AwareDatetime."""
    return UserFactoryAwareDatetime.build()


def test_user(user):
    """Simple user test w/ polyfactory."""
    a_user = user
    
    assert isinstance(a_user, User)
    raw_json = a_user.model_dump_json(indent=4)
    log.info(f"{raw_json}")
    # user_2 = User(first_name="Paul", last_name="Atriedes")
    # log.info(user_2.model_dump_json())
    # assert a_user == User.model_validate_json(raw_json)
    # Now read this in
    # User(**raw_json)

def test_user_aware_datetime(user_aware_datetime):
    log.info(f"{user_aware_datetime}")
    # raw_json = user_aware_datetime.model_dump_json()


def test_update_user_fastapi(user):
    """Test updating a user."""
    client = TestClient(app)
    raw_json = user.model_dump_json()
    log.info(f"{raw_json}")
    # response = client.post("/ ", headers={"Content-Type": "application/json"}, content=raw_json)
    response = client.post("/", json=json.loads(raw_json))
    log.info(f"{response.json()}")
    assert response.status_code == 200
