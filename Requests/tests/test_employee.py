import pytest


def test_create_employee_positive(employee_api):
    data = {
        "first_name": "John",
        "last_name": "Doe",
        "company_id": 1,
        "email": "john.doe@example.com",
        "phone": "+79998881234",
        "birthdate": "1990-01-01",
        "is_active": True
    }
    response = employee_api.create_employee(data)
    assert response.id > 0
    assert response.first_name == "John"
    assert response.email == "john.doe@example.com"


def test_create_employee_validation_error(employee_api):
    data = {
        "first_name": "",  # Неверное имя
        "last_name": "Doe",
        "company_id": 1,
        "email": "invalid-email",  # Неверный email
        "phone": "123",  # Неверный телефон
        "birthdate": "1990-01-01",
        "is_active": True
    }
    with pytest.raises(ValueError):
        employee_api.create_employee(data)


def test_get_employee_by_id(employee_api):
    response = employee_api.get_employee_by_id(1)
    assert response.id == 1
    assert response.first_name is not None
