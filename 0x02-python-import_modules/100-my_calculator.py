#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div


def main():
    if (len(argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif (str(argv[2]) not in ["+", "-", "*", "/"]):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        if (argv[2] == "+"):
            print(f"{argv[1]} + {argv[3]} = {add(int(argv[1]), int(argv[3]))}")
        elif (argv[2] == "-"):
            print(f"{argv[1]} - {argv[3]} = {sub(int(argv[1]), int(argv[3]))}")
        elif (argv[2] == "*"):
            print(f"{argv[1]} * {argv[3]} = {mul(int(argv[1]), int(argv[3]))}")
        else:
            print(f"{argv[1]} / {argv[3]} = {div(int(argv[1]), int(argv[3]))}")


if __name__ == "__main__":
    main()
