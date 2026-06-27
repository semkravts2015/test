from typing import TypeVar, Type
from pydantic import BaseModel
import requests

Res = TypeVar("Res", bound=BaseModel)


class HttpClient:

    def __init__(self, base_url: str):
        self.base_url = base_url

    def post(self, route: str, request: BaseModel, response_model: Type[Res]) -> Res:
        response = requests.post(f"{self.base_url}{route}", json=request.model_dump())

        return response_model.model_validate(response.json())