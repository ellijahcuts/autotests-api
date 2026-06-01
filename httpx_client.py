import httpx

login_payload = {
    "email": 'user@example.com',
    "password": "string"
}
response_login = httpx.post('http://localhost:8000/api/v1/authentication/login', json=login_payload)
response_login_data = response_login.json()
print(response_login.status_code)
print(response_login.json())

client = httpx.Client(
    base_url='http://localhost:8000',
    timeout = 20,
    headers = {'Authorization': f"Bearer {response_login_data['token']['accessToken']}"}
)

get_user_me_response = client.get('/api/v1/users/me')
get_user_me_response_data = get_user_me_response.json()
print('Get user me data: ', get_user_me_response_data)

