import base64
import json

def create_base64_key(data: json) -> str:
    data_loaded = data.dict()
    string_key = ''
    for key, value in data_loaded['data'].items():
        part_key = str(key) + str(value)
        string_key += part_key + ','
    encoded_key = base64.b64encode(bytes(string_key, 'utf-8'))
    return str(encoded_key)

    