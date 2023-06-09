import random
from graph import Graph
from algorithm import Algorithm
from typing import TypeAlias, Tuple

Edge: TypeAlias = Tuple[int, int]


class Karger(Algorithm):
    def __init__(self, graph: Graph) -> None:
        self.graph = graph
        self.nodes_count = graph.nodes + 1

    def run(self) -> int:
        self.nodes_count = self.graph.nodes + 1
        self.aggregated_nodes_description = {}

        graph = {
           'edges': self.graph.edges,
           'nodes': self.graph.nodes
        }

        while True:
            if self.__reached_the_minimum(graph):
                break

            new_edges = []
            choosed_edge = random.choice(graph['edges'])
            first_node, second_node = choosed_edge

            self.aggregated_nodes_description[
                    str(self.nodes_count)
            ] = choosed_edge

            #   print('------------------------------')
            #   print(f'Escolhido -> {choosed_edge}')
            #   print(f"Vertices -> {graph['edges']}\n")

            graph['nodes'] -= 1

            for edge in graph['edges']:
                if edge == choosed_edge:
                    continue

                if first_node in edge:
                    new_edges.append(
                        self.__handle_edge_creation(first_node, edge)
                    )

                    continue
                if second_node in edge:
                    new_edges.append(
                        self.__handle_edge_creation(second_node, edge)
                    )

                    continue

                new_edges.append(edge)

            graph['edges'] = new_edges
            self.nodes_count += 1

        return len(graph['edges'])

    def __reached_the_minimum(self, graph: dict) -> bool:
        unique_edges = set(graph['edges'])

        if len(unique_edges) == 1:
            #   print(unique_edges)
            #   print('---------------------------------')
            #   print(graph['edges'])
            #   print(graph['nodes'])
            return True

        return False

    def __handle_edge_creation(self, node: int, edge: Edge) -> None:
        new_edge = [self.nodes_count if edge_node == node
                    else edge_node for edge_node in edge]

        new_edge.sort()
        return tuple(new_edge)
