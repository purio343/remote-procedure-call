import socket
import os
from calc import create_response
from utils import *

server_address = '/tmp/server_socket_1101'

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
sock.bind(server_address)
sock.listen(1)
print(f'Server starting up on {server_address}')    

try:
    while True:
        connection, address = sock.accept()
        try:
            while True:
                data = connection.recv(1024)
                if data:
                    method, params, id = split_data(data)
                    print(f'受け取ったmethod: {method}')
                    print(f'受け取ったparam: {params}')
                    print(f'受け取ったid: {id}')
                    result = create_response(method, params, id)
                    response = convert_response(result)
                    connection.sendall(response)
                else:
                    break
        finally:
            print("Closing connection")
            connection.close()

except socket.error as e:
    print(f'Socket error: {e}')

finally:
    print('Shutting down server')
    sock.close()