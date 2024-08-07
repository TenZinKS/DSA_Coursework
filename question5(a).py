import random
import math

# Calculate the distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Calculate the total distance of the tour
def total_distance(tour, cities):
    dist = 0
    for i in range(len(tour)):
        dist += distance(cities[tour[i]], cities[tour[(i + 1) % len(tour)]])
    return dist

# generate an initial solution
def generate_initial_solution(cities):
    tour = list(range(len(cities)))
    random.shuffle(tour)
    return tour

# generate neighbors by swapping two cities
def generate_neighbors(tour):
    neighbors = []
    for i in range(len(tour)):
        for j in range(i + 1, len(tour)):
            neighbor = tour[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors

# Hill Climbing algorithm
def hill_climbing(cities):
    current_solution = generate_initial_solution(cities)
    current_distance = total_distance(current_solution, cities)
    while True:
        neighbors = generate_neighbors(current_solution)
        best_neighbor = None
        best_distance = current_distance
        for neighbor in neighbors:
            neighbor_distance = total_distance(neighbor, cities)
            if neighbor_distance < best_distance:
                best_neighbor = neighbor
                best_distance = neighbor_distance
        if best_neighbor is None:
            break
        current_solution = best_neighbor
        current_distance = best_distance
    return current_solution, current_distance

# Example cities (x, y coordinates)
cities = [
    (0, 0), (1, 3), (4, 3), (6, 1),
    (3, 0), (2, 4), (5, 5), (7, 2)
]

# Solve TSP using Hill Climbing
solution, distance = hill_climbing(cities)
print("Best tour:", solution)
print("Total distance:", distance)
