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
                data=config,
                headers=self.headers
            )

            response.raise_for_status()

            json_response = response.json()

            token = json_response.get("token")
            if not token:
                raise ValueError("No token was returned from the response.")

            self.client.headers.update({"Authorization": f"Bearer {token}"})
            print("Authentication successful.")
        except requests.RequestException as req_err:
            raise RuntimeError(f"Request failed: {req_err}")
        except ValueError as val_err:
            raise RuntimeError(f"Unexpected response format: {val_err}")



    def make_request_with_reauth(
            self,
            endpoint: str,
            retries: int = 1
        ):
        """
        Make a request to the provided endpoint with
        retries if the session has expired.
        """
        ...