#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    counter = 0
    new_list = list()
    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            counter += 1
        except (TypeError, ValueError):
            print("wrong type")
            counter += 1
            result = 0
        except ZeroDivisionError:
            print("division by 0")
            counter += 1
            result = 0
        except IndexError:
            print("out of range")
            counter += 1
            result = 0
        finally:
            new_list.append(result)
    return new_list
