from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, s):
        visited = [False] * (max(self.graph) + 1)
        queue = []
        queue.append(s)
        visited[s] = True
        
        bfs_traversal = []
        while queue:
            s = queue.pop(0)
            bfs_traversal.append(s)
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
        return bfs_traversal

    def dfs_util(self, v, visited, dfs_traversal):
        visited.add(v)
        dfs_traversal.append(v)
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.dfs_util(neighbour, visited, dfs_traversal)

    def dfs(self, v):
        visited = set()
        dfs_traversal = []
        self.dfs_util(v, visited, dfs_traversal)
        return dfs_traversal

if __name__ == '__main__':
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("Breadth First Traversal (starting from vertex 2):", g.bfs(2))
    print("Depth First Traversal (starting from vertex 2):", g.dfs(2))
