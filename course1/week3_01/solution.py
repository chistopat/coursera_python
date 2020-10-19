class FileReader:
    """Simple File reader class"""
    def __init__(self, path: str):
        try:
            with open(path, 'r') as file_obj:
                self._data = file_obj.read()
        except FileNotFoundError:
            self._data = ''

    def read(self):
        return self._data
