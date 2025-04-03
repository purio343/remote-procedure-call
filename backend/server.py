import socket
import os
from calc import calc_result
from utils import *

server_address = '/tmp/server_socket_1101'
buffer_size = 1024

def run_server():
    cleanup_socket()

    # ソケット作成
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.bind(server_address)
    sock.listen(5)
    print(f'Server starting up on {server_address}')

    try:
        while True:
            connection, address = sock.accept()
            print('New connection established')
            handle_client(connection)
    except Exception as e:
        print(f'An error occured: {e}')
    finally:
        sock.close()
        cleanup_socket()
        print('Shutting down server')

def cleanup_socket():
    try:
        os.unlink(server_address)
    except FileNotFoundError:
        pass

def handle_client(connection):
    try:
        while True:
            data = connection.recv(buffer_size)
            try:
                if data:
                    method, params, id = split_data(data)
                    print(f'受け取ったmethod: {method}')
                    print(f'受け取ったparam: {params}')
                    print(f'受け取ったid: {id}')
                    result = calc_result(method, params, id)
                    response = convert_result(result)
                    connection.sendall(response)
            except Exception as e:
                print(f'An error occured processing request: {e}')
    except Exception as e:
        print(f'An error occured receiving data: {e}')
    finally:
        print('Closing connection')
        connection.close()

if __name__ == "__main__":
    run_server()