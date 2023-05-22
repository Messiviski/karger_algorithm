import numpy as np
from graph import Graph
from naive import Naive
from karger import Karger
from algorithm import Algorithm
import matplotlib.pyplot as plt


def analyse(graph: Graph, min_cut: int, n_exec: int, n_iter: int) -> None:
    karger = Karger(graph)
    naive = Naive(graph)

    probabilties = []
    iterations = []

    for i in range(4):
        iterations_karger = iterations_naive = 0

        for j in range(1, n_exec + 1):
            result = run_algorithm(karger, n_iter)
            if result == min_cut:
                iterations_karger += 1

        for j in range(1, n_exec + 1):
            result = run_algorithm(naive, n_iter)
            if result == min_cut:
                iterations_naive += 1

        iterations.append([iterations_karger, iterations_naive])
        probabilties.append(
            [iterations_karger / n_exec, iterations_naive / n_exec]
        )

        n_iter += 20

        print(f'=========== {i} ===========')
        print(f'Karger  {iterations_karger / n_exec} - {n_iter}')
        print(f'Naive   {iterations_naive / n_exec} - {n_iter}')

    plot(iterations, probabilties)


def run_algorithm(algorithm_instance: Algorithm, n_iter: int) -> int:
    best_result = algorithm_instance.run()

    for i in range(n_iter):
        new_result = algorithm_instance.run()
        if new_result < new_result:
            best_result = new_result

    return best_result


def plot(x: list[int, int], y: list[float, float]) -> None:
    np_probabilities = np.array(y)
    np_iterations = np.array(x)

    # Karger
    plt.plot(np_iterations[0:, 0], np_probabilities[0:, 0])

    # Naive
    plt.plot(np_iterations[0:, 1], np_probabilities[0:, 1])

    plt.show()
