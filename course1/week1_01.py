import sys


def sum_from_string(string: str) -> int:
    result: int = 0
    if not string.isdigit():
        return -1
    for ch in string:
        result += int(ch)
    return result


def test():
    assert sum_from_string("1234") == 10
    assert sum_from_string("1") == 1
    assert sum_from_string("000") == 0
    assert sum_from_string("") == -1
    assert sum_from_string("asdf") == -1


def main():
    test()
    data: str
    if len(sys.argv) > 1:
        data = sys.argv[1]
        print(sum_from_string(data))


if __name__ == '__main__':
    main()
