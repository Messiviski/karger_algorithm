import numpy as np
from graph import Graph
from naive import Naive
from karger import Karger
import matplotlib.pyplot as plt


def analyse(
            graph: Graph,
            min_cut: int,
            n_exec: int,
            n_iter: int,
            e: float = 0.01
        ) -> None:
    karger = Karger(graph)
    naive = Naive(graph)

    KARGER = 0
    NAIVE = 1

    probabilities = []
    iterations = []

    while True:
        prob_karger = prob_naive = 0
        iterations_karger = iterations_naive = 0

        for j in range(1, n_exec + 1):
            results = iterate(karger, naive, n_iter)

            if results[KARGER] == min_cut:
                iterations_karger += 1

            if results[NAIVE] == min_cut:
                iterations_naive += 1

        prob_karger = iterations_karger / n_exec
        prob_naive = iterations_naive / n_exec

        changed = has_changed(probabilities, prob_naive, e)

        iterations.append(n_iter)
        probabilities.append([prob_karger, prob_naive])

        if not changed:
            break

        n_iter += 20

    plot(iterations, probabilities)


def iterate(karger: Karger, naive: Naive, n_iter: int) -> list[int, int]:
    karger_best_result = karger.run()
    naive_best_result = naive.run()

    for i in range(n_iter):
        karger_new_result = karger.run()
        naive_new_result = naive.run()

        if karger_new_result < karger_best_result:
            karger_best_result = karger_new_result

        if naive_new_result < naive_best_result:
            naive_best_result = naive_new_result

    return [karger_best_result, naive_best_result]


def has_changed(probabilities: list, probability: float, e: float) -> bool:
    if len(probabilities) == 0:
        return True

    last_naive_probability = probabilities[-1][-1]

    if (probability - last_naive_probability) < e:
        return False

    return True


def plot(x: list[int, int], y: list[float, float]) -> None:
    np_probabilities = np.array(y)

    # Karger
    plt.plot(x, np_probabilities[0:, 0], 'r')

    # Naive
    plt.plot(x, np_probabilities[0:, 1], 'b')

    plt.show()
