#!/usr/bin/python3
"""
This is the "3-say_my_name" module.
The 3-say_my_name module supplies 1 func, say_my_name(first_name, last_name="")
"""


def say_my_name(first_name, last_name=""):
    """
        Prints My name is <first name> <last name>
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
