import httpx

login_payload = {
    'email': 'broski@example.ru',
    'password': '1316552'
}

login_response = httpx.post('http://localhost:8000/api/v1/authentication/login', json=login_payload)
login_response_data = login_response.json()
print(f'Login response: {login_response_data}')
print(f'Status Code: {login_response.status_code}')

me_header = {
    'Authorization': f"Bearer {login_response_data['token']['accessToken']}"
}
me_response = httpx.get('http://localhost:8000/api/v1/users/me', headers=me_header)
me_response_data = me_response.json()
print(f'Me response: {me_response_data}')
print(f'Status Code: {me_response.status_code}')