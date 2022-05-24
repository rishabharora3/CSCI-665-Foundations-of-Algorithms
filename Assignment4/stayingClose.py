"""
Description: This code takes in input from user, the size and elements in array.
             The input data is used to determine the largest possible with the given set of conditions.

Input: Size
        int [Size]
        int [Size]

Authors: Karan Ahluwalia(ka7982)
         Rishabh Arora(ra8851)
"""


def lcs_sum1(ar1, ar2, n):
    """"
    Method takes in input as size and int arrays.

    :return: Max sum from consecutive elements in arrays.
    """
    output_matrix = [[[0 for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(3)]  # 3*(n^2) = O(n^2)
    for j in range(1, n + 1):  # O(n)
        for i in range(1, n + 1):  # O(n)

            for z in range(0, 3):  # O(1)
                output_matrix[z][j][i] = max(output_matrix[z][j][i], output_matrix[z][j][i - 1],
                                             output_matrix[z][j - 1][i])

            diff = ar1[i - 1] - ar2[j - 1]

            # if the difference between array1[i] and array2[j] is 0
            if diff == 0:
                output_matrix[1][j][i] = max(ar1[i - 1] + output_matrix[1][j - 1][i - 1], output_matrix[1][j][i])
                if output_matrix[0][j - 1][i - 1] != 0:
                    output_matrix[0][j][i] = max(ar1[i - 1] + output_matrix[0][j - 1][i - 1], output_matrix[0][j][i])
                elif output_matrix[2][j - 1][i - 1] != 0:
                    output_matrix[2][j][i] = max(ar1[i - 1] + output_matrix[2][j - 1][i - 1], output_matrix[2][j][i])

            # if the difference between array1[i] and array2[j] is -1
            elif diff == -1:
                output_matrix[0][j][i] = max(ar1[i - 1] + output_matrix[1][j - 1][i - 1], output_matrix[0][j][i])
                if output_matrix[2][j - 1][i - 1] != 0:
                    output_matrix[1][j][i] = max(ar1[i - 1] + output_matrix[2][j - 1][i - 1], output_matrix[1][j][i])

            # if the difference between array1[i] and array2[j] is -2
            elif diff == -2:
                if output_matrix[2][j - 1][i - 1] != 0:
                    output_matrix[0][j][i] = max(ar1[i - 1] + output_matrix[2][j - 1][i - 1], output_matrix[0][j][i])

            # if the difference between array1[i] and array2[j] is 1
            elif diff == 1:
                if output_matrix[0][j - 1][i - 1] != 0:
                    output_matrix[1][j][i] = max(ar1[i - 1] + output_matrix[0][j - 1][i - 1], output_matrix[1][j][i])
                output_matrix[2][j][i] = max(ar1[i - 1] + output_matrix[1][j - 1][i - 1], output_matrix[2][j][i])

            # if the difference between array1[i] and array2[j] is 2
            elif diff == 2:
                if output_matrix[0][j - 1][i - 1] != 0:
                    output_matrix[2][j][i] = max(ar1[i - 1] + output_matrix[0][j - 1][i - 1], output_matrix[2][j][i])

    return output_matrix[1][n][n]


def main():
    size = int(input())
    input1 = input().split()  # O(n)
    input1 = [int(i) for i in input1]  # O(n)
    input2 = input().split()  # O(n)
    input2 = [int(i) for i in input2]  # O(n)
    print(lcs_sum1(input1, input2, size))


if __name__ == '__main__':
    main()
