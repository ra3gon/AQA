from .base_api import BaseAPI


class AuthAPI(BaseAPI):
    def get_token(self, username, password):
        data = {"username": username, "password": password}
        response = self.post("/auth/login", json=data)
        response.raise_for_status()
        return response.json()["user_token"]
