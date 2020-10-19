import sys
import typing


def equation(a: int, b: int, c: int) -> typing.Tuple[int, int]:
    x1 = (-1*b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    x2 = (-1*b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    return int(x1), int(x2)


def test() -> None:
    assert equation(1, -3, -4) == (4, -1)
    assert equation(13, 236, -396) == (1, -19)
    assert equation(23, -116, 96) == (4, 1)


if __name__ == '__main__':
    test()
    args: typing.List[int] = []
    if len(sys.argv) >= 4:
        [print(x) for x in equation(int(sys.argv[1]),
                                    int(sys.argv[2]),
                                    int(sys.argv[3]))]
