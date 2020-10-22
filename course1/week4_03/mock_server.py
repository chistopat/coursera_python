import socket
from config import Config


def dummy_server(sock, address):
    print('starting up on {} port {}'.format(*address))
    sock.bind(address)
    sock.listen(1)

    get_resp = b'ok\npalm.cpu 10.5 1501864247\npalm.cpu 11.5 1501845247\neardrum.cpu 15.3 1501864259\n\n'
    put_resp = b'ok\n\n'

    while True:
        print('listening for connection...')
        connection, client_address = sock.accept()
        try:
            print('client connected: {}'.format(client_address))
            while True:
                data = connection.recv(Config.buffer_size)
                print('received {}'.format(data.decode('utf-8')))
                if data:
                    if 'get' in data.decode('utf-8'):
                        connection.sendall(get_resp)
                    elif 'put' in data.decode('utf-8'):
                        connection.sendall(put_resp)
                    else:
                        connection.sendall(data)
                else:
                    break
        finally:
            connection.close()


def main():
    address = (Config.address, Config.port)
    with socket.socket() as sock:
        try:
            dummy_server(sock, address)
        except socket.error as err:
            print(err)


if __name__ == '__main__':
    main()
