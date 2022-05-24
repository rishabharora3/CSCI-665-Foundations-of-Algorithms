"""
CSCI-665 Homework #3 Problem 5
file: schedules.py
description: This program finds the number of possible schedules in O(1) time complexity in first case,
and an O(n) dynamic programming solution in the second case
author: Anubhuti Suresh Puppalwar, ap1401@rit.edu
author: Rishabh Arora, ra8851@rit.edu
"""


def find_possible_schedule(n):
    """
    Using 3 base cases to find schedules for all other possible values for number of hours
    Time Complexity : O(1)
    :param n: is the number of hours under consideration
    :return: possible schedules
    """
    possible_schedule = 0
    base_values = (2, 5, 13)  # O(1), because the value is only 3
    if n == 0:  # complexity - O(1)
        return 0
    if n == 1:  # complexity - O(1)
        return base_values[0]
    elif n == 2:  # complexity - O(1)
        return base_values[1]
    elif n == 3:
        return base_values[2]
    if n > 3:  # complexity - O(1)
        q = n // 3  # complexity - O(1)
        r = n % 3  # complexity - O(1)
        possible_schedule = base_values[2] ** q  # complexity - O(1)
        if r == 2:
            possible_schedule *= base_values[1]  # complexity - O(1)
        elif r == 1:
            possible_schedule *= base_values[0]  # complexity - O(1)
    return possible_schedule


def find_possible_schedule_dp(n):
    """
    using dynamic programming to find possible schedules for all possible values for number of hours
    Time Complexity : O(n)
    :param n: number of hours
    :return: possible schedules
    """
    x = (2 * n) + 1
    y = [[0 for _ in range(x)] for _ in range(4)]  # O(n)
    for i in range(1, 4):  # complexity - O(1)
        y[i][1] = 1
        y[i][0] = 1
    for i in range(1, x):  # complexity -  O(n)
        y[1][i] = 1
    for i in range(2, x):  # complexity - O(n)
        y[2][i] = y[2][i - 1] + y[2][i - 2]
    for i in range(2, x):  # complexity - O(n)
        y[3][i] = y[3][i - 1] + y[3][i - 2] + y[3][i - 3]
    return y[3][x - 1]


def main():
    """
    driver code
    :return: None
    """
    n = int(input())
    possible_schedule = find_possible_schedule(n)
    print(possible_schedule)
    possible_schedules_dp = find_possible_schedule_dp(n)
    print(possible_schedules_dp)


if __name__ == '__main__':
    main()
