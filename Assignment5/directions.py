"""
CSCI-665 Homework #5 Problem 2
file: directions.py
description: This program computes the fewest steps of directions possible that allows a friend to move from
point A to point B, even if it is not the most direct path (i.e. the path of fewest steps of directions may
involve more intermediate vertices than other paths)
O(n+m) complexity since using an adjacency list to represent the graph and running a DFS to find the shortest
path.
author: Karan Ahluwalia, ka7982@rit.edu
author: Rishabh Arora, ra8851@rit.edu
"""
import sys


class Directions:

    def __init__(self, vertices, edges):
        self.V = vertices
        self.E = edges
        self.graph = [[] for _ in range(self.V)]
        self.minim = sys.maxsize
        self.count = 0

    def addEdge(self, u, v):
        """
        This function adds an edge to the graph.
        :param u: starting node
        :param v: ending node
        :return: None
        """
        self.graph[u].append(v)
        self.graph[v].append(u)

    def all_paths_helper(self, prev_node, u, end, visited, path, count):
        """
        This function finds all the paths from start to end using recursive DFS.
        :param prev_node: previous node
        :param u: current node
        :param end: ending node
        :param visited: list of visited nodes
        :param path: list of nodes in the path
        :param count: number of nodes in the path
        :return: None
        """
        visited[u] = True
        if self.check_neighbor_options(self.graph[u], visited, prev_node) > 1 and u != end:
            count[u] += 1
            self.count += 1
        path.append(u)  # add current node to path O(1)
        if u == end:
            if self.count < self.minim:  # if the path is shorter than the current shortest path
                self.minim = self.count
        elif self.count < self.minim:  # if the path is not the shortest path
            for i in self.graph[u]:
                if not visited[i]:
                    self.all_paths_helper(u, i, end, visited, path, count)
        path.pop()  # O(1)
        visited[u] = False
        if count[u] > 0:
            self.count -= 1
        count[u] = 0

    def find_all_paths(self, start, end):
        """
        This function finds all the paths from start to end.
        :param start: starting node
        :param end: ending node
        :return: None
        """
        visited = [False] * self.V
        path = []
        count = [0] * self.V
        self.all_paths_helper(start, start, end, visited, path, count)
        print(self.minim)

    def check_neighbor_options(self, neighbor, visited, j):
        """
        This function checks if the neighbor has any unvisited neighbors.
        :param neighbor:list of neighbors
        :param visited: list of visited nodes
        :param j: previous node
        :return: number of unvisited neighbors
        """
        count = 0
        for i in neighbor:  # O(n)
            if not visited[i] or i != j:
                count += 1
                if count > 1:
                    break
        return count


def main():
    """
    This function reads the input from the file and calls the functions to find the shortest path.
    :return: None
    """
    sys.setrecursionlimit(15000)
    n, m, start, end = int(input()), int(input()), int(input()), int(input())
    g = Directions(n, m)
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        g.addEdge(u, v)
    g.find_all_paths(start, end)


if __name__ == '__main__':
    main()
