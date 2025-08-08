# Do your changes here, then push your code.
import os
import requests

BASE_URL = os.getenv("BASE_URL", "https://httpbin.org")

class BaseRequestFactory:
    def __init__(self, path="", headers=None, data=None):  
        self.url = f"{BASE_URL}{path}"
        self.headers = headers or {}
        self.data = data or {}

    def send(self):
        raise NotImplementedError("send() metodu alt siniflarda tanimlanmali.")


class GetRequestFactory(BaseRequestFactory):
    def send(self):
        response = requests.get(self.url, headers=self.headers, params=self.data)
        print("GET response:\n", response.text)
        return response


class PostRequestFactory(BaseRequestFactory):
    def send(self):
        response = requests.post(self.url, headers=self.headers, data=self.data)
        print("POST response:\n", response.text)
        return response


class PutRequestFactory(BaseRequestFactory):
    def send(self):




        response = requests.put(self.url, headers=self.headers, data=self.data)
        print("PUT response:\n", response.text)
        return response


class DeleteRequestFactory(BaseRequestFactory):
    def send(self):
        response = requests.delete(self.url, headers=self.headers, data=self.data)
        print("DELETE response:\n", response.text)
        return response



