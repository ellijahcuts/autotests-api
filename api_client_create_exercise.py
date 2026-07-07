from clients.courses.courses_client import get_private_courses_client
from clients.exercises.exercises_client import get_private_exercises_client
from clients.files.files_client import get_private_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.exercises.exercises_schema import CreateExerciseRequestSchema,UpdateExerciseRequestSchema, GetExerciseQuerySchema

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema()
create_user_response = public_users_client.create_user(create_user_request)

authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

files_client=get_private_files_client(authentication_user)
courses_client=get_private_courses_client(authentication_user)

create_file_request = CreateFileRequestSchema(
    upload_file = './testdata/files/image.png'
)
create_file_response = files_client.create_file(create_file_request)
print('Create file data: ',create_file_response)

create_course_request = CreateCourseRequestSchema(
    preview_file_id = create_file_response.file.id,
    created_by_user_id = create_user_response.user.id
)

create_course_response = courses_client.create_course(create_course_request)
print('Create course data: ',create_course_response)

exercises_client = get_private_exercises_client(authentication_user)

create_exercise_request = CreateExerciseRequestSchema(
    course_id = create_course_response.course.id
)

create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print('Create exercise data: ',create_exercise_response)


#Проверка остальных методов:
get_exercises_request = GetExerciseQuerySchema(
    course_id=create_course_response.course.id,
)
get_exercises_response = exercises_client.get_exercises(get_exercises_request)
print('Список заданий в курсе: ',get_exercises_response)

update_exercise_request = UpdateExerciseRequestSchema()
update_exercise_response = exercises_client.update_exercise(f"{create_exercise_response.exercise.id}",update_exercise_request)
print('Обновленное задание: ',update_exercise_response)

get_exercise_response = exercises_client.get_exercise(f"{create_exercise_response.exercise.id}")
print('Полученное задание по ID(После Апдейта): ',get_exercise_response)
