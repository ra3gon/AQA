from .base_api import BaseAPI
from schemas.employee import EmployeeCreate, EmployeeResponse, UpdateEmployeeDto
from pydantic import ValidationError


class EmployeeAPI(BaseAPI):
    def __init__(self, base_url, token):
        super().__init__(base_url)
        self.headers = {"Authorization": f"Bearer {token}"}

    def create_employee(self, data: dict):
        try:
            EmployeeCreate(**data)  # Валидируем входные данные
        except ValidationError as e:
            raise ValueError(f"Validation error: {e}")

        response = self.post("/employee", json=data, headers=self.headers)
        response.raise_for_status()
        return EmployeeResponse(**response.json())  # Валидируем ответ

    def get_employee_by_id(self, employee_id: int):
        response = self.get(f"/employee/{employee_id}", headers=self.headers)
        response.raise_for_status()
        return EmployeeResponse(**response.json())

    def update_employee(self, employee_id: int, data: dict):
        try:
            UpdateEmployeeDto(**data)
        except ValidationError as e:
            raise ValueError(f"Validation error: {e}")

        response = self.patch(f"/employee/{employee_id}", json=data, headers=self.headers)
        response.raise_for_status()
        return EmployeeResponse(**response.json())
