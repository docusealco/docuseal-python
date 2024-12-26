import json
import urllib.parse
import http.client
from docuseal._version import VERSION


class ApiError(Exception):
    pass


class DocusealHttp:
    BODY_METHODS = {"POST", "PUT"}

    def __init__(self, config):
        self.config = config

    def get(self, path, params=None):
        return self.send_request("GET", path, params)

    def post(self, path, body=None):
        return self.send_request("POST", path, None, body)

    def put(self, path, body=None):
        return self.send_request("PUT", path, None, body)

    def delete(self, path, params=None):
        return self.send_request("DELETE", path, params)

    def send_request(self, method, path, params=None, body=None):
        if params is None:
            params = {}

        url = urllib.parse.urljoin(self.config["url"], path)
        full_path = f"{url}{self.to_query(params)}"

        parsed_url = urllib.parse.urlparse(full_path)
        connection_class = (
            http.client.HTTPSConnection
            if parsed_url.scheme == "https"
            else http.client.HTTPConnection
        )
        conn = connection_class(
            parsed_url.hostname or "", parsed_url.port, timeout=self.config.get("open_timeout", 60)
        )

        headers = self.headers()
        data = json.dumps(body) if body is not None else None

        conn.request(method, f"{parsed_url.path}?{parsed_url.query}", body=data, headers=headers)
        response = conn.getresponse()

        conn.sock.settimeout(self.config.get("read_timeout", 60))

        return self.handle_response(response)

    def headers(self):
        return {
            "X-Auth-Token": self.config["key"] or "",
            "Content-Type": "application/json",
            "User-Agent": f"DocuSeal Python v{VERSION}",
        }

    def to_query(self, params):
        if not params:
            return ""
        return f"?{urllib.parse.urlencode(params)}"

    def handle_response(self, response):
        response_body = response.read().decode("utf-8")
        if 200 <= response.status < 300:
            return json.loads(response_body)
        else:
            raise ApiError(f"API Error {response.status}: {response_body}")
