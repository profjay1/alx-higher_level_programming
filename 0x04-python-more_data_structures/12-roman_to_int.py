#!/usr/bin/python3


def roman_to_int(s):
    if s is None or type(s) != str:
        return 0
    hm = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
    result = 0
    for i in range(0, len(s)):
        if i + 1 < len(s) and hm[s[i]] < hm[s[i + 1]]:
            result -= hm[s[i]]
        else:
            result += hm[s[i]]
    return result
