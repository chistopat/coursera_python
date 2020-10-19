import functools
import json

"""to_json Decorator"""


def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))
    return wrapped


@to_json
def func42():
    return {'answer': 42}


@to_json
def to_be(x="default"):
    return x


def test():
    assert func42() == '{"answer": 42}'
    assert to_be() == '"default"'
    assert to_be("s") == '"s"'


if __name__ == '__main__':
    test()
