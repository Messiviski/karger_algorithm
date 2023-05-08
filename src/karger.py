import random
from typing import TypeAlias, Tuple
from graph import Graph

Edge: TypeAlias = Tuple[int, int]

class Karger:
    def __init__(self, graph: Graph) -> None:
        self.graph = graph
        self.nodes_count = graph.nodes + 1
        self.aggregated_nodes_description = {}

    def run(self) -> int:
        while self.graph.nodes != 2:
            choosed_edge = random.choice(self.graph.edges)
            edge_first_node, edge_second_node = choosed_edge
            self.aggregated_nodes_description[str(self.nodes_count)] = choosed_edge

            graph = Graph()
            graph.nodes = self.graph.nodes - 1

            for edge in self.graph.edges:
                if edge == choosed_edge:
                    continue

                if edge_first_node in edge:
                    graph.edges.append(
                        self.__handle_edge_creation(edge_first_node, edge)
                    )

                    continue
                if edge_second_node in edge:
                    graph.edges.append(
                        self.__handle_edge_creation(edge_second_node, edge)
                    )

                    continue

                graph.edges.append(edge)

            print('------------------------------')
            print(choosed_edge)
            print(self.graph.edges)
            print(graph.edges)

            self.graph = graph
            self.nodes_count += 1

        return len(graph.edges)


    def __handle_edge_creation(self, choosed_edge_node: int, edge: Edge) -> None:
        new_edge = [self.nodes_count if node == choosed_edge_node
                else node for node in edge]

        new_edge.sort()
        return tuple(new_edge)

