from graph import Graph
from functions import read_out_file_and_get_the_minimum_cut, analyse

file_name = 'graph_type1_2'

graph_instance = Graph(f'./src/in/{file_name}')
min_cut = int(read_out_file_and_get_the_minimum_cut(f'./src/out/{file_name}'))

analyse(graph_instance, min_cut, 100, 5)
