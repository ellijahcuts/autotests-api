from clients.api_client import APIClient
from httpx import Response
from clients.public_http_builder import get_public_http_client
from clients.users.users_shema import CreateUserRequestSchema, CreateUserResponseSchema


class PublicUsersClient(APIClient):
    """
    API клиент для публичных методов эндпоинта /api/v1/users.
    Не требует авторизации.
    """

    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Создание нового пользователя.
        :param request: Словарь с данными пользователя (email, password, lastName, firstName, middleName)
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/users", json=request.model_dump(by_alias=True))

    def create_user(self, request: CreateUserRequestSchema) -> CreateUserResponseSchema:
        """
        Описание структуры пользователя.
        """
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)


def get_public_users_client() -> PublicUsersClient:
    """
    Функция создаёт экземпляр PublicUsersClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию PublicUsersClient.
    """
    return PublicUsersClient(client=get_public_http_client())