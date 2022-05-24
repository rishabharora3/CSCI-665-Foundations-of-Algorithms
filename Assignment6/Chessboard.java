/*
CSCI-665 Homework #6 Problem 2
file: Chessboard.java
description: This program compute if it is possible to cover all the empty squares on the chess board by non-overlapping
dominoes
author: Karan Ahluwalia, ka7982@rit.edu
author: Rishabh Arora, ra8851@rit.edu
the time complexity of the above implementation is O(d1d2^3)
*/

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class Chessboard {

    /**
     * reads the input matrix from the console
     *
     * @return the input matrix
     */
    public static int[][] readInput() {
        int[][] inputMatrix = null;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        try {
            String[] line = br.readLine().trim().split(" ");
            int rows = Integer.parseInt(line[0]);
            int cols = Integer.parseInt(line[1]);
            inputMatrix = new int[rows][cols];
            for (int i = 0; i < rows; i++) {
                line = br.readLine().trim().split(" ");
                for (int j = 0; j < cols; j++) {
                    inputMatrix[i][j] = Integer.parseInt(line[j].trim());
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return inputMatrix;
    }


    static class Graph {
        int a;
        int b;
        int[][] adjMatrix;

        public Graph(int a, int b) {
            this.a = b;
            this.b = a;
            adjMatrix = new int[a][b];
        }

        public void addEdge(int a, int b) {
            adjMatrix[a][b] = 1;
        }
    }

    /**
     * This method computes the BFS for the graph
     *
     * @param rGraph the graph
     * @param source the source vertex
     * @param sink   the sink vertex
     * @param parent the parent array
     * @param V      the number of vertices
     * @return find if there is a path from source to sink
     */
    static boolean bfs(int[][] rGraph, int source, int sink, int[] parent, int V) {
        boolean[] visited = new boolean[V];
        for (int i = 0; i < V; ++i)
            visited[i] = false;
        LinkedList<Integer> queue = new LinkedList<>();
        queue.add(source);
        visited[source] = true;
        parent[source] = -1;
        while (queue.size() != 0) {
            int u = queue.poll();
            for (int v = 0; v < V; v++) {
                if (!visited[v]
                        && rGraph[u][v] > 0) {
                    if (v == sink) {
                        parent[v] = u;
                        return true;
                    }
                    queue.add(v);
                    parent[v] = u;
                    visited[v] = true;
                }
            }
        }
        return false;
    }

    /**
     * This method computes the maximum flow possible to cover all the empty squares on the chess board by non-overlapping
     * dominoes of the same color.
     *
     * @param graph  - the graph
     * @param source - the source vertex
     * @param sink   - the sink vertex
     * @param V      - the number of vertices
     * @return maxFlow - the maximum flow
     */
    static int fordFulkerson(int[][] graph, int source, int sink, int V) {
        int u, v;
        int[][] rGraph = new int[V][V];

        for (u = 0; u < V; u++)
            for (v = 0; v < V; v++)
                rGraph[u][v] = graph[u][v];
        int[] parent = new int[V];

        int maxFlow = 0;
        while (bfs(rGraph, source, sink, parent, V)) {
            int pathFlow = Integer.MAX_VALUE;
            for (v = sink; v != source; v = parent[v]) {
                u = parent[v];
                pathFlow = Math.min(pathFlow, rGraph[u][v]);
            }
            for (v = sink; v != source; v = parent[v]) {
                u = parent[v];
                rGraph[u][v] -= pathFlow;
                rGraph[v][u] += pathFlow;
            }
            maxFlow += pathFlow;
        }
        return maxFlow;
    }

    /**
     * This method computes the maximum flow possible to cover all the empty squares on the chess board by non-overlapping
     * dominoes of the same color.
     *
     * @param args - the command line arguments
     */
    public static void main(String[] args) {
        float count = 0;
        boolean flag;
        int[][] inputMatrix = readInput();
        int rows = inputMatrix.length;
        int cols = inputMatrix[0].length;
        int V = rows * cols + 2;
        // Create a graph with V vertices and E edges
        Graph graph = new Graph(V, V);
        List<Coordinates> coordinates = new ArrayList<>();
        // check for neighbors of each square
        coordinates.add(new Coordinates(0, -1));
        coordinates.add(new Coordinates(0, 1));
        coordinates.add(new Coordinates(-1, 0));
        coordinates.add(new Coordinates(1, 0));
        for (int i = 0; i < rows; i++) {
            flag = i % 2 == 0;
            for (int j = 0; j < cols; j++) {
                if (inputMatrix[i][j] == 0)
                    count++;
                for (Coordinates coordinate : coordinates) {
                    int x = i + coordinate.x;
                    int y = j + coordinate.y;
                    if (x >= 0 && x < inputMatrix.length && y >= 0 && y < inputMatrix[0].length) {
                        if (inputMatrix[i][j] == 0 && inputMatrix[x][y] == 0 && isaBoolean(flag, j)) {
                            graph.addEdge(i * cols + j, x * cols + y);
                            // the source and sink are the last two rows in the adjacency matrix
                            graph.addEdge(graph.adjMatrix.length - 2, i * cols + j);
                            graph.addEdge(x * cols + y, graph.adjMatrix.length - 1);
                        }
                    }
                }
            }
        }
        //max flow is the number of squares that can be covered
        float maxFlow = fordFulkerson(graph.adjMatrix, graph.adjMatrix.length - 2, graph.adjMatrix.length - 1, V);
        if (maxFlow == count / 2) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }

    /**
     * swaps the boolean value of the square for reading black squares
     *
     * @param flag - the boolean value based on row
     * @param j    - the column of the square
     * @return
     */
    private static boolean isaBoolean(boolean flag, int j) {
        return flag ? j % 2 == 0 : j % 2 == 1;
    }

    // Class to store coordinates of possible neighboring square
    static class Coordinates {
        int x;
        int y;

        Coordinates(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}
