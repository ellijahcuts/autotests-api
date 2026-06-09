from pydantic import BaseModel,Field, ConfigDict

class GetExerciseQuerySchema(BaseModel):
    """
    Описание структуры запроса на получение списка заданий.
    """
    model_config = ConfigDict(populate_by_name=True)

    course_id: str = Field(alias='courseId')

class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание заданий.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str
    course_id: str = Field(alias='courseId')
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    order_index : int = Field(alias='orderIndex')
    description: str
    estimated_time: str | None = Field(alias='estimatedTime')

class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление задания.
    """
    model_config = ConfigDict(populate_by_name=True)

    title: str | None
    max_score: int | None = Field(alias='maxScore')
    min_score: int | None = Field(alias='minScore')
    order_index : int | None = Field(alias='orderIndex')
    description: str | None
    estimated_time: str | None = Field(alias='estimatedTime')

class ExerciseSchema(BaseModel):
    """
    Описание структуры ответа на создание задания.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    title: str
    course_id: str = Field(alias='courseId')
    max_score: int = Field(alias='maxScore')
    min_score: int = Field(alias='minScore')
    order_index: int = Field(alias='orderIndex')
    description: str
    estimated_time: str | None = Field(alias='estimatedTime')

class GetExercisesResponseSchema(BaseModel):
    """
    Ответ будет в формате списка со всеми заданиями
    """
    exercises: list[ExerciseSchema]
class GetExerciseResponseSchema(BaseModel):
    """
    Структура ответа будет аналогична Exercise
    """
    exercise: ExerciseSchema