import os
import tempfile


class File(object):
    _cache: str
    _file_path: str

    def __init__(self, file_path: str):
        self._file_path = file_path
        if not os.path.exists(self._file_path):
            self.write('')

    def __str__(self):
        return self._file_path

    def __repr__(self):
        return self._file_path

    def __getitem__(self, item):
        with open(self._file_path, 'r') as handle:
            return handle.readlines()[item]

    def __add__(self, other: 'File'):
        temp_path = os.path.join(tempfile.gettempdir(), tempfile.mktemp())
        data = self.read() + other.read()
        node = File(temp_path)
        node.write(data)
        return node

    def read(self) -> str:
        with open(self._file_path, 'r') as handle:
            return handle.read()

    def write(self, data: str) -> None:
        with open(self._file_path, 'w+') as handle:
            handle.write(data)
