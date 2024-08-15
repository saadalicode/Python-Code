# ----------Task 1
# -----------A* alogorithm
import math

class Node:
    def __init__(self, name, g=0, h=0):
        self.name = name        # City name (or identifier)
        self.g = g              # Cost from start to this node
        self.h = h              # Heuristic cost to goal
        self.f = g + h          # Total cost (f = g + h)
        self.parent = None      # Parent node in the path

    def __repr__(self):
        return f"Node(name={self.name}, g={self.g}, h={self.h}, f={self.f})"

def a_star(node_start, node_goal, neighbors, heuristic):
    open_list = []
    closed_list = set()
    
    # Initialize the start node
    node_start.g = 0
    node_start.h = heuristic(node_start.name)
    node_start.f = node_start.g + node_start.h
    open_list.append(node_start)
    
    while open_list:
        # Find the node with the lowest f value in the open list
        node_current = min(open_list, key=lambda node: node.f)
        open_list.remove(node_current)
        
        # Check if we have reached the goal
        if node_current.name == node_goal.name:
            return reconstruct_path(node_current)
        
        closed_list.add(node_current.name)
        
        # Generate the successors
        for neighbor_name, weight in neighbors(node_current.name):
            # Create a successor node
            successor = Node(neighbor_name)
            successor.g = node_current.g + weight
            successor.h = heuristic(successor.name)
            successor.f = successor.g + successor.h
            successor.parent = node_current
            
            if successor.name in closed_list:
                if successor.g >= node_current.g + weight:
                    continue
            
            # Check if successor is already in the open list
            open_node = next((n for n in open_list if n.name == successor.name), None)
            if open_node:
                if successor.g >= open_node.g:
                    continue
                # Update the open list node if needed
                open_list.remove(open_node)
            # Add the successor to the open list
            open_list.append(successor)
    
    return None  # No path found

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.name)
        node = node.parent
    path.reverse()
    return path

# Define the neighbors function with city connections and costs
def neighbors(city_name):
    connections = {
        'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
        'Zerind': [('Oradea', 71)],
        'Oradea': [('Sibiu', 151)],
        'Sibiu': [('Fagaras', 99), ('Rimnicu Vilcea', 80)],
        'Timisoara': [('Lugoj', 111)],
        'Lugoj': [('Mehadia', 70)],
        'Mehadia': [('Drobeta', 75)],
        'Drobeta': [('Craiova', 120)],
        'Craiova': [('Rimnicu Vilcea', 146)],
        'Rimnicu Vilcea': [('Pitesti', 97)],
        'Pitesti': [('Bucharest', 101)],
        'Fagaras': [('Bucharest', 211)],
        'Bucharest': []
    }
    return connections.get(city_name, [])

# Define the heuristic function based on straight-line distances (estimated distances)
def heuristic(city_name):
    straight_line_distances = {
        'Arad': 366,
        'Zerind': 374,
        'Oradea': 380,
        'Sibiu': 253,
        'Timisoara': 329,
        'Lugoj': 244,
        'Mehadia': 241,
        'Drobeta': 242,
        'Craiova': 160,
        'Rimnicu Vilcea': 193,
        'Pitesti': 98,
        'Fagaras': 176,
        'Bucharest': 0
    }
    return straight_line_distances.get(city_name, float('inf'))

# Define start and goal nodes
node_start = Node('Arad')
node_goal = Node('Bucharest')

# Call A* algorithm
path = a_star(node_start, node_goal, neighbors, heuristic)
print("Path found:", path)


# -----------------Task 2
# -----Greedy first search 
class Node:
    def __init__(self, name, h=0):
        self.name = name        # City name (or identifier)
        self.h = h              # Heuristic cost to goal
        self.f = h              # Total cost (f = h, since g is not used)
        self.parent = None      # Parent node in the path

    def __repr__(self):
        return f"Node(name={self.name}, h={self.h}, f={self.f})"

def greedy_best_first_search(node_start, node_goal, neighbors, heuristic):
    open_list = []
    closed_list = set()
    
    # Initialize the start node
    node_start.h = heuristic(node_start.name)
    node_start.f = node_start.h
    open_list.append(node_start)
    
    while open_list:
        # Find the node with the lowest heuristic value in the open list
        node_current = min(open_list, key=lambda node: node.f)
        open_list.remove(node_current)
        
        # Check if we have reached the goal
        if node_current.name == node_goal.name:
            return reconstruct_path(node_current)
        
        closed_list.add(node_current.name)
        
        # Generate the successors
        for neighbor_name, _ in neighbors(node_current.name):
            # Create a successor node
            successor = Node(neighbor_name)
            successor.h = heuristic(successor.name)
            successor.f = successor.h
            successor.parent = node_current
            
            if successor.name in closed_list:
                continue
            
            # Check if successor is already in the open list
            open_node = next((n for n in open_list if n.name == successor.name), None)
            if open_node:
                continue
            
            # Add the successor to the open list
            open_list.append(successor)
    
    return None  # No path found

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.name)
        node = node.parent
    path.reverse()
    return path

