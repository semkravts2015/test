import requests
import http
import faker
from pydantic import BaseModel, EmailStr

fake = faker.Faker()

class UserCreation(BaseModel):
    id: int
    username: str
    firstName: str
    lastName: str
    email: str
    password: str
    phone: str
    userStatus: int

def UserGenerator():
    return UserCreation(
        id=0,
        username=fake.user_name(),
        firstName=fake.first_name(),
        lastName=fake.last_name(),
        email=fake.email(),
        password=fake.password(),
        phone=fake.phone_number(),
        userStatus=0)

class HttpClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()

    def post(self, route: str, **kwargs) -> requests.Response:
        return requests.post(self.base_url + route, **kwargs)

    def get(self, route: str) -> requests.Response:
        return requests.get(self.base_url + route)

def test_user_creation():
    BaseURL = 'https://petstore.swagger.io'
    r = HttpClient(base_url=BaseURL)
    user_data = UserGenerator()
    response = r.post('/v2/user', json=user_data.model_dump())
    assert response.status_code == http.HTTPStatus.OK
    print(response.json())
    response = r.get('/v2/user/logout')
    assert response.status_code == http.HTTPStatus.OK
    print(response.json())
