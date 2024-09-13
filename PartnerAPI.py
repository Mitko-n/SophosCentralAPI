import time
import requests
from requests.adapters import Retry, HTTPAdapter


class Tenant:
    def __init__(self, client_id, client_secret):
        self._client_id = client_id
        self._client_secret = client_secret
        self._access_token = None
        self._token_expiry = None
        self._tenant_id = None
        self._tenant_api_host = None
        self._session = self._create_session()
        self._authenticate()

    def _create_session(self):
        retry_strategy = Retry(
            total=5,
            allowed_methods=["GET", "POST", "PATCH", "DELETE", "PUT"],
            status_forcelist=[429, 500, 502, 503, 504],
            backoff_factor=2,
            raise_on_status=False,
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session = requests.Session()
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        return session

    def _authenticate(self):
        if self._session is None:
            self._session = self._create_session()

        url = "https://id.sophos.com/api/v2/oauth2/token"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        payload = {
            "grant_type": "client_credentials",
            "scope": "token",
            "client_id": self._client_id,
            "client_secret": self._client_secret,
        }
        response = self._session.post(url, headers=headers, data=payload)
        response.raise_for_status()
        response_json = response.json()
        self._access_token = response_json["access_token"]
        self._token_expiry = time.time() + response_json["expires_in"] - 120

        url = "https://api.central.sophos.com/whoami/v1"
        headers = {"Authorization": f"Bearer {self._access_token}", "Accept": "application/json"}
        response = self._session.get(url, headers=headers)
        response.raise_for_status()
        response_json = response.json()
        self._tenant_id = response_json["id"]
        self._tenant_api_host = response_json["apiHosts"]["dataRegion"]

    def _get_headers(self):
        if time.time() > self._token_expiry:
            self._authenticate()
        return {
            "X-Tenant-ID": self._tenant_id,
            "Authorization": f"Bearer {self._access_token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    def _request(self, method, endpoint, **kwargs):
        if self._session is None:
            return {"status": "error", "error": "Session is closed.", "details": "Session is closed."}

        url = f"{self._tenant_api_host}{endpoint}"
        try:
            response = self._session.request(method, url, headers=self._get_headers(), **kwargs)

            if response.ok:
                return {"status": "success", "data": response.json()}
            else:
                return {"status": "error", "error": f"Request failed with status code {response.status_code}", "details": response.text}
        except requests.RequestException as e:
            return {"status": "error", "error": "Request exception occurred.", "details": str(e)}

    def get(self, endpoint, **kwargs):
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint, **kwargs):
        return self._request("POST", endpoint, **kwargs)

    def patch(self, endpoint, **kwargs):
        return self._request("PATCH", endpoint, **kwargs)

    def delete(self, endpoint, **kwargs):
        return self._request("DELETE", endpoint, **kwargs)

    def put(self, endpoint, **kwargs):
        return self._request("PUT", endpoint, **kwargs)

    def close(self):
        if self._session:
            self._session.close()
            self._session = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return False


class Partner(Tenant):
    pass