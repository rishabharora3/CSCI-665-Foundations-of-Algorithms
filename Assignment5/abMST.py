from collections import defaultdict

"""
CSCI-665 Homework #5 Problem 4
file: abMST.py
description: This program finds the minimum spanning tree, given constraints that the edges belong to two sets and 
no more than two edges can travel from one set to another.
author: Karan Ahluwalia, ka7982@rit.edu
author: Rishabh Arora, ra8851@rit.edu
"""

ret_cc = []


def search(lst, platform):
    for i in range(len(lst)):
        if lst[i] == platform:
            return i
    return -1


# This class represents a directed graph in an adjacency list representation using Dictionary
class DictGraph:

    def __init__(self, vertices=0):
        self.graph = defaultdict(list)  # default dictionary to store graph
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def add_vertex(self, key):
        self.graph[key] = []
        self.V += 1

    def dfs_util(self, v, visited):
        visited[self.get_graph_index(v)] = True
        ret_cc.append(v)
        for i in self.graph.get(v):
            if not visited[self.get_graph_index(i)]:
                self.dfs_util(i, visited)

    def get_graph_index(self, value):
        count = 0
        num = value
        for i in self.graph.keys():
            if i == num:
                return count
            count += 1
        return -1

    def fill(self, v, visited, stack):
        visited[self.get_graph_index(v)] = True
        for i in self.graph.get(v):
            if not visited[self.get_graph_index(i)]:
                self.fill(i, visited, stack)
        stack.append(v)

    def transpose(self):
        g = DictGraph()
        count = 0
        for i in self.graph:
            for j in self.graph.get(i):
                g.add_vertex(j)
                g.add_vertex(i)
        for i in self.graph:
            for j in self.graph.get(i):
                g.add_edge(j, i)

                count += 1
        g.V = count
        return g

    def find_scc(self):

        count = 0
        stack = []
        visited = [False] * self.V
        for i in self.graph.keys():
            if not visited[self.get_graph_index(i)]:
                self.fill(i, visited, stack)

        gr = self.transpose()

        visited = [False] * self.V

        while stack:
            i = stack.pop()
            if not visited[self.get_graph_index(i)]:
                gr.dfs_util(i, visited)
                ret_cc.append(-1)
                count += 1

        return count, ret_cc


