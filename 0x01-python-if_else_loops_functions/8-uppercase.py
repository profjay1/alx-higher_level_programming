#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if (ord('a') <= ord(char) and ord(char) <= ord('z')):
            char = chr(ord(char) - 32)
        print(char, end="")
    print("\n", end="")
