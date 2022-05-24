"""
CSCI-665 Homework 3
file: alignPoints.py
description: This program computes the maximum number of pairs of points that can be aligned.
author: Anubhuti Suresh Puppalwar, ap1401@rit.edu
author: Rishabh Arora, ra8851@rit.edu
"""


def findListOfPerpendicularLines(list_points, n):
    """
    For every pair of points compute the slope and midpoint. Find equation of line of the form y = mx + c.
    Find the equation of line perpendicular to this line. Store the coefficient of y, m and c in tuple.
    Create list of such tuples.
    Complexity : O(n^2)
    :param list_points: List of points with x coordinates and y coordinates.
    :param n: Length of list
    :return: list of tuples containing variables of equation of lines
    """
    list_lines = []
    # O(n^2) for the nested for loop
    for i in range(0, n):
        for j in range(i + 1, n):
            x1 = list_points[i][0]
            x2 = list_points[j][0]
            y1 = list_points[i][1]
            y2 = list_points[j][1]
            yintercept = y2 - y1
            xintercept = x2 - x1
            if yintercept == 0:
                mid_x = (x1 + x2) / 2
                c = mid_x
                line = (0, -1, c)
            elif xintercept == 0:
                mid_y = (y1 + y2) / 2
                slope = 0
                c = mid_y
                line = (1, slope, c)
            else:
                slope = yintercept / xintercept
                mid_x = (x1 + x2) / 2
                mid_y = (y1 + y2) / 2
                slope = -1 * slope
                c = mid_y - slope * mid_x
                line = (1, slope, c)
            # O(1) for append operation
            list_lines.append(line)
    return list_lines


def countMostFrequentLine(list_lines):
    """
    Finds the maximum occurance of a line.
    :param list_lines: List of tuples having information of line
    :return: Maximum number a particular tuple occurs in list.
    """
    list_lines.sort()
    max_count = 1
    # O(1) for finding length
    lenlist = len(list_lines)
    curr_count = 1
    # O(n) for the for loop
    for i in range(1, lenlist):
        if list_lines[i][0] == list_lines[i - 1][0] and list_lines[i][1] == list_lines[i - 1][1] and list_lines[i][2] == \
                list_lines[i - 1][2]:
            curr_count += 1
        else:
            if curr_count > max_count:
                max_count = curr_count
            curr_count = 1
    # If last element is most frequent
    if curr_count > max_count:
        max_count = curr_count
    return max_count


def findAlignments(list_points, n):
    """
    Calls list of perpendicular lines and counts maximum frequency of line
    :param list_points: list of points
    :param n: number of points
    :return: maximum frequency
    """
    list_lines = findListOfPerpendicularLines(list_points, n)
    num = countMostFrequentLine(list_lines)
    return num


if __name__ == '__main__':
    """
    driver code
    return: None
    """
    n = int(input())
    list_points = []
    # O(n) for all the input points
    for i in range(0, n):
        input_ele = input()
        # split has O(n) complexity
        x, y = input_ele.split()
        point = (int(x), int(y))
        # O(1) for append operation
        list_points.append(point)
    print(findAlignments(list_points, n))
