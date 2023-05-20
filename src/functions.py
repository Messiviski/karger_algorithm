from graph import Graph
from naive import Naive
from karger import Karger
from algorithm import Algorithm


def analyse(graph_instance: Graph, n_exec: int, n_iter: int) -> None:
    karger = Karger(graph_instance)
    naive = Naive(graph_instance)

    for i in range(n_exec):
        print(run_algorithm(karger, n_iter))
        print(run_algorithm(naive, n_iter))
        print('=====================================')


def run_algorithm(algorithm_instance: Algorithm, n_iter: int) -> int:
    best_result = algorithm_instance.run()

    for i in range(n_iter):
        new_result = algorithm_instance.run()
        if new_result < new_result:
            best_result = new_result

    return best_result
