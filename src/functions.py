from graph import Graph
from naive import Naive
from karger import Karger
from algorithm import Algorithm
import matplotlib.pyplot as plt


def analyse(graph: Graph, min_cut: int, n_exec: int, n_iter: int) -> None:
    karger = Karger(graph)
    naive = Naive(graph)
    #    general_prob = 0

    plt.axis([0, n_iter, 0, 1])

    for i in range(1000):
        prob_karger = prob_naive = 0.0
        iterations_karger = iterations_naive = 0

        for j in range(1, n_exec + 1):
            result = run_algorithm(karger, n_iter)
            if result == min_cut:
                iterations_karger += 1

        for j in range(1, n_exec + 1):
            result = run_algorithm(naive, n_iter)
            if result == min_cut:
                iterations_naive += 1

        prob_karger = iterations_karger / n_exec
        prob_naive = iterations_naive / n_exec

        plt.scatter(prob_karger, iterations_karger, cmap='r')
        plt.scatter(prob_naive, iterations_naive, cmap='b')
        plt.pause(0.05)
        #   print(prob_karger)
        #   print(prob_naive)
        #   print("============================")

        n_iter += 10


def run_algorithm(algorithm_instance: Algorithm, n_iter: int) -> int:
    best_result = algorithm_instance.run()

    for i in range(n_iter):
        new_result = algorithm_instance.run()
        if new_result < new_result:
            best_result = new_result

    return best_result
