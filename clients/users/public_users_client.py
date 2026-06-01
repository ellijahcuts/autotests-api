from clients.api_client import APIClient
from httpx import Response
from typing import TypedDict

class PublicUsersDict(TypedDict):
    """
    Описание структуры запроса для создания пользователя.
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(APIClient):
    """
    API клиент для публичных методов эндпоинта /api/v1/users.
    Не требует авторизации.
    """

    def create_user_api(self, request: PublicUsersDict) -> Response:
        """
        Создание нового пользователя.
        :param request: Словарь с данными пользователя (email, password, lastName, firstName, middleName)
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request)