import random
import math
import csv

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
    log = []
    current_order = initial_order
    the_best_order = current_order
    temperature = initial_temperature
    while temperature > 1e-5:
        current_distance = get_total_distance(current_order)
        new_order = search_with_swap(current_order)
        new_distance = get_total_distance(new_order)
        r = random.random()
        new_record = ["A"+"".join(order_to_cities(new_order))+"A", new_distance, new_distance - current_distance, r]
        if new_distance < current_distance or r < math.exp((current_distance - new_distance) / temperature):
            current_order = new_order
            new_record.append("Acc")
        else:
            new_record.append("Rej")
        if new_distance < get_total_distance(the_best_order):
            the_best_order = new_order
        new_record.append("A"+"".join(order_to_cities(the_best_order))+"A")
        log.append(new_record)
        temperature *= cooling_rate
    return the_best_order, log


solution, log = simulated_annealing([2, 3, 4, 1], 100, 0.9)

with open('solution.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Sequence", "Distance", "Difference", "R", "Option", "Best"])
    writer.writerows(log)
    f.close()
