
from queue import PriorityQueue

# State representation: (position of camel, position of bananas, number of bananas carried)
# The initial state is (0, 0, 0) and the goal state is (distance_to_travel, distance_to_travel, distance_to_travel)
# The camel starts at position 0, and the bananas start at the position distance_to_travel.
# The goal is to transport all bananas to the destination (distance_to_travel), with the camel carrying them.

def heuristic(state, distance_to_travel):
    # Heuristic function: Manhatten distance to the goal
    return abs(distance_to_travel - state[0]) + abs(distance_to_travel - state[1]) + state[2]

def camel_banana_problem(distance_to_travel):
    initial_state = (0, distance_to_travel, 0)
    goal_state = (distance_to_travel, distance_to_travel, distance_to_travel)

    # Priority queue to store states with their heuristics
    pq = PriorityQueue()
    pq.put((heuristic(initial_state, distance_to_travel), initial_state, []))

    # Visited states set
    visited = set()

    while not pq.empty():
        _, current_state, path = pq.get()

        # Goal check
        if current_state == goal_state:
            return path + [current_state]

        visited.add(current_state)

        # Generate next possible states
        next_states = []

        # Camel moves
        for move in [-1, 1]:
            next_pos_camel = current_state[0] + move
            if 0 <= next_pos_camel <= distance_to_travel:
                next_states.append((next_pos_camel, current_state[1], current_state[2]))

        # Camel picks up bananas
        if current_state[0] == current_state[1]:
            next_states.append((current_state[0], current_state[1], min(current_state[2] + 1, distance_to_travel)))

        # Camel drops bananas
        if current_state[0] == 0 and current_state[2] > 0:
            next_states.append((current_state[0], current_state[1], 0))

        # Add next states to the priority queue
        for next_state in next_states:
            if next_state not in visited:
                pq.put((heuristic(next_state, distance_to_travel), next_state, path + [current_state]))

    return None

# Example usage:
distance_to_travel = 10

solution = camel_banana_problem(distance_to_travel)
if solution:
    print("Solution found:")
    for state in solution:
        print(state)
else:
    print("No solution found.")
