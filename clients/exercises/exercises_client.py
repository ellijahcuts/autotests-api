from httpx import Response

from clients.api_client import APIClient

from typing import TypedDict
from clients.private_http_builder import get_private_http_client, AuthorizationUserDict

class GetExerciseQueryDict(TypedDict):
    """
    Описание структуры запроса на получение списка заданий.
    """
    courseId: str

class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание заданий.
    """
    title: str
    courseId: str
    maxScore: int | None
    minScore: int | None
    orderIndex : int
    description: str
    estimatedTime: str | None

class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление задания.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex : int | None
    description: str | None
    estimatedTime: str | None

class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """
    def get_exercises_api(self, query: GetExerciseQueryDict) -> Response:
        """
        Метод получения списка заданий.
        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises", params=query)

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения задания.
        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод создания задания.
        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(f"/api/v1/exercises", json=request)

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
        """
        Метод обновления задания.
        :param exercise_id: Идентификатор задания.
        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления задания.
        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

def get_private_exercises_client(user:AuthorizationUserDict) -> ExercisesClient:
    """
    Функция создаёт экземпляр PrivateClient с уже настроенным HTTP-клиентом.
    :return: Готовый к использованию PrivateClient.
    """
    return ExercisesClient(client=get_private_http_client(user))