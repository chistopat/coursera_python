import sys


def main():
    n: int = 1
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    for i in range(1, n+1):
        print(' '*(n-i) + '#' * i)


if __name__ == '__main__':
    main()
