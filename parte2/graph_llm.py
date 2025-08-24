class Graph:
    def __init__(self, nodes=None, edges=None, file_path=None, directed=False):
        self.directed = directed
        self.nodes = nodes if nodes else []
        self.edges = edges if edges else []

        if file_path:
            self._load_from_file(file_path)

        # Build adjacency list
        self.adj = {node: [] for node in self.nodes}
        for u, v in self.edges:
            self.adj[u].append(v)
            if not self.directed:
                self.adj[v].append(u)

    def _load_from_file(self, file_path):
        with open(file_path, "r") as f:
            content = f.read().strip().split("#")

        graph_type = content[0].strip()
        self.directed = (graph_type == "digraph")

        # eval used for simplicity (file format is Python-like list)
        self.nodes = eval(content[1].strip())
        self.edges = eval(content[2].strip())

    def _dfs(self, start, visited, adj):
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                stack.extend(adj[node])

    def check_connected(self) -> bool:
        if not self.nodes:
            return True

        if self.directed:
            # Weak connectivity: convert to undirected graph
            undirected_adj = {node: [] for node in self.nodes}
            for u, v in self.edges:
                undirected_adj[u].append(v)
                undirected_adj[v].append(u)

            visited = set()
            self._dfs(self.nodes[0], visited, undirected_adj)
            return len(visited) == len(self.nodes)

        else:
            # Undirected case
            visited = set()
            self._dfs(self.nodes[0], visited, self.adj)
            return len(visited) == len(self.nodes)
