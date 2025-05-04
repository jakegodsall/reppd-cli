import os
import json
import requests
from utils.config import get_config_data
from utils.exceptions import ConfigurationError

class ReppdClient:
    def __init__(self):
        self._base_path = None
        self.client = requests.Session()
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    @property
    def base_path(self):
        if not self._base_path:
            base_path = os.getenv('REPPD_BASE_PATH', '')
            if base_path == '':
                raise RuntimeError("Reppd base path is not valid")
            self._base_path = base_path
        return self._base_path

    def authenticate(self):
        """
        Authenticate with Reppd and store the
        session key inside the session object.
        """
        config = get_config_data()

        if config is None:
            raise ConfigurationError("Missing configuration")
        if "email" not in config or "password" not in config:
            raise ConfigurationError("Missing required credentials in config")
        
        try:
            response = self.client.post(
                f"{self.base_path}/login",
                json=config,
                headers=self.headers,
                verify=False
            )

            response.raise_for_status()

            json_response = response.json()

            token = json_response.get("token")
            if not token:
                raise ValueError("No token was returned from the response.")

            self.client.headers.update({"Authorization": f"Bearer {token}"})
            print(f"Authentication successful. Token: {token}")
        except requests.RequestException as req_err:
            raise RuntimeError(f"Request failed: {req_err}")
        except ValueError as val_err:
            raise RuntimeError(f"Unexpected response format: {val_err}")


    def make_request_with_reauth(
            self,
            endpoint: str,
            method: str = 'GET',
            retries: int = 1,
            **kwargs
        ):
        """
        Make a request to the provided endpoint with
        retries if the session has expired.
        """
        try:
            if method == 'GET':
                response = self.client.get(url=endpoint, **kwargs)
            if method == 'POST':
                response = self.client.post(url=endpoint, **kwargs)
        
            if response.status_code == 401 and retries > 0:
                print("Unauthorised. Reauthenticating...")
                self.authenticate()
                self.make_request_with_reauth(
                    endpoint,
                    method,
                    retries=retries-1,
                    **kwargs
                )

            response.raise_for_status()
            return response

        except requests.RequestException as req_err:
            raise RuntimeError(f"Request failed: {req_err}")
        
    def get_competency_list(self):
        endpoint = f"{self.base_path}/competencies"
        try:
            response = self.make_request_with_reauth(
                endpoint=endpoint,
                method='GET',
                retries=3,
                verify=False,
            )
            print(response.text)
        except requests.RequestException as req_err:
            raise RuntimeError(f"Request failed: {req_err}")
