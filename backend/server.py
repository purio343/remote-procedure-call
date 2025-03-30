import socket
import os
import json
from calc import calc

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server_address = '/tmp/server_socket_1101'

response_type = {}

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

sock.bind(server_address)
sock.listen(1)
print(f'Server starting up on {server_address}')    

try:
    while True:
        connection, address = sock.accept()
        while True:
            data = connection.recv(80)
            if data:
                # JSON文字列をPythonオブジェクトに変換。
                data_str = json.loads(data)
                method_name = data_str['method']
                params = data_str['params']
                print(f'受け取ったメソッド名: {method_name}')
                print(f'受け取ったparam: {params}')
                # ans = func_table[method_name]
                ans = calc(method_name, params)
                response_type["results"] = str(ans)
                response_type["result_type"] = "int"
                response_str = json.dumps(response_type, indent=4)
                response = response_str.encode('utf-8')
                connection.sendall(response)
            else:
                break
finally:
    print('Closing connection')
    connection.close()