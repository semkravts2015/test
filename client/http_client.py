import requests
from enum import StrEnum

class HttpMethod(StrEnum):
    GET = 'GET'
    POST = 'POST'

class ApiRoutes(StrEnum):
    CREATE = '/create'


class HttpClient:
    def __init__(self, session: requests.Session, base_url: str):
        self.session = session
        self.base_url = base_url

    def request(self, method: HttpMethod, route: str, **kwargs) -> requests.Response:
        return self.session.request(method, self.base_url + route, **kwargs)

    def get(self, route: str, **kwargs) -> requests.Response:
        return self.request(HttpMethod.GET, route, **kwargs)

    def post(self, route: str, **kwargs) -> requests.Response:
        return self.request(HttpMethod.POST, route, **kwargs)

r = HttpClient(session=requests.Session(), base_url='https://petstore.swagger.io')
r.get(ApiRoutes.CREATE)