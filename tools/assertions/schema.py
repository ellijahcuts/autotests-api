from jsonschema import validate
from jsonschema.validators import Draft202012Validator
from typing import Any


def validate_json_schema(instance: Any, schema: dict) -> None:
    """
    Функция проверяет соответствие JSON-обьекта заданной JSON-схеме
    :param instance: Данные которые нужно проверить
    :param schema: Ожидаемый результат
    :raises: json.exceptions.ValidationError: Если instance не соответствует schema
    """
    validate(
        instance=instance,
        schema=schema,
        format_checker=Draft202012Validator.FORMAT_CHECKER
    )