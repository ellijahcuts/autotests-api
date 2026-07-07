from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import  get_public_users_client
from clients.users.private_users_client import get_private_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
import tools.fakers
from tools.assertions.schema import validate_json_schema

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email=tools.fakers.generate_email(),
    password=tools.fakers.generate_password(),
    last_name=tools.fakers.generate_last_name(),
    first_name=tools.fakers.generate_first_name(),
    middle_name=tools.fakers.generate_middle_name()
)

create_user_response = public_users_client.create_user_api(create_user_request)
create_user_response_schema = CreateUserResponseSchema.model_json_schema()
created_user = CreateUserResponseSchema.model_validate(create_user_response.json())
print(f'Created Response: {create_user_response}')
print('Create user data: ',created_user.model_dump())

validate_json_schema(instance=create_user_response.json(), schema=create_user_response_schema)

authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)
private_users_client = get_private_users_client(authentication_user)

get_user_response = private_users_client.get_user_api(created_user.user.id)
get_user_response_schema = GetUserResponseSchema.model_json_schema()
get_user = GetUserResponseSchema.model_validate(get_user_response.json())
print('Get Response: ', get_user_response)
print('Get user data: ', get_user.model_dump())

validate_json_schema(instance=get_user_response.json(), schema=get_user_response_schema)