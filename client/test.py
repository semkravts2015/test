import requests
from enum import StrEnum
from pydantic import BaseModel


class HttpMethod(StrEnum):
    GET = "GET"
    POST = "POST"


class ApiRoutes(StrEnum):
    GET_INFO = "/api/v1/orders/1"


class HttpClient:

    def __init__(self, session: requests.Session, base_url: str):
        self.session = session
        self.base_url = base_url

    def request(self, method: HttpMethod, route: ApiRoutes, **kwargs) -> requests.Response:
        response = self.session.request(method=method, url=f"{self.base_url}{route}", **kwargs)

        response.raise_for_status()

        return response

    def get(self, route: ApiRoutes, **kwargs) -> requests.Response:
        return self.request(HttpMethod.GET, route, **kwargs)


class UserInfo(BaseModel):
    id: int
    user_id: int
    product: str
    quantity: int
    status: str


client = HttpClient(
    session=requests.Session(),
    base_url="http://localhost:8000"
)

response = client.get(ApiRoutes.GET_INFO)

user = UserInfo.model_validate(response.json())

print(user)
print(user.id)
print(user.product)