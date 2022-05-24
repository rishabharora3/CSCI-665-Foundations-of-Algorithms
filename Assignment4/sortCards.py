"""
CSCI-665 Homework #4 Problem 3
file: sortCards.py
description: This program computes determines the minimum number of cards that need
to be moved in order to get the whole set of n cards in sorted, ascending order
author: Karan Alhuwalia, ka7982@rit.edu
author: Rishabh Arora, ra8851@rit.edu
"""


def min_card_to_move(elements, s):
    """
    this function computes the longest increasing subsequence which tell us what all cards are already sorted
    and we subtract them from the total length of cards to obtain how many card needs to move.
    :param elements:
    :param s: temp array to keep the longest subsequence count.
    :return: min moves
    """
    size = len(elements)
    # O(n^2)
    for i in range(len(elements)):  # O(n)
        for j in range(i):  # O(n)
            if elements[j] < elements[i] and s[i] <= s[j]:
                s[i] += 1
    return size - max(s)  # max complexity is O(n)


def main():
    """
    driver code
    :return: None
    """
    n = int(input())
    elements = input().split()  # O(n)
    elements = [int(i) for i in elements]  # O(n)
    s = []  # initial array to store elements of LIS
    for i in range(n):  # O(n)
        s.append(1)
    s[0] = 0
    print(min_card_to_move(elements, s))


if __name__ == '__main__':
    main()
