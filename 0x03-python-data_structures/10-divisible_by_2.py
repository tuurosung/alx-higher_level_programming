#!/usr/bin/python3

def division_by_2(my_list=[]):

    all_multiples = []
    for i in range(len(my_list)) :
        if my_list[i] % 2 == 0:
            all_multiples.append(True)
        else:
            all_multiples.append(False)
    return (all_multiples)
