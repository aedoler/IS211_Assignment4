#!user/bin/env python
# -*- coding: utf-8 -*-
"""Algorhythms"""

import random
import time

def main():
    randint500 = random.randint(1, 500)
    randint1000 = random.randint(1, 1000)
    randint10000 = random.randint(1,10000)


    randlist500 = [[] for i in range(100)]
    randlist1000 = [[] for i in range(100)]
    randlist10000 = [[] for i in range(100)]

    for int in xrange(500):
        int = random.randrange(1, 500, 1)
        randlist500.append(int)

    for int in xrange(1000):
        int = random.randrange(1, 1000, 1)
        randlist1000.append(int)

    for int in xrange(10000):
        int = random.randrange(1, 10000, 1)
        randlist10000.append(int)

    seq500 = sequential_search(randlist500, randint500)
    seq1000 = sequential_search(randlist1000, randint1000)
    seq10000 = sequential_search(randlist10000, randint10000)
    seq_total_time = (seq500 + seq1000 + seq10000) / 3
    print "Sequential search took {} seconds to run, on average".format(seq_total_time)

    ord_seq500 = ordered_sequential_search(randlist500, randint500)
    ord_seq1000 = ordered_sequential_search(randlist1000, randint1000)
    ord_seq10000 = ordered_sequential_search(randlist10000, randint10000)
    ord_seq_total_time = (ord_seq500 + ord_seq1000 + ord_seq10000) / 3
    print "Ordered sequential search took {} seconds" \
          " to run, on average".format(ord_seq_total_time)

    bin500 = binary_search_iterative(randlist500, randint500)
    bin1000 = binary_search_iterative(randlist1000, randint1000)
    bin10000 = binary_search_iterative(randlist10000, randint10000)
    bin_total_time = (bin500 + bin1000 + bin10000) / 3
    print "Iterative binary" \
          " search took {} seconds to run, on average".format(bin_total_time)

    bin_rec500 = binary_search_recursive(randlist500, randint500)
    bin_rec1000 = binary_search_recursive(randlist1000, randint1000)
    bin_rec10000 = binary_search_recursive(randlist10000, randint10000)
    bin_rec_total_time = (bin_rec500 + bin_rec1000 + bin_rec10000) / 3
    print "Recursive binary search took {} seconds" \
          " to run, on average".format(bin_rec_total_time)



def sequential_search(a_list, item):
    a_list.sort()
    start = time.time()
    counter = 0

    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1
    counter += 1

    end = time.time()
    total_time = end - start

    return total_time


def ordered_sequential_search(a_list, item):
    a_list.sort()
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
    return total_time

def binary_search_iterative(a_list, item):
    a_list.sort()
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
    return total_time


def binary_search_recursive(a_list, item):
    a_list.sort()
    start = time.time()
    if len(a_list) == 0:
        end = time.time()
        total_time = end - start
        return total_time
    else:
        midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        end = time.time()
        total_time = end - start
        return total_time
    else:
        if item < a_list[midpoint]:
            end = time.time()
            total_time = end - start
            return total_time
        else:
            end = time.time()
            total_time = end - start
            return total_time


randint500 = random.randint(1, 500)
randint1000 = random.randint(1, 1000)
randint10000 = random.randint(1,10000)

"""
listOfLists = [[] for i in range(10)]
randlist = []

for list in listOfLists:
    for int in xrange(10):
        i"nt = random.randrange(1, 1000, 1)
        list.append(int)

for n in listOfLists:
    for num, sub in enumerate(n):
        print 'hi', num

print listOfLists"" \
                 """


if __name__ == '__main__':
    main()




