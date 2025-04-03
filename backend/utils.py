import json

def convert_result(data):
    data_json = json.dumps(data, indent=4)
    return data_json.encode('utf-8')

def split_data(data):
    data_str = json.loads(data)
    method = data_str['method']
    params = data_str['params']
    id = data_str['id']
    return [method, params, id]