from pydantic import BaseModel, Field


class Address(BaseModel):
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = Field(alias='isActive')
    #address : Address


user = User(
    id=1,
    name='Svetra',
    email='Smim@mail.ru',
    is_active=False,
    #address = Address(city="Minsk", zip_code="512312")
)
print(user.model_dump_json())
print(user.model_dump())