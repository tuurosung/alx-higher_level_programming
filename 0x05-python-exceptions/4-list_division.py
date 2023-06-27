#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    new_list = []
    result = 0

    if (isinstance(my_list_1, list) and isinstance(my_list_2, list) and
        isinstance(list_length, int)):

        for i in range(0, list_length):
            try:
                result = my_list_1[i] / my_list_2[i]
            except TypeError:
                print("wront type")
            except ZeroDivisionError:
                print("division by 0")
            except IndexError:
                print("out of range")
            finally:
                new_list.append(result)
                result = 0
        return (new_list)
