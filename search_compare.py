#!user/bin/env python
# -*- coding: utf-8 -*-
"""Algorhythms"""

import random
import time

def main():
    randint500 = random.randint(1, 500)
    randint1000 = random.randint(1, 1000)
    randint10000 = random.randint(1,10000)

    randlist = []

    for int in xrange(1000):
        int = random.randrange(1, 1000, 1)
        randlist.append(int)

    sequential_search(randlist, )


def sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1
    end = time.time()
    total_time = end - start

    return found, total_time


def ordered_sequential_search(a_list, item):
    start = time.time()
    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos+1
    end = time.time()
    total_time = end - start
    return found, total_time

def binary_search_iterative(a_list, item):
    start = time.time()
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if a_list[midpoint] == item:
           found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    end = time.time()
    total_time = end - start
    return found, total_time


def binary_search_recursive(a_list, item):
    start = time.time()
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        return True
    else:
        if item < a_list[midpoint]:
            return binary_search_recursive(a_list[:midpoint], item)
        else:
            return binary_search_recursive(a_list[midpoint + 1:], item)
    end = time.time()
    total_time = end - start
    return total_time



randint500 = random.randint(1, 500)
randint1000 = random.randint(1, 1000)
randint10000 = random.randint(1,10000)

listOfLists = [[] for i in range(10)]
randlist = []

for list in listOfLists:
    for int in xrange(10):
        int = random.randrange(1, 1000, 1)
        list.append(int)

print listOfLists




