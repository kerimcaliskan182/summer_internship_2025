import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://httpbin.org")

class BaseRequestFactory:
    def __init__(self, path, headers=None, data=None):
        # Basic validations
        if not isinstance(path, str) or not path.startswith("/"):
            raise ValueError("Path must be a string starting with '/'")
        if headers is not None and not isinstance(headers, dict):
            raise TypeError("Headers must be a dictionary.")
        if data is not None and not isinstance(data, dict):
            raise TypeError("Data must be a dictionary.")

        self.base_url = BASE_URL
        self.path = path
        self.headers = headers or {}
        self.data = data or {}

    def send(self):
        raise NotImplementedError("Warning: You should implement this method in the subclass!")

class GetRequestFactory(BaseRequestFactory):
    def send(self):
        url = self.base_url + self.path
        response = requests.get(url, headers=self.headers, params=self.data)
        print(f"GET {url} - Status: {response.status_code}")
        print(response.text)
        return response

class PostRequestFactory(BaseRequestFactory):
    def send(self):
        url = self.base_url + self.path
        response = requests.post(url, headers=self.headers, json=self.data)
        print(f"POST {url} - Status: {response.status_code}")
        print(response.text)
        return response

class PutRequestFactory(BaseRequestFactory):
    def send(self):
        url = self.base_url + self.path
        response = requests.put(url, headers=self.headers, json=self.data)
        print(f"PUT {url} - Status: {response.status_code}")
        print(response.text)
        return response

class DeleteRequestFactory(BaseRequestFactory):
    def send(self):
        url = self.base_url + self.path
        response = requests.delete(url, headers=self.headers, json=self.data)
        print(f"DELETE {url} - Status: {response.status_code}")
        print(response.text)
        return response

if __name__ == "__main__":
    get_factory = PutRequestFactory(path="/put", headers={"Case": "Octoxlabs"}, data={"name": "octoxlabs"})
    get_factory.send()

    post_factory = DeleteRequestFactory(path="/delete", headers={"Case": "Octoxlabs"}, data={"name": "octoxlabs"})
    post_factory.send()
