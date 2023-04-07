class Graph:
    def __init__(self, file_path):
        graph_instance = self.__remove_empty_lines(open(file_path).read().split('\n'))

        self.nodes = int(graph_instance[0])
        self.adjacency_matrix = self.__create_adjacency_matrix(graph_instance[1:])
        self.adjacency_list = self.__create_adjacency_list(graph_instance[1:])

    def __remove_empty_lines(self, instance):
        return [row for row in instance if row != '']

    def __create_adjacency_matrix(self, instance):
        adjacency_matrix = []
        for i in range(len(instance)):
            adjacency_matrix.append(
            [int(item) for item in instance[i].split(' ') if item != '']
        )

        return adjacency_matrix

    def __create_adjacency_list(self, instance):
        adjacency_list = []

        for i in range(len(instance)):
            adjacency_list_row = []
            row = [int(item) for item in instance[i].split(' ') if item != '']
            for j in range(len(row)):
                if(row[j] == 0): continue;
                adjacency_list_row.append(j + 1)
          
            adjacency_list.append(adjacency_list_row)

        return adjacency_list
