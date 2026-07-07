import json

## Json to Python
json_data = '{"name": "Иван","age": 30,  "is_student": false}'

json_newdata = """{
  "name": "Иван",
  "age": 30,
  "is_student": false,
  "courses": [
    "Python",
    "QA Automation",
    "Api Tests"
  ],
  "address": {
    "city": "Москва",
    "zip": "1422214"
  }
}"""
parsed_data = json.loads(json_data)
parsed_data1 = json.loads(json_newdata)
print(parsed_data)
print(parsed_data1['address'])

## Py to JSON
data = {
    'name': 'Browns',
    'age': 11,
    'is_student': False,
}

json_string = json.dumps(data, indent=4)
print(json_string)


## Парсинг файла JSON

with open('json_example.json', 'r', encoding="utf-8") as file:
    read_data = json.load(file)
    print(read_data)


## создание файла JSON
with open('json_testuser.json', 'w', encoding="utf-8") as file:
    json.dump(data, file, indent=2, ensure_ascii=False)