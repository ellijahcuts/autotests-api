import httpx

response = httpx.get('https://jsonplaceholder.typicode.com/todos/1')
print(response.status_code)
print(response.json())

data = {
    'userId': 6125123421,
    'id': 511234,
    'title': 'delectus 123aut123 autem',
    'completed': True
}
response_1 = httpx.post('https://jsonplaceholder.typicode.com/todos/', json=data)
print(response_1.status_code)
print(response_1.json())

data_2 = {
    'username': "broski228",
    'password': 2280
}
response_2 = httpx.post('https://httpbingo.org/post', data=data_2)

print(response_2.status_code)
#print(response_2.request.headers) #заголовки
print(response_2.json())


headers = {'Authorization': 'Bearer 5552'}

response_3 = httpx.get('https://httpbingo.org/get', headers=headers)
print(response_3.status_code)
print(response_3.request.headers)
print(response_3.json())

params = {"userId": 1}
#response_4 = httpx.get('https://jsonplaceholder.typicode.com/todos?userId=1') #без словаря
response_4 = httpx.get('https://jsonplaceholder.typicode.com/todos', params=params)
print(response_4.status_code)
print(response_4.url)
print(response_4.json())

files = {"file": ("example.txt", open("example.txt", "rb"))}
response_5 = httpx.post('https://httpbingo.org/post', files=files)
print(response_5.json())


with httpx.Client() as client:
    response_6 = client.get('https://jsonplaceholder.typicode.com/todos/1')
    response_7 = client.get('https://jsonplaceholder.typicode.com/todos/2')

print(response_6.json())
print(response_7.json())

client = httpx.Client(headers={'Authorization': 'Bearer 5552'})
response_8 = client.get('https://httpbingo.org/get')
print(response_8.json())

try:
    response_error_0 = httpx.get('https://jsonplaceholder.typicode.com/invalidnaya-urla')
    response_error_0.raise_for_status()
except httpx.HTTPStatusError as e:
    print(f'Ошибка в запросе: {e}')

try:
    response_error_1 = httpx.get('https://httpbingo.org/delay/5', timeout=2)
except httpx.ReadTimeout:
    print("ggwp timeout")