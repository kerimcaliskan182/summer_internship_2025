# Do your changes here, then push your code.
import os
import requests
from abc import ABC, abstractmethod
from dotenv import load_dotenv

load_dotenv()

class BaseRequestFactory(ABC):
    def __init__(self, path, headers=None, data=None):
        self.base_url = os.getenv("BASE_URL")
        self.path = path
        self.headers = headers or {}
        self.data = data or {}

    @abstractmethod
    def send(self):
        pass

# GET class
class GetRequestFactory(BaseRequestFactory):
    def send(self):
        url = self.base_url + self.path
        response = requests.get(url, headers=self.headers, params=self.data)
        print("GET Response:")
        print("Status code:", response.status_code)
        print("Response body:", response.text)

# POST class
class PostRequestFactory(BaseRequestFactory):
    def send(self):
        url = self.base_url + self.path
        response = requests.post(url, headers=self.headers, json=self.data)
        print("POST Response:")
        print("Status code:", response.status_code)
        print("Response body:", response.text)

# PUT class
class PutRequestFactory(BaseRequestFactory):
    def send(self):
        url = self.base_url + self.path
        response = requests.put(url, headers=self.headers, json=self.data)
        print("PUT Response:")
        print("Status code:", response.status_code)
        print("Response body:", response.text)

# DELETE class
class DeleteRequestFactory(BaseRequestFactory):
    def send(self):
        url = self.base_url + self.path
        response = requests.delete(url, headers=self.headers, json=self.data)
        print("DELETE Response:")
        print("Status code:", response.status_code)
        print("Response body:", response.text)


# Test 
get_factory = GetRequestFactory(
    path="/get",
    headers={"Case": "Octoxlabs"},
    data={"name": "octoxlabs"}
)
get_factory.send()

post_factory = PostRequestFactory(
    path="/post",
    headers={"Case": "Octoxlabs"},
    data={"name": "octoxlabs"}
)
post_factory.send()

put_factory = PutRequestFactory(
    path="/put",
    headers={"Case": "Octoxlabs"},
    data={"name": "octoxlabs"}
)
put_factory.send()

delete_factory = DeleteRequestFactory(
    path="/delete",
    headers={"Case": "Octoxlabs"},
    data={"name": "octoxlabs"}
)
delete_factory.send()

