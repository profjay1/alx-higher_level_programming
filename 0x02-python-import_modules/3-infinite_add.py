#!/usr/bin/python3
from sys import argv


def main():
    result = 0
    if (len(argv) == 1):
        result = 0
    else:
        for i in argv[1:]:
            result += int(i)
    print(result)


if __name__ == "__main__":
    main()
