import random
import math

distance_map = [
    [None, 7, 9, 6, 7],
    [7, None, 4, 11, 4],
    [9, 4, None, 7, 4],
    [6, 11, 7, None, 9],
    [7, 4, 4, 9, None]
]


def get_distance(city_i, city_j):
    return distance_map[city_i][city_j]


def get_total_distance(order):
    total_distance = 0
    total_distance += get_distance(0, order[0])
    for i in range(len(order) - 1):
        total_distance += get_distance(order[i], order[i + 1])
    total_distance += get_distance(order[-1], 0)
    return total_distance


def search_with_swap(order):
    m, n = 0, 0
    while m == n:
        m, n = random.randint(0, len(order)-1), random.randint(0, len(order)-1)
    order[m], order[n] = order[n], order[m]
    return order


def order_to_cities(order):
    city_ref = ["A", "B", "C", "D", "E"]
    cities = []
    for i in order:
        cities.append(city_ref[i])
    return cities


def simulated_annealing(initial_order, initial_temperature, cooling_rate):
    current_order = initial_order
    the_best_order = current_order
    temperature = initial_temperature
    while temperature > 1e-5:
        current_distance = get_total_distance(current_order)
        new_order = search_with_swap(current_order)
        new_distance = get_total_distance(new_order)
        if new_distance < current_distance or random.random() < math.exp((current_distance - new_distance) / temperature):
            current_order = new_order
        if new_distance < get_total_distance(the_best_order):
            the_best_order = new_order
        temperature *= cooling_rate
    return the_best_order


solution = simulated_annealing([2, 3, 4, 1], 100, 0.9)
print(solution)
