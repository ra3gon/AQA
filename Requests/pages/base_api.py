import requests


class BaseAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def post(self, endpoint, json=None, headers=None):
        return requests.post(f"{self.base_url}{endpoint}", json=json, headers=headers)

    def get(self, endpoint, headers=None):
        return requests.get(f"{self.base_url}{endpoint}", headers=headers)

    def patch(self, endpoint, json=None, headers=None):
        return requests.patch(f"{self.base_url}{endpoint}", json=json, headers=headers)
