#!user/bin/env python
# -*- coding: utf-8 -*-
"""Algorhythms"""

import time
import random

def main():
    randlist500 = []
    randlist1000 = []
    randlist10000 = []

    for int in xrange(500):
        int = random.randrange(1, 500, 1)
        randlist500.append(int)

    for int in xrange(1000):
        int = random.randrange(1, 1000, 1)
        randlist1000.append(int)

    for int in xrange(10000):
        int = random.randrange(1, 10000, 1)
        randlist10000.append(int)

    ins500 = insertion_sort(randlist500)
    ins1000 = insertion_sort(randlist1000)
    ins10000 = insertion_sort(randlist10000)
    ins_total_time = (ins500 + ins1000 + ins10000) / 3
    print "Insertion sort search took {} seconds to run, on average".format(ins_total_time)

    shell500 = shell_sort(randlist500)
    shell1000 = shell_sort(randlist1000)
    shell10000 = shell_sort(randlist10000)
    shell_total_time = (shell500 + shell1000 + shell10000) / 3
    print "Shell sort took {} seconds to run, on average".format(shell_total_time)

    py500 = python_sort(randlist500)
    py1000 = python_sort(randlist1000)
    py10000 = python_sort(randlist10000)
    py_sort_total_time = (py500 + py1000 + py10000) / 3
    print "Python sort took {} seconds to run, on average".format(py_sort_total_time)


def insertion_sort(a_list):
    start = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value
    end = time.time()
    total_time = end - start
    return total_time

def shell_sort(a_list):
    start = time.time()
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        # print("After increments of size", sublist_count, "The list is", a_list)
        sublist_count = sublist_count // 2
    end = time.time()
    total_time = end - start
    return total_time

def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
        a_list[position] = current_value

def python_sort(a_list):
    start = time.time()
    a_list.sort()
    end = time.time()
    total_time = end - start
    return total_time

if __name__ == '__main__':
    main()


