import argparse
import json
import sys
import typing
import tempfile
import os

"""Simple console key-value storage"""

class Storage:
    _data: typing.Dict[str, typing.List[str]] = {}
    _default: str = 'storage.data'
    _file_path: str = ''

    def __init__(self):
        self._file_path = os.path.join(tempfile.gettempdir(), self._default)
        if os.path.isfile(self._file_path):
            with open(self._file_path, 'r') as file_obj:
                data = file_obj.read()
            if data:
                self._data = json.loads(data)

    def get_value(self, key) -> typing.List[str]:
        if self._data.get(key):
            return self._data[key]
        return ['None']


    def set_value(
            self,
            key: str,
            value: typing.Union[str]
    ) -> None:
        if self._data.get(key):
            self._data[key].append(value)
        else:
            self._data[key] = [value]

    def __del__(self):
        with open(self._file_path, 'w') as file_obj:
            file_obj.write(json.dumps(self._data))


def main():
    argparser = argparse.ArgumentParser()
    argparser.add_argument('-k', '--key', required=True)
    argparser.add_argument('-v', '--val')
    args = argparser.parse_args()

    storage = Storage()
    if args.val:
        storage.set_value(args.key, args.val)
    else:
        print(", ".join(storage.get_value(args.key)))


if __name__ == '__main__':
    main()
