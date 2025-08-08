import os
import requests
from dotenv import load_dotenv

load_dotenv()

class RequestFactory:
    def __init__(self, method, path, headers=None, data=None):
        self.base_url = os.getenv("BASE_URL", "https://httpbin.org")

        # Basic input validations
        if not isinstance(method, str):
            raise TypeError("Method must be a string.")
        if method.upper() not in {"GET", "POST", "PUT", "DELETE"}:
            raise ValueError("Method must be one of: GET, POST, PUT, DELETE.")
        self.method = method.lower()

        if not isinstance(path, str) or not path.startswith("/"):
            raise ValueError("Path must be a string starting with '/'.")
        self.path = path

        if headers is not None and not isinstance(headers, dict):
            raise TypeError("Headers must be a dictionary.")
        self.headers = headers or {}

        if data is not None and not isinstance(data, dict):
            raise TypeError("Data must be a dictionary.")
        self.data = data or {}

    def send(self):
        url = self.base_url + self.path
        response = requests.request(
            method=self.method,
            url=url,
            headers=self.headers,
            json=self.data
        )
        print("Status Code:", response.status_code)
        print("Response:", response.text)
        return response

if __name__ == "__main__":
    factory = RequestFactory(
        method="GET",
        path="/get",
        headers={"Case": "Octoxlabs"},
        data={"name": "octoxlabs"}
    )
    factory.send()
