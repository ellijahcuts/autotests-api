import httpx
import tools.fakers

payload = {
  "email": tools.fakers.generate_email(),
  "password": tools.fakers.generate_password(),
  "lastName": tools.fakers.generate_last_name(),
  "firstName": tools.fakers.generate_first_name(),
  "middleName": tools.fakers.generate_middle_name(),
}
response_create_user = httpx.post('http://localhost:8000/api/v1/users', json=payload)
response_create_user_data = response_create_user.json()
print(response_create_user.status_code)
print(response_create_user.json())

login_payload = {
    "email": payload["email"],
    "password": payload["password"]
}
response_login = httpx.post('http://localhost:8000/api/v1/authentication/login', json=login_payload)
response_login_data = response_login.json()
print(response_login.status_code)
print(response_login.json())

header = {
    'Authorization': f"Bearer {response_login_data['token']['accessToken']}"
}
response_get_user = httpx.get(f'http://localhost:8000/api/v1/users/{response_create_user_data['user']['id']}', headers=header)
print(response_get_user.status_code)
print(response_get_user.json())

response_create_file = httpx.post(
    f'http://localhost:8000/api/v1/files',
    data={"filename": "image.png" , "directory": "courses"},
    files={"upload_file": open('./testdata/files/image.png', 'rb')},
    headers=header
)
print(response_create_file.status_code)
print(response_create_file.json())
