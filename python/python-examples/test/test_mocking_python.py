"""Test mocking with python."""
import logging as log
import pytest
from unittest.mock import patch
from datetime import date
import requests

FAKE_RESULTS = None

def get_dune_character():
    """ Singleton function to get dune character(s)"""
    global FAKE_RESULTS
    if FAKE_RESULTS is None:
        # Retrieve results
        log.info("Attempting request")
        FAKE_RESULTS = requests.get("http://fakeurl.com/names")
    
    return FAKE_RESULTS


@patch("requests.get")
def test_unittest_singleton(mock_request):
    """Example mocking using"""
    x_return_value = ["Leto Atreides"]
    mock_request.return_value = x_return_value
    results = get_dune_character()
    log.info(f"Results {results}")
    assert x_return_value == results


@pytest.mark.xfail
@patch("requests.get")
def test_unittest_singleton_second_call(mock_request):
    """ Example mocking singleton second call that should fail because singleton already loaded. """
    x_return_value = ["Paul Atreides", "Leto Atreides"]
    mock_request.return_value = x_return_value
    results = get_dune_character()
    assert x_return_value == results


# You can use `auto-use` here to make this happen automatically
@pytest.fixture
def reload_module():
    import importlib
    import test_mocking_python
    importlib.reload(test_mocking_python)


@pytest.mark.parametrize("x_return_value", [
    (["Paul Atreides", "Leto Atreides"]),
    (["Sir Duncan Idaho"]),
    (["Lady Jessica"]),
    (["Feyd-Rautha Harkonnen"])
])
@patch("requests.get")
def test_unittest_singleton_reload(mock_request, reload_module, x_return_value):
    """ Example mocking singleton second call reload """
    mock_request.return_value = x_return_value
    results = get_dune_character()
    assert x_return_value == results