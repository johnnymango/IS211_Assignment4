#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""IS 211.  Assignment 4. Searches. """

import time
import random

#Function Performs the sequential search.
def sequential_search(a_list, item):
    time_start = time.time()
    pos = 0
    found = False

    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos + 1
    time_stop = time.time()
    run_time = time_stop - time_start
    return found, run_time

#Function performs the ordered sequential search.  List is sorted.
def ordered_sequential_search(a_list, item):
    a_list.sort()
    time_start = time.time()
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
                pos = pos + 1
    time_stop = time.time()
    run_time = time_stop - time_start
    return found, run_time

#Function performs the iterative binary search.  List is sorted.
def binary_search_iterative(a_list, item):
    a_list.sort()
    time_start = time.time()
    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last)
        if a_list[midpoint] == item:
            found = True
        else:
            if item < a_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    time_stop = time.time()
    run_time = time_stop - time_start
    return found, run_time

#Function performs the recursive binary search.  List is sorted.
def binary_search_recursive(a_list, item):
    a_list.sort()
    time_start = time.time()
    if len(a_list) == 0:
        time_stop = time.time()
        run_time = time_stop - time_start
        return False, run_time
    else:
        midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        time_stop = time.time()
        run_time = time_stop - time_start
        return True, run_time
    else:
        if item < a_list[midpoint]:
            return binary_search_recursive(a_list[:midpoint], item)
        else:
            return binary_search_recursive(a_list[midpoint + 1:], item)

#Generates a random list of integers.
def list_generator(list_size):
    my_list = []
    for i in range(list_size):
        my_list.append(random.randint(1, list_size))
    return my_list

#Main function creates 100 lists of each size and passes it function.  Totals are then divided by 100 for the avg.
def main():
    list_size = [500, 1000, 10000]
    for i in list_size:
        list_counter = 100
        search_results = [0, 0, 0, 0]

        while list_counter > 0:
            my_list = list_generator(i)
            search_results[0] += sequential_search(my_list, -1)[1]
            search_results[1] += ordered_sequential_search(my_list, -1)[1]
            search_results[2] += binary_search_iterative(my_list, -1)[1]
            search_results[3] += binary_search_recursive(my_list, -1)[1]
            list_counter -= 1

#Prints the average search time for each search type.
    print ('Sequential Search took %10.7f seconds to run, on average.') % (search_results[0] / 100)
    print ('Ordered Sequential Search took %10.7f seconds to run, on average.') % (search_results[1] / 100)
    print ('Iterative Binary Search took %10.7f seconds to run, on average.') % (search_results[2] / 100)
    print ('Recursive Binary Search took %10.7f seconds to run, on average.') % (search_results[3] / 100)

if __name__ == "__main__":
    main()

