"""
CSCI-665 Homework #1 Problem 4
file: match.py
description: This programs implements the stable matching algorithm
author: Anubhuti Suresh Puppalwar, ap1401@rit.edu
author: Rishabh Arora, ra8851@rit.edu
"""


def gale_shapley(requester, responder, matrix_size):
    """
    Implements gale shapley algorithm
    :param requester: matrix of the requester
    :param responder: matrix of the responder
    :param matrix_size: matrix size
    :return: requester and responder matrix
    time complexity: O(n^2)
    """
    requester_matrix = [-1 for _ in range(matrix_size)]  # O(n)
    responder_matrix = [-1 for _ in range(matrix_size)]  # O(n)
    count = [-1 for _ in range(matrix_size)]  # O(n)
    stack = [index for index in range(matrix_size - 1, -1, -1)]  # O(n)
    inverse_matrix = [[0] * matrix_size for _ in range(matrix_size)]  # O(n)
    # O(n^2)
    # preprocessing to create an inverse_matrix matrix to check preference for requesters in constant time
    for i in range(matrix_size):
        for j in range(matrix_size):
            inverse_matrix[i][responder[i][j]] = j

    while len(stack) > 0:
        requester1 = stack.pop()  # O(1)
        count[requester1] += 1
        responder1 = requester[requester1][count[requester1]]
        if responder_matrix[responder1] == -1:
            responder_matrix[responder1] = requester1
            requester_matrix[requester1] = responder1
        elif inverse_matrix[responder1][requester1] < inverse_matrix[responder1][responder_matrix[responder1]]:
            stack.append(responder_matrix[responder1])
            requester_matrix[requester1] = responder1
            responder_matrix[responder1] = requester1
        else:
            stack.append(requester1)

    return requester_matrix, responder_matrix


def get_preferences(matrix, matrix_size):
    """
    taking user input from standard input
    :param matrix: empty matrix
    :param matrix_size: matrix size
    :return: None
    time complexity: O(n^2)
    """
    for i in range(matrix_size):
        row = []
        # split complexity: O(n)
        for j in input().split():
            row.append(int(j))
        matrix.append(row)
    return matrix


def main():
    """
    driver code
    :return: None
    """
    matrix_size = int(input())
    matrix_one = get_preferences([], matrix_size)
    matrix_two = get_preferences([], matrix_size)
    requester1, responder1 = gale_shapley(matrix_one, matrix_two, matrix_size)
    requester2, responder2 = gale_shapley(matrix_two, matrix_one, matrix_size)
    if requester1 == responder2 and requester2 == responder1:
        print("NO")
    else:
        print("YES")


if __name__ == '__main__':
    main()