# Define the neighbors function with city connections and costs (costs are ignored in greedy search)
def neighbors(city_name):
    connections = {
        'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
        'Zerind': [('Oradea', 71)],
        'Oradea': [('Sibiu', 151)],
        'Sibiu': [('Fagaras', 99), ('Rimnicu Vilcea', 80)],
        'Timisoara': [('Lugoj', 111)],
        'Lugoj': [('Mehadia', 70)],
        'Mehadia': [('Drobeta', 75)],
        'Drobeta': [('Craiova', 120)],
        'Craiova': [('Rimnicu Vilcea', 146)],
        'Rimnicu Vilcea': [('Pitesti', 97)],
        'Pitesti': [('Bucharest', 101)],
        'Fagaras': [('Bucharest', 211)],
        'Bucharest': []
    }
    return connections.get(city_name, [])

# Define the heuristic function based on straight-line distances (estimated distances)
def heuristic(city_name):
    straight_line_distances = {
        'Arad': 366,
        'Zerind': 374,
        'Oradea': 380,
        'Sibiu': 253,
        'Timisoara': 329,
        'Lugoj': 244,
        'Mehadia': 241,
        'Drobeta': 242,
        'Craiova': 160,
        'Rimnicu Vilcea': 193,
        'Pitesti': 98,
        'Fagaras': 176,
        'Bucharest': 0
    }
    return straight_line_distances.get(city_name, float('inf'))

# Define start and goal nodes
node_start = Node('Arad')
node_goal = Node('Bucharest')

# Call Greedy Best-First Search algorithm
path = greedy_best_first_search(node_start, node_goal, neighbors, heuristic)
print("Path found:", path)


# ----- Task 3
#  8 puzzle problem

import heapq
from collections import deque

class PuzzleState:
    def __init__(self, board, move="", parent=None):
        self.board = board
        self.move = move
        self.parent = parent
        self.blank_pos = self.find_blank_position()
        self.g = 0
        self.h = self.calculate_heuristic()
        self.f = self.g + self.h
    
    def find_blank_position(self):
        for r in range(3):
            for c in range(3):
                if self.board[r][c] == 0:
                    return (r, c)
    
    def calculate_heuristic(self):
        # Heuristic: Number of misplaced tiles
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        misplaced = 0
        for r in range(3):
            for c in range(3):
                if self.board[r][c] != goal[r][c] and self.board[r][c] != 0:
                    misplaced += 1
        return misplaced
    
    def __lt__(self, other):
        return self.f < other.f

    def get_neighbors(self):
        neighbors = []
        row, col = self.blank_pos
        moves = [("Up", -1, 0), ("Down", 1, 0), ("Left", 0, -1), ("Right", 0, 1)]
        for move, r_offset, c_offset in moves:
            new_row, new_col = row + r_offset, col + c_offset
            if 0 <= new_row < 3 and 0 <= new_col < 3:
                new_board = [row[:] for row in self.board]
                new_board[row][col], new_board[new_row][new_col] = new_board[new_row][new_col], new_board[row][col]
                neighbors.append(PuzzleState(new_board, move, self))
        return neighbors
    
    def __repr__(self):
        return f"Board: {self.board}\nMove: {self.move}\nHeuristic: {self.h}\nTotal cost: {self.f}\n"

def a_star_search(start_state):
    open_list = []
    closed_list = set()
    heapq.heappush(open_list, start_state)
    
    while open_list:
        current_state = heapq.heappop(open_list)
        
        if current_state.calculate_heuristic() == 0:
            return reconstruct_path(current_state)
        
        closed_list.add(tuple(map(tuple, current_state.board)))
        
        for neighbor in current_state.get_neighbors():
            if tuple(map(tuple, neighbor.board)) in closed_list:
                continue
            neighbor.g = current_state.g + 1
            neighbor.h = neighbor.calculate_heuristic()
            neighbor.f = neighbor.g + neighbor.h
            if any(nei.f <= neighbor.f for nei in open_list if nei.board == neighbor.board):
                continue
            heapq.heappush(open_list, neighbor)
    
    return None

def reconstruct_path(state):
    path = []
    while state:
        path.append(state)
        state = state.parent
    path.reverse()
    return path

def print_solution(path):
    for state in path:
        for row in state.board:
            print(row)
        print("Move:", state.move)
        print("Heuristic:", state.h)
        print("Total cost:", state.f)
        print()

# Example usage:

initial_board = [
    [1, 2, 3],
    [4, 5, 6],
    [0, 7, 8]
]

goal_board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

start_state = PuzzleState(initial_board)
solution_path = a_star_search(start_state)

if solution_path:
    print_solution(solution_path)
else:
    print("No solution found.")
