import requests
import random 
class EmployeeApi:
    url = "https://x-clients-be.onrender.com"
    def __init__(self,url):
        self.url = url
    def get_token(self, user = 'bloom', password = 'fire-fairy'):
        creds = {'username': user,
             'password': password}
        resp = requests.post(self.url + '/auth/login', json=creds)
        self.user_token = resp.json()["userToken"]
        return self.user_token

    def create_new_company(self, name, description):
        company = {"name": name, 
        "description": description}
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/company', json=company, headers=my_headers)
        return resp.json()["id"]
    

    def get_employee(self, name, description):
        params = {
        'name': name,
        'description': description
    }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.get(self.url + '/employee', params=params, headers=my_headers)
        return resp.json()


    def add_employee(self, name, description, id, first_name, last_name, middle_name, company_id, mail, employee_url, phone, birthdate, is_active):
        company = {"name": name, 
        "description": description}
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/company', json=company, headers=my_headers)
        company_id = resp.json()["id"]
        employee_data = {
        "id": id,
        "first_name": first_name,
        "last_name": last_name,
        "middle_name": middle_name,
        "company_id": company_id,
        "mail": mail,
        "employee_url": employee_url,
        "phone": phone,
        "birthdate": birthdate,
        "is_active": is_active
    }
        if not all([first_name, last_name, company_id, mail, phone, birthdate]): 
          raise ValueError("Не все обязательные поля заполнены") 
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(self.url + '/employee', json = employee_data, headers = my_headers)
        return resp.json()
