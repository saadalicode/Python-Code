
# ---------4.1 Solution

# class to create graph and printing node values
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, v, w):
        self.graph[v].append(w)

    def DFSUtil(self, v, visited):
        visited[v] = True
        print(v, end=' ')

        for neighbour in self.graph[v]:
            if not visited[neighbour]:
                self.DFSUtil(neighbour, visited)
    
    def DFS(self, v):
        visited = [False] * self.V
        self.DFSUtil(v, visited)


# Main program to create a graph and perform DFS
if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("Following is the Depth First Traversal (starting from vertex 2)")
    g.DFS(2)


# ---------6.1 Solution

# Graph Class using string labels
class Graph:
    def __init__(self):
        self.graph = {}
        self.found_goal = False  # To keep track of whether we have found the goal

    def add_edge(self, v, w):
        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append(w)

    def DFSUtil(self, v, visited):
        if self.found_goal:
            return  # Stop recursion if the goal has been found

        visited.add(v)
        print(v, end=' ')
        
        if v == 'G':  # Check if the current vertex is the goal
            print("Reached goal G")
            self.found_goal = True  # Mark that the goal has been found
            return  # Stop further DFS

        for neighbour in self.graph.get(v, []):
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
    
    def DFS(self, v):
        visited = set()
        self.DFSUtil(v, visited)


# Main program to create a graph and perform DFS
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'F')
    g.add_edge('A', 'D')
    g.add_edge('A', 'E')
    g.add_edge('B', 'K')
    g.add_edge('B', 'J')
    g.add_edge('D', 'G')
    g.add_edge('E', 'C')
    g.add_edge('E', 'H')
    g.add_edge('E', 'I')
    g.add_edge('I', 'L')
    g.add_edge('K', 'N')
    g.add_edge('K', 'M')

    print("Following is the Depth First Traversal (starting from vertex 'A')")
    g.DFS('A')
