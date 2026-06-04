from clients.private_http_builder import AuthorizationUserDict
from clients.users.public_users_client import CreateUserRequestDict, get_public_users_client
from clients.users.private_users_client import get_private_users_client
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
print('Create user data: ', create_user_response)

authentication_user = AuthorizationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)
private_users_client = get_private_users_client(authentication_user)

get_user_response = private_users_client.get_user(create_user_response["user"]["id"])
print('Get user data: ', get_user_response)