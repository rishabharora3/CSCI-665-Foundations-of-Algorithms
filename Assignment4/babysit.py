"""
CSCI-665 Homework #4 Problem 3
file: sortCards.py
description: This program computes determines the minimum number of cards that need
to be moved in order to get the whole set of n cards in sorted, ascending order
author: Karan Alhuwalia, ka7982@rit.edu
author: Rishabh Arora, ra8851@rit.edu
"""
import heapq

MAX_CHILDREN = 4


def get_rho_list(job_list):
    """
    calculating rho based on start time and end time
    :param job_list:
    :return:
    """
    rho_list = [0] * (len(job_list))
    i = len(job_list) - 1
    while i > 0:
        j = i
        while j >= 0:
            if not job_list[i].start_time < job_list[j].end_time:
                rho_list[i] = rho_list[i] + 1
            j -= 1
        i -= 1
    return rho_list


def compute_profit(job_list, rho_list):
    """
    computing profit
    :param job_list: sorted job list based on day
    :param rho_list:
    :return:
    """
    profit_list = [[0] * (len(job_list) + 1) for _ in range(len(job_list) + 1)]
    i = 1
    while i < len(profit_list[0]):
        if job_list[i - 1].children >= MAX_CHILDREN:
            profit_list[0][i] = profit_list[0][i - 1]
        else:
            profit_list[0][i] = max(job_list[i - 1].profit + profit_list[0][rho_list[i - 1]], profit_list[0][i - 1])
        i += 1
    i = 1
    while i < len(profit_list):
        if job_list[i - 1].children >= MAX_CHILDREN:
            profit_list[i][0] = profit_list[i - 1][0]
        else:
            profit_list[i][0] = max(job_list[i - 1].profit + profit_list[rho_list[i - 1]][0], profit_list[i - 1][0])
        i += 1
    i = 1
    while i < len(profit_list):
        j = 1
        while j < len(profit_list[0]):
            if i == j:
                if job_list[j - 1].children >= MAX_CHILDREN:
                    profit_list[i][j] = max(job_list[j - 1].profit + profit_list[rho_list[j - 1]][rho_list[j - 1]],
                                            profit_list[j - 1][j - 1])
                else:
                    profit_list[i][j] = max(job_list[j - 1].profit + profit_list[rho_list[j - 1]][j - 1],
                                            profit_list[j - 1][j - 1])

            elif i > j:
                if job_list[i - 1].children >= MAX_CHILDREN:
                    profit_list[i][j] = profit_list[i - 1][j]
                else:
                    profit_list[i][j] = max(job_list[i - 1].profit + profit_list[rho_list[i - 1]][j],
                                            profit_list[i - 1][j])
            else:
                if job_list[j - 1].children >= MAX_CHILDREN:
                    profit_list[i][j] = profit_list[i][j - 1]
                else:
                    profit_list[i][j] = max(job_list[j - 1].profit + profit_list[i][rho_list[j - 1]],
                                            profit_list[i][j - 1])
            j += 1
        i += 1
    print(profit_list[len(profit_list) - 1][len(profit_list) - 1])


class Job:
    """
    Class to store jobs as objects
    """
    __slots__ = "day", "start_time", "end_time", "children", "pay_rate", "profit"

    def __init__(self, day, start_time, end_time, children, pay_rate):
        self.day = day
        self.start_time = start_time
        self.end_time = end_time
        self.end_time = end_time
        self.children = children
        self.pay_rate = pay_rate
        self.profit = ((self.end_time - self.start_time) * pay_rate) // 100

    def __lt__(self, other):
        """
        using it for sorting based on deadline of tasks
        :param other:
        :return:
        """
        if self.day < other.day:
            return True
        elif self.day == other.day:
            return self.end_time < other.end_time


def main():
    """
    driver code
    :return: None
    """
    size = int(input())
    job_list = sort_list(size)
    rho_list = get_rho_list(job_list)
    compute_profit(job_list, rho_list)


def sort_list(task_size):
    """
    sorting list based on priority
    :param task_size:
    :return:
    """
    job_list = []
    job_list_sorted_temp = []
    job_list_sorted = []
    for i in range(task_size):
        task_details = input().split()
        job_list.append(Job(int(task_details[0]), int(task_details[1]), int(task_details[2]), int(task_details[3]),
                            int(task_details[4])))
        if job_list[i].start_time >= 600 and job_list[i].end_time <= 2300:
            heapq.heappush(job_list_sorted_temp, job_list[i])
    while len(job_list_sorted_temp) != 0:
        job_list_sorted.append(heapq.heappop(job_list_sorted_temp))

    return job_list_sorted


if __name__ == '__main__':
    main()
