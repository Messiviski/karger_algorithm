import random
from graph import Graph
from algorithm import Algorithm
from naive_node import NaiveNode
from typing import TypeAlias, Tuple

Edge: TypeAlias = Tuple[int, int]


class Naive(Algorithm):
    def __init__(self, graph: Graph):
        self.graph = graph
        self.nodes: NaiveNode = {'blue': [], 'red': []}

    def run(self) -> int:
        self.__clear_nodes_colors()
        self.__handle_colored_nodes_creation()
        cuts = 0

        for edge in self.graph.edges:
            if self.__is_a_cut(edge):
                cuts += 1

        return cuts

    def __clear_nodes_colors(self):
        self.nodes['blue'] = []
        self.nodes['red'] = []

    def __handle_colored_nodes_creation(self) -> list:
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

    def __is_a_cut(self, edge: Edge) -> bool:
        first_node, second_node = edge

        if first_node in self.nodes['blue']:
            if second_node in self.nodes['red']:
                return True
        if first_node in self.nodes['red']:
            if second_node in self.nodes['blue']:
                return True

        return False
