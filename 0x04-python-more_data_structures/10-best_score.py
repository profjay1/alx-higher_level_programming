#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary:
        h = max(list(a_dictionary.values()))
        return list(a_dictionary.keys())[list(a_dictionary.values()).index(h)]
    return None
