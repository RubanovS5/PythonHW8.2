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
        company = {"name": name, "description": description}
        company_id = self.create_new_company(name, description)  
        params = {'name': name, 'description': description} 
        resp = requests.get(self.url + '/employee', params=params)
        return resp.json()


    def add_employee(self, name=None, description=None, **employee_data): 
        id = random.randint(1, 1000) 
        first_name = employee_data.get('first_name') 
        last_name = employee_data.get('last_name') 
        middle_name = employee_data.get('middle_name') 
        company_id = self.create_new_company(name, description) 
        mail = employee_data.get('mail') 
        employee_url = employee_data.get('url') 
        phone = employee_data.get('phone') 
        birthdate = employee_data.get('birthdate') 
        is_active = employee_data.get('is_active', True) 
        if not all([first_name, last_name, company_id, mail, phone, birthdate]): 
          raise ValueError("Не все обязательные поля заполнены") 
        add_employee_data = { 
            "id": id, 
            "firstName": first_name, 
            "lastName": last_name, 
            "middleName": middle_name, 
            "companyId": company_id, 
            "email": mail, 
            "url": employee_url, 
            "phone": phone, 
            "birthdate": birthdate, 
            "isActive": is_active 
        } 
        my_headers = {} 
        my_headers["x-client-token"] = self.get_token() 
        resp = requests.post(self.url+'/employee', json=add_employee_data, headers=my_headers) 
        return resp.json()

  