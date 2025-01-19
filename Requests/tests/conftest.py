import pytest
from pages.auth_api import AuthAPI
from pages.employee_api import EmployeeAPI

BASE_URL = "http://5.101.50.27:8000"
CREDS = {"username": "harrypotter", "password": "expelliarmus"}


@pytest.fixture(scope="session")
def token():
    auth = AuthAPI(BASE_URL)
    return auth.get_token(**CREDS)


@pytest.fixture(scope="session")
def employee_api(token):
    return EmployeeAPI(BASE_URL, token)
