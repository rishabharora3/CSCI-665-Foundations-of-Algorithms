"""
CSCI-665 Homework #2 Problem 4
file: boss.py
description: This program determines whether it is possible to complete all of the tasks without missing any deadlines
author: Anubhuti Suresh Puppalwar, ap1401@rit.edu
author: Rishabh Arora, ra8851@rit.edu
"""
import heapq


class Task:
    """
    Class to store tasks as objects with arrival_time, deadline_time, completion_time
    """
    __slots__ = "arrival_time", "deadline_time", "completion_time"

    def __init__(self, arrival_time, deadline_time, completion_time):
        self.arrival_time = arrival_time
        self.deadline_time = deadline_time
        self.completion_time = completion_time

    def __lt__(self, other):
        """
        using it for sorting based on deadline of tasks
        :param other:
        :return:
        """
        return self.deadline_time < other.deadline_time


def run_tasks(task_list):
    """
    logic for checking if the tasks can run without missing any deadlines
    :param task_list: list of tasks read from standard input
    :return: True or False
    """
    heap = []
    current_time = 0
    i = 0
    heapq.heappush(heap, task_list[0])  # O(log n)
    size = len(task_list)  # O(n)
    while i < len(task_list):  # O(n)
        task = heapq.heappop(heap)  # O(log n)
        # if current task cannot be completed before the deadline return false
        if current_time + task.completion_time > task.deadline_time:
            return False
        # if the next job's comes before the ongoing task completion
        if i + 1 < size and task_list[i + 1].arrival_time < current_time + task.completion_time:
            task.completion_time -= abs(current_time - task_list[i + 1].arrival_time)
            current_time = task_list[i + 1].arrival_time
            heapq.heappush(heap, task)  # O(log n)
            heapq.heappush(heap, task_list[i + 1])  # O(log n)
            i += 1
        else:
            if not current_time + task.completion_time > task.deadline_time:
                current_time += task.completion_time
            else:
                return False
        if len(heap) == 0:
            i += 1
            if i < size:
                heapq.heappush(heap, task_list[i])
                current_time = task_list[i].arrival_time
    return True


def main():
    """
    driver code
    :return: None
    """
    task_list = []
    task_size = int(input())
    for i in range(task_size):
        task_details = input().split()
        task_list.append(Task(int(task_details[0]), int(task_details[1]), int(task_details[2])))
    if run_tasks(task_list):
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
