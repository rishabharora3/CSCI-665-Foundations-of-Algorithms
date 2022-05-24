"""
CSCI-665 Homework #2 Problem 3
file: picture.py
description: This program computes the minimum number of swaps necessary to get the class into the desired order.
author: Anubhuti Suresh Puppalwar, ap1401@rit.edu
author: Rishabh Arora, ra8851@rit.edu
"""


def _split(data, mid):
    """
    Split the data into halves and return the two halves
    :param data: The list to split in half
    :return: Two lists, cut in half
    """
    return data[:mid], data[mid:]


def _merge(left, right):
    """
    Merges two list, left and right, into a combined result such that all 7 year olds in increasing order
    of height come before Teacher, and then 8 year olds in descending order of heights
    while calculating inversions.
    :param left: A list with desired property
    :param right: A list with desired property
    :return: One combined list with desired order and number of swaps done.
    """

    result = []
    leftIndex, rightIndex = 0, 0
    inversions = 0

    # loop through until either the left or right list is exhausted
    while leftIndex < len(left) and rightIndex < len(right):

        # checks when both students are of age 7
        if left[leftIndex][0] == 7 and right[rightIndex][0] == 7 and left[leftIndex][1] <= right[rightIndex][1]:
            result.append(left[leftIndex])
            leftIndex += 1
        elif left[leftIndex][0] == 7 and right[rightIndex][0] == 7 and left[leftIndex][1] > right[rightIndex][1]:
            result.append(right[rightIndex])
            inversions += len(left) - leftIndex
            rightIndex += 1

        # checks when both students are of age 8
        elif left[leftIndex][0] == 8 and right[rightIndex][0] == 8 and left[leftIndex][1] < right[rightIndex][1]:
            result.append(right[rightIndex])
            inversions += len(left) - leftIndex
            rightIndex += 1
        elif left[leftIndex][0] == 8 and right[rightIndex][0] == 8 and left[leftIndex][1] >= right[rightIndex][1]:
            result.append(left[leftIndex])
            leftIndex += 1

        # checks when a student is of age 7 and other student is of age 8
        elif left[leftIndex][0] == 7 and right[rightIndex][0] == 8:
            result.append(left[leftIndex])
            leftIndex += 1
        elif left[leftIndex][0] == 8 and right[rightIndex][0] == 7:
            result.append(right[rightIndex])
            inversions += len(left) - leftIndex
            rightIndex += 1

        # checks when a student is of age 7 and a teacher
        elif left[leftIndex][0] == 7 and right[rightIndex][0] != 7 and right[rightIndex][0] != 8:
            result.append(left[leftIndex])
            leftIndex += 1
        elif right[rightIndex][0] == 7 and left[leftIndex][0] != 7 and left[leftIndex][0] != 8:
            result.append(right[rightIndex])
            inversions += len(left) - leftIndex
            rightIndex += 1

        # checks when a student is of age 8 and a teacher
        elif left[leftIndex][0] == 8 and right[rightIndex][0] != 7 and right[rightIndex][0] != 8:
            result.append(right[rightIndex])
            inversions += len(left) - leftIndex
            rightIndex += 1
        elif right[rightIndex][0] == 8 and left[leftIndex][0] != 7 and left[leftIndex][0] != 8:
            result.append(left[leftIndex])
            leftIndex += 1

    # take the un-exhausted list and extend the remainder onto the result
    #extend has O(k) complexity
    if leftIndex < len(left):
        result.extend(left[leftIndex:])
    elif rightIndex < len(right):
        result.extend(right[rightIndex:])

    return result, inversions


def picture(data):
    """
    Performs divide and conquer approach to split the list into 2 parts and merge
    it to get the desired order list.
    :param data: list
    :return: result containing the list in desired order and number of inversions
    """
    inversions = 0
    if len(data) == 1:
        return data, 0
    if len(data) == 0:
        return None, 0
    else:
        # split the data into left and right halves
        mid_index = len(data) // 2
        left, right = _split(data, mid_index)

        # return the merged recursive mergeSort of the halves
        leftdata, x = picture(left)
        inversions = inversions + x
        rightdata, y = picture(right)
        inversions = inversions + y
        result, total = _merge(leftdata, rightdata)
        inversions = inversions + total
    return result, inversions


if __name__ == '__main__':
    n = int(input())
    list_stud = []
    for i in range(0, n):
        input_ele = input()
        #split has O(n) complexity
        age, ht = input_ele.split()
        entry = (int(age), float(ht))
        list_stud.append(entry)
    result = []
    result, inversions = picture(list_stud)
    print(inversions)
