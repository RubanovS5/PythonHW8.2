import requests
import random
from employeApi import EmployeeApi
url = "https://x-clients-be.onrender.com"

api = EmployeeApi(url)
def test_create_new_employee():
    user = 'bloom'
    password = 'fire-fairy'
    api.get_token(user, password)  
    name = "Новая"
    description = "Супер 555"
    company_id = api.create_new_company(name=name, description=description)
    employee_before = api.get_employee(name=name, description=description)  
    api.add_employee(
        id="3158",
        first_name="Sasha",
        last_name="Doe",
        middle_name="Ivanovich",
        company_id= company_id,
        mail="datch@example.com",
        employee_url="http://example.com",
        phone="8976493208",
        birthdate='2024-03-06T11:24:56.028Z',
        is_active=True
    )
    employee_after = api.get_employee(name=name, description=description)
    assert  len(employee_before) < len(employee_after) 

def test_create_new_employee_76421():
    user = 'bloom'
    password = 'fire-fairy'
    api.get_token(user, password)  
    name = "Топовая"
    description = "Лучшая компания"
    company_id = api.create_new_company(name = name, description=description)
