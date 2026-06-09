from uuid import uuid4
from pydantic import BaseModel, Field, EmailStr, ConfigDict


class UserSchema(BaseModel):
    """
    Описание структуры пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str = Field(default_factory=lambda: str(uuid4()))
    email: EmailStr
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')

class CreateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса для создания пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr
    password: str
    last_name: str  = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')

class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа при создании пользователя.
    """
    user: UserSchema

class UpdateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса для обновленияя пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr | None
    last_name: str | None = Field(alias='lastName')
    first_name: str | None = Field(alias='firstName')
    middle_name: str | None = Field(alias='middleName')

class GetUserResponseSchema(BaseModel):
    """
    Описание структуры ответа для получения пользователя.
    """
    user: UserSchema

class UpdateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа после обновления пользователя.
    """
    user: UserSchema