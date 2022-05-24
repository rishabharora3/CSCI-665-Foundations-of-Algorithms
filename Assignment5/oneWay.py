"""
CSCI-665 Homework #5 Problem 3
file: directions.py
description: This program determine if there exists a
pair of vertices u and v such that adding an edge from u to v
makes the graph strongly connected.
O(n+m) complexity
author: Karan Ahluwalia, ka7982@rit.edu
author: Rishabh Arora, ra8851@rit.edu
"""
import sys

A = -100


class OneWay:
    def __init__(self, n):
        """
        This function initializes the class
        :param n: number of vertices
        """
        self.n = n
        self.adj_list = [[] for _ in range(n)]
        self.adj_list_new = [[] for _ in range(n)]
        self.count = 0
        self.visited_bfs = []
        self.end = []
        for _ in range(n):
            self.end.append(A)
        self.sequence = 0
        self.ind = 0
        self.adj_list_rev = [[] for _ in range(self.n)]
        self.visited_dfs = set()
        self.strong_con_comp = []
        self.k = []
        self.end_new = []

    def find_path_bfs(self):
        """
        This function finds the path between two vertices using BFS
        :return: None
        """
        for i in self.adj_list:
            self.count = self.count + 1
            if len(i) != 0 or self.adj_list.index(i) in self.visited_bfs:
                pass
            else:
                self.visited_bfs.append(self.adj_list.index(i))
            if len(i) != 0 or self.count in self.end or self.adj_list.index(i) not in self.visited_bfs:
                pass
            else:
                self.end[self.count] = self.sequence
                self.sequence = self.sequence + 1
            if 0 == len(i):
                continue
            self.ind = self.count
            self.k = self.adj_list[self.ind]
            self.find_shortest_path()

    def find_shortest_path(self):
        """
        This function finds the shortest path between two vertices using BFS
        :return: None
        """
        while len(self.k) != 0:
            if self.adj_list[self.ind][0] not in self.visited_bfs:
                self.k = self.adj_list[self.adj_list[self.ind][0]]
                ind_new = self.adj_list[self.ind][0]
                self.adj_list[self.ind].pop(0)
                if self.ind in self.visited_bfs:
                    pass
                else:
                    self.visited_bfs.append(self.ind)
                self.ind = ind_new
            elif self.adj_list[self.ind][0] in self.visited_bfs:
                self.adj_list[self.ind].pop(0)
                if self.ind in self.visited_bfs:
                    continue
                self.visited_bfs.append(self.ind)
        if self.ind in self.visited_bfs:
            pass
        else:
            self.visited_bfs.append(self.ind)
        for k1 in reversed(self.visited_bfs):
            if len(self.adj_list[k1]) == 0 or len(self.visited_bfs) == self.n:
                if self.end[k1] == -100:
                    self.end[k1] = self.sequence
                    self.sequence = self.sequence + 1
                elif len(self.adj_list[k1]) != 0 and len(self.visited_bfs) != self.n:
                    self.ind = k1
                    self.k = self.adj_list[k1]
                    if len(self.visited_bfs) < self.n:
                        self.find_shortest_path()
            elif 0 != len(self.adj_list[k1]) and self.n != len(self.visited_bfs):
                self.ind = k1
                self.k = self.adj_list[k1]
                if len(self.visited_bfs) >= self.n:
                    continue
                self.find_shortest_path()

    def reverse_edges(self):
        """
        This function reverses the edges in the graph
        :return: None
        """
        global k
        self.count = 0
        for i in self.adj_list_new:
            for k in i:
                self.adj_list_rev[k].append(self.count)
            self.count = self.count + 1
            self.adj_list_rev[k].sort()
        for i in range(self.n):
            self.end_new.append(self.end.index(i))
        self.end_new.reverse()

    def find_path(self, k):
        """
        This function finds the  path between two vertices using DFS
        :param k: The vertex to start the search from
        :return: None
        """
        for i in self.adj_list_rev[k]:
            if i in self.visited_dfs:
                pass
            else:
                self.visited_dfs.add(i)
                self.k.add(i)
            if i not in self.k:
                continue
            tmp = []
            for x in self.k:
                tmp.append(x)
            self.strong_con_comp.append(tmp)
            self.k.clear()
            break

    def find_strong_conn_comp(self):
        for i in self.end_new:
            if i not in self.visited_dfs:
                self.k.add(i)
                for j in self.adj_list_rev[i]:
                    if j not in self.k:
                        if j not in self.visited_dfs:
                            self.visited_dfs.add(j)
                            self.k.add(j)
                        self.find_path(j)
                        continue
                    tmp = []
                    for x in self.k:
                        tmp.append(x)
                    self.strong_con_comp.append(tmp)
                    self.k.clear()
                    break
            else:
                continue

    def find_edge(self):
        u = 0
        v = 0
        for i in self.strong_con_comp:
            c = 0
            t2 = set()
            t3 = set()
            t1 = set(i)
            for j in self.adj_list_rev:
                if c not in i:
                    t2.update(j)
                else:
                    t3.update(j)
                c = c + 1
            if len(t3.difference(t1)) != 0:
                pass
            else:
                v = v + 1
            if len(t2.intersection(t1)) != 0:
                continue
            u = u + 1
        self.print_output(u, v)

    def print_output(self, u, v):
        if u != 1 or v != 1:
            print("NO")
        else:
            print("YES")


def main():
    """
    This function is the main function of the program
    :return: None
    """
    sys.setrecursionlimit(200000000)
    n = int(input())
    one_way = OneWay(n)
    read_input(n, one_way)
    one_way.count = -1
    one_way.find_path_bfs()
    one_way.reverse_edges()
    one_way.k = set()
    one_way.find_strong_conn_comp()
    one_way.find_edge()


def read_input(n, one_way):
    """
    This function reads the input from the stdin
    :param n: The number of vertices in the graph
    :param one_way: The object of the class OneWay
    :return: None
    """
    for i in range(n):
        inp = input()
        for k in inp.split(" "):
            if int(k) != 0:
                one_way.adj_list[i].append(int(k.strip()) - 1)
        one_way.adj_list[i].sort()
    for i in one_way.adj_list:
        for k in i:
            one_way.adj_list_new[one_way.count].append(k)
        one_way.count = one_way.count + 1


if __name__ == '__main__':
    main()
