from clients.courses.courses_client import get_private_courses_client
from clients.exercises.exercises_client import get_private_exercises_client
from clients.files.files_client import get_private_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_builder import AuthorizationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.exercises.exercises_schema import CreateExerciseRequestSchema,UpdateExerciseRequestSchema, GetExerciseQuerySchema
import tools.fakers

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=tools.fakers.generate_email(),
    password=tools.fakers.generate_password(),
    last_name=tools.fakers.generate_last_name(),
    first_name=tools.fakers.generate_first_name(),
    middle_name=tools.fakers.generate_middle_name()
)
create_user_response = public_users_client.create_user(create_user_request)

authentication_user = AuthorizationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

files_client=get_private_files_client(authentication_user)
courses_client=get_private_courses_client(authentication_user)

create_file_request = CreateFileRequestSchema(
    filename = 'image.png',
    directory = 'courses',
    upload_file = './testdata/files/image.png'
)
create_file_response = files_client.create_file(create_file_request)
print('Create file data: ',create_file_response)

create_course_request = CreateCourseRequestSchema(
    title = 'Python QA',
    max_score = 100,
    min_score = 0,
    description = "Обучение тестированию на Пайтоне",
    estimated_time = "500 часов и это не предел",
    preview_file_id = create_file_response.file.id,
    created_by_user_id = create_user_response.user.id
)

create_course_response = courses_client.create_course(create_course_request)
print('Create course data: ',create_course_response)

exercises_client = get_private_exercises_client(authentication_user)

create_exercise_request = CreateExerciseRequestSchema(
    title= "Создание задания",
    course_id = create_course_response.course.id,
    max_score= 10,
    min_score= 0,
    order_index = 1,
    description = "Создание запроса",
    estimated_time = "15 мин"
)

create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print('Create exercise data: ',create_exercise_response)


"""
#Проверка остальных методов:
get_exercises_request = GetExerciseQuerySchema(
    course_id=create_course_response.course.id,
)
get_exercises_response = exercises_client.get_exercises(get_exercises_request)
print('Список заданий в курсе: ',get_exercises_response)

update_exercise_request = UpdateExerciseRequestSchema(
    title='Задание было изменено и это новое название',
    max_score= 500,
    min_score= 150,
    order_index= 22,
    description= "Измененное задание(После апдейта)",
    estimated_time= "0 лет"
)
update_exercise_response = exercises_client.update_exercise(f"{create_exercise_response.exercise.id}",update_exercise_request)
print('Обновленное задание: ',update_exercise_response)
get_exercise_response = exercises_client.get_exercise(f"{create_exercise_response.exercise.id}")
print('Полученное задание по ID(После Апдейта): ',get_exercise_response)
"""