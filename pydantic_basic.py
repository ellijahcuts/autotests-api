"""
{
  "course": {
    "id": "string",
    "title": "string",
    "maxScore": 0,
    "minScore": 0,
    "description": "string",
    "previewFile": {
      "id": "string",
      "filename": "string",
      "directory": "string",
      "url": "https://example.com/"
    },
    "estimatedTime": "string",
    "createdByUser": {
      "id": "string",
      "email": "user@example.com",
      "lastName": "string",
      "firstName": "string",
      "middleName": "string"
    }
  }
}
"""
from uuid import uuid4
from pydantic import BaseModel, Field, ConfigDict, computed_field, HttpUrl, EmailStr, ValidationError
from pydantic.alias_generators import to_camel

class PreviewFileSchema(BaseModel):
    id: str
    filename: str
    directory: str
    url: HttpUrl

class CreatedByUserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias='lastName')
    first_name: str = Field(alias='firstName')
    middle_name: str = Field(alias='middleName')
    @computed_field
    def username(self)->str:
        return f"{self.first_name} {self.last_name}"
    def get_username(self)->str:
        return f"{self.first_name} {self.last_name}"

class CourseSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)

    id: str = Field(default_factory=lambda:str(uuid4()))
    title: str = 'playWright'
    max_score: int = Field(alias='maxScore', default=100)
    min_score: int = Field(alias='minScore', default=0)
    description: str = 'Course PlayWright'
    preview_file: PreviewFileSchema = Field(alias='previewFile')
    estimated_time: str = Field(alias='estimatedTime', default='Mnoga')
    created_by_user: CreatedByUserSchema = Field(alias='createdByUser')

course_default_model = CourseSchema(
    id = 'course_id11111111111',
    title = 'playWright11',
    maxScore = 10011,
    minScore = 0,
    description = 'Course PlayWrigh1111t',
    previewFile = PreviewFileSchema(
        id = 'previewFileAvatarka',
        filename = 'previewFileAvatarka.jpg',
        directory = 'previewFileAvatarka',
        url = 'https://example.com/'
    ),
    estimatedTime = 'Mnoga111',
    createdByUser = CreatedByUserSchema(
        id = 'createdByUser',
        email = 'mail.mail@nail.ruy',
        lastName = 'Nickerson',
        firstName = 'Nick',
        middleName = 'Nickname'
    )

)

print('course_default_model:' ,course_default_model)

course_dict = {
    "id": "course_id",
    "title":"playWright",
    "maxScore": 100,
    "minScore": 0,
    "description": "Course PlayWright",
    "previewFile":
    {
        "id": "previewFileAvatarka",
        "filename": "previewFileAvatarka.jpg",
        "directory" : "previewFileAvatarka",
        "url": "https://example.com/"
    },
    "estimatedTime": 'Mnoga',
    "createdByUser" :
        {
        "id" : "createdByUser",
        "email" : "mail.mail@nail.ruy",
        "lastName" : "Nickerson",
        "firstName" : "Nick",
        "middleName" : "Nickname"
    }
}

course_dict_model = CourseSchema(**course_dict)

print('course_dict:' ,course_dict_model)

course_json = """{
    "id": "course_id",
    "title": "playWright",
    "maxScore": 100,
    "minScore": 0,
    "description": "Course PlayWright",
    "previewFile": {
        "id": "previewFileAvatarka",
        "filename": "previewFileAvatarka.jpg",
        "directory": "previewFileAvatarka",
        "url": "https://example.com/"
    },
    "estimatedTime": "Mnoga",
    "createdByUser": {
        "id": "createdByUser",
        "email": "mail.mail@nail.ruy",
        "lastName": "Nickerson",
        "firstName": "Nick",
        "middleName": "Nickname"
    }
}"""

course_json_model = CourseSchema.model_validate_json(course_json)
print('course_json_model:' ,course_json_model)
print(course_json_model.model_dump(by_alias=True))
print(course_json_model.model_dump_json(by_alias=True))


new_user = CreatedByUserSchema(
    id = 'new_user',
    email = 'new_email@mail.com',
    lastName = 'new_last_name',
    firstName = 'new_first_name',
    middleName = 'new_middle_name'
)


print(new_user.get_username(), new_user.username)


try:
    file = PreviewFileSchema(
        id = 'previewFileAvatarka',
        filename = 'previewFileAvatarka.jpg',
        directory = 'previewFileAvatarka',
        url = 'local'
    )
except ValidationError as error:
    print(error)
    print(error.errors())