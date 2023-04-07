from dfsnode import DFSNode
from graph import Graph

class DFS:
    def __init__(self, graph_instance: Graph):
        self.graph = graph_instance
        self.colors_matrix = []
        self.time = 0
        self.nodes = [DFSNode(0, 0, None) for i in range(graph_instance.nodes)]

    def run(self, initial_node):
        self.time += 1
        self.nodes[node - 1].input = self.time

        for i in range(len(self.nodes)):
            if(self.nodes[i].input != 0):
                # must mark the father and add mark the new edge
                print(1)

