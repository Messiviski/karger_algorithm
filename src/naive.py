import random
from typing import Array
from naive_node import NaiveNode
from graph import Graph


class Naive:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.nodes: NaiveNode = {'blue': [], 'red': []}

    def run(self) -> int:
        self.__handle_colored_nodes_creation()
        cuts = 0

        for edge in self.graph.edges:
            first_node, second_node = edge
            cut_condition_count = 0

            if first_node in self.nodes['blue'] or first_node in self.nodes['red']:
                cut_condition_count += 1
            elif second_node in self.nodes['blue'] or second_node in self.nodes['red']:
                cut_condition_count += 1

            if cut_condition_count == 2:
                cuts += 1

    def __handle_colored_nodes_creation(self) -> Array:
        for i in range(self.graph.nodes):
            node_color = random.choice(['b', 'r'])

            if node_color == 'b':
                self.nodes['blue'].append(i + 1)
            else:
                self.nodes['red'].append(i + 1)

        if len(self.nodes['blue']) == 0:
            node = random.choice(self.nodes['red'])
            self.nodes['blue'].append(node)
        elif len(self.nodes['red']) == 0:
            node = random.choice(self.nodes['blue'])
            self.nodes['red'].append(node)
