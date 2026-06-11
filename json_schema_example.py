from jsonschema import validate


schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "integer"},
    },
    "required": ["name"]
}



data = {
    "name": "Nick",
    "age": 19
}

validate(instance=data, schema=schema)