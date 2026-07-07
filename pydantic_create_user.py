from uuid import uuid4
from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    """
    Описание структуры пользователя.
    """
    id: str = Field(default_factory=lambda: str(uuid4()))
    email: EmailStr
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')

class CreateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса для создания пользователя.
    """
    email: EmailStr
    password: str
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')

class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа при создании пользователя.
    """
    user: UserSchema


new_user = CreateUserRequestSchema(
    email='Broski@agma.com',
    password='15866441',
    lastName="Last",
    firstName="First",
    middleName="Middle"
)

print('New user created: ', new_user)