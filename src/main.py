from graph import Graph
from karger import Karger

file_name = 'graph_type1_1'
file_path = f'./src/in/{file_name}'

graph_instance = Graph()
graph_instance.read_file(file_path)

teste = Karger(graph_instance)
print(teste.run())
print(teste.aggregated_nodes_description)
