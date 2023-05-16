import random
from typing import TypeAlias, Tuple
from graph import Graph

Edge: TypeAlias = Tuple[int, int]


class Karger:
    def __init__(self, graph: Graph) -> None:
        self.graph = graph
        self.nodes_count = graph.nodes + 1

    def run(self) -> int:
        self.aggregated_nodes_description = {}

        graph = {
           'edges': self.graph.edges,
           'nodes': self.graph.nodes
        }

        while graph['nodes'] != 2:
            new_edges = []
            choosed_edge = random.choice(graph['edges'])
            first_node, second_node = choosed_edge

            self.aggregated_nodes_description[
                str(self.nodes_count)
            ] = choosed_edge

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

            print('---------------------------------------------')
            print(f'Choosed Edge -> {choosed_edge}')
            print(f'Old Edges -> {graph["edges"]}')

            graph['edges'] = new_edges
            graph['nodes'] = len(new_edges)
            self.nodes_count += 1

            print(f'New Edges -> {new_edges}')

        return len(graph['edges'])

    def __handle_edge_creation(self, node: int, edge: Edge) -> None:
        new_edge = [self.nodes_count if edge_node == node
                    else edge_node for edge_node in edge]

        new_edge.sort()
        return tuple(new_edge)
