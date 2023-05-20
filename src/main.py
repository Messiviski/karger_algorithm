from graph import Graph
from functions import analyse

file_name = 'graph_type1_1'
file_path = f'./src/in/{file_name}'

graph_instance = Graph(file_path)

analyse(graph_instance, 1, 10000)
