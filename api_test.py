import requests
from employeApi import EmployeeApi
url = "https://x-clients-be.onrender.com"

api = EmployeeApi(url)
def test_create_new_employee():
    user = 'bloom'
    password = 'fire-fairy'
    api.get_token(user, password)  
    name = "Призрак Цусимы"
    description = "Игра от сони"
    company_id = api.create_new_company(name, description)
    employee_before = api.get_employee(company_id)
    new_employee = api.add_employee(
        id="3158",
        first_name="Sasha",
        last_name="Morgan",
        middle_name="Ivanovich",
        company_id= company_id,
        mail="datch@example.com",
        employee_url="http://example.com",
        phone="8976493208",
        birthdate='2024-03-14T11:24:56.028Z',
        is_active=True
    )
    employee_after = api.get_employee(company_id)
    assert  len(employee_before) < len(employee_after)
    assert employee_after[-1]["id"] == new_employee["id"]
    assert employee_after[-1]["firstName"] == "Sasha"
    assert employee_after[-1]["lastName"] == "Morgan"
    assert employee_after[-1]["middleName"] == "Ivanovich"
    assert employee_after[-1]["companyId"] == company_id
    assert employee_after[-1]["email"] == None
    assert employee_after[-1]["avatar_url"] == "http://example.com"
    assert employee_after[-1]["phone"] == "8976493208"
    assert employee_after[-1]["birthdate"] == "2024-03-14"
    assert employee_after[-1]["isActive"] == True



def test_get_employee_id():
    user = 'musa'
    password = 'music-fairy'
    api.get_token(user, password)
    name = "OOO Питер"
    description = "Строительство мостов"
    company_id = api.create_new_company(name, description)
    returned_id = api.add_employee(
        id="7893",
        first_name="Kolya",
        last_name="Vannov",
        middle_name="Ivanovich",
        company_id=company_id,
        mail="datch@example.com",
        employee_url="http://google.com",
        phone="89214932428",
        birthdate='2024-03-11T15:23:56.028Z',
        is_active=True
    )
    employee_id = api.get_employee_id(returned_id)
    assert employee_id["id"] == returned_id["id"]
    assert employee_id["firstName"] == "Kolya"
    assert employee_id["lastName"] == "Vannov"
    assert employee_id["middleName"] == "Ivanovich"
    assert employee_id["companyId"] == company_id
    assert employee_id["email"] == None
    assert employee_id["avatar_url"] == "http://google.com"
    assert employee_id["phone"] == "89214932428"
    assert employee_id["birthdate"] == "2024-03-11"
    assert employee_id["isActive"] == True
    

    
def test_update_employee():
    user = 'donatello'
    password = 'does-machines'
    api.get_token(user, password)
    name = "ООО Моя Оборона"
    description = "Корпоративы, свадьбы"
    company_id = api.create_new_company(name, description)
    employee = api.add_employee(
        id="789",
        first_name="Dmitry ",
        last_name="Susloparov",
        middle_name="Vladimirovich",
        company_id=company_id,
        mail="catsh@example.com",
        employee_url="http://ya.ru/",
        phone="89879809089",
        birthdate='2024-03-13T13:23:56.028Z',
        is_active=True
    )
    api.change_employee(
        id = employee,
        change_lastName = "Teylor" ,
        change_email = "samurai@cyber.ru", 
        change_url = "https://www.google.ru/", 
        change_phone = "89763215423",
        change_active = False
    )
    id_update_employee = api.get_employee_id(employee)
    assert  id_update_employee["isActive"] == False
    assert  id_update_employee["email"] == "samurai@cyber.ru"
    assert  id_update_employee["avatar_url"] == "https://www.google.ru/"
   
