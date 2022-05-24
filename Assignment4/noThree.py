"""
CSCI-665 Homework #4 Problem 2
file: noThree.py
description: This program computes the maximum sum of elements of the sequence satisfying the constraint that
no three consecutive elements are included.
author: Karan Alhuwalia, ka7982@rit.edu
author: Rishabh Arora, ra8851@rit.edu
"""


def subsequence_maximum_sum(elements, max_sum_array):
    """
    finding maximum sum of elements of the sequence satisfying the constraint that
    no three consecutive elements are included in O(n) time complexity
    :param elements: input array
    :param max_sum_array: initial array to store sums
    :return: max sum on the last index of sum array
    """
    size = len(elements)
    if size >= 1:
        max_sum_array[0] = elements[0]
    if size >= 2:
        max_sum_array[1] = elements[0] + elements[1]
    if size >= 3:
        sum1 = elements[1] + elements[2]  # skipping element 0
        sum2 = elements[0] + elements[2]  # skipping element 1
        sum3 = elements[0] + elements[1]  # skipping element 2
        max_sum_array[2] = max(sum1, sum2, sum3)  # finding max between the 3 cases

    for i in range(3, size):  # O(n)
        sum1 = max_sum_array[i - 1]
        sum2 = max_sum_array[i - 2] + elements[i]
        sum3 = elements[i] + elements[i - 1] + max_sum_array[i - 3]
        max_sum_array[i] = max(sum1, sum2, sum3)

    return max_sum_array[size - 1]


def main():
    n = int(input())
    elements = input().split()  # O(n)
    elements = [int(i) for i in elements]  # O(n)
    max_sum_array = []
    for i in range(n):  # O(n)
        max_sum_array.append(0)
    print(subsequence_maximum_sum(elements, max_sum_array))


if __name__ == '__main__':
    main()
