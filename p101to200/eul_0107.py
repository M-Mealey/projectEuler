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
    mtx = []
    for r in str_in.strip().split("\n"):
        mtx.append([int(i) if i != "-" else 0 for i in r.split(",")])
    return mtx


def calc_total_weight(m):
    """ calculate the total weight of an adjacency matrix """
    return sum(sum(r) for r in m)//2


def solve(input_files=("resources/network.txt",)):
    """ solve problem 107.
    Uses Prim's Algorithm: https://en.wikipedia.org/wiki/Prim%27s_algorithm """

    with open(input_files[0], 'r', encoding='utf-8') as f:
        data = f.read()
        adj_mtx = read_adj_matrix(data)

    new_adj_mtx = [[0 for x in adj_mtx] for y in adj_mtx]
    visited = {0}
    edge_queue = []  # should find more efficient data type here
    for i, e in enumerate(adj_mtx[0]):
        if e > 0:
            edge_queue.append((e, i))
    next_vert = 0
    next_edge_weight = 1000000
    while len(visited) < len(adj_mtx):
        edge_queue.sort()
        last_vert = next_vert
        while next_vert in visited:
            next_edge_weight, next_vert = edge_queue.pop(0)
        # add this edge to new adjacency matrix
        new_adj_mtx[last_vert][next_vert] = next_edge_weight
        new_adj_mtx[next_vert][last_vert] = next_edge_weight
        # add new edges to queue
        for i, e in enumerate(adj_mtx[next_vert]):
            if e > 0 and i not in visited:
                edge_queue.append((e, i))
        # done with this vertex, mark as visited and continue
        visited.add(next_vert)
    return calc_total_weight(adj_mtx) - calc_total_weight(new_adj_mtx)


if __name__ == "__main__":
    print(solve())
