import pytest


@pytest.fixture(autouse=True, scope="function")
def enable_db_access_for_all_tests(db):
    """
    give access to all tests
    """


@pytest.fixture()
def api_client():
    from rest_framework.test import APIClient
    client = APIClient()
    yield client
