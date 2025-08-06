# Do your changes here, then push your code.
import os
import requests
from dotenv import load_dotenv

load_dotenv()

class RequestFactory:
    def __init__(self, path, method, headers=None, data=None):
        self.base_url = os.getenv("BASE_URL")
        self.path = path
        self.method = method.lower()
        self.headers = headers
        self.data = data

    def send(self):
        url = self.base_url + self.path

        # Hangi metodla çalışacağını seç
        if self.method == "get":
            response = requests.get(url, headers=self.headers, params=self.data)
        elif self.method == "post":
            response = requests.post(url, headers=self.headers, json=self.data)
        elif self.method == "put":
            response = requests.put(url, headers=self.headers, json=self.data)
        elif self.method == "delete":
            response = requests.delete(url, headers=self.headers, json=self.data)
        else:
            raise ValueError("Unsupported HTTP method")

        print("Status Code:", response.status_code)
        print("Response Body:", response.text)


if __name__ == "__main__":
    factory = RequestFactory(
        path="/post",
        method="POST",
        headers={"Case": "Octoxlabs"},
        data={"name": "octoxlabs"}
    )
    factory.send()
