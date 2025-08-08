# Do your changes here, then push your code.
import requests
class RequestFactory:
    BASE_URL = "https://httpbin.org"

    def __init__(self, path, method, headers=None, data=None):
        self.url = self.BASE_URL + path
        self.method = method.lower()
        self.headers = headers or {}
        self.data = data

    def send(self):
        if self.method == "post":
            response = requests.post(self.url, headers=self.headers, data=self.data)
        elif self.method == "get":
            response = requests.get(self.url, headers=self.headers, params=self.data)
        elif self.method == "put":
            response = requests.put(self.url, headers=self.headers, data=self.data)
        elif self.method == "delete":
            response = requests.delete(self.url, headers=self.headers, data=self.data)
        else:
            raise ValueError("Unsupported HTTP method")
        return response
factory = RequestFactory(path="/post", method="post", headers={"case": "Deniz Kaan"}, data={"name":"Deniz Kaan"})
response = factory.send()
print(response.text)
factory = RequestFactory(path="/get", method="get", headers={"case": "Deniz Kaan"}, data={"query": "test"})
response = factory.send()
print(response.text)

factory = RequestFactory(path="/put", method="put", headers={"case": "Deniz Kaan"}, data={"name":"Guncellendi"})
response = factory.send()
print(response.text)

factory = RequestFactory(path="/delete", method="delete", headers={"case":"Deniz Kaan"}, data={"id": "123"})
response = factory.send()
print(response.text)





