import os
import requests
from dotenv import load_dotenv

class RequestFactory:
    def __init__(self, method, path, headers=None, data=None):
        load_dotenv() 
        self.base_url = os.getenv("BASE_URL")  
        self.method = method.lower()          
        self.path = path                      
        self.headers = headers or {}   #1        
        self.data = data or {}                 
    def send(self):
        url = self.base_url + self.path
        try:
            response = requests.request(
                method=self.method,
                url=url,
                headers=self.headers,
                json=self.data
            )
            print("Status Code:", response.status_code)
            print("Response:", response.json())
            return response
        except requests.RequestException as e:
            print("An error occurred:", e)
            return None
