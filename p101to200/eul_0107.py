"""
Project Euler Problem 107
=========================

The following undirected network consists of seven vertices and twelve
edges with a total weight of 243.

The same network can be represented by the matrix below.

               +-----------------------------------------+
               |      | A  | B  | C  | D  | E  | F  | G  |
               |------+----+----+----+----+----+----+----|
               | A    | -  | 16 | 12 | 21 | -  | -  | -  |
               |------+----+----+----+----+----+----+----|
               | B    | 16 | -  | -  | 17 | 20 | -  | -  |
               |------+----+----+----+----+----+----+----|
               | C    | 12 | -  | -  | 28 | -  | 31 | -  |
               |------+----+----+----+----+----+----+----|
               | D    | 21 | 17 | 28 | -  | 18 | 19 | 23 |
               |------+----+----+----+----+----+----+----|
               | E    | -  | 20 | -  | 18 | -  | -  | 11 |
               |------+----+----+----+----+----+----+----|
               | F    | -  | -  | 31 | 19 | -  | -  | 27 |
               |------+----+----+----+----+----+----+----|
               | G    | -  | -  | -  | 23 | 11 | 27 | -  |
               +-----------------------------------------+

However, it is possible to optimise the network by removing some edges and
still ensure that all points on the network remain connected. The network
which achieves the maximum saving is shown below. It has a weight of 93,
representing a saving of 243 93 = 150 from the original network.

Using network.txt, a 6K text file containing a network with forty vertices,
and given in matrix form, find the maximum saving which can be achieved by
removing redundant edges whilst ensuring that the network remains connected.
"""
import heapq

EXAMPLE_NETWORK = """-,16,12,21,-,-,-
16,-,-,17,20,-,-
12,-,-,28,-,31,-
21,17,28,-,18,19,23
-,20,-,18,-,-,11
-,-,31,19,-,-,27
-,-,-,23,11,27,-
"""


def read_adj_matrix(str_in):
    """ read a string input, return adjacency matrix """
    mtx = {}
    for i, r in enumerate(str_in.strip().split("\n")):
        mtx[i] = [(int(w), v) for v, w in enumerate(r.split(",")) if w != "-"]
    return mtx


def calc_total_weight(m):
    """ calculate the total weight of a graph from its adjacency matrix """
    total = 0
    for v in m.values():
        total += sum(x[0] for x in v)
    return total//2


def solve(input_files=("resources/network.txt",)):
    """ solve problem 107.
    Uses Prim's Algorithm: https://en.wikipedia.org/wiki/Prim%27s_algorithm """

    with open(input_files[0], 'r', encoding='utf-8') as f:
        data = f.read()
        adj_mtx = read_adj_matrix(data)

    new_adj_mtx = {}
    for k in adj_mtx:
        new_adj_mtx[k] = []
    visited = {0}
    edge_queue = []
    heapq.heapify(edge_queue)
    for e, v in adj_mtx[0]:
        if e > 0:
            heapq.heappush(edge_queue, (e, v))
    next_vert = 0
    next_edge_weight = 1000000
    while len(visited) < len(adj_mtx):
        last_vert = next_vert
        while next_vert in visited:
            next_edge_weight, next_vert = heapq.heappop(edge_queue)
        # add this edge to new adjacency matrix
        new_adj_mtx[last_vert].append((next_edge_weight, next_vert))
        new_adj_mtx[next_vert].append((next_edge_weight, last_vert))
        # add new edges to queue
        for e, v in adj_mtx[next_vert]:
            if e > 0 and v not in visited:
                heapq.heappush(edge_queue, (e, v))
        # done with this vertex, mark as visited and continue
        visited.add(next_vert)
    return calc_total_weight(adj_mtx) - calc_total_weight(new_adj_mtx)


if __name__ == "__main__":
    print(solve())
