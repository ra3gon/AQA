from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class EmployeeCreate(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    company_id: int = Field(..., gt=0)
    email: EmailStr
    phone: str = Field(..., regex=r"^\+?\d{10,15}$")
    birthdate: str = Field(..., regex=r"^\d{4}-\d{2}-\d{2}$")
    is_active: bool


class UpdateEmployeeDto(BaseModel):
    last_name: Optional[str] = Field(None, min_length=1, max_length=50)
    email: Optional[EmailStr]
    phone: Optional[str] = Field(None, regex=r"^\+?\d{10,15}$")
    is_active: Optional[bool]


class EmployeeResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    company_id: int
    email: EmailStr
    phone: str
    birthdate: str
    is_active: bool
