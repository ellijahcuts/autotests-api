from jsonschema import validate
from clients.users.public_users_client import  get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema
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

validate_json_schema(instance=create_user_response.json(), schema=create_user_response_schema)