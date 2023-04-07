from dfsnode import DFSNode
from graph import Graph

class DFS:
    def __init__(self, graph_instance: Graph):
        self.graph = graph_instance
        self.colors_matrix = []
        self.time = 0
        self.nodes = [DFSNode(0, 0, None) for i in range(graph_instance.nodes)]

    def run(self, node):
        print(1)
