#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""IS 211.  Assignment 4. Sorts. """

import time
import random

#Functon for Insertion Sort.
def insertion_sort(a_list):
    time_start = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position -= 1
        a_list[position] = current_value
    time_stop = time.time()
    run_time = time_stop - time_start
    return run_time

#Function for Shell Sort
def shell_sort(a_list):
    time_start = time.time()
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        sublist_count = sublist_count // 2
    time_stop = time.time()
    run_time = time_stop - time_start
    return run_time

#Helper Function for Shell Sort
def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
        a_list[position] = current_value

#Wrapper function for Python sort.
def python_sort(a_list):
    time_start = time.time()
    a_list.sort()
    time_stop = time.time()
    run_time = time_stop - time_start
    return run_time

#Generates a random list of integers.
def list_generator(list_size):
    my_list = []
    for i in range(list_size):
        my_list.append(random.randint(1, list_size))
    return my_list


#Main function creates 100 lists of each size and passes it to sort functions.  Totals are then divided by 100 for the
# avg.  My function cannot sort a list of 10000 values.
def main():
    list_size = [500, 1000]
    for i in list_size:
        list_counter = 100
        sort_results = [0, 0, 0]

        while list_counter > 0:
            my_list = list_generator(i)
            sort_results[0] += insertion_sort(my_list)
            sort_results[1] += shell_sort(my_list)
            sort_results[2] += python_sort(my_list)
            list_counter -= 1

#Prints the average sort time for each sort type.
    print ('Insertion Sort took %10.7f seconds to run, on average.') % (sort_results[0] / 100)
    print ('Shell Sort took %10.7f seconds to run, on average.') % (sort_results[1] / 100)
    print ('Python took %10.7f seconds to run, on average.') % (sort_results[2] / 100)


if __name__ == "__main__":
    main()
