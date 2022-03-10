import base64
import json
from db.db import engine
from typing import List


def create_base64_key(data: json) -> str:
    string_key = ''
    for key, value in data.items():
        part_key = str(key) + str(value)
        string_key += part_key + ','
    encoded_key = base64.b64encode(bytes(string_key, 'utf-8'))
    return encoded_key.decode("utf-8")


def get_statistics():
    RAW_SQL = '''
        SELECT 
        (SELECT SUM( CASE WHEN count>0 THEN count END))/
        (SELECT SUM(count+1))*100
        FROM record;
    '''
    with engine.connect() as conn:
        rs = conn.execute(RAW_SQL)
        result = rs.fetchone()[0]
    return f'{int(result)}%'