import os
import requests

class RequestFactory:
    def __init__(self, method, path, headers=None, data=None):
        self.base_url ="http://127.0.0.1:8000"

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
            json=self.data
        )
        print("Status Code:", response.status_code)
        print("Response:", response.text)
        return response

for i in range(41):
    device_request = RequestFactory(
        method="POST",
        path="/api/devices/",
        data={
            "hostname": f"host{i}",
            "device_name": f"Device{i}",
            "device_type": "Router",
            "serial_number": f"SN{i}",
            "ip_address": f"192.168.0.{i}",
            "mac_address": f"AA:BB:CC:DD:EE:{i:02X}",
            "os_type": "Linux",
        }
    )
    device_request.send()


    

