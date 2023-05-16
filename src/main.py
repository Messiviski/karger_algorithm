from graph import Graph
from karger import Karger

file_name = 'graph_type1_1'
file_path = f'./src/in/{file_name}'

graph_instance = Graph(file_path)

teste = Karger(graph_instance)
best_result = teste.run()

#   for i in range(10000):
#       new_result = teste.run()
#       if new_result < best_result:
#           best_result = new_result

# print(best_result)
# print(teste.aggregated_nodes_description)
