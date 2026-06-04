from clients.courses.courses_client import get_private_courses_client, CreateCourseRequestDict
from clients.exercises.exercises_client import get_private_exercises_client, CreateExerciseRequestDict, GetExerciseQueryDict, UpdateExerciseRequestDict
from clients.files.files_client import get_private_files_client, CreateFileRequestDict
from clients.private_http_builder import AuthorizationUserDict
from clients.users.public_users_client import CreateUserRequestDict, get_public_users_client
import tools.fakers

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestDict(
    email=tools.fakers.generate_email(),
    password=tools.fakers.generate_password(),
    lastName=tools.fakers.generate_last_name(),
    firstName=tools.fakers.generate_first_name(),
    middleName=tools.fakers.generate_middle_name()
)
create_user_response = public_users_client.create_user(create_user_request)

authentication_user = AuthorizationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)

files_client=get_private_files_client(authentication_user)
courses_client=get_private_courses_client(authentication_user)

create_file_request = CreateFileRequestDict(
    filename = 'image.png',
    directory = 'courses',
    upload_file = './testdata/files/image.png'
)
create_file_response = files_client.create_file(create_file_request)
print('Create file data: ',create_file_response)

create_course_request = CreateCourseRequestDict(
    title = 'Python QA',
    maxScore = 100,
    minScore = 0,
    description = "Обучение тестированию на Пайтоне",
    estimatedTime = "500 часов и это не предел",
    previewFileId = create_file_response['file']['id'],
    createdByUserId = create_user_response['user']['id']
)

create_course_response = courses_client.create_course(create_course_request)
print('Create course data: ',create_course_response)

exercises_client = get_private_exercises_client(authentication_user)

create_exercise_request = CreateExerciseRequestDict(
    title= "Создание задания",
    courseId = create_course_response['course']['id'],
    maxScore= 10,
    minScore= 0,
    orderIndex = 1,
    description = "Создание запроса",
    estimatedTime = "15 мин"
)

create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print('Create exercise data: ',create_exercise_response)










"""
#Проверка остальных методов:
get_exercises_request = GetExerciseQueryDict(
    courseId=create_course_response['course']['id']
)
get_exercises_response = exercises_client.get_exercises(get_exercises_request)
print('Список заданий в курсе: ',get_exercises_response)

update_exercise_request = UpdateExerciseRequestDict(
    title='Задание было изменено и это новое название',
    maxScore= 500,
    minScore= 150,
    orderIndex= 22,
    description= "Измененное задание(После апдейта)",
    estimatedTime= "0 лет"
)
update_exercise_response = exercises_client.update_exercise(f"{create_exercise_response['exercise']['id']}",update_exercise_request)
print('Обновленное задание: ',update_exercise_response)
get_exercise_response = exercises_client.get_exercise(f"{create_exercise_response['exercise']['id']}")
print('Полученное задание по ID(После Апдейта): ',get_exercise_response)
"""