from httpx import Client

from clients.authentication.authentication_client import get_authentication_client, LoginRequestDict
from typing import TypedDict

class AuthorizationUserDict(TypedDict):
    email: str
    password: str


def get_private_http_client(user:AuthorizationUserDict) -> Client:
    """
    Функция создаёт экземпляр httpx.Client с базовыми настройками.
    :param user: Обьект со схемой авторизации и данными email и password
    :return: Готовый к использованию объект httpx.Client.
    """
    authorization_client = get_authentication_client()
    login_request = LoginRequestDict(email=user['email'], password=user['password'])
    login_response = authorization_client.login(login_request)
    return Client(
        timeout=100,
        base_url="http://localhost:8000",
        headers={"Authorization": f'Bearer {login_response['token']["accessToken"]}'},
    )