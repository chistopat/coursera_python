import socket
import time
from typing import List, Tuple, Dict, Union


class Config(object):
    address: str = 'localhost'
    port: int = 8888
    timeout: int = 5
    buffer_size = 1024


class ClientError(BaseException):
    """Client error exception"""
    pass


class PutRequest:
    _message: bytes = None

    def __init__(
            self,
            metric: str,
            value: Union[int, float],
            timestamp: int,
    ) -> None:
        if not timestamp:
            timestamp = int(time.time())
        command = 'put'
        request_data = ' '.join((metric, str(value), str(timestamp)))
        message = '{} {}\n'.format(command, request_data)
        self._message = message.encode('utf-8')

    @property
    def message(self):
        return self._message


class PutResponse:
    code: str = None
    message: str = None

    def __init__(self, code: str, message: str = None):
        self.code = code

    @classmethod
    def from_bytes(cls, data: bytes):
        if not data:
            raise ClientError
        response = data.decode('utf-8').strip()
        code = response.split('\n', 1)
        if code[0] != 'ok':
            raise ClientError
        return cls(code[0])


class GetRequest:
    _message: bytes = None

    def __init__(
            self,
            metric: str
    ) -> None:
        command = 'get'
        message = '{} {}\n'.format(command, metric)
        self._message = message.encode('utf-8')

    @property
    def message(self):
        return self._message


class GetResponse:
    code: str = None
    data: Dict[str, List[Tuple[Union[int, float]]]] = {}

    def __init__(self, code: str, data: dict = None):
        self.code = code
        self.data = data

    @staticmethod
    def make_result(tokens):
        result = {}
        for row in tokens[1:]:
            items = row.split(' ')
            metric = items[0]
            value = float(items[1])
            timestamp = int(items[2])
            pair = (timestamp, value)
            if metric not in result:
                result[metric] = [pair]
            else:
                result[metric].append(pair)
        for k, v in result.items():
            result[k] = sorted(v)
        return result

    @classmethod
    def from_bytes(cls, data: bytes):
        if not data:
            raise ClientError
        response = data.decode('utf-8').strip()
        tokens = response.split('\n')
        code = tokens[0]
        if code != 'ok':
            raise ClientError
        try:
            result = cls.make_result(tokens)
        except (IndexError, ValueError):
            raise ClientError
        return cls(code, result)


class Client:
    def __init__(
            self,
            address: str,
            port: int,
            timeout: int = None
    ) -> None:
        try:
            self.address = (address, port)
            self.socket = socket.socket()
            self.socket.settimeout(timeout)
            self.socket.connect(self.address)
        except (OSError, socket.error) as err:
            print(err)

    def get(self, metric: str) -> Dict[str, List[Tuple[Union[int, float]]]]:
        request = GetRequest(metric)
        try:
            self.socket.sendall(request.message)
            response = GetResponse.from_bytes(
                self.socket.recv(Config.buffer_size)
            )
            return response.data
        except (OSError, socket.error) as err:
            print(err)

    def put(
        self,
        metric: str,
        value: Union[int, float],
        timestamp: int = None
    ) -> None:
        request = PutRequest(metric, value, timestamp)
        try:
            self.socket.sendall(request.message)
            PutResponse.from_bytes(self.socket.recv(Config.buffer_size))
        except (socket.error, OSError) as err:
            print(err)

    def __del__(self):
        self.socket.close()
