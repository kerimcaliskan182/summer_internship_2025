# Do your changes here, then push your code.
import os
import requests
from dotenv import load_dotenv

load_dotenv()

class RequestFactory:
    def __init__(self, path, method, headers=None, data=None):
        self.base_url = os.getenv("BASE_URL")

        self.path = self.validate_path(path)
        self.method = self.validate_method(method)
        self.headers = self.validate_dict(headers, "headers")
        self.data = self.validate_dict(data, "data")

    def validate_base_url(self):
        if not self.base_url or not isinstance(self.base_url, str):
            raise ValueError("BASE_URL is missing or invalid in the .env file.")

    def validate_path(self, path):
        if not isinstance(path, str):
            raise ValueError("Path must be a string.")
        if not path.startswith("/"):
            raise ValueError("Path must start with '/'.")
        return path

    def validate_method(self, method):
        if not isinstance(method, str):
            raise ValueError("HTTP method must be a string.")
        method_lower = method.lower()
        if method_lower not in ["get", "post", "put", "delete"]:
            raise ValueError(f"Unsupported HTTP method: {method}")
        return method_lower

    def validate_dict(self, value, name):
        if value is None:
            return {}
        if not isinstance(value, dict):
            raise ValueError(f"{name} must be a dictionary.")
        return value    

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
