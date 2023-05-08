from typing import List, Tuple


class Graph:
    def __init__(self) -> None:
        self.nodes = 0
        self.edges = []
        self.adjacency_matrix = []
        self.adjacency_list = []

    def read_file(self, file_path: str) -> None:
        file_without_new_lines = open(file_path).read().split('\n')
        graph_instance = self.__remove_empty_lines(file_without_new_lines)

        self.nodes = int(graph_instance[0])
        adjacencies = graph_instance[1:]

        self.adjacency_matrix = self.__create_adjacency_matrix(adjacencies)
        self.adjacency_list = self.__create_adjacency_list(adjacencies)


    def __remove_empty_lines(self, instance: List[str]) -> List[str]:
        return [row for row in instance if row != '']

    def __create_adjacency_matrix(self, adjacencies: List[str]) -> List[List[int]]:
        adjacency_matrix = []
        for i in range(len(adjacencies)):
            adjacency_matrix.append(
                [int(item) for item in adjacencies[i].split(' ') if item != '']
            )

        return adjacency_matrix

    def __create_adjacency_list(self, adjacencies: List[str]) -> List[List[int]]:
        adjacency_list = []

        for i in range(len(adjacencies)):
            adjacency_list_row = []
            row = [int(item) for item in adjacencies[i].split(' ') if item != '']
            for j in range(len(row)):
                if (row[j] == 0):
                    continue

                adjacency_list_row.append(j + 1)
                self.__create_edge(i + 1, j + 1)

            adjacency_list.append(adjacency_list_row)

        return adjacency_list

    def __create_edge(self, first_node: int, second_node: int) -> None:
        edge = [first_node, second_node]
        edge.sort()

        edge = tuple(edge)
        if edge not in self.edges:
            self.edges.append(edge)


