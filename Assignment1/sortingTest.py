"""
CSCI-665 Homework #1 Problem 5
file: sortingTest.py
description: This program implements MergeSort, InsertionSort and BucketSort.
author: Anubhuti Suresh Puppalwar, ap1401@rit.edu
author: Rishabh Arora, ra8851@rit.edu
"""
import math
import random
import time


def merge_sort(unsorted):
    """
    This method uses merge sort technique to sort the unsorted list
    :param unsorted:
    :return sorted list:
    """
    if len(unsorted) > 1:
        mid_index = len(unsorted) // 2
        first = unsorted[:mid_index]
        second = unsorted[mid_index:]
        merge_sort(first)
        merge_sort(second)
        first_ind = second_ind = i = 0
        while first_ind < len(first) and second_ind < len(second):
            if first[first_ind] < second[second_ind]:
                unsorted[i] = first[first_ind]
                first_ind = first_ind + 1
            else:
                unsorted[i] = second[second_ind]
                second_ind = second_ind + 1
            i = i + 1

        while first_ind < len(first):
            unsorted[i] = first[first_ind]
            first_ind = first_ind + 1
            i = i + 1

        while second_ind < len(second):
            unsorted[i] = second[second_ind]
            second_ind = second_ind + 1
            i = i + 1
    return unsorted


def insertion_sort(unsorted):
    """
    This method uses insertion sort technique to sort the unsorted list
    :param unsorted:
    :return sorted list:
    """
    for index in range(1, len(unsorted)):
        element = unsorted[index]
        prev_element = index - 1
        while prev_element >= 0 and unsorted[prev_element] > element:
            unsorted[prev_element + 1] = unsorted[prev_element]
            prev_element -= 1
        unsorted[prev_element + 1] = element
    return unsorted


def bucket_sort(unsorted):
    """
    This method uses bucket sort technique to sort the unsorted list
    :param unsorted:
    :return sorted list:
    """
    buckets_count = len(unsorted)
    bucket_list = [[] for _ in range(buckets_count)]
    for j in unsorted:
        index_b = math.floor(buckets_count * j)
        bucket_list[index_b].append(j)
    for bucket in range(buckets_count):
        bucket_list[bucket] = insertion_sort(bucket_list[bucket])
    count = 0
    for bucket in range(buckets_count):
        for j in range(len(bucket_list[bucket])):
            unsorted[count] = bucket_list[bucket][j]
            count += 1
    return unsorted


def fetch_running_time(type_dist):
    """
    running all sorting algos
    :param type_dist:
    :return:
    """
    for power in range(2, 6):
        mean = 0.5
        variance = 1 / 10000
        arr = []
        if type_dist == "uniform":
            for _ in range(10 ** power):
                temp = random.uniform(0, 1)
                arr.append(temp)
            print("\nUniform distribution Size:", 10 ** power, "\n")
        else:
            for _ in range(10 ** power):
                temp = random.gauss(mean, variance)
                arr.append(temp)
            print("\nGaussian (normal) distribution Size: ", 10 ** power, "\n")

        start_time = time.time()
        merge_sort(arr[:])
        print("Total time for Merge Sort: ", (time.time() - start_time))
        start_time = time.time()
        insertion_sort(arr[:])
        print("Total time for Insertion Sort: ", (time.time() - start_time))
        start_time = time.time()
        bucket_sort(arr[:])
        print("Total time for Bucket Sort: ", (time.time() - start_time))


def main():
    """"
    driver function
    :return: None
    """
    fetch_running_time("uniform")
    fetch_running_time("gaussian")


if __name__ == '__main__':
    main()
