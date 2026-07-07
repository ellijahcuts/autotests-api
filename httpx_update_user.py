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
payload_patch_user = {
  "email": tools.fakers.generate_email(),
  "lastName": payload['lastName'],
  "firstName": payload['firstName'],
  "middleName": payload['middleName'],
}
response_update_user = httpx.patch(f"http://localhost:8000/api/v1/users/{response_create_user_data['user']['id']}",headers=header, json=payload_patch_user)
print(response_update_user.status_code)
print(response_update_user.json())