# This class represents a directed graph in an adjacency list representation using List
class ListGraph:

    def __init__(self, vertices=0):
        self.V = vertices  # No. of vertices
        self.graph = []  # default dictionary

    def add_edge(self, u, v, w=0):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        x_root = self.find(parent, x)
        y_root = self.find(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root

        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskal_mst(self):
        result = []
        i = 0
        e = 0
        parent = []
        rank = []
        self.graph = sorted(self.graph, key=lambda item: item[2])

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while i < self.V:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        minimum_cost = 0
        for u, v, weight in result:
            minimum_cost += weight
        return minimum_cost


def min_spanning_tree(a_scc, b_scc, a_graph, b_graph, full_graph, graph_list, a_cc_list, b_cc_list):
    do_nothing = 0  # This is a placeholder variable(Not useful in the program)
    total_scc = a_scc + b_scc
    min_crossing_edge_weight = 100001
    min_crossing_edge = (0, 0, 0)
    min_crossing_edge2 = (0, 0, 0)
    min_spanning_graph = ListGraph()
    min_crossing_edge2_weight = 100001
    count = 0
    if total_scc > 3:
        return -1
    elif b_scc == 0 and a_scc != 0:
        return a_graph.kruskal_mst()  # O(m log n)
    elif a_scc == 0 and b_scc != 0:
        return b_graph.kruskal_mst()  # O(m log n)
    elif a_scc == 1 and b_scc == 1:
        for edge in full_graph.graph:  # O(m)
            if (graph_list[edge[0]] == 0 and graph_list[edge[1]] == 1) or (
                    graph_list[edge[0]] == 1 and graph_list[edge[1]] == 0):
                if min_crossing_edge_weight > edge[2]:
                    min_crossing_edge_weight = edge[2]
                    min_crossing_edge = edge

        for edge in full_graph.graph:  # O(m)
            if (graph_list[edge[0]] == 0 and graph_list[edge[1]] == 1) or (
                    graph_list[edge[0]] == 1 and graph_list[edge[1]] == 0):
                if min_crossing_edge2_weight > edge[2] > min_crossing_edge_weight:
                    min_crossing_edge2_weight = edge[2]
                    min_crossing_edge2 = edge

        for edge in full_graph.graph:  # O(m)
            if (graph_list[edge[0]] == 0 and graph_list[edge[1]] == 1) or (
                    graph_list[edge[0]] == 1 and graph_list[edge[1]] == 0):
                if min_crossing_edge_weight == edge[2]:
                    min_spanning_graph.add_edge(min_crossing_edge[0], min_crossing_edge[1], min_crossing_edge[2])
                    count += 1
                if min_crossing_edge2_weight == edge[2]:
                    min_spanning_graph.add_edge(min_crossing_edge2[0], min_crossing_edge2[1], min_crossing_edge2[2])
                    count += 1
            else:
                min_spanning_graph.add_edge(edge[0], edge[1], edge[2])
                count += 1

        min_spanning_graph.V = count
        return min_spanning_graph.kruskal_mst()
    elif a_scc == 1 and b_scc == 2:
        include_mid_edges = [(0, 0, 100001)]
        for edge in full_graph.graph:
            if (graph_list[edge[0]] == 0 and graph_list[edge[1]] == 1) or (
                    graph_list[edge[0]] == 1 and graph_list[edge[1]] == 0):
                for b_cc_elements in b_cc_list:
                    if b_cc_elements == -1:
                        include_mid_edges.append((0, 0, 100001))
                    if edge[0] == b_cc_elements or edge[1] == b_cc_elements:
                        if include_mid_edges[len(include_mid_edges) - 1][2] > edge[2]:
                            include_mid_edges[len(include_mid_edges) - 1] = edge[0], edge[1], edge[2]

        for edge in full_graph.graph:
            if (graph_list[edge[0]] == 0 and graph_list[edge[1]] == 1) or (
                    graph_list[edge[0]] == 1 and graph_list[edge[1]] == 0):
                do_nothing += 1
            else:
                min_spanning_graph.add_edge(edge[0], edge[1], edge[2])
                count += 1

        for edge in include_mid_edges:
            min_spanning_graph.add_edge(edge[0], edge[1], edge[2])
            count += 1

        min_spanning_graph.V = count
        return min_spanning_graph.kruskal_mst()
    elif a_scc == 2 and b_scc == 1:
        include_mid_edges = [(0, 0, 100001)]
        for edge in full_graph.graph:
            if (graph_list[edge[0]] == 0 and graph_list[edge[1]] == 1) or (
                    graph_list[edge[0]] == 1 and graph_list[edge[1]] == 0):
                for a_cc_elements in a_cc_list:
                    if a_cc_elements == -1:
                        include_mid_edges.append((0, 0, 100001))
                    if edge[0] == a_cc_elements or edge[1] == a_cc_elements:
                        if include_mid_edges[len(include_mid_edges) - 1][2] > edge[2]:
                            include_mid_edges[len(include_mid_edges) - 1] = edge[0], edge[1], edge[2]

        for edge in full_graph.graph:
            if (graph_list[edge[0]] == 0 and graph_list[edge[1]] == 1) or (
                    graph_list[edge[0]] == 1 and graph_list[edge[1]] == 0):
                do_nothing += 1
            else:
                min_spanning_graph.add_edge(edge[0], edge[1], edge[2])
                count += 1

        for edge in include_mid_edges:
            min_spanning_graph.add_edge(edge[0], edge[1], edge[2])
            count += 1

        min_spanning_graph.V = count
        return min_spanning_graph.kruskal_mst()


def main():
    n = int(input())  # Number of vertices
    m = int(input())  # Number of edges
    a_size = 0
    b_size = 0
    graph_list = []
    full_graph = ListGraph()
    a_graph = DictGraph()
    b_graph = DictGraph()
    aw_graph = ListGraph()
    bw_graph = ListGraph()

    for i in range(0, n):  # O(n)
        if int(input()) == 0:
            graph_list.append(0)
            a_graph.add_vertex(i)
        else:
            graph_list.append(1)
            b_graph.add_vertex(i)

    for _ in range(0, m):  # O(m)
        from_vertex, to_vertex, weight = input().split()
        from_vertex = int(from_vertex)
        to_vertex = int(to_vertex)
        weight = int(weight)
        if graph_list[from_vertex] == 0 and graph_list[to_vertex] == 0:
            a_graph.add_edge(from_vertex, to_vertex)
            aw_graph.add_edge(from_vertex, to_vertex, weight)
        elif graph_list[from_vertex] == 1 and graph_list[to_vertex] == 1:
            b_graph.add_edge(from_vertex, to_vertex)
            bw_graph.add_edge(from_vertex, to_vertex, weight)
        full_graph.add_edge(from_vertex, to_vertex, weight)

    for i in graph_list:  # O(m)
        if i == 0:
            a_size += 1
        else:
            b_size += 1

    a_graph.V = a_size
    b_graph.V = b_size
    a_scc, ret_cc_a = a_graph.find_scc()  # O(m+n)
    b_scc, ret_cc_b = b_graph.find_scc()  # O(m+n)
    # print("Total SCC: ", a_scc + b_scc, "\na: ", a_scc, "\nb: ", b_scc)
    aw_graph.V = a_graph.V
    bw_graph.V = b_graph.V

    print(min_spanning_tree(a_scc, b_scc, aw_graph, bw_graph, full_graph, graph_list, ret_cc_a, ret_cc_b))


if __name__ == '__main__':
    main()
