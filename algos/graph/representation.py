from algos.linear.array import Array


class Node:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, to_node, from_node, cost=0):
        self.to_node = to_node
        self.from_node = from_node
        self.cost = cost


class EdgeList:
    def __init__(self):
        self.edge_list = DynamicArray(Edge)

    def addedge(self, edge):
        self.edge_list.append(edge)

    def alledges(self):
        for i in range(len(edge_list)):
            yield edge_list[i]


def edgelist_to_matrix(edgelist):
    no_of_vertices = len(edgelist)
