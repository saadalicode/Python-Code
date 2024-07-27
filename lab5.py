def bfs(graph, start_node):
    # Create a queue for BFS
    queue = [start_node]
    # Set of visited nodes
    visited_nodes = set()
    # Mark the source node as visited
    visited_nodes.add(start_node)

    while queue:
        # Dequeue a vertex from the queue
        current_node = queue.pop(0)
        print(current_node, end=' ')

        # Get all adjacent vertices of the dequeued vertex
        for neighbor in graph[current_node]:
            if neighbor not in visited_nodes:
                # Enqueue the neighbor and mark it as visited
                queue.append(neighbor)
                visited_nodes.add(neighbor)

# Define the graph as an adjacency list
graph = {
    '0': ['1', '2', '3'],
    '1': ['4', '5'],
    '2': ['6', '7'],
    '3': ['7'],
    '4': [],
    '5': [],
    '6': [],
    '7': []
}

# Perform BFS starting from node '0'
bfs(graph, '0')

def bfs_with_goal(graph, start_node, goal_node):
    # Create a queue for BFS
    queue = [start_node]
    # Set of visited nodes
    visited_nodes = set()
    # Mark the source node as visited
    visited_nodes.add(start_node)

    while queue:
        # Dequeue a vertex from the queue
        current_node = queue.pop(0)
        print(current_node, end=' ')

        # If the goal node is found, stop the search
        if current_node == goal_node:
            print("\nGoal node found:", current_node)
            return

        # Get all adjacent vertices of the dequeued vertex
        for neighbor in graph[current_node]:
            if neighbor not in visited_nodes:
                # Enqueue the neighbor and mark it as visited
                queue.append(neighbor)
                visited_nodes.add(neighbor)

    print("\nGoal node not found in the graph.")

# Define the graph as an adjacency list
graph_with_goal = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': ['G'],
    'E': [],
    'F': [],
    'G': []
}

# Perform BFS starting from node 'A' with goal node 'E'
bfs_with_goal(graph_with_goal, 'A', 'E')


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def insert(self, item, priority):
        self.elements.append((priority, item))

    def extract_max(self):
        if self.is_empty():
            return None
        
        # Find the item with the highest priority
        max_priority_index = 0
        for i in range(1, len(self.elements)):
            if self.elements[i][0] > self.elements[max_priority_index][0]:
                max_priority_index = i
        
        # Extract the item with the highest priority
        max_priority_item = self.elements[max_priority_index][1]
        del self.elements[max_priority_index]
        return max_priority_item

    def peek_max(self):
        if self.is_empty():
            return None

        max_priority_index = 0
        for i in range(1, len(self.elements)):
            if self.elements[i][0] > self.elements[max_priority_index][0]:
                max_priority_index = i

        return self.elements[max_priority_index][1]

# Example Usage
priority_queue = PriorityQueue()
priority_queue.insert("Task A", 2)
priority_queue.insert("Task B", 1)
priority_queue.insert("Task C", 3)

print("Element with highest priority:", priority_queue.peek_max())  # Should print "Task C"

while not priority_queue.is_empty():
    print(priority_queue.extract_max(), end=' ')  # Should print elements in order of priority: "Task C Task A Task B"
