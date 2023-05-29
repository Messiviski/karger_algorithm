import numpy as np
from graph import Graph
from naive import Naive
from karger import Karger
import matplotlib.pyplot as plt


def analyse(
        graph: Graph, min_cut: int, n_exec: int, n_iter: int,
        e: float = 0.01) -> None:

    karger, naive = Karger(graph), Naive(graph)
    KARGER, NAIVE = 0, 1
    probabilities, iterations = [], []
    karger_stop_condition = False
    stop_count = 0

    while True:
        iterations_karger = iterations_naive = 0

        for j in range(1, n_exec + 1):
            results = iterate(karger, naive, n_iter)

            if results[KARGER] == min_cut:
                iterations_karger += 1

            if results[NAIVE] == min_cut:
                iterations_naive += 1

        iterations.append(n_iter)
        probabilities.append(
            calculate_probabilities(iterations_karger, iterations_naive, n_exec)
        )

        if probabilities[-1][KARGER] == 1.0 and karger_stop_condition is False:
            karger_stop_condition = True

        if check_stop_conditions(probabilities, e):
            stop_count += 1

        if stop_count == 5:
            break

        n_iter += 20

        print(f'Latest Probabilities -> {probabilities[-1]}')

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


def calculate_probabilities(karger: int, naive: int, n_exec: int) -> None:
    return [karger / n_exec, naive / n_exec]


def check_stop_conditions(probabilities: list, e: float) -> None:
    if len(probabilities) <= 1:
        return False

    new_probabilities = np.array(probabilities)
    KARGER, NAIVE = 0, 1

    current_odds, last_probabilities = new_probabilities[-2:]

    if current_odds[KARGER] == 1.0 and current_odds[NAIVE] == 1.0:
        return True

    karger_odds, naive_odds = get_latest_probabilities(new_probabilities)

    if not has_changed(karger_odds, e) and not has_changed(naive_odds, e):
        return True


def get_latest_probabilities(probabilities: list) -> list:
    last_probabilities = probabilities[-2:]
    return [last_probabilities[0:, 0], last_probabilities[0:, 1]]


def has_changed(probabilities: list, e: float):
    LAST, BEFORE_LAST = [1, 0]

    if (probabilities[LAST] - probabilities[BEFORE_LAST]) < e:
        return False

    return True


def plot(x: list[int, int], y: list[float, float]) -> None:
    np_probabilities = np.array(y)

    # Karger
    plt.plot(x, np_probabilities[0:, 0], 'r')

    # Naive
    plt.plot(x, np_probabilities[0:, 1], 'b')

    plt.show()
