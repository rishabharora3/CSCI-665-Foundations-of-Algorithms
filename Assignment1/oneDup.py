"""
CSCI-665 Homework #1 Problem 3
file: oneDup.py
description: This program finds which number is present twice in the array in O(log n) time complexity using binary search
author: Anubhuti Suresh Puppalwar, ap1401@rit.edu
author: Rishabh Arora, ra8851@rit.edu
"""
import math


def find_duplicate(array, size):
    """
    finding a duplicate in the list using the binary search
    :param array: given input
    :param size: size of array
    :return:duplicate value
    Time complexity: O(log n)
    """
    left = 0
    right = size - 1
    while left <= right:
        middle = (left + right) // 2
        if array[middle] == array[middle + 1] or array[middle] == array[middle - 1]:
            return array[middle]
        elif math.ceil((array[right] + array[left]) / 2) == array[middle]:
            left = middle + 1
        else:
            right = middle - 1


def main():
    """
    driver code
    :return: None
    """
    arr = []
    n = int(input().strip())
    # O(n)
    for _ in range(n + 2):
        arr.append(int(input().strip()))  # O(1)
    print(find_duplicate(arr, len(arr)))


if __name__ == '__main__':
    main()
